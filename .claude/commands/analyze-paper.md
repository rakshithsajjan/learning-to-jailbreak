---
allowed-tools: [mcp__arxiv-mcp-server__search_papers, mcp__arxiv-mcp-server__download_paper, mcp__arxiv-mcp-server__read_paper, mcp__arxiv-mcp-server__list_papers]
description: Autonomously analyze research papers for jailbreak RL project
---

# Paper Analysis Workflow

## Target Paper
$ARGUMENTS

## Analysis Mission
Execute a comprehensive, autonomous analysis of the specified research paper for the jailbreak RL project. This workflow should run end-to-end without user intervention, following the established research methodology.

## Workflow Steps

### Step 1: Paper Acquisition
- If given arXiv ID (e.g., 2310.06987): Use `mcp__arxiv-mcp-server__download_paper` to download and convert
- If given local PDF path: Note that direct PDF reading fails - extract arXiv ID if possible and use MCP
- If given research topic: Search for relevant papers using `mcp__arxiv-mcp-server__search_papers`

### Step 2: Context Discovery
- Use `mcp__arxiv-mcp-server__search_papers` to get paper metadata
- Extract: title, authors, abstract, categories, publication date, relevance to adversarial ML

### Step 3: Content Analysis
- Use `mcp__arxiv-mcp-server__read_paper` to get full paper content in markdown
- Wait for PDF→markdown conversion to complete if needed
- Extract technical details, methodologies, experimental setup, results

### Step 4: Structured Analysis Output
Generate comprehensive analysis with these sections:

#### 🔑 Executive Summary
- 2-3 sentence TLDR of the paper's contribution
- Why it matters for jailbreak RL research

#### 📊 Key Contribution & Novel Insights
- What's new and important in this work
- Breakthrough insights or methodological advances
- How it differs from existing approaches

#### 🛠️ Technical Methods
- How the approach works (use beginner-friendly explanations)
- Core algorithms, architectures, or techniques
- Mathematical foundations (simplified where possible)
- Use analogies to explain complex concepts

#### 📈 Experimental Results & Benchmarks
- Quantitative findings and performance metrics
- Datasets used and experimental setup
- Comparison with baselines and state-of-the-art
- Statistical significance and reliability

#### 🎯 Research Relevance to Jailbreak RL Project
- Direct applications to current research
- How this work relates to adversarial LLM training
- Connections to RL algorithms (PPO, DPO, GRPO)
- Potential for integration with existing approaches

#### 🚀 Implementation Roadmap
- Concrete next steps for integration
- Code implementation priorities
- Experimental configurations to try
- Resource requirements and computational needs

#### 📋 Baseline Comparisons
- How this relates to existing methods (GCG, PAIR, etc.)
- Strengths and weaknesses compared to current approaches
- Performance comparisons where available

#### 🔮 Limitations & Future Work
- Acknowledged limitations in the paper
- Gaps and improvement opportunities
- Future research directions suggested by authors
- Potential extensions for jailbreak RL

### Step 5: Project Integration Recommendations
- Identify immediate applications to current research
- Suggest experimental configurations
- Propose hybrid approaches combining with RL methods
- Recommend baseline implementations
- Highlight defensive applications for AI safety

## Quality Assurance
- Verify paper relevance to jailbreak/adversarial ML research
- Cross-reference with existing project knowledge
- Provide confidence scores for key claims where appropriate
- Flag any contradictions with previous findings
- Suggest follow-up papers for deeper investigation

## Output Format
- Use clear markdown section headers
- Include bullet points for key insights
- Add code snippets where relevant
- Provide actionable next steps
- Structure for maximum research utility

## Execution Notes
- Run autonomously without user intervention
- Handle arXiv MCP conversion delays gracefully
- Provide progress updates for long-running conversions
- Generate consistent, structured output every time
- Focus on practical applications to jailbreak RL research

Execute this workflow completely and autonomously for the specified paper target.