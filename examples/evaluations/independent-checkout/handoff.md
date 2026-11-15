# Checkout

Request: prototype checkout with a Pay button; payment service unavailable. Assumptions: a buyer purchases two notebooks; prices, product, brand, delivery cost and email confirmation are illustrative and have not been verified.

Behavior: browser validates a required email; submitting valid input prevents navigation and displays “Pembayaran belum tersedia. Tidak ada transaksi yang dilakukan.” Focus moves to that status. No payment, order creation, email, data storage or network request is implemented.

Limitations: no payment provider, order management, payment methods, tax calculation, delivery-address form, server-side validation, accessibility conformance, browser compatibility or actual user research. The wording promising email confirmation describes a future service; it should be reviewed or removed because email is not sent. Actual checkout needs provider validation, errors and uncertain-result recovery before use.
