# Installation Guide

This guide will help you set up the development environment for the jailbreak RL project.

## Prerequisites

### System Requirements
- **Python 3.8+** (Python 3.9+ recommended)
- **Git** for version control
- **CUDA** (optional, for GPU acceleration)
- **At least 8GB RAM** (16GB+ recommended)

### Check Your Setup
```bash
python --version  # Should show 3.8+
pip --version     # Should be installed
git --version     # Should be installed
```

## Quick Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd jailbreak-rl
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install basic requirements
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

### 4. Verify Installation
```bash
# Run basic tests
python -m pytest tests/

# Check imports work
python -c "import torch; import transformers; print('All imports successful!')"
```

## Detailed Setup

### Virtual Environment Management

#### Why Use Virtual Environments?
- Isolates project dependencies
- Prevents conflicts with other projects
- Makes sharing easier

#### Managing Your Environment
```bash
# Activate environment
source venv/bin/activate

# Check active environment
which python  # Should point to venv/bin/python

# Install packages
pip install package_name

# Save current packages
pip freeze > requirements.txt

# Deactivate when done
deactivate
```

### GPU Setup (Optional)

#### CUDA Installation
If you have an NVIDIA GPU, install CUDA support:

```bash
# Check if CUDA is available
python -c "import torch; print(torch.cuda.is_available())"

# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Verify GPU Setup
```bash
python -c "import torch; print(f'GPU available: {torch.cuda.is_available()}')"
python -c "import torch; print(f'GPU count: {torch.cuda.device_count()}')"
```

### Development Tools

#### Code Editor Setup
Recommended extensions for VS Code:
- Python
- Pylance
- Black Formatter
- autoDocstring

#### Git Configuration
```bash
# Set up git (if not already done)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Create .gitignore (already provided)
```

## Dependencies Explained

### Core Libraries
- **torch**: Deep learning framework
- **transformers**: Hugging Face library for LLMs
- **numpy**: Numerical computing
- **pandas**: Data manipulation
- **matplotlib**: Plotting and visualization

### RL Libraries
- **ray[rllib]**: Distributed RL framework
- **gym**: RL environments
- **stable-baselines3**: RL algorithms

### Utilities
- **wandb**: Experiment tracking
- **tqdm**: Progress bars
- **pytest**: Testing framework
- **black**: Code formatting

## Common Issues & Solutions

### Issue: Python Version Too Old
```bash
# Update Python (on macOS with Homebrew)
brew install python@3.9

# Update Python (on Ubuntu)
sudo apt update
sudo apt install python3.9
```

### Issue: CUDA Not Found
```bash
# Check CUDA installation
nvidia-smi

# Install CUDA toolkit
# Follow instructions at: https://developer.nvidia.com/cuda-downloads
```

### Issue: Out of Memory
```bash
# Monitor memory usage
htop  # or top on macOS

# Reduce batch size in configs
# Use gradient accumulation
# Use smaller models for testing
```

### Issue: Package Conflicts
```bash
# Create fresh environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing Your Setup

### Basic Functionality Test
```bash
# Run this script to test basic functionality
python scripts/test_setup.py
```

### Model Download Test
```bash
# Test downloading a small model
python -c "
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModel.from_pretrained('gpt2')
print('Model download successful!')
"
```

### GPU Memory Test
```bash
# Test GPU memory allocation
python -c "
import torch
if torch.cuda.is_available():
    x = torch.randn(1000, 1000).cuda()
    print(f'GPU memory allocated: {torch.cuda.memory_allocated()/1e9:.2f}GB')
else:
    print('GPU not available')
"
```

## Next Steps

### After Installation
1. **Read the Documentation**: Check `docs/tutorials/` for beginner guides
2. **Run Examples**: Try scripts in `scripts/examples/`
3. **Explore the Code**: Look at `src/` structure
4. **Set Up Experiment Tracking**: Configure Weights & Biases

### Development Workflow
1. **Activate Environment**: `source venv/bin/activate`
2. **Make Changes**: Edit code in `src/`
3. **Run Tests**: `python -m pytest`
4. **Format Code**: `black src/`
5. **Commit Changes**: `git commit -m "Description"`

### Getting Help
- **Documentation**: Check `docs/` for detailed guides
- **Code Examples**: Look at `scripts/examples/`
- **Troubleshooting**: See this file's "Common Issues" section
- **Research Questions**: Use the professor mode guidance in `CLAUDE.md`

## Environment Variables

Create a `.env` file in the project root:
```bash
# API keys (optional)
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here

# Weights & Biases (optional)
WANDB_API_KEY=your_key_here
WANDB_PROJECT=jailbreak-rl

# Paths
DATA_DIR=./data
RESULTS_DIR=./results
MODELS_DIR=./models
```

## Final Verification

Run this comprehensive test:
```bash
python scripts/verify_installation.py
```

This should output:
- ✅ Python version OK
- ✅ Required packages installed
- ✅ GPU available (if applicable)
- ✅ Model download works
- ✅ Basic functionality works

You're now ready to start working on the jailbreak RL project!