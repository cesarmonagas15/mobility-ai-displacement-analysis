#!/usr/bin/env python3
"""
Dependency Checker for Interactive Dashboard
Verifies all required packages are installed and compatible
"""

import sys
import os

def check_python_version():
    """Check if Python version is adequate"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ ERROR: Python 3.8 or higher is required")
        return False
    else:
        print("✓ Python version is adequate")
        return True

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {package_name:25s} (version: {version})")
        return True
    except ImportError:
        print(f"❌ {package_name:25s} NOT FOUND")
        return False

def check_data_file():
    """Check if required data file exists"""
    if os.path.exists('merged_clean.csv'):
        size = os.path.getsize('merged_clean.csv')
        print(f"✓ merged_clean.csv found ({size:,} bytes)")
        return True
    else:
        print("❌ merged_clean.csv NOT FOUND")
        return False

def main():
    print("="*60)
    print("  Dashboard Dependency Checker")
    print("="*60)
    print()
    
    all_good = True
    
    # Check Python version
    print("Checking Python version...")
    if not check_python_version():
        all_good = False
    print()
    
    # Check required packages
    print("Checking required packages...")
    packages = [
        ('dash', 'dash'),
        ('dash-bootstrap-components', 'dash_bootstrap_components'),
        ('plotly', 'plotly'),
        ('pandas', 'pandas'),
        ('numpy', 'numpy'),
        ('scipy', 'scipy'),
        ('requests', 'requests')
    ]
    
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_good = False
    print()
    
    # Check data file
    print("Checking data files...")
    if not check_data_file():
        all_good = False
    print()
    
    # Summary
    print("="*60)
    if all_good:
        print("✅ ALL CHECKS PASSED!")
        print("="*60)
        print()
        print("You're ready to run the dashboard:")
        print("  python interactive_dashboard.py")
        print()
        print("Or use the launch script:")
        print("  ./launch_dashboard.sh")
        print()
        return 0
    else:
        print("❌ SOME CHECKS FAILED")
        print("="*60)
        print()
        print("To install missing packages:")
        print("  pip install -r requirements.txt")
        print()
        print("If merged_clean.csv is missing:")
        print("  Ensure you have the data file in the same directory")
        print()
        return 1

if __name__ == '__main__':
    exit(main())

