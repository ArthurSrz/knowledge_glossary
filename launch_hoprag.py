#!/usr/bin/env python3
"""
HopRAG Launcher
Quick launcher for the HopRAG Streamlit application
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit', 'plotly', 'pandas', 'networkx', 
        'numpy', 'sentence-transformers', 'transformers', 'torch'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Installing requirements...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Requirements installed successfully!")

def main():
    """Main launcher function"""
    print("🔗 HopRAG - Knowledge-Intensive AI Launcher")
    print("=" * 50)
    
    # Check if we're in the right directory
    current_dir = Path.cwd()
    if not (current_dir / "hoprag_streamlit_app.py").exists():
        print("❌ Error: Please run this script from the knowledge_glossary directory")
        return
    
    # Check requirements
    try:
        check_requirements()
    except Exception as e:
        print(f"❌ Error installing requirements: {e}")
        return
    
    # Ask user which version to run
    print("\nChoose HopRAG version:")
    print("1. Basic HopRAG (hoprag_streamlit_app.py)")
    print("2. Enhanced HopRAG with HF integration (hoprag_hf_enhanced.py)")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        app_file = "hoprag_streamlit_app.py"
        print("\n🚀 Launching Basic HopRAG...")
    elif choice == "2":
        app_file = "hoprag_hf_enhanced.py"
        print("\n🚀 Launching Enhanced HopRAG with HF integration...")
    else:
        print("❌ Invalid choice. Defaulting to Basic HopRAG.")
        app_file = "hoprag_streamlit_app.py"
    
    # Launch Streamlit app
    try:
        cmd = [sys.executable, '-m', 'streamlit', 'run', app_file, '--server.address', '0.0.0.0', '--server.port', '8501']
        print(f"Running: {' '.join(cmd)}")
        print("\n🌐 The app will open in your browser at: http://localhost:8501")
        print("Press Ctrl+C to stop the application")
        
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n👋 HopRAG application stopped.")
    except Exception as e:
        print(f"❌ Error launching application: {e}")

if __name__ == "__main__":
    main()