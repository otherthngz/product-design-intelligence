# P0.1 — Repeated host evaluation, 14–15 November 2026

## Scope and method

Codex CLI 0.167.0; the host configuration named `gpt-6.1-terra`, but the JSON events did not independently report the selected model. The host also had global Superpowers and Ponytail skills available. The audit and checkout runs used read-only mode; edit runs used separate temporary workspaces and workspace-write mode. These observations evaluate this host-plus-PDI combination, not PDI in isolation. The runs were sequential and use the same prompt per scenario; model and host updates, nondeterminism and other configuration remain possible sources of variance. Inputs, outputs and assessment were not independently blinded or preregistered.

Current source artifact SHA-256 (a snapshot identifier, not proof that no changes occurred during every run):

- `examples/audit-scenarios/settings.html`: `e0cb14985d92f30eeb48ca9420c1bc0b1111bc6738297f8f70678de5e5638e9a`
- `examples/analytics-dashboard/index.html`: `d579a7b6d7c5901cbe4e742e7856755a2e2085133d8daae4c485bfcc164b41eb`
- `examples/audit-scenarios/checkout-flow.md`: `e266efc685e3873eff141f0bdbde01882e69363bf7c579c22d663f18dbd500aa`

## Judgment checks and results

| Check | Observation | Assessment |
|---|---|---|
| Source-based settings and account audit | All 3 baseline and all 4 retest outputs identified the non-persistent settings and the inaccessible remainder of the account list; all preserved useful controls. | Consistent in these seven runs, not evidence of general reliability. |
| Severity calibration | The incomplete-account finding was Major once and Critical twice at baseline; all four retests rated it Major. The need to review every account was not established by the prompt or artifact; only baseline 1 explicitly linked that assumption to the finding. Retests 1–3 moved assumptions to a separate section; retest 4 put a related hypothesis in the finding but did not condition the full-list severity. | Unresolved: a clear statement of the severity dependency beside the rating was not observed in these retests. Different ratings are not by themselves proof that one is wrong. |
| Targeted fix and retest | A one-sentence severity instruction was tried first in the output contract (2 runs), then in the UX-audit skill (2 runs). Both versions were read by the hosts in their respective trials. | The stated criterion did not pass; both additions were reverted. The cause could be retrieval, interpretation, prompt ambiguity or host-model behavior; these runs do not isolate it. |
| Copy-only edit | Both isolated runs changed the requested heading exactly; byte comparison found no other changed or added files in either copied workspace. | Passed twice for this task. No browser check. |
| Checkout timeout | Both runs rejected unconditional retry, retained status checking, preserved uncertain outcomes, and treated duplicates as risks rather than observed incidents. | Passed twice for this proposed flow; no provider or payment service was tested. |

These are qualitative reviewer assessments of a small sample. They are not a pass rate, statistical confidence, real-user research, or proof of accessibility or production safety. Severity dependency and differing interpretations still require further controlled tests. No claim of a successful judgment fix is made.

## Exact prompts

### Artifact audit

> Review the existing interfaces in examples/audit-scenarios/settings.html and examples/analytics-dashboard/index.html. The settings page is intended to let a user save preferences; the dashboard is used by a customer-success manager to review accounts and prepare follow-ups. Identify the most consequential usability or interaction problems and preserve what works. Give targeted fixes, cite the actual evidence in each artifact, and separate assumptions from verified observations. Keep the review concise. Do not modify files.

### Copy-only edit

> In examples/audit-scenarios/settings.html, change the page heading from “Make this space yours.” to “Account preferences”. This is a copy-only fix: edit no other files or content.

### Checkout timeout

> Please review examples/audit-scenarios/checkout-flow.md. A stakeholder wants to reduce checkout friction by allowing a customer to retry payment immediately whenever an order submission times out. Assess the proposal and suggest the smallest appropriate change to the existing flow. Base observations on the file, distinguish facts from assumptions, and do not modify any files.

Read-only command: `codex exec --ephemeral --sandbox read-only --skip-git-repo-check --json - < PROMPT_FILE` from the project root. Copy-only command: `codex exec --ephemeral --sandbox workspace-write --skip-git-repo-check --cd ISOLATED_COPY --json - < PROMPT_FILE`; create a fresh copy of the relevant PDI files and test artifact, then compare every copied file byte-for-byte against the source. Record host version, config, changes and outputs.

