# ModerationToxicityConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.ModerationToxicityConfig.html
**Word Count:** 58
**Links Count:** 111
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# ModerationToxicityConfig\#

_class _langchain\_experimental.comprehend\_moderation.base\_moderation\_config.ModerationToxicityConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_config.html#ModerationToxicityConfig)\#     

Bases: `BaseModel`

Configuration for Toxicity moderation filter.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _labels _: List\[str\]__ = \[\]_\#     

List of toxic labels, defaults to list\[\]

_param _threshold _: float_ _ = 0.5_\#     

Threshold for Toxic label confidence score, defaults to 0.5 i.e. 50%

__On this page