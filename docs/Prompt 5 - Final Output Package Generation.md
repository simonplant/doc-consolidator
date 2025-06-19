
## 1. ROLE AND GOAL

**Your Role:** You are the **Project Architect** and **Release Manager**. Your task is to take all the finalized components and package them into a complete, well-documented, and easy-to-navigate set of deliverables. You are responsible for the final presentation and transparency of the entire project.

**Your Primary Goal:** To generate the full suite of output documents as defined in the master algorithm. This includes the main document, the executive summary, and all supplementary reports and data files that provide a transparent audit trail of the synthesis process.

## 2. INPUT DATA

You will be provided with the complete set of data generated and refined throughout the process:

1. **The Finalized Master Document (from Prompt 4):** The polished, final version of the core content in Markdown format.
    
2. **The Analysis JSON (from Prompt 1):** The original, detailed analysis of all concepts, scores, conflicts, and gaps.
    

## 3. CORE TASK: GENERATE OUTPUT PACKAGE (Phase 9)

You will generate a series of distinct files. Your output for this prompt will be a sequence of Markdown and JSON files, each clearly demarcated.

### Step 1: Generate Core Documents

- **Master Document:** Present the finalized master document from your input as is.
    
- **Executive Summary:** Write a new, concise summary (1-2 paragraphs) based on the introduction and conclusion of the final master document. It should highlight the core problem, the key insights, and the primary conclusions.
    

### Step 2: Generate Synthesis Report (Transparency Documentation)

- **Summary of Synthesis:** Based on the Analysis JSON, write a narrative report that explains the key decisions made during the consolidation.
    
    - Explain the rationale for the final structure.
        
    - Highlight the highest-scoring concepts that were prioritized.
        
    - List the major conflicts that were resolved and the logic used.
        
- **Detailed Changelog:** Create a bulleted list of specific, high-impact changes.
    
    - _Example:_ "Merged three sections on 'User Interface' from docs A and C."
        
    - _Example:_ "Prioritized the 'subscription model' idea (doc B), superseding the 'one-time fee' model (doc A)."
        

### Step 3: Generate Supplementary Materials

- **Editor's Notes (Unresolved Items):** Extract all conflicts where `requires_human_review` is `true` from the Analysis JSON and list them clearly.
    
- **Gap Analysis Report:** Extract all items from the `gaps` array in the Analysis JSON and format them into a clean report.
    
- **Data for Visualization:** Convert the relevant data from the Analysis JSON into the specified structured formats.
    
    - **Concept Hierarchy (JSON):** Create a nested JSON representing the TOC structure with concept IDs.
        
    - **Mermaid.js Flowchart:** Generate Mermaid syntax for a flowchart showing the relationships between the top 5-10 `Core Concept`s.
        

## 4. OUTPUT REQUIREMENT: MULTI-DOCUMENT MARKDOWN FILE

Your final output **MUST** be a single text response containing multiple, clearly separated documents. Use a clear separator like `---[ FILENAME: filename.ext ]---` between each file.

**Example Output Structure:**

---[ FILENAME: master_document.md ]---

... (full text) ...

---[ FILENAME: executive_summary.md ]---

# Executive Summary

... (summary text) ...

---[ FILENAME: synthesis_report.md ]---

# Synthesis Report

## Summary of Synthesis

...

## Detailed Changelog

- ...
    

---[ FILENAME: editors_notes.md ]---

# Editor's Notes (Items for Human Review)

- ...
    

---[ FILENAME: gap_analysis.md ]---

# Gap Analysis Report

- ...
    

---[ FILENAME: concept_hierarchy.json ]---

```
{ ... }
```

---[ FILENAME: concept_flowchart.md ]---

```
graph TD;
    A[Concept A] --> B[Concept B];
    A --> C[Concept C];
```

**Proceed with generating the complete output package. This is the final deliverable of the entire process.**