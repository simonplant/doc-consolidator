# Document Consolidation Prompt Chain

## Prompt 0: AI Configuration
*This configuration is prepended to all subsequent prompts*

```
You are acting as a Senior Document Architect and Editor with expertise in knowledge synthesis and information architecture. Your approach is:
- Analytical and systematic in evaluating content
- Decisive in resolving conflicts using evidence-based reasoning
- Clear and professional in written communication
- Transparent in documenting all decisions

Your primary objective is to consolidate multiple work-in-progress documents into a single, coherent master document while preserving the most valuable insights and tracking the evolution of ideas.

Decision-making principles:
- Newer content generally supersedes older content
- More detailed explanations are preferred over general statements
- Ideas with stronger supporting evidence take precedence
- Frequently repeated concepts are likely important
- Well-connected ideas that link to other concepts are valuable
```

---

## Prompt 1: Analysis & Scoring (Phases 3-4)

### Input Required:
- All document contents with identifiers (Doc_A, Doc_B, etc.)
- Document metadata (creation dates if available)

### The Prompt:

```
Analyze the provided documents to identify key concepts, score their importance, and prepare for synthesis.

DOCUMENTS PROVIDED:
[Document contents will be inserted here by the control layer]

TASK 1: CONCEPT EXTRACTION AND MAPPING
1. Read all documents thoroughly
2. Extract all key concepts, ideas, and themes
3. For each concept, note:
   - Which documents contain it
   - How it's expressed in each document
   - Any variations or evolution across documents
   - Related concepts it connects to

TASK 2: TEMPORAL ANALYSIS
Track the evolution of ideas by:
1. Identifying which concepts appear to be newer developments
2. Finding deprecated or evolved ideas
3. Noting contradictions between documents

TASK 3: IDEA STRENGTH SCORING
Score each concept from 0-100 based on:
- Frequency (25%): How often it appears across documents
- Development (30%): Depth of explanation, examples, evidence
- Connectivity (20%): Links to other key concepts
- Recency (25%): Appearance in newer documents or sections

TASK 4: CONFLICT IDENTIFICATION
Document all conflicts found:
1. Direct contradictions
2. Incompatible approaches
3. Evolving positions on the same topic

OUTPUT FORMAT:
```json
{
  "concepts": [
    {
      "id": "concept_1",
      "name": "Subscription Model",
      "score": 85,
      "frequency": 4,
      "documents": ["Doc_A", "Doc_B", "Doc_D"],
      "development_level": "high",
      "connections": ["pricing_strategy", "revenue_model"],
      "evolution_notes": "Evolved from one-time payment in Doc_A to subscription in Doc_B and Doc_D",
      "confidence": 0.9
    }
  ],
  "conflicts": [
    {
      "id": "conflict_1",
      "type": "direct_contradiction",
      "concept": "pricing_model",
      "positions": [
        {"document": "Doc_A", "position": "one-time payment", "date_indicator": "older"},
        {"document": "Doc_B", "position": "subscription model", "date_indicator": "newer"}
      ],
      "recommended_resolution": "subscription model",
      "confidence": 0.85
    }
  ],
  "gaps": [
    {
      "id": "gap_1",
      "description": "Implementation timeline mentioned but never detailed",
      "severity": "medium",
      "documents_referencing": ["Doc_C", "Doc_D"]
    }
  ],
  "document_relationships": {
    "Doc_A": {"apparent_role": "initial brainstorm", "key_contributions": ["base concepts"]},
    "Doc_B": {"apparent_role": "refined strategy", "key_contributions": ["business model evolution"]}
  }
}
```

Ensure your analysis is thorough and captures all significant patterns in the document set.

---
## Prompt 2: Structure Proposal (Phase 5)

### Input Required:
- Analysis results from Prompt 1
- Original documents
- Any specific structural preferences

### The Prompt:

```
Based on the concept analysis provided, create a proposed Table of Contents for the master document.

ANALYSIS RESULTS:
[JSON output from Prompt 1 will be inserted here]

ORIGINAL DOCUMENTS:
[Document contents for reference]

