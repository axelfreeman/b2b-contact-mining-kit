---
name: b2b-contact-mining
description: Find and verify B2B business contacts without buying a database — mine fresh leads from Google, Telegram and Discord, then SMTP-validate every email for a 2–5% bounce rate. Use when the user wants to find business emails or phone numbers, build a cold-outreach lead list, scrape contacts from a company website or a Discord/Telegram community, replace Apollo/ZoomInfo/Hunter, or verify an email address is real — "find b2b contacts", "cold outreach leads", "email finder", "apollo alternative".
version: 1.0.0
author: Axel Freeman (axelfreeman)
license: MIT
---

# B2B Contact Mining

Find and verify B2B business contacts without buying a database. The agent mines fresh leads from Google, Telegram, and Discord — then SMTP-validates every email before it goes into a cold-outreach list. Free, self-hosted, no vendor lock-in.

## When to Use
- The user wants to find B2B business emails or phone numbers.
- Building a cold-outreach / lead-gen list from scratch.
- Replacing Apollo, ZoomInfo, Hunter, or a resold contact database.
- Mining leads from Telegram channels or Discord communities.
- Verifying that a list of emails is real before sending.

Don't use for: buying or reselling contact data, or non-B2B consumer leads.

## Prerequisites
- The agent's own web-search tool for Google / Telegram / Discord.
- `pip install -r requirements.txt` — for the SMTP validator (`dnspython`).
- Optional: TAPAC API key (https://tapacapi.com/get-key) to automate the pipeline as an MCP server.

## How to Run
- SMTP-validate a list of emails: `python scripts/email_validator.py emails.txt` → prints `VALID / INVALID / UNKNOWN` per line.
- Ready prompts for any agent: `prompts/ai-agent-prompts.md`.
- The agent does the searching itself; this skill supplies the methodology + the validator.

## Procedure
1. **Define target** — ask (or infer): industry, company size, job titles, location.
2. **Search** — Google (multiple passes), then Telegram channels and Discord communities if thin.
3. **Extract** — names, titles, emails; cross-reference on LinkedIn.
4. **Validate** — run `scripts/email_validator.py` (SMTP, 2–5% bounce vs 25–35% for bought DBs). Never send to unverified emails.
5. **Output** — structured data (name, title, company, email, source, verification status) as JSON / CSV / CRM.

## Pitfalls
- Never buy a contact database — 23% of contacts change jobs annually, 40% of emails die within 2 years.
- Always SMTP-validate before sending; unverified sends destroy sender reputation.
- Never invent contacts — return only what was actually found.
- Scraping public company / social data is legal (hiQ Labs v. LinkedIn, 2022); stay off private or credential-gated data.

## Verification
- Every returned contact carries a source and a verification status.
- Emails passed through `email_validator.py` before outreach.
- The methodology matches `AGENTS.md` and `README.md`.
