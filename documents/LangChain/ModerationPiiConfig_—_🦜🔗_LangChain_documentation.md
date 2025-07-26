# ModerationPiiConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPiiConfig.html
**Word Count:** 74
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# ModerationPiiConfig\#

_class _langchain\_experimental.comprehend\_moderation.base\_moderation\_config.ModerationPiiConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_config.html#ModerationPiiConfig)\#     

Bases: `BaseModel`

Configuration for PII moderation filter.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _labels _: List\[str\]__ = \[\]_\#     

List of PII Universal Labels. Defaults to list\[\]

_param _mask\_character _: str_ _ = '\*'_\#     

Redaction mask character in case redact=True, defaults to asterisk \(\*\)

_param _redact _: bool_ _ = False_\#     

Whether to perform redaction of detected PII entities

_param _threshold _: float_ _ = 0.5_\#     

Threshold for PII confidence score, defaults to 0.5 i.e. 50%

__On this page