# Open Research Questions

## Fundamental Questions

### 1. Problem Formulation
- [ ] Is jailbreaking best modeled as a single-turn or multi-turn problem?
- [ ] Should we focus on specific harm categories or general jailbreaking?
- [ ] How do we balance exploration of new attacks vs exploiting known weaknesses?

### 2. Reward Design
- [ ] How to avoid reward hacking (e.g., generating gibberish that triggers keywords)?
- [ ] Should rewards be sparse (binary success) or dense (partial progress)?
- [ ] How to incorporate human feedback without manual annotation?

### 3. Generalization
- [ ] Will attacks learned on one model family transfer to others?
- [ ] Can we create a universal jailbreak model or need specialized ones?
- [ ] How does model size affect attack success?

## Technical Questions

### 1. Training Dynamics
- [ ] How to prevent mode collapse in attack strategies?
- [ ] What's the optimal ratio of exploration vs exploitation?
- [ ] Should we use population-based training?

### 2. Evaluation Metrics
- [ ] How to measure attack "novelty" objectively?
- [ ] What constitutes a "successful" jailbreak?
- [ ] How to evaluate stealth/detectability?

### 3. Computational Efficiency
- [ ] Can we use smaller proxy models for faster iteration?
- [ ] Is there a way to predict attack success without full generation?
- [ ] How to efficiently search the vast prompt space?

## Ethical & Safety Questions

### 1. Responsible Development
- [ ] How to prevent misuse of our attack model?
- [ ] Should we release model weights or just findings?
- [ ] What's our disclosure timeline for discovered vulnerabilities?

### 2. Broader Impact
- [ ] Could this accelerate an adversarial arms race?
- [ ] How might this change LLM deployment practices?
- [ ] What are the dual-use implications?

## Research Strategy Questions

### 1. Scope Definition
- [ ] Focus on text-only or multimodal jailbreaks?
- [ ] Target open-source or commercial models?
- [ ] Single language or multilingual attacks?

### 2. Baseline Comparisons
- [ ] What existing jailbreak methods should we benchmark against?
- [ ] How to fairly compare automated vs manual approaches?
- [ ] Should we include prompt engineering baselines?

### 3. Publication Strategy
- [ ] Target conference (NeurIPS, ICML, ACL) or journal?
- [ ] How much implementation detail to share?
- [ ] Coordinate with model providers before publication?