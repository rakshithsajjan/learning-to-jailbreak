#!/usr/bin/env python3
"""
Installation verification script for jailbreak-rl project.
Run this after installation to verify everything is working correctly.
"""

import sys
import subprocess
from pathlib import Path

def print_status(message, status="info"):
    """Print colored status messages."""
    colors = {
        "info": "\033[94m",      # Blue
        "success": "\033[92m",   # Green
        "warning": "\033[93m",   # Yellow
        "error": "\033[91m",     # Red
        "end": "\033[0m"         # Reset
    }
    
    if status == "success":
        print(f"{colors['success']}✅ {message}{colors['end']}")
    elif status == "error":
        print(f"{colors['error']}❌ {message}{colors['end']}")
    elif status == "warning":
        print(f"{colors['warning']}⚠️  {message}{colors['end']}")
    else:
        print(f"{colors['info']}ℹ️  {message}{colors['end']}")

def check_python_version():
    """Check Python version is 3.8+."""
    print_status("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - OK", "success")
        return True
    else:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - Need 3.8+", "error")
        return False

def check_required_packages():
    """Check that required packages can be imported."""
    print_status("Checking required packages...")
    
    required_packages = [
        "torch",
        "transformers", 
        "numpy",
        "pandas",
        "matplotlib",
        "tqdm"
    ]
    
    optional_packages = [
        "ray",
        "gym", 
        "wandb",
        "pytest"
    ]
    
    all_good = True
    
    for package in required_packages:
        try:
            __import__(package)
            print_status(f"{package} - OK", "success")
        except ImportError:
            print_status(f"{package} - MISSING", "error")
            all_good = False
    
    for package in optional_packages:
        try:
            __import__(package)
            print_status(f"{package} - OK", "success")
        except ImportError:
            print_status(f"{package} - MISSING (optional)", "warning")
    
    return all_good

def check_gpu_availability():
    """Check GPU availability."""
    print_status("Checking GPU availability...")
    
    try:
        import torch
        if torch.cuda.is_available():
            gpu_count = torch.cuda.device_count()
            gpu_name = torch.cuda.get_device_name(0)
            print_status(f"GPU available: {gpu_name} (count: {gpu_count})", "success")
            return True
        else:
            print_status("GPU not available (CPU only)", "warning")
            return False
    except Exception as e:
        print_status(f"Error checking GPU: {e}", "error")
        return False

def check_model_download():
    """Test downloading a small model."""
    print_status("Testing model download...")
    
    try:
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained('gpt2')
        print_status("Model download successful", "success")
        return True
    except Exception as e:
        print_status(f"Model download failed: {e}", "error")
        return False

def check_project_structure():
    """Check project directory structure."""
    print_status("Checking project structure...")
    
    required_dirs = [
        "src",
        "docs", 
        "data",
        "experiments",
        "results",
        "scripts"
    ]
    
    project_root = Path(__file__).parent.parent
    all_good = True
    
    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print_status(f"Directory {dir_name}/ - OK", "success")
        else:
            print_status(f"Directory {dir_name}/ - MISSING", "error")
            all_good = False
    
    return all_good

def check_environment_variables():
    """Check for optional environment variables."""
    print_status("Checking environment variables...")
    
    import os
    
    optional_vars = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY", 
        "WANDB_API_KEY",
        "HF_TOKEN"
    ]
    
    for var in optional_vars:
        if os.getenv(var):
            print_status(f"{var} - SET", "success")
        else:
            print_status(f"{var} - NOT SET (optional)", "warning")

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("🔍 Jailbreak RL Installation Verification")
    print("=" * 60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Packages", check_required_packages),
        ("GPU Availability", check_gpu_availability),
        ("Model Download", check_model_download),
        ("Project Structure", check_project_structure),
        ("Environment Variables", check_environment_variables)
    ]
    
    results = []
    
    for check_name, check_func in checks:
        print(f"\n--- {check_name} ---")
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print_status(f"Check failed with error: {e}", "error")
            results.append((check_name, False))
    
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    
    critical_checks = ["Python Version", "Required Packages"]
    critical_passed = True
    
    for check_name, passed in results:
        if check_name in critical_checks:
            if passed:
                print_status(f"{check_name}: PASSED", "success")
            else:
                print_status(f"{check_name}: FAILED", "error")
                critical_passed = False
        else:
            if passed:
                print_status(f"{check_name}: PASSED", "success")
            else:
                print_status(f"{check_name}: FAILED (non-critical)", "warning")
    
    print("\n" + "=" * 60)
    
    if critical_passed:
        print_status("🎉 Installation verification PASSED! You're ready to start.", "success")
        print_status("Next steps:", "info")
        print("   1. Read docs/tutorials/ for beginner guides")
        print("   2. Try scripts/examples/ for sample code")
        print("   3. Check docs/paper_summaries/ for research background")
        return 0
    else:
        print_status("❌ Installation verification FAILED!", "error")
        print_status("Please fix the critical issues above before continuing.", "error")
        return 1

if __name__ == "__main__":
    sys.exit(main())