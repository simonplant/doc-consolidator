# Improved Document Consolidation Prompts - Life Planning Edition

## Critical Process Rules (MUST READ FIRST)

### 🛑 STOP BEHAVIORS:

1. **DO NOT** jump ahead in the process
2. **DO NOT** summarize or kill content - consolidate everything
3. **DO NOT** score based on frequency - score based on alignment to current vision
4. **DO NOT** analyze individual files - analyze concepts across ALL files
5. **DO NOT** assume the human has all the answers - this is a discovery process
6. **DO NOT** reorganize without explicit approval

### ✅ REQUIRED BEHAVIORS:

1. **FOLLOW** each prompt exactly as written
2. **PRESERVE** all content in appropriate sections or appendices
3. **PRIORITIZE** newest thinking over repeated old ideas
4. **FOCUS** on practical execution and income generation
5. **CREATE** parking lot documents for unresolved conflicts
6. **WAIT** for human approval before proceeding

---

## Enhanced Prompt 0: Context & Configuration

```
You are helping someone navigate a major life transition through document consolidation. This is a DISCOVERY process where they are figuring out "what should I do next with my life" after significant changes (divorce, job loss, career pivot).

CRITICAL CONTEXT:
- The human is in active discovery mode - they don't have all the answers
- Latest thinking is more valuable than frequently repeated old ideas
- ALL content must be preserved (main doc or appendices)
- Focus on income-generating opportunities and executable actions
- Old career paths (consulting, professional services) are DEAD - don't resurrect them
- Success = clear, simple, executable plan with high chance of success

YOUR APPROACH:
- Analytical but understanding this is life planning, not business planning
- Preserve everything - consolidate and organize, don't summarize and delete
- Recognize emotional evolution in documents
- Focus on practical next steps, not theoretical frameworks
- Create clear distinction between current thinking and archived ideas
```

---

## Enhanced Prompt 1: Analysis & Scoring (With Life Planning Focus)

````
Analyze ALL documents as a complete body of knowledge for life planning and transition. Read everything before scoring anything.

DOCUMENTS PROVIDED:
[All documents inserted here]

PRIMARY QUESTION BEING ANSWERED: "What should I do next with my life?"
CONTEXT: Post-divorce, post-redundancy, seeking financial sovereignty

TASK 1: COMPREHENSIVE CONCEPT EXTRACTION
Extract ALL concepts, opportunities, and ideas across ALL documents:
- Income opportunities (jobs, contracting, trading, AI ventures, etc.)
- Life strategies (where to live, how to reduce costs)
- Emotional insights and evolution
- Practical action items
- Dreams and aspirations

TASK 2: EVOLUTION TRACKING
Identify the journey of thinking:
- What ideas appeared early but were later abandoned?
- What new directions emerged in recent documents?
- What pivots occurred and why?
- What remains consistent throughout?

TASK 3: ALIGNMENT-BASED SCORING (NOT frequency-based)
Score each concept 0-100 based on:
- Alignment to Current Vision (40%): How well does this fit the latest thinking?
- Income Potential (30%): Can this generate cash flow soon?
- Executability (20%): How actionable is this right now?
- Evidence/Validation (10%): Is there proof this works?

CRITICAL: Latest thinking in newest documents should score higher than repeated old ideas!

TASK 4: CATEGORIZATION FOR ACTION
Classify ALL content into:
- ACTIVE PURSUIT: Aligned with current vision, executable now
- EXPERIMENTS: Worth testing but not proven
- PARKING LOT: Conflicts or needs more thought
- ARCHIVE: Old thinking to preserve but not pursue

OUTPUT FORMAT:
```json
{
  "current_situation": {
    "summary": "Brief overview of where the person is now",
    "key_constraints": ["List of limitations"],
    "key_assets": ["List of strengths/resources"]
  },
  "opportunities": {
    "immediate_income": [
      {
        "opportunity": "Trading",
        "current_income": "$11K/month",
        "score": 95,
        "evidence": "Already working",
        "next_actions": ["Scale up", "Systemize"]
      }
    ],
    "quick_wins": [...],
    "medium_term": [...],
    "experiments": [...]
  },
  "deprecated_paths": [
    {
      "path": "IT Consulting",
      "reason": "Market dead, 400K jobs lost",
      "documents_mentioning": ["Doc_A", "Doc_B"],
      "archive_status": "Move to appendix"
    }
  ],
  "evolution_summary": {
    "major_pivots": ["From consulting to AI solopreneur"],
    "consistent_themes": ["Financial sovereignty", "Location independence"],
    "emerging_directions": ["AI tools", "Content creation"]
  },
  "parking_lot": [
    {
      "conflict": "Fractional CTO vs full independence",
      "needs_resolution": true,
      "documents": ["Doc_C", "Doc_E"]
    }
  ]
}
````

DO NOT PROCEED TO STRUCTURE UNTIL THIS ANALYSIS IS COMPLETE AND APPROVED!

## Enhanced Prompt 2: Life-Focused Structure Proposal

```
Based on the analysis, create a structure that answers "What should I do next?" 
Focus on EXECUTABLE PLANS, not theoretical frameworks.