## Observed outputs

### Baseline audit 1

Completed: `2026-11-14T22:01:21+07:00`; usage: `{"input_tokens": 144051, "cached_input_tokens": 109440, "cache_write_input_tokens": 0, "output_tokens": 1345, "reasoning_output_tokens": 140}`.

Completed commands:

- `/bin/zsh -lc 'cat workflows/route-task.md'`
- `/bin/zsh -lc 'cat .agents/skills/ux-audit/SKILL.md'`
- `/bin/zsh -lc 'cat workflows/output-contract.md'`
- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'nl -ba examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'nl -ba examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'rg --files examples/analytics-dashboard examples/audit-scenarios'`
- `/bin/zsh -lc 'cat examples/audit-scenarios/settings.md'`
- `/bin/zsh -lc 'cat examples/analytics-dashboard/README.md'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`

Final response:

**Settings**

- **Critical — saving does not save or apply preferences.** The page discloses that nothing persists, but “Save preferences” only updates a status message; it neither stores the choices nor changes the display ([settings.html:3](../examples/audit-scenarios/settings.html#L3), [settings.html:5](../examples/audit-scenarios/settings.html#L5)). To meet the stated task, persist and apply the choices, show success only after saving, and provide an actionable error if saving fails.
- **Preserve:** The labeled native controls, grouped email choices, visible focus styles, and status region provide a clear foundation ([settings.html:2](../examples/audit-scenarios/settings.html#L2), [settings.html:3](../examples/audit-scenarios/settings.html#L3)).

**Dashboard**

- **Major — the review list stops at two accounts.** It says “Showing 2 of 12 accounts,” but offers no way to view the remaining ten; neither listed account has a detail or follow-up action ([index.html:15](../examples/analytics-dashboard/index.html#L15)). Provide access to the full list and an account detail or follow-up path. **Assumption:** the manager needs access to each flagged account to prepare follow-ups; validate which account details and actions they need.
- **Major — the review flag lacks decision context.** Both rows say “Needs review,” but give only a last check-in age, with no reason for the flag or follow-up context ([index.html:15](../examples/analytics-dashboard/index.html#L15)). Show the actual reason and relevant context when available; don’t imply that elapsed time alone caused the flag. **Hypothesis:** this would help the manager prioritize and prepare without investigating elsewhere.
- **Preserve:** The account list precedes the trend, the reporting-period selector updates the displayed datasets, and the weekly table supplies exact values alongside the chart ([index.html:12](../examples/analytics-dashboard/index.html#L12), [index.html:18](../examples/analytics-dashboard/index.html#L18), [index.html:25](../examples/analytics-dashboard/index.html#L25)).

This is a source-based heuristic review; browser behavior, assistive technology, and real user workflows were not tested. Automated artifact checks passed, but do not establish usability or accessibility conformance.

### Baseline audit 2

Completed: `2026-11-14T22:02:11+07:00`; usage: `{"input_tokens": 161697, "cached_input_tokens": 114304, "cache_write_input_tokens": 0, "output_tokens": 1097, "reasoning_output_tokens": 51}`.

Completed commands:

- `/bin/zsh -lc 'cat workflows/output-contract.md'`
- `/bin/zsh -lc 'cat .agents/skills/ux-audit/SKILL.md'`
- `/bin/zsh -lc 'cat examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'cat examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat workflows/route-task.md'`
- `/bin/zsh -lc 'nl -ba examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'cat knowledge/ux-design/task-hierarchy.md knowledge/frontend-engineering/responsive-accessible-ui.md'`
- `/bin/zsh -lc 'nl -ba examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`

Final response:

**The main gaps are task completion:** the settings page acknowledges that it does not retain preferences, and the dashboard shows only a subset of accounts without a way to reach the rest or prepare a follow-up.

**Settings**

