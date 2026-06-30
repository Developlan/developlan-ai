# Developlan AI
## Current Sprint

Sprint: 002

Status: Active

---

# Sprint Title

AI Investigation Engine

---

# Story Status

Story 002.2 — Investigation Orchestrator: COMPLETE

Story 002.3 — Investigation Memory: IN REVIEW

Story 002.4 — Investigation Completion & Opportunity Handoff: PLANNED

Story 002.5 — Supporting Document Acquisition: PLANNED

Story 002.6 — Opportunity Intelligence Package: PLANNED

Milestone M2 — End-to-End Investigation Demonstration: PLANNED

---

# Objective

Transform the current acquisition engine into an intelligent investigation engine.

The system should no longer simply identify whether a page is a portal, listing or opportunity.

It should actively investigate opportunity ecosystems and determine what should be explored next.

---

# Business Goal

Increase the intelligence of opportunity discovery.

The platform should begin behaving like an experienced Business Development specialist rather than a web scraper.

---

# Current State

Implemented

✓ Page acquisition

✓ Playwright rendering

✓ HTML capture

✓ Text extraction

✓ Opportunity document discovery

✓ Portal detection

✓ Listing detection

✓ Opportunity detection

✓ Investigation Orchestrator

---

# This Sprint

Implement AI-driven investigation.

When a page is acquired the system should decide:

- What type of page is this?
- Is further investigation required?
- Which links deserve investigation?
- Which links should be ignored?
- Is this the actual opportunity?
- Is this part of a wider opportunity ecosystem?

The result should be an investigation plan rather than a simple page classification.

---

# Acceptance Criteria

The platform should be able to:

• distinguish portal pages

• distinguish listing pages

• distinguish opportunity pages

• identify candidate opportunity links

• ignore navigation

• ignore help/privacy/resources

• rank investigation priority

• recursively investigate selected pages

• stop when sufficient evidence has been collected

---

# Constraints

Do not break existing acquisition.

Preserve current API behaviour where practical.

Prefer GPT reasoning over large rule sets.

Avoid hard-coded donor-specific logic unless absolutely necessary.

---

# Deliverables

New Investigation Engine

AI Investigation Prompt

Investigation Planner

Recursive Investigation Controller

Updated Analyse Workflow

---

# Out of Scope

Proposal generation

Capability matching

Strategic assessment

Qdrant ingestion

These belong to future sprints.

---

# Definition of Done

The prototype can start from a portal homepage and intelligently locate genuine funding opportunities without relying on manually written navigation rules.

---

# Engineering Notes

Prefer reasoning.

Avoid deterministic scraping where AI investigation produces materially better results.

Every implementation decision should increase the intelligence of the platform.
