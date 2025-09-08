from setuptools import setup, find_packages

setup(
    name="pentestool",
    version="1.0.0",
    description="AI-Powered Penetration Testing Tool",
    author="FYP Project",
    packages=find_packages(),
    install_requires=[
        "python-nmap>=0.7.1",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "lxml>=4.9.3",
        "scapy>=2.5.0",
        "dnspython>=2.4.2",
        "cryptography>=41.0.4",
        "jinja2>=3.1.2",
        "matplotlib>=3.7.2",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "scikit-learn>=1.3.0",
        "tensorflow>=2.13.0",
        "nltk>=3.8.1",
        "colorama>=0.4.6",
        "rich>=13.5.2",
        "click>=8.1.7",
        "pyfiglet>=0.8.post1",
    ],
    entry_points={
        "console_scripts": [
            "pentestool=pentestool.main:main",
        ],
    },
    python_requires=">=3.8",
)