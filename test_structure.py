#!/usr/bin/env python3
"""
Simple test script to verify the tool structure and basic functionality
"""

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_structure():
    """Test that all required files and directories exist"""
    print("🔍 Testing project structure...")
    
    required_files = [
        'pentestool/__init__.py',
        'pentestool/main.py',
        'pentestool/core/__init__.py',
        'pentestool/core/scanner.py',
        'pentestool/core/webapp.py',
        'pentestool/ai/__init__.py',
        'pentestool/ai/analyzer.py',
        'pentestool/reports/__init__.py',
        'pentestool/reports/generator.py',
        'pentestool/gui/__init__.py',
        'pentestool/gui/main_window.py',
        'pentestool/utils/__init__.py',
        'pentestool/utils/config.py',
        'requirements.txt',
        'setup.py',
        'pentestool.spec',
        'README.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"✓ {file_path}")
    
    if missing_files:
        print(f"\n❌ Missing files: {missing_files}")
        return False
    else:
        print("\n✅ All required files present!")
        return True

def test_basic_imports():
    """Test basic imports without external dependencies"""
    print("\n🔍 Testing basic imports...")
    
    try:
        import pentestool
        print("✓ pentestool package")
        
        print(f"✓ Package version: {pentestool.__version__}")
        print(f"✓ Package description: {pentestool.__description__}")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_cli_help():
    """Test that the CLI help works"""
    print("\n🔍 Testing CLI help...")
    
    try:
        from pentestool.main import cli
        print("✓ CLI module imported successfully")
        return True
    except Exception as e:
        print(f"❌ CLI test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 AI-Powered Penetration Testing Tool - Structure Test\n")
    
    tests = [
        ("Project Structure", test_structure),
        ("Basic Imports", test_basic_imports),
        ("CLI Help", test_cli_help)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print('='*50)
        
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed}/{total} tests passed")
    print('='*50)
    
    if passed == total:
        print("🎉 All tests passed! The tool structure is correct.")
        print("\n📋 Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run the tool: python -m pentestool.main --help")
        print("3. Build executable: ./build.sh (Linux/Mac) or build.bat (Windows)")
    else:
        print("⚠️  Some tests failed. Please check the project structure.")
    
    return passed == total

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)