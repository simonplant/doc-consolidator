---
FILENAME: prompts/2_structure_prompt.md
---
# Prompt 2: Master Document Structure Proposal

## 1. ROLE AND GOAL

**Your Role:** You are an information architect acting as a {ai_persona}.

**Your Primary Goal:** Using the detailed analysis provided in the input JSON, design and propose a logical Table of Contents (TOC) for the new master document.

## 2. INPUT DATA

You will be provided with the complete JSON output from the analysis step.

"[...analysis_json...]"

## 3. CORE TASK: TABLE OF CONTENTS GENERATION

1.  **Identify Main Sections:** Use the `Core Concept`s with the highest `idea_strength_score` to form the main sections.
2.  **Define Subsections:** Use `Supporting Idea` and `Exploratory Thought` concepts for subsections.
3.  **Add Annotations:** For any section related to a conflict or gap, you **must** add a clear annotation. (e.g., `(Note: Relates to unresolved conflict...)`).

## 4. OUTPUT REQUIREMENT: MARKDOWN DOCUMENT

Your final output **MUST** be a single, clean Markdown document titled "Proposed Master Document Structure".

```markdown
# Proposed Master Document Structure

## Introduction

*A brief, generated overview of the document's purpose and key themes.*

---

## 1.0 Main Section Title
*Brief description of this section's content.*

### 1.1 Subsection Title
*Description of subsection. (Note: Relates to unresolved conflict...)*

---

## Appendix

### A.1 Unresolved Conflicts
*A bulleted list of all conflict descriptions.*

### A.2 Identified Gaps
*A bulleted list of all identified information gaps.*
```