REQUIREMENTS:
1. Main document = Current actionable plan
2. Appendices = ALL other content organized thematically
3. Preserve EVERYTHING - no content deletion
4. Action-oriented sections

PROPOSED STRUCTURE TEMPLATE:

# Life Transition Master Plan

## Executive Summary: The Path Forward
*The answer to "What should I do next?"*

## Part 1: Current Reality & Immediate Actions

### 1.1 Situation Assessment
*Where I am now financially, personally, professionally*

### 1.2 Immediate Income Stabilization
*What's working now and how to protect/scale it*
- Trading income ($11K/month)
- Quick wins available now
- Expense optimization moves

### 1.3 30-Day Action Plan
*Concrete steps to take immediately*

## Part 2: Income Architecture Development

### 2.1 Active Income Streams
*Opportunities to pursue NOW*

### 2.2 Experiments Worth Testing
*Low-risk trials with upside potential*

### 2.3 Building Toward Sovereignty
*Medium-term plays for independence*

## Part 3: Life Design Decisions

### 3.1 Living Situation Optimization
### 3.2 Relationship & Support Structure
### 3.3 Health & Sustainability

## Part 4: Parking Lot - Decisions Needed
*Conflicts and unresolved questions requiring attention*

---

## APPENDICES (Preserving ALL Content)

### Appendix A: All Opportunities Master Table
| Opportunity | Type | Income Potential | Time to Revenue | Status |
|------------|------|------------------|-----------------|---------|
| [EVERY opportunity mentioned across ALL documents] |

### Appendix B: Evolution of Thinking
*Chronological journey through all documents*

### Appendix C: Deprecated Strategies Archive
*Old thinking preserved for reference*
- Professional services pivot
- Consulting frameworks
- Corporate return scenarios

### Appendix D: Detailed Financial Analysis
*All financial scenarios and calculations*

### Appendix E: Emotional Journey & Insights
*Personal growth and realizations*

### Appendix F: Resources & Tools Mentioned
*Everything referenced that might be useful*

### Appendix G: Raw Brainstorms & Ideas
*Unprocessed creative output*

STOP HERE AND WAIT FOR HUMAN APPROVAL OF THIS STRUCTURE!

## Enhanced Prompt 3: Full Content Synthesis

Synthesize ALL content according to the approved structure. 
CRITICAL: Include EVERYTHING somewhere - main doc or appendices.

SYNTHESIS RULES:
1. Main document gets CURRENT, ACTIONABLE content
2. Everything else goes in thematic appendices
3. NO SUMMARIZATION - use actual content
4. Preserve specific numbers, dates, examples
5. When in doubt, include rather than exclude

For the main document sections:
- Use latest thinking only
- Focus on executable next steps
- Include specific metrics and evidence
- Make it scannable for quick action

For appendices:
- Organize thematically, not by source document
- Include ALL opportunities in master table
- Preserve emotional journey and insights
- Keep old thinking clearly marked as "archived"

Mark conflicts for parking lot with:
📌 PARKING LOT: [Description of conflict needing resolution]

OUTPUT: Complete document with ALL content organized appropriately

---

## Process Improvements Based on Your Experience:

### 1. **Pre-Process Briefing**
Before starting, establish:
- Current life situation clearly
- What "success" looks like
- Which ideas are already deprecated
- Timeline urgency for income

### 2. **Checkpoint Questions**
After Analysis:
- "Does this capture your CURRENT vision, not old thinking?"
- "Are deprecated paths clearly marked for archival?"
- "Are all income opportunities identified?"

### 3. **Parking Lot Protocol**
Create a separate document for:
- Conflicts between documents
- Questions needing answers
- Ideas requiring more research
- Emotional processing needed

### 4. **Success Metrics**
The process succeeds when:
- You have a clear 30/60/90 day plan
- All opportunities are catalogued
- Income path is clear
- Nothing valuable is lost
- Old thinking is archived, not active

---

## Quick Reference Card for Humans

### When the AI goes off track:

1. **If it's summarizing instead of consolidating**:
   "Include ALL content - organize don't summarize. Everything goes in main doc or appendices."

2. **If it's scoring based on frequency**:
   "Score based on alignment to my CURRENT vision, not how often something appears."

3. **If it's jumping ahead**:
   "Stop. Follow only the current phase prompt. Don't anticipate next steps."

4. **If it's resurrecting old thinking**:
   "That's deprecated thinking. Archive it, don't activate it."

5. **If it's being too theoretical**:
   "Focus on executable actions and income generation, not frameworks."

### Your Control Phrases:
- "Stick to the prompt only"
- "All files are equal - analyze across all"
- "This is discovery, not documentation"
- "Archive old thinking, don't revive it"
- "Focus on answering: what should I do next?"
```