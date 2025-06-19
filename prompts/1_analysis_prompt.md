// FILENAME: prompts/1_analysis_prompt.md
Prompt 1: Document Corpus Analysis, Scoring, and Reporting

## 1. ROLE AND GOAL

**Your Role:** You are a {ai_persona}.

**Your Primary Goal:** Analyze the entire provided document corpus to identify, score, and classify all key concepts, ideas, and data points. You will then produce a detailed, structured JSON object containing your complete analysis. This output is critical as it will be the foundation for all subsequent steps in creating a master document.

**Your Processing Principles:** You will operate based on these principles: {processing_principles}.

## 2. INPUT DATA

You will be provided with a collection of documents in a JSON array format.

"[...documents...]"

## 3. CORE TASK: ANALYSIS & SCORING

Perform the following analysis steps across the ENTIRE document corpus:

### Step 1: Concept Extraction and Temporal Analysis
* Read and understand the content of ALL provided documents.
* Identify all significant concepts, ideas, proposals, facts, and key terms.
* For each concept, track its evolution based on document timestamps.

### Step 2: Idea Strength Scoring
For each unique concept you identify, calculate a composite `idea_strength_score` on a scale of 0-100 based on: Frequency (25%), Development (30%), Connectivity (20%), and Recency (25%).

### Step 3: Conflict and Gap Identification
* Identify any direct contradictions between documents.
* Identify logical gaps where information is missing.

## 4. OUTPUT REQUIREMENT: STRUCTURED JSON

Your final output for this prompt **MUST** be a single, valid JSON object, and nothing else.

```json
{
  "analysis_summary": {
    "documents_processed": 0,
    "total_concepts_identified": 0,
    "total_conflicts_found": 0,
    "total_gaps_found": 0
  },
  "concepts": [
    {
      "concept_id": "concept_001",
      "concept_name": "Example Concept",
      "description": "A one-sentence summary.",
      "category": "Core Concept | Supporting Idea | Exploratory Thought | Deprecated Content",
      "idea_strength_score": 95,
      "scoring_justification": {
        "frequency": "Appears frequently",
        "development": "Well-developed with examples",
        "connectivity": "Connects to multiple other ideas",
        "recency": "Mentioned in the latest documents"
      },
      "evolution_timeline": [{"doc_id": "doc.txt", "timestamp": "...", "summary_of_mention": "..."}],
      "source_passages": [{"doc_id": "doc.txt", "passage": "..."}]
    }
  ],
  "conflicts": [
    {
      "conflict_id": "conflict_001",
      "description": "Description of the conflict.",
      "conflicting_documents": [{"doc_id": "doc1.txt", "conflicting_passage": "..."}, {"doc_id": "doc2.txt", "conflicting_passage": "..."}],
      "proposed_resolution": "Recommended resolution.",
      "resolution_confidence": "High | Medium | Low",
      "requires_human_review": false
    }
  ],
  "gaps": [
    {
      "gap_id": "gap_001",
      "description": "Description of the missing information.",
      "relevant_concepts": ["concept_001"],
      "source_documents": ["doc1.txt"],
      "potential_resolution": "Suggestion on how to resolve the gap."
    }
  ]
}
```
