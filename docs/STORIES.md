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
