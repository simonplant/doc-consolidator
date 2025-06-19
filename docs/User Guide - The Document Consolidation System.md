
## 1. Introduction

Welcome! This guide explains how to use the automated Document Consolidation System. This system is designed to take a collection of your scattered, work-in-progress notes, drafts, and outlines and transform them into a single, coherent, and polished master document.

The process is a collaboration between you and an AI assistant. You provide the raw materials and key decisions, and the AI handles the heavy lifting of analysis, writing, and organization.

## 2. Getting Started: The Setup

Before you begin, you need to prepare your input and configure the AI.

### Step 1: Gather Your Documents

1. Locate all the source documents you want to consolidate.
    
2. Place them all into the designated `/input` folder. The system will read everything in this directory.
    

_Tip: The more context the AI has, the better. Include everything from rough notes to partial drafts._

### Step 2: Configure the AI's Personality

Before running the process, you need to tell the AI _how_ to behave. In the system's configuration file, you will set the following:

- **Primary Role:** Is the AI an `Editor`, a `Technical Writer`, or a `Creative Strategist`? This defines its overall approach.
    
- **Writing Style:** Should the final document be `Formal`, `Professional`, or `Conversational`?
    
- **Conflict Resolution Bias:** When ideas conflict, should the AI prefer the most `Recent` idea, the most `Frequent` one, or the one with the most `Depth`?
    

This configuration ensures the final output matches your desired tone and perspective.

## 3. Running the Process: The Automated Workflow

Once you've set up, you can kick off the automated process. The system will execute the following steps, with one crucial checkpoint for your review.

### Step 3: The AI Analyzes Everything

**(This is an automated step)**

The system will now run **Prompt 1**. The AI reads every document and performs a deep analysis to:

- Identify all the key ideas and concepts.
    
- Track how those ideas evolved over time.
    
- Score the strength of each idea based on its frequency, detail, and recency.
    
- Pinpoint any contradictions or information gaps.
    

All of this analysis is saved to a detailed JSON file in the `/processing` folder. You don't need to read this file, but it powers all subsequent steps.

### Step 4: Review and Approve the Blueprint (Your Key Task)

**(This is a manual checkpoint)**

The system will now run **Prompt 2** and present you with a single file: **`Proposed_Table_of_Contents.md`**.

**This is the most important step for you.** This document is the proposed blueprint for the final master document. You must:

1. **Review the Structure:** Do the main sections and subsections make sense? Is the flow logical?
    
2. **Check the Annotations:** The AI will have flagged sections that relate to conflicts or gaps (e.g., `(Note: Key data is missing)`).
    
3. **Approve or Edit:** You can approve the structure as-is or make changes directly in the Markdown file (reorder sections, rename titles, etc.).
    

The system will wait until you give your final approval on this structure.

## 4. Finalizing the Document

Once you approve the blueprint, the system will automatically complete the final steps.

### Step 5: The AI Writes and Edits the Draft

**(This is an automated step)**

The system now runs **Prompts 3 and 4**.

- First, the AI writes the full draft, using the approved structure as its guide and populating it with content synthesized from your original notes.
    
- Next, it performs a meticulous self-edit, refining the language, improving the flow, and ensuring a consistent, professional tone.
    

### Step 6: Receive Your Final Package

**(This is the final output)**

The system will run **Prompt 5** and deliver a complete package of documents to the `/output` folder.

## 5. Understanding Your Output

Your `/output` folder will contain several files designed for full transparency:

- **`master_document.md`**: This is the main event—the final, polished document ready for you to use.
    
- **`executive_summary.md`**: A high-level, one-page summary of the master document.
    
- **`synthesis_report.md`**: A "making of" document. It explains _how_ the AI created the final document, including which ideas it prioritized and why.
    
- **`editors_notes.md`**: A critical file listing any conflicts or ambiguities the AI could not resolve on its own. **Review this file first** to see what decisions still need a human touch.
    
- **`gap_analysis.md`**: A to-do list identifying any missing information the AI detected.
    

You have now successfully consolidated your documents! You can use the master document, address the items in the editor's notes, and plan your next steps based on the gap analysis.