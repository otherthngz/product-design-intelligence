# Account overview prototype

User-supplied: a responsive B2B SaaS dashboard for customer-success managers, including metrics, follow-up accounts and a period filter.

Assumptions: managers use a list to prepare follow-up conversations. Account names, counts and dates are invented solely for the prototype. No real customer information, product definitions, research, backend, persistence or design system was provided. The two shown accounts are illustrative rows; the full follow-up count is not represented by a complete list.

Decision: put a small set of period metrics before a table so a manager can see the summary and then identify accounts. A different order could fit teams that work account-first; this requires user research. A native period selector updates all displayed values from local data. Table labels, visible focus, scrollable table region and narrow layout support usability, but are not proof of accessibility compliance.

Open questions: definitions of active accounts and follow-up flags, actual data source, complete results, sorting, account actions, timezone and ownership, and empty/loading/error states for a live service. No customer contact action or save operation is implemented.
