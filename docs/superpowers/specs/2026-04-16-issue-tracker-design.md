# Issue Tracker — Design Spec

**Date:** 2026-04-16
**Status:** Approved

## Overview

A maintenance and issue tracking system for strata schemes, built into the existing Django app. The initial implementation serves a single building with one power user (the author), visible publicly in read-only form. The design explicitly accommodates growth to committee members, all owners, and eventually multiple buildings (multi-tenancy).

The interface for phase one is Django admin for data entry, plus a set of custom public read-only views.

---

## Entity-Relationship Diagram

The upper section shows FK/ownership structure. The lower section lists many-to-many relationships separately to avoid crossing lines.

```
OWNERSHIP / FK STRUCTURE
────────────────────────────────────────────────────────────────────────

  Organisation ──────────────────────────────────────────────────────────┐
  (name, phone,          Contact (name?, email, phone, hidden)           │
   email, url,            │  FK ──────────────────────────────────────►  │
   notes)                 │  (reverse: org.contacts)                     │
      │                   │                                               │
      └─ Engagement ─────►│  Building                                    │
         (service,         │     │                                        │
          from, to)        │     ├──► Parcel ◄── Tenure ─────────────────┘
                           │     │       (name,    (contact FK,
                           │     │        type)     role, from, to)
                           │     │
                           │     ├──► Tag (name, slug)
                           │     │
                           │     ├──► Issue (title, description,
                           │     │           completed_at)
                           │     │
                           │     └──► Event (event_type, date, duration,
                           │                 cancelled, rescheduled_from FK)
                           │                    │
                           │                    └──► Document (file, title,
                           │                               mimetype, size)
                           │
MANY-TO-MANY RELATIONSHIPS
────────────────────────────────────────────────────────────────────────

  Issue  ↔  Tag
  Issue  ↔  Parcel
  Issue  ↔  Event
  Event  ↔  Contact    (minimum 1 per event)
  Event  ↔  Parcel
```

---

## Data Model

### Building
`name`, `address`, `slug`

The top-level multi-tenancy unit. Slug is used for URLs now. A `domain` field will be added later to support per-building custom domain names; Django middleware will resolve requests by domain when present, falling back to slug. The two approaches coexist cleanly.

### Organisation
`name`, `phone`, `email`, `url`, `notes`

Global — not scoped to a building. Represents any external company or firm (tradespeople, engineers, strata managers, legal firms). One Organisation record per real-world entity regardless of how many buildings use them. `phone`, `email`, and `url` store the general office contact details, distinct from any named individual's details.

### Engagement
`organisation` (FK), `building` (FK), `service` (text, e.g. "Strata Manager", "Fire Services", "Gardening"), `from_date`, `to_date` (nullable)

Records which organisation provided a specific service to a building over time. A null `to_date` means the engagement is current. Answers: "who was our strata manager between 2018 and 2022?" Future: add scoring, review, and preferred-provider fields here.

### Contact
`name` (optional), `email`, `phone`, `organisation` (FK, optional), `hidden` (boolean, default False)

Global — not scoped to a building. `name` is optional: a contact without a name must have an Organisation FK and represents the organisation's office or admin line ("Acme Plumbing (office)") when no specific individual is known. A named contact without an organisation represents an owner, tenant, or independent person. `name` being blank on a contact without an organisation FK is rejected at validation.

When `hidden` is True, the contact's name is redacted in all public views.

