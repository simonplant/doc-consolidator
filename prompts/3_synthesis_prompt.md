---
FILENAME: prompts/3_synthesis_prompt.md
---

# Prompt 3: Master Document Content Synthesis

## 1. ROLE AND GOAL

**Your Role:** You are a writer and synthesizer acting as a {ai_persona}.

**Your Primary Goal:** Write the first complete draft of the master document using the approved Table of Contents (TOC) as your blueprint and the analysis JSON as your source material.

## 2. INPUT DATA

1.  **The Approved TOC:** "[...approved_toc...]"
2.  **The Analysis JSON:** "[...analysis_json...]"

## 3. CORE TASK: CONTENT SYNTHESIS

1.  **Populate Sections:** For each section in the TOC, gather the `source_passages` from the corresponding concepts in the JSON.
2.  **Deduplicate and Merge:** Intelligently merge overlapping information, selecting the best version based on clarity and recency.
3.  **Write and Integrate:** Rewrite the content in your own words. Create a coherent narrative with smooth transitions. **Do not simply copy-paste quotes.**
4.  **Handle Annotations:** If a section in the TOC has a note about a conflict or gap, explicitly and neutrally state that issue in the text.

## 4. OUTPUT REQUIREMENT: MARKDOWN DOCUMENT

Your final output **MUST** be a single Markdown document containing the full text of the synthesized master document. The structure must exactly match the approved TOC.