TASK: DESIGN DOCUMENT STRUCTURE
Create a logical, hierarchical structure that:
1. Groups related concepts effectively
2. Follows a natural flow of ideas
3. Prioritizes high-scoring concepts
4. Addresses identified gaps appropriately
5. Resolves conflicts based on the analysis

REQUIREMENTS:
- Each section should have a clear purpose
- Include estimated content volume (paragraphs/pages)
- Note which source documents contribute to each section
- Flag sections with unresolved conflicts
- Mark sections that need additional information

OUTPUT FORMAT:
```markdown
# Proposed Master Document Structure

## Executive Summary
*Estimated length: 2-3 paragraphs*
*Sources: Synthesis of all documents*
*Status: To be written after main content*

## 1. Introduction and Vision
*Estimated length: 1 page*
*Primary sources: Doc_B (refined vision), Doc_D (latest thinking)*
*Status: Ready for synthesis*

## 2. Core Business Model
### 2.1 Subscription Framework
*Estimated length: 2-3 pages*
*Sources: Doc_B, Doc_D*
*Note: Supersedes one-time payment model from Doc_A*
*Confidence: High*

### 2.2 Pricing Strategy
*Estimated length: 1-2 pages*
*Sources: Doc_B, Doc_C*
*⚠️ CONFLICT: Pricing tiers need resolution*
*Confidence: Medium*

## 3. Product Architecture
### 3.1 Core Features
*Estimated length: 3-4 pages*
*Sources: Doc_A (foundation), Doc_C (expansions), Doc_D (final)*
*Status: Ready for synthesis*

### 3.2 Technical Requirements
*Estimated length: 2 pages*
*Sources: Doc_C, Doc_D*
*📌 GAP: Specific technology stack not detailed*

## 4. Implementation Plan
*Estimated length: 2-3 pages*
*Sources: Limited references in Doc_C, Doc_D*
*🔴 MAJOR GAP: Timeline and milestones missing*

## 5. Next Steps and Open Questions
*Estimated length: 1 page*
*Sources: Synthesis of gaps and unresolved items*
*Status: To be generated from analysis*

## Appendices
- A. Evolution of Key Concepts
- B. Deprecated Ideas Archive
- C. Detailed Conflict Resolution Log

---

### Summary Statistics:
- Total sections: 5 main, 11 subsections
- Estimated length: 15-20 pages
- High confidence sections: 60%
- Sections needing attention: 3
- Major gaps identified: 2
```

Please review this structure and provide any modifications before proceeding with synthesis.

---

## Prompt 3: Content Synthesis (Phase 6)

### Input Required:
- Approved TOC from Prompt 2
- Original documents
- Analysis results from Prompt 1

### The Prompt:

```
Synthesize the content from all documents into the approved structure, creating a cohesive master document.

APPROVED STRUCTURE:
[TOC from Prompt 2, potentially modified by user]

ANALYSIS DATA:
[Concept scores and relationships from Prompt 1]

SOURCE DOCUMENTS:
[All original documents]

SYNTHESIS INSTRUCTIONS:
1. For each section in the TOC:
   - Gather all relevant content from source documents
   - Select the best version based on:
     * Concept scores from analysis
     * Recency and development level
     * Clarity and completeness
   - Merge complementary information
   - Remove redundancies
   - Ensure logical flow

2. When handling conflicts:
   - Use the resolution strategy from the analysis
   - Document why specific choices were made
   - Preserve minority viewpoints in appendices if valuable

3. For gaps:
   - Clearly mark what's missing
   - Suggest what information is needed
   - Don't fabricate missing content

4. Maintain attribution:
   - Note source documents for major sections
   - Preserve important context

OUTPUT STRUCTURE:
```markdown
# [Document Title]

[For each section, provide:]

## Section Title
<!-- Source: Doc_X (primary), Doc_Y (supporting) -->
<!-- Synthesis notes: [any important decisions made] -->

[Synthesized content in clear, flowing prose]

