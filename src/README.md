# Source Code Directory

This directory contains all the implementation code for the jailbreak RL project.

## Directory Structure

### `/models/`
- **Attack Models**: RL agents that generate jailbreak prompts
- **Defense Models**: Target LLMs being tested
- **Base Classes**: Common interfaces and utilities

### `/algorithms/`
- **GRPO**: Gradient-based RL for policy optimization
- **PPO**: Proximal Policy Optimization
- **DPO**: Direct Preference Optimization
- **Custom**: Novel RL algorithms for jailbreak generation

### `/attacks/`
- **Baseline Methods**: GCG, PAIR, manual jailbreaks
- **RL Attacks**: Reinforcement learning-based attack strategies
- **Evaluation**: Attack success metrics and analysis

### `/evaluation/`
- **Metrics**: ASR, ATR, NPD calculation
- **Benchmarks**: Standard evaluation datasets
- **Analysis**: Statistical analysis and visualization

### `/utils/`
- **Data Loading**: Dataset utilities and preprocessing
- **Logging**: Experiment tracking and monitoring
- **Common**: Shared utility functions

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment: See `docs/setup/installation.md`
3. Run examples: Check `scripts/examples/`

## Code Style

- Follow PEP 8 for Python code
- Use type hints for all functions
- Document with docstrings
- Add unit tests for new functionality