Every staff user has a corresponding Contact record (one-to-one link with Django's User model), created at account setup. This allows an event's author to be pre-populated as a contact on new events.

### Parcel
`building` (FK), `name`, `area_type` (private / common / exclusive use)

Represents any subdivision of the strata plan: a private lot ("Lot 5"), a common area ("Roof", "Foyer", "Car Park"), or an exclusive use area ("Exclusive Use Space 3"). Names are stable once established.

### Tenure
`contact` (FK), `parcel` (FK), `role` (owner / tenant), `from_date`, `to_date` (nullable)

Links contacts to parcels over time. A null `to_date` means current. Supports: one owner with multiple parcels, multiple owners per parcel, tenants changing over time, owners with lots in multiple buildings.

### Tag
`building` (FK), `name`, `slug`

Free-form labels for classifying issues. Scoped per building so tags don't leak between schemes. Slug for URL cleanliness.

### Issue
`building` (FK), `title`, `description`, `completed_at` (nullable datetime), `tags` (M2M → Tag), `parcels` (M2M → Parcel), `created_at`

A goal or task that groups related events. Parcels can be assigned directly to an issue (workflow: create issue, then associate events). Explicit priority is omitted — urgency is computed from event activity and completion state, which is a better signal than a manually maintained priority field.

`completed_at` marks an issue as definitively done. Null means ongoing or dormant.

**Computed fields (not stored):**
- `urgency_state`: computed in order — if `completed_at` is set → **done**; else if a planned event has a past date → **overdue**; else if a planned event has a future date → **waiting**; else if a recent occurred event exists → **active**; else → **idle**
- `affected_parcels`: union of directly assigned parcels and parcels on linked events
- `last_activity`: date of most recent occurred event

### Event
`building` (FK), `title` (optional), `description`, `event_type`, `cancelled` (boolean, default False), `date` (datetime), `duration` (optional), `rescheduled_from` (self-FK, nullable), `issues` (M2M → Issue), `contacts` (M2M → Contact), `parcels` (M2M → Parcel), `created_at`

The primary entity. Everything that happens is an Event. An event with no linked issues is valid — it may be promoted to an issue later, or remain a standalone log entry.

`date` is a datetime field capturing when the event occurred or is scheduled. `duration` is an optional duration field (e.g. for meetings or work sessions).

**event_type choices:** phone call / email / meeting / conversation / notice / work / observation / other
These are expected to evolve. Changing Django choice fields requires a migration but is straightforward and not a concern at this scale.

**Derived event state (not stored, computed from data):**

| State | Rule |
|---|---|
| planned | `date` > now, `cancelled` = False |
| occurred | `date` ≤ now, `cancelled` = False |
| cancelled | `cancelled` = True |
| rescheduled | another event has `rescheduled_from` pointing to this one |

There is no stored `status` field. `planned` and `occurred` are purely a function of the date. Only `cancelled` needs explicit recording. `rescheduled` is detectable via the reverse FK relation. The four states are mutually exclusive: `cancelled` and `rescheduled` are never both true on the same event.

When an event is rescheduled: leave the old event as-is (do not set `cancelled`), create a new planned event with `rescheduled_from` pointing to the old one. The old event's state becomes `rescheduled` via the reverse FK — no flag needed.

`title` is optional. The admin displays an auto-generated preview: `{event_type} · {primary contact} · {date}`. A user may override with an explicit title.

Every event must have at least one contact. The creating user's associated Contact record is pre-populated. When no specific individual is known, the organisation's nameless "office" contact may be used.

Events have a M2M relationship with Issues. This is intentional — a single event (e.g. a meeting) can touch multiple issues. Changing to a single-issue FK later is possible via data migration but M2M is the correct model given explicit requirements.

### Document
`event` (FK → Event), `file` (FileField), `title`, `mimetype` (auto-detected on upload), `file_size`, `uploaded_at`

Documents belong to events and reach issues through them. Files are stored on disk via Django's FileField (path stored in DB); later swappable to S3 via django-storages with minimal code change. Always edited inline within the Event admin — a document without its event context is hard to interpret. A read-only searchable document list is a useful future addition.

---

## Relationships Summary

| Model | Key relationships |
|---|---|
| Building | root of the tenancy tree |
| Organisation | global; `phone`/`email`/`url` for office contact; linked to buildings via Engagement |
| Engagement | organisation ↔ building join, carries service type and date range |
| Contact | global; optional name; optional FK to Organisation; linked to Parcels via Tenure |
| Parcel | belongs to Building; M2M with Issues and Events |
| Tenure | Contact ↔ Parcel join, carries role and date range |
| Tag | belongs to Building; M2M with Issues |
| Issue | belongs to Building; M2M Tags, Parcels, Events |
| Event | belongs to Building; M2M Issues, Contacts, Parcels; self-FK for rescheduling; `cancelled` boolean |
| Document | belongs to Event |

---

## Django Admin

**Building, Tag** — simple list/edit pages.

**Parcel** — list filtered by building, area_type visible at a glance. Inline Tenure rows showing current and past occupants (contact name, role, dates).

**Organisation** — simple list/edit page. No inline Engagement rows (not relevant from an owner's perspective; a future admin concern).

**Contact** — search by name, phone, email, and organisation name. Inline Tenure rows. Detail page shows all Events linked to this contact — the primary way to answer "everything involving Acme Plumbing."

**Issue** — list with computed urgency indicator (done / overdue / waiting / active / idle), filterable by state. M2M widgets for tags and parcels. Read-only panel showing linked events in chronological order with derived state indicators. `completed_at` shown as a datestamp when set, with a "Mark complete" action.

**Event** — the primary data entry page:
- `title` optional; auto-preview shown below the field
- `cancelled` checkbox; `rescheduled_from` FK shown when not null, links to the predecessor event
- Derived state (planned / occurred / cancelled / rescheduled) shown as a read-only label
- `date` is a datetime picker; `duration` is optional
- Contacts, Issues, Parcels widgets filtered to the selected building
- Inline Document rows with file upload; mimetype and file_size auto-populated on save

**Document** — no standalone admin page; always inline within Event.

---

## Public Read-Only Views

Three pages, no authentication required, no create/edit capability.

**Issue list** (`/issues/`)
Sorted by urgency state then recency. Each row shows: title, tags, urgency badge (done / overdue / waiting / active / idle), affected parcels, date of last activity. Hidden contacts are not exposed. In the single-building phase the building is implicit. When multi-tenancy is active, URLs will be prefixed with `/b/<slug>/` (e.g. `/b/acacia-gardens/issues/`).

**Issue detail** (`/issues/<pk>/`)
Full event timeline in chronological order. Each event shows: date, derived state, event type, duration (if set), description, linked contacts (redacted if hidden), affected parcels, downloadable document links. Rescheduled events show a link to their successor. Affected parcels shown as a union of directly assigned and event-accumulated parcels.

**Contact/organisation pages** — deferred to a later phase.

---

## Multi-Tenancy

All models except Organisation, Contact, and Tenure carry a `building` FK. This is enforced from the start even with a single building. Admin querysets will be filtered by building once multiple users are introduced. Public views will resolve the building from the URL slug (or domain name in future).

---

## Growth Path

| Phase | Users | Auth | Notes |
|---|---|---|---|
| Now | Author only | Admin login | Single building, public read-only |
| Medium term | Committee members | Django auth + per-building roles | Admin still primary UI |
| Long term | All owners | Full auth | Custom owner-facing UI replaces/supplements admin |
| Complete | Multiple buildings | Multi-tenant | Domain-based routing added alongside slug routing |

---

## Explicitly Out of Scope

- Organisation scoring, reviews, and preferred-provider logic (Engagement model is the hook)
- LLM-generated progress summaries (event log structure is ready)
- Digital voting, financial dashboard, community features (separate future specs)
- Mobile app
- Email/notification integration
