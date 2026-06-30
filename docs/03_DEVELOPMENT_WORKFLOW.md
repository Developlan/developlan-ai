# Developlan AI
## Development Workflow

Version: 1.0

---

# Purpose

This document defines how Developlan AI is engineered.

The objective is to maximise engineering quality, implementation speed and product intelligence.

Development should remain disciplined while allowing rapid iteration.

---

# Development Philosophy

The platform is developed using short engineering sprints.

Each sprint should produce a demonstrable increase in business development intelligence.

Working software is preferred over speculative architecture.

Every sprint should be capable of demonstration.

---

# Roles

## Product Architect (ChatGPT)

Responsible for:

- product direction
- intelligence design
- system architecture
- engineering stories
- acceptance criteria
- technical review
- design decisions
- sprint planning

Focus

Build the right product.

---

## Implementation Engineer (Codex)

Responsible for:

- writing code
- refactoring
- tests
- integration
- Docker updates
- API implementation
- documentation updates

Focus

Build the product correctly.

---

## Product Owner (Dave)

Responsible for:

- product vision
- commercial direction
- strategic decisions
- testing
- validation
- deployment
- sprint acceptance

Focus

Build the product customers need.

---

# Engineering Cycle

Each sprint follows the same process.

---

## Step 1

Define the Engineering Story.

Produced by ChatGPT.

Includes:

- objective
- rationale
- acceptance criteria
- affected modules
- constraints
- expected behaviour

---

## Step 2

Codex reviews:

- PROJECT_DOCTRINE
- PRODUCT_VISION
- SYSTEM_OVERVIEW
- CURRENT_SPRINT

Codex summarises understanding before making changes.

No code is written until the understanding is confirmed.

---

## Step 3

Codex implements the sprint.

Expected behaviour:

- modify existing code where possible
- avoid unnecessary complexity
- preserve existing functionality
- produce complete working files
- explain significant design decisions

---

## Step 4

Build and test on the VPS.

Testing includes:

- Docker build
- endpoint testing
- behavioural validation
- regression testing

The objective is to validate behaviour, not merely compilation.

---

## Step 5

Review.

Questions include:

- Does the behaviour improve platform intelligence?
- Does it satisfy the acceptance criteria?
- Does it align with the Project Doctrine?

---

## Step 6

Commit.

Update:

- CHANGELOG
- CURRENT_SPRINT
- Git

---

# Engineering Standards

Always prefer:

- readable code
- explicit behaviour
- modular design
- complete implementations
- AI reasoning over fixed rules

Avoid:

- placeholder implementations
- speculative abstractions
- unnecessary configuration
- premature optimisation
- excessive documentation

---

# Working Principle

Every engineering decision should improve one of:

- intelligence
- capability
- maintainability
- demonstrability

If it improves none of these, it should not be implemented.

---

# Sprint Size

Each sprint should normally require between one and four hours.

A sprint should:

- solve one meaningful problem
- produce one demonstrable improvement
- remain independently testable

Avoid large multi-day implementation batches.

---

# Testing Principle

Testing should demonstrate business behaviour.

Passing unit tests alone is insufficient.

Questions include:

- Does the platform investigate better?
- Does it reason better?
- Does it recommend better?
- Does it discover more intelligently?

---

# Success Measure

Success is measured by increased business development intelligence rather than increased software complexity.