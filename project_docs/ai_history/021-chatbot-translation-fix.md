# 021 - Chatbot Translation Fix and English Restriction

**Date:** 2026-01-31
**Developer:** AI Assistant

## Summary

Fixed a critical issue where the chatbot was outputting raw translation keys (e.g., `t('services.web.title')`) instead of actual content. Also restricted the chatbot to English-only responses per user request.

## Changes Made

### 1. Fixed Chatbot Content Extraction
**Problem:** The scraper was reading raw React `.tsx` source files which contained translation keys, not values.
**Solution:** Created `Chatbot/translation_extractor.py` that parses `src/translations/serviceTranslations.ts` and `src/contexts/LanguageContext.tsx` to build the knowledge base from REAL English content.

- **New File:** `Chatbot/translation_extractor.py`
- **Updated:** `Chatbot/scraper.py` to use `translation_extractor` when running in local development mode.

### 2. English-Only Restriction
**Problem:** The chatbot needs to speak only English for now.
**Solution:** Updated the System Prompt in `Chatbot/rag_pipeline.py` to strictly enforce English responses.

- **Updated:** `Chatbot/rag_pipeline.py`
  - Added "STRICTLY ENGLISH ONLY" constraint to system prompt.
  - Instructed AI to polite decline other languages.

### 3. CLI Testing Tool
**Problem:** Need a way to test chatbot backend without running the full API server.
**Solution:** Created a CLI chat interface.

- **New File:** `Chatbot/cli_chat.py`
- Usage: `python Chatbot/cli_chat.py`

## Verification

tested using `cli_chat.py`:
- **Query:** "What services do you provide?"
- **Previous Output:** "We offer `t('services.web.feature1')`..."
- **Fixed Output:** "We offer complete online store solutions including..." (Actual English text)

## Git Commits

```
fix(chatbot): Implement translation-aware content extraction and restrict to English
```
