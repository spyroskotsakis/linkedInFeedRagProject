# TextModerationInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.edenai.text_moderation.TextModerationInput.html
**Word Count:** 41
**Links Count:** 409
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# TextModerationInput\#

_class _langchain\_community.tools.edenai.text\_moderation.TextModerationInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/edenai/text_moderation.html#TextModerationInput)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

Text to moderate

__On this page