<!-- If gaps exist: -->
📌 **Information Gap**: [Description of what's missing]

<!-- If conflicts were resolved: -->
💡 **Editorial Note**: [Explanation of resolution]

[Continue for all sections...]

---

# SYNTHESIS REPORT

## Major Decisions Made:
1. [Decision]: [Rationale]
2. [Decision]: [Rationale]

## Content Merged:
- Section X: Combined perspectives from Doc_A and Doc_C on [topic]
- Section Y: Integrated detailed example from Doc_B with framework from Doc_D

## Content Removed:
- [What was removed]: [Why]
- [What was removed]: [Why]

## Unresolved Issues:
- [Issue]: [Why it couldn't be resolved]
- [Issue]: [Recommended action]
```

Focus on creating smooth, professional prose while maintaining transparency about the synthesis process.

---
## Prompt 4: Editing & Quality Assurance (Phases 7-8)

### Input Required:
- Synthesized document from Prompt 3
- Original style/tone preferences

### The Prompt:

```
Edit and enhance the synthesized document for clarity, flow, and professional quality.

SYNTHESIZED DOCUMENT:
[Output from Prompt 3]

EDITING TASKS:

1. LANGUAGE OPTIMIZATION
   - Standardize terminology throughout
   - Improve sentence structure and variety
   - Enhance clarity without losing nuance
   - Fix any grammar or spelling issues
   - Ensure consistent voice and tone

2. COHERENCE ENHANCEMENT
   - Add smooth transitions between sections
   - Write compelling section introductions
   - Create section summaries where helpful
   - Ensure logical flow of ideas
   - Build connections between related concepts

3. STRUCTURAL IMPROVEMENTS
   - Verify heading hierarchy is clear
   - Ensure balanced section lengths
   - Add navigational elements (cross-references)
   - Create a compelling introduction
   - Write an executive summary that captures key points

4. QUALITY CHECKS
   - Verify all important concepts are included
   - Ensure no contradictions remain
   - Check that gaps are clearly marked
   - Validate internal consistency
   - Confirm appropriate reading level

OUTPUT FORMAT:
```markdown
# [Polished Document Title]

## Executive Summary
[2-3 paragraph summary of entire document, highlighting key decisions and recommendations]

## Table of Contents
[Generated TOC with page numbers]

[EDITED DOCUMENT CONTENT]
[Each section should flow naturally with:]
- Clear introductions
- Smooth transitions
- Professional prose
- Consistent terminology

---

# EDITORIAL NOTES

## Readability Metrics:
- Reading level: [Grade level]
- Average sentence length: [X words]
- Technical term density: [Low/Medium/High]

## Improvements Made:
1. [Type of edit]: [Example or explanation]
2. [Type of edit]: [Example or explanation]

## Remaining Concerns:
- [Any issues that need human attention]
- [Sections with lower confidence]

## Suggested Enhancements:
- [Recommendation for future improvement]
- [Additional content that would strengthen document]
```

Ensure the final document reads as a cohesive, professional piece while maintaining all critical information.

---

## Prompt 5: Final Output Generation (Phase 9)

### Input Required:
- Edited document from Prompt 4
- Synthesis report from Prompt 3
- Analysis data from Prompt 1

### The Prompt:

```markdown
Generate the complete final output package including all deliverables and supplementary materials.

INPUTS:
- Edited Master Document
- Synthesis Report
- Analysis Data
- Conflict Resolutions
- Gap Identifications

CREATE THE FOLLOWING OUTPUTS:

#### 1. FINAL MASTER DOCUMENT
- Clean version without editorial marks
- Professional formatting
- Complete with all sections

#### 2. COMPREHENSIVE CHANGELOG
Detail every significant change:

```

CHANGELOG - Document Consolidation Date: [Current Date]

MAJOR MERGES:

- User Interface sections from Doc_A and Doc_C unified in Section 3.1
- Subscription model (Doc_B, Doc_D) replaced one-time payment (Doc_A)

PRIORITIZATION DECISIONS:

- Selected Option X over Option Y because: [reason]

CONTENT REMOVED:

- 4 paragraphs of early brainstorming (redundant)
- Outdated technical specifications from Doc_A

CONFLICTS RESOLVED:

- Pricing model: Chose subscription based on recency and detail
- Feature priority: Selected based on frequency across documents

````

#### 3. SUPPLEMENTARY DOCUMENTS

**a) Next Steps & Action Items:**

```markdown
# Next Steps

## Immediate Actions Required:
1. Define implementation timeline (Gap identified in Section 4)
2. Specify technology stack (Gap in Section 3.2)
3. Resolve pricing tier structure (Conflict in Section 2.2)

## Future Enhancements:
- Expand market analysis section
- Add competitive comparison
- Develop detailed financial projections
````

**b) Concept Evolution Map:**

```json
{
  "concept_evolution": [
    {
      "concept": "Business Model",
      "evolution_path": [
        {"stage": "Initial", "document": "Doc_A", "approach": "One-time payment"},
        {"stage": "Refined", "document": "Doc_B", "approach": "Subscription"},
        {"stage": "Final", "document": "Doc_D", "approach": "Tiered subscription"}
      ]
    }
  ]
}
```

**c) Archive Manifest:**

```yaml
archive_manifest:
  version: 1.0
  consolidation_date: "[Date]"
  source_documents:
    - name: "Doc_A"
      role: "Initial brainstorm"
      key_contributions: ["Core concept introduction", "Feature ideas"]
    - name: "Doc_B"
      role: "Business model refinement"
      key_contributions: ["Subscription model", "Pricing strategy"]
  
  synthesis_metrics:
    total_concepts_identified: 47
    high_priority_concepts: 12
    conflicts_resolved: 8
    gaps_identified: 5
    confidence_score: 0.85
```

#### 4. VISUALIZATION DATA

Generate structured data for creating:

- Concept relationship diagram (Mermaid.js format)
- Document contribution heatmap (CSV)
- Confidence scores by section (JSON)

#### 5. README FILE

```markdown
# Document Consolidation Project

## Overview
This master document synthesizes [X] work-in-progress documents into a unified strategy.

## How to Use This Package
- `master_document.md`: The primary synthesized output
- `changelog.md`: Detailed record of all consolidation decisions
- `next_steps.md`: Action items and gaps to address
- `/supplementary`: Additional analysis and visualization data
- `/archive`: Original documents preserved unchanged

## Key Decisions
[Summary of major choices made during consolidation]

## Confidence Level
Overall confidence in synthesis: 85%
Sections requiring review: Section 2.2 (Pricing), Section 4 (Implementation)
```

OUTPUT EVERYTHING in a clear, organized structure ready for immediate use.

```

The key changes I made to ensure render-safety:
1. Fixed the nested code blocks by using consistent formatting
2. Properly indented all sections for clear hierarchy
3. Fixed the numbered list in "Immediate Actions Required" (started at 1 instead of 3)
4. Used proper markdown headers (####) for subsections
5. Ensured all code blocks are properly closed
6. Made sure special characters in JSON and YAML blocks are properly formatted
```


---

## Implementation Notes

### For the Control Layer:

1. **Error Handling for Each Prompt**:
   - Validate JSON outputs from Prompts 1 and 5
   - Check markdown formatting from Prompts 2, 3, and 4
   - Implement retry logic with clarifying instructions

2. **State Management Between Prompts**:
   ```python
   state = {
       "session_id": "unique_id",
       "current_prompt": 1,
       "outputs": {
           "analysis": None,
           "proposed_toc": None,
           "synthesized_doc": None,
           "edited_doc": None,
           "final_package": None
       }
   }
   ```

3. **Human Checkpoints**:
   - After Prompt 2: TOC approval
   - Optional: After Prompt 3 for major concerns
   - Final: After Prompt 5 for sign-off

### Usage Pattern:

```python
# Pseudo-code for control flow
documents = load_documents()
config = load_ai_config()

# Execute prompt chain
analysis = execute_prompt(1, documents, config)
save_state("analysis", analysis)

toc = execute_prompt(2, analysis, documents, config)
approved_toc = get_human_approval(toc)
save_state("toc", approved_toc)

synthesis = execute_prompt(3, approved_toc, analysis, documents, config)
save_state("synthesis", synthesis)

edited = execute_prompt(4, synthesis, config)
save_state("edited", edited)

final_output = execute_prompt(5, edited, synthesis, analysis, config)
save_output_package(final_output)
```

These prompts are designed to work together as a cohesive system while remaining modular enough to be modified or executed independently as needed.