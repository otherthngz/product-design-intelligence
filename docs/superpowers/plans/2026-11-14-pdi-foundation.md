# PDI foundation implementation plan

**Goal:** Deliver portable design skills and a locally runnable onboarding example.
**Architecture:** One coordinating agent reads a router and loads focused Agent Skills; a standard-library script copies the working prototype to a new location. Markdown holds knowledge, contracts and evidence.
**Stack:** Markdown, HTML, CSS, JavaScript, Python 3 standard library. No services or credentials.

1. Define deterministic checks for skill metadata, example routing, and safe artifact generation; run them before implementation.
2. Write five skills, routing, knowledge, human and engineering documentation, and evaluation cases.
3. Build the responsive onboarding example and a local generator that refuses to overwrite an existing file.
4. Run tests, validate the generated artifact, and check the prototype in a browser if available; record exactly what remains unverified.
