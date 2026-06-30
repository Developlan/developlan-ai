# Developlan AI
## Acquisition Architecture

Version: 1.0

---

# 1. Purpose

Developlan AI may discover opportunities through many acquisition methods, but all methods converge into the same AI Investigation Engine.

The intelligence produced by the platform must be independent of how an opportunity is discovered. A page reached from a public URL, an authenticated portal, search, scheduled monitoring, email, RSS or a document repository should enter the same investigation process once it can be acquired as evidence.

Acquisition methods are entry points.

Investigation is the common intelligence layer.

---

# 2. Acquisition Entry Points

## 2.1 Public URL

Purpose

Support the current MVP by allowing a user or workflow to provide a direct public URL for investigation.

Examples

- A public donor opportunity page
- A procurement notice URL
- A public funding announcement
- A public listing page containing multiple opportunities

## 2.2 Authenticated Portal

Purpose

Investigate opportunity portals that require authentication while preserving the same downstream investigation workflow.

Examples

- UN Partner Portal
- UNGM
- Devex
- donor portals

## 2.3 Search

Purpose

Allow a user to supply an information need rather than a known URL.

The platform determines where to investigate, which sources are likely to contain useful opportunities, and which results should enter the AI Investigation Engine.

## 2.4 Scheduled Monitoring

Purpose

Continuously monitor configured opportunity sources.

Scheduled monitoring should detect meaningful changes, such as new opportunities, updated deadlines, new supporting documents or materially changed opportunity content.

The platform should notify only when a change is meaningful for business development intelligence.

---

# 3. Session Manager

The Session Manager is responsible for browser and authentication state.

Responsibilities

- login
- session persistence
- cookie management
- authentication refresh
- browser lifecycle

The Investigation Engine must never manage authentication.

The Investigation Engine should receive acquired pages and evidence. It should not know whether a page came from a public browser session, an authenticated portal, search, monitoring or another source.

---

# 4. Source Profiles

Source profiles describe how the platform reaches and interacts with each opportunity source.

Each opportunity source should define:

- name
- authentication
- entry URL
- search capability
- listing capability
- document types
- notes

## Example: UN Partner Portal

name:
UN Partner Portal

authentication:
Required.

entry URL:
Authenticated portal landing page or configured opportunity listing page.

search capability:
Portal search and filtered opportunity listings.

listing capability:
Yes. The portal exposes lists of opportunities and opportunity detail pages.

document types:
Webpage content, PDFs, Word documents, Excel files, annexes, templates and supporting procurement documents.

notes:
Requires managed login, session persistence and authentication refresh. Investigation should operate on acquired pages, not on authentication logic.

## Example: ReliefWeb

name:
ReliefWeb

authentication:
Not required for public opportunity and job content.

entry URL:
Public search results, topic pages, country pages or individual notice pages.

search capability:
Public search and filtered browsing.

listing capability:
Yes. ReliefWeb exposes public listing pages and individual content pages.

document types:
Webpage content and linked public documents where available.

notes:
Suitable for public URL, search and scheduled monitoring entry points. Authentication should not be required for standard acquisition.

---

# 5. Common Investigation Pipeline

Every acquisition mode eventually enters the same investigation pipeline.

Browser Session

↓

Acquire Page

↓

Investigate

↓

Evidence

↓

Opportunity Brief

↓

Opportunity Intelligence

---

# 6. Future Expansion

Future acquisition sources should be added without changing the Investigation Engine.

Possible future sources include:

- email
- RSS
- SharePoint
- Teams
- Google Drive
- CRM

These sources should use entry adapters that acquire relevant pages, documents or evidence and then pass that evidence into the common investigation pipeline.
