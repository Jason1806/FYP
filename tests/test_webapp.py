import unittest
from unittest.mock import MagicMock, patch
from pentestool.core.webapp import WebAppScanner

class TestWebAppScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = WebAppScanner()

    @patch('pentestool.core.webapp.requests.Session')
    def test_sql_injection_in_second_field(self, mock_session):
        # Mock the session object
        def mock_post(url, data, timeout, verify):
            mock_response = MagicMock()
            if data.get('password') and 'OR' in data['password']:
                mock_response.text = "sql syntax error"
            else:
                mock_response.text = ""
            return mock_response

        mock_session.return_value.post.side_effect = mock_post

        self.scanner.session = mock_session()

        # Define a form with two input fields
        forms = [{
            'action': 'login.php',
            'method': 'post',
            'inputs': [
                {'name': 'username', 'type': 'text'},
                {'name': 'password', 'type': 'password'}
            ]
        }]

        # Call the function to be tested
        vulnerabilities = self.scanner._test_sql_injection('http://test.com', forms)

        # Assert that a vulnerability is found
        self.assertEqual(len(vulnerabilities), 1)
        self.assertEqual(vulnerabilities[0]['vulnerable_parameter'], 'password')

if __name__ == '__main__':
    unittest.main()
