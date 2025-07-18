# Essential Papers for Literature Review

## Priority 1: Core Adversarial LLM Papers

### Jailbreaking & Red-Teaming
1. **"Universal and Transferable Adversarial Attacks on Aligned Language Models"** (Zou et al., 2023)
   - Key contribution: GCG attack method
   - Relevance: Baseline for automated jailbreaking

2. **"Red Teaming Language Models with Language Models"** (Perez et al., 2022)
   - Key contribution: Using LLMs to find LLM failures
   - Relevance: Similar approach but without RL

3. **"Jailbroken: How Does LLM Safety Training Fail?"** (Wei et al., 2023)
   - Key contribution: Taxonomy of jailbreak types
   - Relevance: Understanding attack surfaces

### RL for LLMs
4. **"Training Language Models to Follow Instructions with Human Feedback"** (Ouyang et al., 2022)
   - Key contribution: RLHF methodology
   - Relevance: RL training framework

5. **"Direct Preference Optimization"** (Rafailov et al., 2023)
   - Key contribution: Simpler alternative to RLHF
   - Relevance: Potential training method

## Priority 2: Related Adversarial ML

### GAN-inspired Approaches
6. **"Adversarial Training for Free!"** (Shafahi et al., 2019)
   - Key contribution: Efficient adversarial training
   - Relevance: Computational efficiency ideas

7. **"Generating Natural Adversarial Examples"** (Zhao et al., 2018)
   - Key contribution: Natural-looking adversarial examples
   - Relevance: Stealth in jailbreaks

### Safety & Alignment
8. **"Constitutional AI"** (Bai et al., 2022)
   - Key contribution: Self-supervised safety training
   - Relevance: Understanding defense mechanisms

9. **"The Alignment Problem from a Deep Learning Perspective"** (Ngo et al., 2023)
   - Key contribution: Theoretical framework
   - Relevance: Understanding fundamental challenges

## Priority 3: Technical Background

### RL Algorithms
10. **"Proximal Policy Optimization Algorithms"** (Schulman et al., 2017)
    - Key contribution: PPO algorithm
    - Relevance: Potential RL method

11. **"Group Robust Policy Optimization"** (GRPO paper - need exact citation)
    - Key contribution: GRPO algorithm
    - Relevance: Mentioned training method

### Evaluation Methods
12. **"Evaluating Large Language Models Trained on Code"** (Chen et al., 2021)
    - Key contribution: Evaluation framework
    - Relevance: Metric design ideas

## Reading Strategy
1. Start with papers 1-3 for jailbreaking context
2. Review papers 4-5 for RL methodology
3. Skim others based on specific needs

## Notes Template
For each paper, document:
- Core contribution
- Methodology
- Results & limitations
- Relevance to our work
- Ideas to incorporate/improve