# 024 - Scroll Performance & Service Labels Fix

## Summary
- Improved scroll smoothness by reducing the animated background workload and honoring reduced-motion preference.
- Fixed last two service labels to resolve to full translated titles.
- Enabled native smooth scrolling globally.

## Changes Made
- Optimized particle animation: lower density, capped connections, throttled frames, reduced mouse force.
- Added reduced-motion short-circuit render for the animated background.
- Added fallback translation logic for `services.*` short keys to use `services.*.title`.
- Enabled `scroll-behavior: smooth` in global styles.

## Files Updated
- src/components/AnimatedBackground.tsx
- src/contexts/LanguageContext.tsx
- src/styles/globals.css

## Notes
- Applied to both Startup and NGT repos.
