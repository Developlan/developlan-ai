# Engineering Decisions

---

## D001

Capability drives opportunity discovery.

Reason

The platform sells strategic intelligence rather than keyword matching.

---

## D002

Prototype before platform.

Reason

Demonstrable intelligence is more valuable than speculative architecture.

---

## D003

AI investigates.

Reason

Reasoning provides greater commercial value than deterministic scraping.

---

## D004

Complete file replacement.

Reason

Replacing entire files during development is faster, more reliable and less error-prone than incremental edits.

---

## D005

Structured domain models before report rendering.

Reason

Opportunity intelligence should be generated as reusable domain objects before being rendered into Markdown or any future output format. This keeps AI generation focused on structured intelligence and allows Google Docs, PDF, HTML or JSON renderers to be introduced without changing the underlying reasoning logic.

---

## D006

Multiple Acquisition Entry Points.

Reason

New acquisition capabilities are added through entry adapters, not by modifying the Investigation Engine. This keeps opportunity intelligence independent of whether evidence comes from a public URL, authenticated portal, search, scheduled monitoring or future source integrations.
