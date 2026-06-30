# Developlan AI Engineering Stories

---

## Story 002.1
### AI Investigation Engine

### Objective

Replace static page classification with AI-guided investigation.

The engine should investigate a page, determine its type, identify promising next actions, ignore irrelevant navigation, and continue until sufficient evidence has been collected to identify an opportunity or conclude that none exists.

### Success Criteria

- AI decides what a page represents.
- AI proposes next links to investigate.
- AI ignores privacy, support, login and similar pages.
- Investigation can recurse.
- Investigation stops when evidence is sufficient.
- Demonstrable on UN Partner Portal.

Status:
IN PROGRESS

---

## Story 002.2
### Investigation Orchestrator

### Objective

Create an orchestration layer that manages an investigation lifecycle without performing business reasoning.

Reasoning remains the responsibility of the AI Investigation Engine.

### Success Criteria

- Creates and returns an Investigation object.
- Calls page acquisition and AI page investigation.
- Maintains visited URLs.
- Maintains candidate and completed actions.
- Prioritises high, medium and low actions.
- Prevents revisiting URLs.
- Stops when evidence is complete, limits are reached or no actions remain.

Status:
COMPLETE

---

## Story 002.3
### Investigation Memory

### Objective

Enable the AI Investigator to reason over accumulated investigation memory rather than only the current page.

### Inputs

- Completed page investigations
- Observations
- Active hypotheses
- Reasoning history

### Outputs

- Updated Investigation memory
- Observations
- Hypotheses
- Rejected hypotheses
- Memory context for subsequent page investigations

### Acceptance Criteria

- Each page investigation adds an observation.
- Reasoning history is retained.
- Active and rejected hypotheses are tracked simply.
- The AI Investigator receives compact memory context.
- No persistent storage is introduced.

### Out Of Scope

- Capability matching
- Opportunity scoring
- Proposal generation
- Multi-agent reasoning
- Persistent storage

Status:
IN REVIEW

---

## Story 002.4
### Investigation Completion & Opportunity Handoff

### Objective

Stabilise the investigation lifecycle and hand off a discovered opportunity page into the existing analysis workflow.

### Inputs

- Start URL
- Completed Investigation
- Investigation evidence
- Opportunity-classified page package

### Outputs

- Completed Investigation object
- Final investigation status
- Selected opportunity package
- Opportunity source URL
- Investigation context attached to the analysis response

### Acceptance Criteria

- Investigation can start from a portal or listing page.
- Investigation follows AI-selected actions by priority.
- Investigation does not revisit URLs.
- Investigation stops for a clear reason.
- The analyse workflow uses the opportunity page discovered by the investigation.
- Non-opportunity investigations return investigation state without triggering document processing.
- Opportunity pages proceed into the existing download and extraction flow.

### Out Of Scope

- Capability matching
- Bid/no-bid recommendations
- Proposal generation
- Persistent storage
- Multi-agent workflows
- Ranking multiple viable opportunities

Status:
PLANNED

---

## Story 002.5
### Supporting Document Acquisition

### Objective

Ensure supporting documents from the discovered opportunity are downloaded and extracted as part of the investigation-driven workflow.

### Inputs

- Selected opportunity package
- Existing document discovery
- Existing download logic
- Existing extraction logic

### Outputs

- Downloaded supporting documents
- Extracted document text
- Updated opportunity package
- Evidence corpus ready for intelligence analysis

### Acceptance Criteria

- Documents linked from the discovered opportunity page are downloaded.
- Supported document types are extracted.
- Missing or unavailable documents do not break the workflow.
- The evidence corpus includes webpage text and extracted supporting documents.
- Existing document acquisition behaviour is preserved.

### Out Of Scope

- Recursive document discovery
- Document quality scoring
- OCR improvements
- Long-term evidence storage
- Proposal document generation

Status:
PLANNED

---

## Story 002.6
### Opportunity Intelligence Package

### Objective

Produce a structured Opportunity Intelligence package from the discovered opportunity and its supporting evidence.

### Inputs

- Completed Investigation
- Opportunity package
- Evidence corpus
- Existing Opportunity Intelligence Engine

### Outputs

- Structured opportunity profile
- Investigation summary
- Evidence summary
- Unknowns and risks identified by the existing intelligence engine

### Acceptance Criteria

- The final analyse response contains the investigation, opportunity package and structured profile.
- The profile is generated from the full available evidence corpus.
- The output is suitable for executive opportunity review.
- Unknowns remain explicit rather than guessed.
- No capability matching or bid recommendation is introduced.

### Out Of Scope

- Strategic assessment
- Organisation-specific fit analysis
- Consortium recommendations
- Proposition design
- Proposal writing

Status:
PLANNED

---

## Milestone M2
### End-to-End Investigation Demonstration

### Objective

Demonstrate a complete Sprint 002 workflow from opportunity landscape investigation to structured Opportunity Intelligence package.

### Acceptance Criteria

- The workflow starts from a landscape page rather than a known opportunity detail page.
- The investigation path is visible through visited URLs, actions, reasoning history and observations.
- A genuine opportunity is discovered or a clear no-opportunity conclusion is returned.
- Supporting documents are extracted when available.
- A structured Opportunity Intelligence package is produced for a discovered opportunity.

Status:
PLANNED
