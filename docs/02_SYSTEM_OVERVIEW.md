# Developlan AI
## System Overview

Version: 1.0

---

# Purpose

This document describes the current architecture of the Developlan AI Business Development Intelligence Platform.

The architecture is capability-driven rather than technology-driven.

Each component exists because it materially increases business development intelligence.

---

# High-Level Architecture

```
Capability Engine
        │
        ▼
Opportunity Intelligence Planner
        │
        ▼
Multi-Source Discovery Engine
        │
        ▼
AI Investigation Engine
        │
        ▼
Evidence Acquisition Engine
        │
        ▼
Opportunity Intelligence Engine
        │
        ▼
Strategic Assessment Engine
        │
        ▼
Proposition Engine
        │
        ▼
Proposal Development Engine
```

---

# Component Overview

## 1. Capability Engine

Purpose

Understand what an organisation is capable of delivering.

Outputs

- capability profile
- transferable capability
- adjacent capability
- geographic capability
- partnership capability

Status

Planned (existing prototype components available)

---

## 2. Opportunity Intelligence Planner

Purpose

Determine where the platform should search.

Examples

- UN Partner Portal
- Devex
- UNGM
- ADB CMS
- RSS
- email
- donor websites
- procurement portals

Status

Prototype

---

## 3. Multi-Source Discovery Engine

Purpose

Continuously monitor multiple opportunity ecosystems.

Responsibilities

- portal search
- website monitoring
- RSS monitoring
- email monitoring
- API integration
- authenticated portals

Status

Prototype

---

## 4. AI Investigation Engine

Purpose

Investigate opportunity ecosystems.

This component uses AI to decide:

- what deserves investigation
- what can be ignored
- which links are opportunities
- which pages are listings
- where additional evidence exists

This is the core intelligence layer.

Status

Current Sprint

---

## 5. Evidence Acquisition Engine

Purpose

Acquire every useful piece of evidence.

Examples

- webpage
- TOR
- annexes
- budget
- templates
- FAQs
- procurement documents

Status

Prototype

---

## 6. Opportunity Intelligence Engine

Purpose

Build an intelligent understanding of the opportunity.

Produces

- strategic assessment
- donor priorities
- mandatory requirements
- capability fit
- risks
- unknowns
- executive summary

Status

Working Prototype

---

## 7. Strategic Assessment Engine

Purpose

Compare opportunity intelligence against organisational capability.

Produces

- strategic fit
- capability stretch
- partnership recommendations
- competitiveness
- bid recommendation

Status

Planned

---

## 8. Proposition Engine

Purpose

Develop possible delivery models.

Examples

- consortium
- localisation strategy
- implementation approach
- technical methodology
- staffing concept

Status

Planned

---

## 9. Proposal Development Engine

Purpose

Convert proposition into proposal content.

Potential outputs

- executive summary
- technical approach
- staffing
- methodology
- workplan
- compliance matrix

Status

Planned

---

# Supporting Services

Current technologies

- FastAPI
- Docker
- Playwright
- OpenAI GPT-5.5
- Qdrant
- n8n

Future integrations

- Devex
- UNGM
- ADB CMS
- Google Workspace
- Email
- RSS
- CRM

---

# Engineering Principle

The system should become progressively more intelligent.

Every sprint should increase reasoning capability rather than simply increasing automation.

Automation supports intelligence.

Automation is not the objective.