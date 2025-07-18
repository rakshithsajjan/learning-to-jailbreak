# Core Research Ideas & Hypotheses

## Main Hypothesis
**RL-trained adversarial models can discover novel, transferable jailbreaks more efficiently than manual methods**

## Key Innovations

### 1. Adversarial Game Formulation
- **Attack Model**: RL-finetuned to maximize jailbreak success
- **Defense Model**: Target LLM with safety guardrails
- **Game Dynamics**: Continuous adaptation between attack and defense

### 2. Reward Engineering
- **Primary Signal**: Successful harmful content generation
- **Secondary Signals**: 
  - Novelty of attack patterns
  - Transferability across models
  - Stealth (avoiding obvious red flags)

### 3. Training Strategies
- **Curriculum Learning**: Start with easier targets, progressively harder
- **Multi-Model Training**: Train against diverse target models
- **Self-Play**: Attack model vs hardened versions of itself

## Potential Breakthroughs

1. **Automated Vulnerability Discovery**: Find unknown weaknesses systematically
2. **Defense Co-Evolution**: Generate stronger safety mechanisms
3. **Transferable Attack Patterns**: Discover universal jailbreak principles

## Technical Approaches to Explore

### RL Algorithms
- **GRPO**: Good for discrete action spaces
- **PPO**: Stable, widely used
- **DPO**: Direct preference optimization
- **REINFORCE**: Simple baseline

### Architecture Choices
- Base model selection (GPT-2, Llama, etc.)
- Parameter efficient finetuning (LoRA, QLoRA)
- Multi-agent setups

## Measurement & Evaluation
- Attack Success Rate (ASR)
- Attack Transferability Rate (ATR)
- Novel Pattern Discovery (NPD)
- Computational Efficiency