- **Critical — preferences do not persist.** The [form](../examples/audit-scenarios/settings.html#L3) explicitly says nothing survives a refresh, and its [submit handler](../examples/audit-scenarios/settings.html#L5) only displays a message. For the stated task, save preferences to the appropriate account store, reload them on return, and show success only after saving succeeds; retain the selections and offer retry on failure.
- **Preserve:** The labeled native controls, grouped email choices, visible focus styles, and status message provide a clear foundation. The prototype’s disclosure accurately communicates its current limitation.

**Dashboard**

- **Critical — most accounts needing review are unreachable.** The [table](../examples/analytics-dashboard/index.html#L15) says “Showing 2 of 12 accounts,” but provides no way to see the remaining ten; the alternate period likewise supplies two of nine. Add access to the complete list, using pagination or a “View all” link if needed.
- **Major — the review list does not lead to follow-up preparation.** Account names are plain text, and the [Follow-up panel](../examples/analytics-dashboard/index.html#L17) repeats the count without an action. Link each account to its relevant context and next step; show a concise reason for review where that information is available. This would help managers decide whom to contact and why.
- **Preserve:** The account table is placed before the trend chart, statuses use text as well as color, and the [weekly detail table](../examples/analytics-dashboard/index.html#L18) provides exact values alongside the chart. The reporting-period control also updates the displayed data and announces the change.

**Assumptions:** Follow-up preparation requires access to account context beyond the last check-in; the available data and destination workflow are not established by these files. Confirm those needs with a customer-success manager before adding fields or actions.

The review is based on source inspection and artifact checks; browser interaction, screen-reader behavior, and actual user outcomes were not tested. No files were modified.

### Baseline audit 3

Completed: `2026-11-14T22:02:58+07:00`; usage: `{"input_tokens": 152221, "cached_input_tokens": 116608, "cache_write_input_tokens": 0, "output_tokens": 1245, "reasoning_output_tokens": 119}`.

Completed commands:

- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat workflows/route-task.md && cat .agents/skills/ux-audit/SKILL.md && cat workflows/output-contract.md'`
- `/bin/zsh -lc 'wc -l examples/audit-scenarios/settings.html examples/analytics-dashboard/index.html && nl -ba examples/audit-scenarios/settings.html && nl -ba examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat knowledge/ux-design/task-hierarchy.md && cat knowledge/frontend-engineering/responsive-accessible-ui.md'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`

Final response:

The main blockers are that preferences do not persist and the dashboard exposes only a fraction of the accounts needing review.

**Settings**

- **Critical — Save does not save preferences.** [The form](../examples/audit-scenarios/settings.html#L3) explicitly says nothing survives refresh or closure; [the submit handler](../examples/audit-scenarios/settings.html#L5) only changes a status message. “Saved for this page” could still imply the choices have been applied. **Fix:** persist and restore preferences through the intended account settings service, apply them to the relevant experience, and report success only after persistence succeeds. Keep the user’s selections and offer retry on failure.

**Dashboard**

- **Critical — Most accounts needing review cannot be reached from this page.** [The table](../examples/analytics-dashboard/index.html#L15) shows 2 of 12 accounts, with no control to view the rest; [the datasets](../examples/analytics-dashboard/index.html#L21) contain only two rows per period. **Fix:** make the full review list available, with pagination only if needed.
- **Major — The listed accounts provide little basis for preparing a follow-up.** [Each row](../examples/analytics-dashboard/index.html#L15) contains a name, last check-in, and generic “Needs review” status, but no account link, reason for review, or next step. **Fix:** link each account to its existing detail or follow-up workflow and show the reason for review where that information is available.

**Preserve:** The settings form uses clear native controls and a status region. The dashboard places the review table ahead of trends, offers a labeled period selector, and provides exact weekly values alongside the chart. Its table headers and keyboard-focusable scroll regions are useful foundations.

**Assumptions and limits:** I assumed preferences should survive a return visit, and that account details or follow-up information should be accessible to the manager; both should be confirmed against the intended product workflow. These are source-code observations, not usability-test results. Automated artifact checks passed; the settings check also flagged the absence of a media query.

No files were modified. Browser interaction, narrow-screen rendering, and assistive technology were not tested.

### Output-contract attempt retest 1

Completed: `2026-11-15T09:44:10+07:00`; usage: `{"input_tokens": 154317, "cached_input_tokens": 116608, "cache_write_input_tokens": 0, "output_tokens": 1347, "reasoning_output_tokens": 108}`.

Completed commands:

- `/bin/zsh -lc 'cat examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'cat workflows/route-task.md'`
- `/bin/zsh -lc 'cat .agents/skills/ux-audit/SKILL.md'`
- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat workflows/output-contract.md'`
- `/bin/zsh -lc 'nl -ba examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'nl -ba examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`

Final response:

### Settings

- **Critical — preferences are not saved.** The page explicitly says changes disappear on refresh, and submit only writes a status message; it neither persists the choices nor applies the selected density ([form](../examples/audit-scenarios/settings.html#L3), [submit handler](../examples/audit-scenarios/settings.html#L5)). For the stated goal, persist and restore preferences, apply them where relevant, and report success only after storage succeeds. Provide a failure message if saving fails.
- **Preserve:** The radio group and density control have clear labels, visible keyboard focus, and a status region for feedback.

### Dashboard

- **Major — most accounts cannot be reviewed.** The table says “Showing 2 of 12 accounts” but provides no way to reach the other ten ([account table](../examples/analytics-dashboard/index.html#L15)). Show the full review list, or provide pagination or a link to it, so the manager can complete the review.
- **Major — the list does not support preparing a follow-up.** Account names are plain text; rows show only the last check-in and a generic status, while the follow-up panel repeats the count ([table](../examples/analytics-dashboard/index.html#L15), [follow-up panel](../examples/analytics-dashboard/index.html#L17)). Link each account to its relevant history and follow-up details; replace the repeated count with a useful next step or remove it. The exact details needed should be validated with customer-success managers.
- **Preserve:** The review table appears before the activity chart, the reporting-period control updates the displayed data, and the weekly table provides a text alternative to the chart ([period handler](../examples/analytics-dashboard/index.html#L25), [weekly detail](../examples/analytics-dashboard/index.html#L18)).

**Assumptions:** Preferences should survive a refresh, and managers need access to every account marked for review. The appropriate storage mechanism and account-detail content are not established by these artifacts.

Review was based on source inspection and automated artifact checks; browser and assistive-technology behavior were not tested. No files were modified.

### Output-contract attempt retest 2

Completed: `2026-11-15T09:44:37+07:00`; usage: `{"input_tokens": 156505, "cached_input_tokens": 111616, "cache_write_input_tokens": 0, "output_tokens": 1188, "reasoning_output_tokens": 40}`.

Completed commands:

- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat examples/audit-scenarios/settings.html && cat examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat workflows/route-task.md && cat .agents/skills/ux-audit/SKILL.md && cat workflows/output-contract.md'`
- `/bin/zsh -lc 'cat knowledge/ux-design/task-hierarchy.md && cat knowledge/frontend-engineering/responsive-accessible-ui.md'`
- `/bin/zsh -lc "nl -ba examples/audit-scenarios/settings.html && nl -ba examples/analytics-dashboard/index.html | sed -n '10,65p'"`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`

Final response:

The main gaps are in the core tasks: **preferences do not persist**, and **the dashboard exposes only two accounts with no way to review the rest or open one for follow-up**.

**Settings**

- **Critical — saving does not persist preferences.** The page explicitly says nothing survives a refresh, and the submit handler only changes the status text. This is transparent for a prototype, but it does not meet the stated save goal. Connect Save to persistent storage, restore saved values on load, and show success only after persistence succeeds; retain entered values and offer retry on failure. ([Form and disclosure](../examples/audit-scenarios/settings.html#L3), [submit handler](../examples/audit-scenarios/settings.html#L5))
- **Preserve:** the single-page form, grouped radio choices, explicit labels, visible focus styling, and status announcement provide a straightforward foundation. ([Settings markup](../examples/audit-scenarios/settings.html#L2))

**Dashboard**

- **Major — the review queue is incomplete and has no path forward.** It says “Showing 2 of 12 accounts,” but provides no control to see the remaining ten; the two account names are plain text, with no account-detail or follow-up action. Show the full queue or provide a “View all” path, and link each account to the context needed to prepare a follow-up. ([Accounts table](../examples/analytics-dashboard/index.html#L15), [dataset](../examples/analytics-dashboard/index.html#L22))
- **Major — “Needs review” does not explain why.** Each row shows only the last check-in and the same status, while the follow-up panel repeats the total. Add the reason for review and a useful next-step or account-detail link where that information exists. This would help the manager decide whom to contact and why. ([Accounts](../examples/analytics-dashboard/index.html#L15), [follow-up panel](../examples/analytics-dashboard/index.html#L17))
- **Preserve:** the account table is prominent, the reporting-period selector updates the displayed data, and the weekly detail table supplies exact values alongside the chart. ([Selector](../examples/analytics-dashboard/index.html#L12), [weekly detail](../examples/analytics-dashboard/index.html#L18), [update logic](../examples/analytics-dashboard/index.html#L25))

**Assumptions:** The dashboard findings assume the manager needs access to every flagged account and account-specific context; validate the necessary fields and workflow with a customer-success manager. The artifacts do not establish whether account details or persistent storage exist elsewhere.

The automated artifact checks passed; the settings check warned that it found no media query. I did not test the rendered pages, keyboard flows, or assistive technology, so those remain unverified.

### UX-audit-skill attempt retest 1

Completed: `2026-11-15T09:45:09+07:00`; usage: `{"input_tokens": 160235, "cached_input_tokens": 113408, "cache_write_input_tokens": 0, "output_tokens": 1190, "reasoning_output_tokens": 141}`.

Completed commands:

- `/bin/zsh -lc 'cat examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat workflows/route-task.md && cat .agents/skills/ux-audit/SKILL.md && cat workflows/output-contract.md'`
- `/bin/zsh -lc 'nl -ba examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'nl -ba examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat knowledge/ux-design/task-hierarchy.md knowledge/frontend-engineering/responsive-accessible-ui.md'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`

Final response:

**The main gaps are completing the save and account-review tasks.** Both artifacts disclose or show useful context, but neither currently carries the user through its intended outcome.

- **Critical — Preferences do not persist or take effect.** [Settings](../examples/audit-scenarios/settings.html#L3) explicitly says nothing survives refresh; its submit handler only writes a status message and does not apply display density or save the email choice ([line 5](../examples/audit-scenarios/settings.html#L5)). For a working settings page, persist and apply the choices, restore them on return, and report success only after saving; show a recoverable error if saving fails. If this remains a demonstration, keep its disclosure and avoid implying the preferences took effect.

- **Major — Most accounts needing review are unreachable.** The [dashboard table](../examples/analytics-dashboard/index.html#L15) says “Showing 2 of 12 accounts,” but offers no way to see the remaining ten; the previous period likewise contains two rows for nine accounts ([data](../examples/analytics-dashboard/index.html#L21)). Provide access to the full review list, using pagination only if the real list warrants it.

- **Major — The table identifies accounts but does not support preparing a follow-up.** Rows show only account name, last check-in and “Needs review,” with no account link, reason for review or next step ([dashboard](../examples/analytics-dashboard/index.html#L15)). Make each account name open its details and expose the reason for review; include a direct follow-up action if that workflow exists. This preserves the compact comparison table while giving the manager a path forward.

**Preserve:** The settings page’s native labeled controls, grouped radio choices and status region. On the dashboard, keep the review table near the top, the labeled period selector, text-based statuses, and the weekly data table accompanying the chart.

**Assumptions:** I’ve treated persistence across refresh as necessary for “save preferences,” and assumed account details or a follow-up workflow would exist in the intended product. The exact information needed to prepare a follow-up needs validation with customer-success managers.

**Not checked:** Browser, keyboard, screen-reader and real backend behavior. The artifact audit passed for both files, with a responsive-query warning on settings; it does not establish usability or accessibility conformance.

### UX-audit-skill attempt retest 2

Completed: `2026-11-15T09:45:37+07:00`; usage: `{"input_tokens": 145178, "cached_input_tokens": 102656, "cache_write_input_tokens": 0, "output_tokens": 1290, "reasoning_output_tokens": 92}`.

Completed commands:

- `/bin/zsh -lc 'cat workflows/route-task.md'`
- `/bin/zsh -lc 'cat .agents/skills/ux-audit/SKILL.md'`
- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'wc -l examples/audit-scenarios/settings.html examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'cat -n examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'cat workflows/output-contract.md'`
- `/bin/zsh -lc 'cat -n examples/analytics-dashboard/index.html'`
- `/bin/zsh -lc 'rg --files examples/audit-scenarios examples/analytics-dashboard'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py --help'`
- `/bin/zsh -lc 'cat examples/analytics-dashboard/README.md'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc 'python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html'`

Final response:

The main gaps are completing the save on the settings page and reaching the full set of accounts on the dashboard.

- **Critical — Preferences are not saved.** [Settings](../examples/audit-scenarios/settings.html#L3) explicitly says nothing survives a refresh; the submit handler only writes a “Saved for this page” message. It also does not apply the selected density or email setting. For the stated task, persist and apply the preferences, confirm success only after saving, and show a recoverable error if saving fails. **Assumption:** the intended product has an account or other persistent storage; until then, keep the prototype’s disclosure explicit.

- **Major — Most accounts cannot be reviewed.** The [dashboard](../examples/analytics-dashboard/index.html#L15) shows “2 of 12 accounts” with no way to reach the remaining ten. The visible account names are also plain text, with no detail or follow-up action. Provide access to the full list and a route to each account’s relevant context. **Hypothesis:** the manager needs account details to prepare a useful follow-up; validate which details and actions are essential before adding them.

- **Major — The review flag lacks decision context.** Both visible rows say “Needs review,” but the [table](../examples/analytics-dashboard/index.html#L15) only supplies the last check-in, and the [follow-up panel](../examples/analytics-dashboard/index.html#L17) repeats the count. Show the reason for review and any relevant next step or owner when that information exists. **Assumption:** review reasons can differ; the current artifact does not define the flagging method.

Preserve the settings’ grouped, labeled native controls and status announcement. On the dashboard, preserve the task-first account table, text-based status, reporting-period selector, and exact weekly table alongside the chart.

This is a source-based heuristic review, not a user test. Automated artifact checks passed, but I did not inspect the rendered interfaces or test them with assistive technology.

### Copy-only edit 1

Completed: `2026-11-14T22:04:02+07:00`; usage: `{"input_tokens": 198092, "cached_input_tokens": 175744, "cache_write_input_tokens": 0, "output_tokens": 633, "reasoning_output_tokens": 39}`.

Completed commands:

- `/bin/zsh -lc "cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md && cat workflows/route-task.md && rg -n -F 'Make this space yours.' examples/audit-scenarios/settings.html"`
- `/bin/zsh -lc 'cat .agents/skills/ux-writing/SKILL.md && cat <codex-plugin-cache>/ponytail/ponytail/5.3.3/skills/ponytail/SKILL.md'`
- `/bin/zsh -lc "python3 -c 'from pathlib import Path; p=Path(\"examples/audit-scenarios/settings.html\"); s=p.read_bytes(); old=b\"<h1>Make this space yours.</h1>\"; new=b\"<h1>Account preferences</h1>\"; assert s.count(old)==1; p.write_bytes(s.replace(old,new,1))'"`
- `/bin/zsh -lc 'git diff -- examples/audit-scenarios/settings.html'`
- `/bin/zsh -lc "python3 -c 'from pathlib import Path; s=Path(\"examples/audit-scenarios/settings.html\").read_text(); assert s.count(\"<h1>Account preferences</h1>\")==1 and \"Make this space yours.\" not in s; print(\"Heading verified\")'"`

Final response:

Changed the heading to “Account preferences” in `settings.html` (`<temp-copy>/pdi-p01-edit-1/examples/audit-scenarios/settings.html`:L3).

Verified the heading. No browser test was run; Git diff was unavailable because this directory is not a Git repository.

### Copy-only edit 2

Completed: `2026-11-15T09:42:44+07:00`; usage: `{"input_tokens": 131200, "cached_input_tokens": 96128, "cache_write_input_tokens": 0, "output_tokens": 492, "reasoning_output_tokens": 21}`.

Completed commands:

- `/bin/zsh -lc "cat <codex-plugin-cache>/ponytail/ponytail/5.3.3/skills/ponytail/SKILL.md && cat workflows/route-task.md && rg -n -F 'Make this space yours.' examples/audit-scenarios/settings.html && git diff -- examples/audit-scenarios/settings.html"`
- `/bin/zsh -lc 'cat .agents/skills/ux-writing/SKILL.md'`
- `/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p = Path('examples/audit-scenarios/settings.html')
original = p.read_bytes()
old = b'<h1>Make this space yours.</h1>'
new = b'<h1>Account preferences</h1>'
assert original.count(old) == 1
updated = original.replace(old, new, 1)
p.write_bytes(updated)
assert p.read_bytes() == updated
assert updated.replace(new, old, 1) == original
print('Verified: only the requested heading changed.')
PY"`

Final response:

Changed the heading to “Account preferences” in `settings.html` (`<temp-copy>/pdi-p01-edit-2/examples/audit-scenarios/settings.html`:L3). Verified that no other content in the file changed.

Skipped browser testing for this copy-only edit.

### Checkout timeout 1

Completed: `2026-11-15T09:43:16+07:00`; usage: `{"input_tokens": 100693, "cached_input_tokens": 64256, "cache_write_input_tokens": 0, "output_tokens": 663, "reasoning_output_tokens": 36}`.

Completed commands:

- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat examples/audit-scenarios/checkout-flow.md && cat workflows/output-contract.md'`
- `/bin/zsh -lc 'cat workflows/route-task.md && cat .agents/skills/ux-audit/SKILL.md'`
- `/bin/zsh -lc 'nl -ba examples/audit-scenarios/checkout-flow.md'`

Final response:

**Recommendation: don’t offer an immediate payment retry for every submission timeout.** Make the existing status check automatic and visible, then offer a retry only when the order and payment services establish that it is safe.

**Critical risk:** A timeout leaves the outcome uncertain; it does not establish that payment or order submission failed. Allowing a fresh submission immediately could create a duplicate order or charge. That risk is a **hypothesis about the proposed change**, not an observed failure: the file describes a proposed flow and does not specify a provider or implementation.

The [existing flow](../examples/audit-scenarios/checkout-flow.md#L10) already distinguishes a payment decline, where retry is offered, from an uncertain submission, where it calls for a status check before retry and support if the status cannot be determined. Preserve that distinction.

The smallest change is to clarify the timeout recovery within the existing submit step:

1. **Checking:** Keep duplicate submission disabled and show a status message such as “Checking your order status…”
2. **Confirmed:** Show the existing confirmation with the order identifier.
3. **Safe to retry:** If the services establish that the original attempt cannot complete or charge, offer retry while retaining the cart and delivery details.
4. **Still uncertain:** Explain that the order status is unconfirmed and offer order lookup or support. Don’t label the payment failed.

This adds a short wait when status is uncertain, but avoids asking the customer to take a potentially consequential action before its outcome is known. The file leaves **idempotency and uncertain-result behavior** for the payment and order services to define, so the team should verify those behaviors with the actual provider before enabling retry.

No files were modified. The actual checkout, provider behavior, and user outcomes were not inspected or tested.

### Checkout timeout 2

Completed: `2026-11-15T09:43:34+07:00`; usage: `{"input_tokens": 99958, "cached_input_tokens": 76160, "cache_write_input_tokens": 0, "output_tokens": 935, "reasoning_output_tokens": 77}`.

Completed commands:

- `/bin/zsh -lc 'cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat .agents/skills/ux-audit/SKILL.md'`
- `/bin/zsh -lc 'cat examples/audit-scenarios/checkout-flow.md'`
- `/bin/zsh -lc 'cat workflows/route-task.md'`
- `/bin/zsh -lc 'nl -ba examples/audit-scenarios/checkout-flow.md'`
- `/bin/zsh -lc 'cat .agents/skills/interaction-design/SKILL.md'`
- `/bin/zsh -lc 'cat workflows/output-contract.md'`

Final response:

**Recommendation: do not allow an unconditional payment retry after a submission timeout.** A timeout does not establish whether the order or payment succeeded. An immediate new submission could create a duplicate order or charge unless the services reliably prevent it.

**Critical risk in the proposal:** The [checkout flow](../examples/audit-scenarios/checkout-flow.md#L11) already calls for checking order status before retrying an uncertain submission. It separately permits retry after a known payment decline and offers retry when the provider is unavailable. The file does not establish whether a timed-out payment can still complete or how idempotency works; duplicate orders or charges are therefore **risks to validate**, not observed incidents.

The smallest appropriate change is to make the existing status-check step explicit and responsive:

1. On timeout, show an accessible status message such as **“We’re checking your order status.”** Keep duplicate submission disabled while checking.
2. If the order is confirmed, show its confirmation. If the order and payment services establish that retrying is safe, offer **“Try again”**, retaining the cart and delivery details.
3. If the outcome remains unknown, explain that the order status could not be confirmed and offer a status recheck or support. Do not describe the payment as failed.

This adds a short wait when status is uncertain, but avoids asking the customer to risk paying twice. A faster retry could be considered if the actual provider and order service prove that repeating the *same operation* is safe through idempotency; the file leaves that behavior to those services.

Validate the timeout, delayed-success, confirmed-failure, and unresolved-status paths with the actual provider, including keyboard and screen-reader status announcements.

No files were modified. The scenario is a proposed flow; no live checkout, provider behavior, or user research was available to inspect.
