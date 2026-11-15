# Designer request: checkout flow

**Scope:** a proposed web checkout; no payment provider, regulatory context or research was supplied. **Assumptions:** a signed-in or guest buyer has a cart; shipping may be needed; payment is processed by a third-party provider. Specific policies and wording require product and legal review. Routed to `product-framing` and `interaction-design`, using `product-outcomes` and `task-hierarchy`.

| Step | User action and system response | Errors and recovery |
|---|---|---|
| Review cart | Show items, quantities, price, tax/shipping estimate and currency; allow editing. | Empty cart offers return to shopping. Changed price/availability is explained and requires review; preserve remaining items. |
| Contact and delivery | Collect email and required shipping address; offer billing address when needed. | Label fields and describe validation beside each field; retain valid entries and focus the first error on submit. Address lookup unavailable → permit manual entry. |
| Delivery method | Show available options and costs before selection. | No eligible method → explain constraints and offer address edit or support. Changed quote → show change and request acceptance. |
| Payment | Collect method through provider's accessible controls; show total and place-order action. | Decline → explain next step without exposing sensitive details; allow retry or another method. Provider unavailable → keep cart and delivery details; offer retry. Do not store raw card details. |
| Submit | Disable duplicate submissions while pending; communicate progress. | If response is uncertain, do not invite an immediate duplicate order: check order status through the service before retrying. Offer support if status cannot be determined. |
| Confirmation | Show order identifier, summary and next steps once confirmed. | If confirmation cannot be loaded, offer order lookup or support, not a claim that payment failed. |

**Acceptance and handoff:** retain non-sensitive input when going Back; keyboard operable controls, visible focus, associated errors and status messages; server validates prices and stock; payment and order services define idempotency and uncertain-result behavior. Test with the actual provider, devices and assistive technology. Required decisions: tax, guest eligibility, data retention, delivery countries, payment methods and support ownership. This is a proposed flow, not a tested checkout or a claim of legal compliance.
