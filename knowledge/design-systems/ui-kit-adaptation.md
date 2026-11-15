<!-- pdi-topic: {"id":"ui-kit-adaptation","domain":"design-systems","depths":["foundation","practitioner","advanced"],"sources":["uswds-tokens","wcag22","pdi-guidance"]} -->
# Adapting to existing UI kits (shadcn/ui, Nuxt UI, Apple HIG, Material 3, Custom)

## What and why
Most real-world product design and engineering work builds on an established UI kit or platform design system rather than inventing components from scratch. AI agents frequently fail by generating bespoke HTML/CSS components or arbitrarily overriding spacing, radii, and colors even when a project already uses a standard kit. Strictly reusing the active UI kit preserves engineering velocity, visual consistency, and built-in accessibility contracts.

## When to apply
Whenever framing, specifying interactions, defining tokens, building prototypes, or writing handoffs for web or mobile products—whether using **shadcn/ui**, **Nuxt UI**, **Apple Human Interface Guidelines (iOS/iPadOS/macOS)**, **Google Material Design 3 (Android)**, or a **Custom Design System**.

## Fundamental principles
**Foundation (Strict Default-First Rule):**
1. **Detect or ask for the UI kit before designing or coding.** Inspect `package.json`, `components.json`, `nuxt.config.ts`, `Podfile`/`Package.swift`, `build.gradle`, or existing CSS tokens.
2. **Use stock UI kit components and variants as-is.** Do not invent custom components, wrapper divs with competing padding, or arbitrary CSS overrides when the kit already provides the component and variant.
3. **Modify only on explicit request or proven gap.** Customize a component's appearance or behavior only when the user explicitly requests a change or when a documented task requirement cannot be met by any native component in the kit.

## Practical implementation
**Practitioner (Mechanism by Platform & UI Kit):**

- **1. Web — `shadcn/ui` (React / Next.js / Tailwind CSS):**
  - **Mechanism:** Inspect `components.json` and `components/ui/`. Compose interfaces strictly from official shadcn/ui primitives (`Button`, `Input`, `Label`, `Select`, `Dialog`, `Sheet`, `Table`, `Tabs`, `Card`, `Badge`, `Alert`, `Form`, `Sonner`/`Toast`).
  - **Styling & Tokens:** Use semantic CSS variables (`bg-background`, `text-foreground`, `bg-primary`, `text-muted-foreground`, `border-input`, `ring-ring`, `text-destructive`) and native component variants (`variant="default" | "secondary" | "outline" | "ghost" | "destructive"`, `size="default" | "sm" | "lg" | "icon"`). Never attach raw hex classes (`bg-[#123456]`) or override internal primitive padding unless requested.

- **2. Web — `Nuxt UI` (Vue 3 / Nuxt / Tailwind CSS):**
  - **Mechanism:** Inspect `nuxt.config.ts` and `app.config.ts`. Compose strictly from Nuxt UI components (`UButton`, `UInput`, `UForm`, `UFormField` / `UFormGroup`, `USelect`, `UModal`, `USlideover`, `UTable`, `UTabs`, `UCard`, `UBadge`, `UAlert`, `UToast`).
  - **Styling & Tokens:** Use Nuxt UI semantic props (`color="primary" | "neutral" | "error" | "warning" | "success"`, `variant="solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`, `size="xs" | "sm" | "md" | "lg" | "xl"`). Configure theme tokens via `app.config.ts` (`ui.colors`) rather than ad-hoc inline CSS overrides.

- **3. Mobile — `Apple Human Interface Guidelines / HIG` (iOS / SwiftUI / UIKit) & `Google Material Design 3 / M3` (Android / Jetpack Compose):**
  - **Mechanism:** Never put web patterns (hamburger menus on top of bottom tabs, web-style breadcrumbs, custom non-native select dropdowns) onto native mobile screens.
  - **Apple HIG (iOS):** Use native navigation and containers (`NavigationStack`, `TabView`, `List` with `.insetGrouped`, `Sheet` with presentation detents, `Alert`, `ConfirmationDialog`, `Picker`, `Toggle`). Respect Safe Areas, Dynamic Type (`font(.body)`, `.headline`, `.subheadline`), SF Symbols, standard `44x44pt` minimum hit targets, and system semantic colors (`systemBackground`, `secondarySystemBackground`, `label`, `secondaryLabel`, `systemBlue`, `systemRed`).
  - **Google Material 3 (Android):** Use native M3 Compose/View components (`Scaffold`, `TopAppBar`, `NavigationBar`, `NavigationDrawer`, `FilledButton`, `OutlinedButton`, `TextButton`, `OutlinedTextField`, `ModalBottomSheet`, `AlertDialog`, `Snackbar`, `Card`). Bind strictly to `MaterialTheme.colorScheme` (`primary`, `onPrimary`, `surface`, `surfaceContainer`, `onSurface`, `error`), `MaterialTheme.typography` (`headlineMedium`, `bodyLarge`, `labelLarge`), and `48x48dp` minimum touch targets.

- **4. Custom UI Kit / Bespoke CSS Token System (Vanilla HTML/CSS or Proprietary Library):**
  - **Mechanism:** When no third-party kit is used, define a locked minimal primitive-to-semantic token table and a small set of canonical component classes (`.btn`, `.btn-primary`, `.btn-secondary`, `.btn-danger`, `.field`, `.card`, `.alert`) **before** building screens. Every screen must reuse those exact classes without inventing one-off per-page button or input styles.

**Advanced:** In multi-platform organizations, map shared domain states and copy matrices (`templates/handoff-and-changelog.md`) once, then bind each state to its native platform equivalent (e.g., a destructive confirmation maps to `<AlertDialog>` in shadcn/ui, `<UModal>` in Nuxt UI, `.confirmationDialog` in SwiftUI, and `AlertDialog` in Material 3) rather than forcing iOS to look like Android or Web.

## Good and bad examples
Good: Using stock `<Button variant="destructive">` and `<AlertDialog>` from `shadcn/ui` with zero custom CSS overrides, documenting the mapping in the handoff table. Bad: Writing `<div class="custom-red-btn px-[19px] py-[7px] rounded-[11px] bg-[#e11d48]">` inside a project that already has `shadcn/ui` or `Nuxt UI` installed.

## Common mistakes
Inventing custom dropdowns, modals, or buttons when the active UI kit already provides accessible primitives; overriding standard UI kit spacing/radius without user feedback; mixing web top-nav bars into iOS/Android mobile flows; failing to document why a custom component was necessary in the handoff.

## Evaluate the result
Did the agent identify the target UI kit before prototyping? Are 100% of standard controls using unmodified kit components and semantic variants? If any component was modified or custom-built, is there an explicit user request or documented gap in the handoff table?

## AI application
Always inspect the workspace or ask the user which UI kit applies (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or `Custom`). Default to zero modifications on kit primitives; log every component mapping and any approved customization in `templates/handoff-and-changelog.md`.

## Related concepts
[Tokens and component contracts](component-contracts.md), [Design tokens, component APIs and system governance](token-governance.md), [Responsive and accessible interfaces](../frontend-engineering/responsive-accessible-ui.md).

## References and further learning
[USWDS Design tokens](https://designsystem.digital.gov/design-tokens/), [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) and [PDI design practice](../design-practice.md). [Source registry](../sources.yaml) records provenance and review scope.
