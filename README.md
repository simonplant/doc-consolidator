## The Document Consolidation System

An AI-powered system designed to process multiple work-in-progress documents and synthesize them into a single, coherent, and polished master document.

## 1. Overview

This project provides a robust framework for tackling information chaos. It takes a collection of scattered notes, drafts, and outlines and uses a multi-step AI process to analyze, score, organize, write, and edit the content. The system identifies the strongest ideas, tracks their evolution, resolves conflicts, and produces a final, high-quality document along with a suite of transparency reports.

This system is built for developers, writers, researchers, and teams who need to consolidate knowledge from multiple unstructured sources into a single source of truth.

## 2. Features

- **AI-Powered Synthesis:** Leverages Large Language Models to perform deep semantic analysis and content generation.
    
- **Configurable AI Persona:** Easily configure the AI's role, writing style, and decision-making approach to match your project's needs.
    
- **Idea Strength Scoring:** A weighted algorithm scores concepts based on frequency, development, connectivity, and recency to ensure the most important ideas are preserved.
    
- **Conflict & Gap Detection:** Automatically identifies contradictions and information gaps between source documents, flagging them for resolution.
    
- **Human-in-the-Loop Workflow:** Includes a mandatory checkpoint for human review and approval of the proposed document structure before the final draft is written.
    
- **Comprehensive Output Package:** Delivers not just the final document, but also an executive summary, a synthesis report, a list of unresolved issues, and a gap analysis.
    

## 3. System Architecture

The system is designed as an orchestrated multi-prompt architecture, ensuring modularity and robustness.

1. **Control Layer:** An external script (e.g., `consolidate.py`) that manages the end-to-end process. It handles file I/O, runs the prompt sequence, manages state, and handles errors.
    
2. **AI Processing Layer:** A series of five distinct, chained prompts that perform the core logic:
    
    - **Prompt 1:** Analysis & Scoring
        
    - **Prompt 2:** Structure Proposal (TOC Generation)
        
    - **Prompt 3:** Content Synthesis
        
    - **Prompt 4:** Final Editing & QA
        
    - **Prompt 5:** Final Output Generation
        
3. **Visualization Layer (Optional):** The system generates structured data (JSON, Mermaid.js syntax) that can be used by external tools to create visual artifacts like concept maps and charts.
    

For a complete breakdown of the system's design, see the [Document Consolidation Master Algorithm](https://gemini.google.com/app/doc-consolidation-algorithm.md "null").

## 4. Getting Started

### Prerequisites

- Python 3.8+
    
- An environment variable `API_KEY` with your AI provider's API key.
    

### Installation

1. Clone the repository:
    
    ```
    git clone https://github.com/your-username/doc-consolidator.git
    cd doc-consolidator
    ```
    
2. Install dependencies (if any):
    
    ```
    pip install -r requirements.txt
    ```
    

### Configuration

Before running the system, you must configure your project.

1. **Create a `config.json` file.** You can copy the provided `config.example.json`.
    
2. **Define the AI Persona:** Edit the `config.json` to set the AI's role, style, and biases.
    
    ```
    {
      "ai_persona": {
        "primary_role": "Technical Writer",
        "writing_style": "Formal",
        "decision_making_approach": "Balanced",
        "domain_expertise": "Software Engineering"
      },
      "processing_principles": {
        "transparency_level": "High",
        "conflict_resolution_bias": "Recency",
        "gap_handling": "Flag"
      }
    }
    ```
    
3. **Add Your Documents:** Place all your source files (`.txt`, `.md`, etc.) into the `/input` directory.
    

## 5. How to Run

Execute the consolidation process from your terminal using the main control script.

```
python consolidate.py --config config.json
```

The script will provide real-time updates on its progress, from analysis to the final output generation. It will pause and wait for your input during the "Review and Approve the Blueprint" step.

## 6. Understanding the Output Directory

Once the process is complete, the `/output` directory will be populated with the following:

- **`master_document.md`**: The final, polished document.
    
- **`executive_summary.md`**: A high-level, one-page summary.
    
- **`synthesis_report.md`**: A "making of" document explaining how the AI created the final version.
    
- **`editors_notes.md`**: A critical file listing any conflicts or ambiguities that require human review.
    
- **`gap_analysis.md`**: A to-do list identifying missing information.
    
- **`/supplementary`**: A folder containing structured data outputs (JSON, Mermaid syntax) for visualization.
    

## 7. How to Contribute

Contributions are welcome! Whether it's improving the control script, refining the prompts, or adding new features, your input is valuable. Please follow these steps:

1. Fork the repository.
    
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
    
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
    
4. Push to the branch (`git push origin feature/AmazingFeature`).
    
5. Open a Pull Request.
    

Please read the [Master Algorithm](https://gemini.google.com/app/doc-consolidation-algorithm.md "null") to understand the core design principles before making significant changes.