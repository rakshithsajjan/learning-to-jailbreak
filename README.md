# Jailbreak RL: Automated LLM Safety Testing

> **Research Project**: Using reinforcement learning to train adversarial agents for automated jailbreak testing of language models.

## 🎯 Project Overview

This project explores using RL algorithms (GRPO, PPO, DPO) to train language models as adversarial agents that can systematically discover vulnerabilities in other LLMs. Think of it as "AI vs AI" for safety testing.

### The Big Picture
- **Attack Agent**: RL-trained LLM that generates jailbreak prompts
- **Target Model**: LLM being tested for safety vulnerabilities  
- **Game**: Adversarial training where attack agent tries to find prompts that make target model produce harmful content

## 🚀 Quick Start

### For Complete Beginners

1. **Read the Professor's Guide**: Check out [`CLAUDE.md`](CLAUDE.md) for research philosophy and approach
2. **Understand the Literature**: Start with [`docs/paper_summaries/tier_s/`](docs/paper_summaries/tier_s/) for essential papers
3. **Learn the Basics**: Follow tutorials in [`docs/tutorials/`](docs/tutorials/)

### For Developers

1. **Setup Environment**: Follow [`docs/setup/installation.md`](docs/setup/installation.md)
2. **Run Examples**: Try scripts in [`scripts/examples/`](scripts/examples/)
3. **Explore Code**: Check out [`src/`](src/) directory structure

## 📚 Research Foundation

### Essential Papers (Tier S)
1. **GCG** - Universal adversarial attacks ([summary](docs/paper_summaries/tier_s/gcg_zou_2023.md))
2. **PAIR** - Automated jailbreak generation ([summary](docs/paper_summaries/tier_s/pair_chao_2023.md))
3. **Szegedy et al.** - Adversarial examples foundations ([summary](docs/paper_summaries/tier_s/szegedy_2013.md))
4. **Goodfellow et al.** - FGSM and adversarial training ([summary](docs/paper_summaries/tier_s/goodfellow_2014.md))

### Key Research Questions
1. Can RL agents find better jailbreaks than gradient-based methods?
2. How do we balance attack success with query efficiency?
3. What makes jailbreaks transfer between different models?
4. Can we use RL to generate defenses, not just attacks?

## 🏗️ Project Structure

```
jailbreak-rl/
├── 📖 docs/                    # All documentation
│   ├── paper_summaries/        # Detailed paper reviews
│   ├── tutorials/              # Step-by-step guides
│   ├── setup/                  # Installation guides
│   └── references/             # Literature references
├── 💻 src/                     # Source code
│   ├── models/                 # Attack & defense models
│   ├── algorithms/             # RL algorithms (GRPO, PPO, DPO)
│   ├── attacks/                # Attack strategies
│   ├── evaluation/             # Metrics and benchmarks
│   └── utils/                  # Helper functions
├── 📊 data/                    # Datasets and prompts
│   ├── prompts/                # Jailbreak prompts
│   ├── datasets/               # Training/evaluation data
│   └── examples/               # Sample inputs/outputs
├── 🧪 experiments/             # Experiment configs
├── 📈 results/                 # Experimental outputs
└── 🛠️ scripts/                 # Utility scripts
```

## 🎓 Learning Path

### Phase 1: Understanding (Week 1-2)
- [ ] Read professor's guidance in `CLAUDE.md`
- [ ] Study Tier S paper summaries
- [ ] Complete basic tutorials
- [ ] Understand adversarial examples concept

### Phase 2: Reproduction (Week 3-4)
- [ ] Implement GCG baseline
- [ ] Reproduce PAIR results
- [ ] Set up evaluation metrics
- [ ] Test on small models

### Phase 3: Innovation (Week 5-8)
- [ ] Design RL-based attack agent
- [ ] Implement GRPO/PPO algorithms
- [ ] Compare RL vs gradient methods
- [ ] Analyze transferability

### Phase 4: Research (Week 9-12)
- [ ] Novel RL techniques
- [ ] Defense mechanisms
- [ ] Evaluation frameworks
- [ ] Paper writing

## 🔬 Current Status

### ✅ Completed
- [x] Project structure setup
- [x] Comprehensive literature review (Tier S papers)
- [x] Beginner-friendly documentation
- [x] Research methodology defined

### 🔄 In Progress
- [ ] Tier A paper summaries
- [ ] Development environment setup
- [ ] Baseline implementation planning

### 📋 Next Steps
- [ ] Complete literature review
- [ ] Set up development environment
- [ ] Implement GCG baseline
- [ ] Design RL framework

## 🛠️ Technical Stack

### Core Technologies
- **Python 3.8+**: Primary language
- **PyTorch**: Deep learning framework
- **Transformers**: Hugging Face library
- **Ray/RLlib**: Reinforcement learning
- **Weights & Biases**: Experiment tracking

### Models & Algorithms
- **Attack Models**: Fine-tuned LLMs (GPT-2, LLaMA)
- **Target Models**: Various LLMs for testing
- **RL Algorithms**: GRPO, PPO, DPO
- **Baselines**: GCG, PAIR, manual methods

## 🔒 Ethical Guidelines

### Research Ethics
- **Defensive Only**: All research for safety improvement
- **No Deployment**: No harmful content generation
- **Responsible Disclosure**: Coordinate with model providers
- **Team Collaboration**: Work with safety researchers

### Safety Measures
- **Filtered Datasets**: Remove truly harmful content
- **Controlled Environment**: Isolated testing setup
- **Regular Audits**: Review research direction
- **Documentation**: Track all experiments

## 📞 Getting Help

### Resources
- **Literature**: Check `docs/paper_summaries/` for paper explanations
- **Tutorials**: Follow `docs/tutorials/` for step-by-step guides
- **Code**: Explore `src/` with detailed documentation
- **Progress**: Track work in `PROGRESS.md`

### Research Support
- **Professor Mode**: Use CLAUDE.md guidance for research questions
- **Daily Logs**: Document progress in `docs/daily_logs/`
- **Meeting Notes**: Record discussions in `docs/meeting_notes/`

## 🌟 Contributing

This is a research project focused on AI safety. Contributions should:
- Follow ethical guidelines
- Include proper documentation
- Add comprehensive tests
- Maintain research quality

## 📈 Success Metrics

### Technical Metrics
- **Attack Success Rate (ASR)**: % of successful jailbreaks
- **Attack Transferability Rate (ATR)**: Cross-model effectiveness
- **Novel Pattern Discovery (NPD)**: Finding new attack types
- **Query Efficiency**: Attacks per successful jailbreak

### Research Metrics
- **Literature Coverage**: Comprehensive paper reviews
- **Reproducibility**: Baseline method reproduction
- **Innovation**: Novel RL techniques developed
- **Impact**: Contributions to AI safety

---

**Remember**: This is defensive security research. The goal is to make AI systems safer, not to create harmful tools. Every experiment should contribute to our understanding of how to build more robust and aligned AI systems.