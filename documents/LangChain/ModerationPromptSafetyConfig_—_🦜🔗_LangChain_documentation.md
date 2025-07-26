# ModerationPromptSafetyConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPromptSafetyConfig.html
**Word Count:** 55
**Links Count:** 109
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# ModerationPromptSafetyConfig\#

_class _langchain\_experimental.comprehend\_moderation.base\_moderation\_config.ModerationPromptSafetyConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_config.html#ModerationPromptSafetyConfig)\#     

Bases: `BaseModel`

Configuration for Prompt Safety moderation filter.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _threshold _: float_ _ = 0.5_\#     

Threshold for Prompt Safety classification confidence score, defaults to 0.5 i.e. 50%

__On this page