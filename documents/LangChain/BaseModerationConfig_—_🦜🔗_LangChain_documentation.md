# BaseModerationConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.BaseModerationConfig.html
**Word Count:** 52
**Links Count:** 112
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# BaseModerationConfig\#

_class _langchain\_experimental.comprehend\_moderation.base\_moderation\_config.BaseModerationConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_config.html#BaseModerationConfig)\#     

Bases: `BaseModel`

Base configuration settings for moderation.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _filters _: List\[[ModerationPiiConfig](https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPiiConfig.html#langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPiiConfig "langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPiiConfig") | [ModerationToxicityConfig](https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.ModerationToxicityConfig.html#langchain_experimental.comprehend_moderation.base_moderation_config.ModerationToxicityConfig "langchain_experimental.comprehend_moderation.base_moderation_config.ModerationToxicityConfig") | [ModerationPromptSafetyConfig](https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPromptSafetyConfig.html#langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPromptSafetyConfig "langchain_experimental.comprehend_moderation.base_moderation_config.ModerationPromptSafetyConfig")\]__ = \[ModerationPiiConfig\(threshold=0.5, labels=\[\], redact=False, mask\_character='\*'\), ModerationToxicityConfig\(threshold=0.5, labels=\[\]\), ModerationPromptSafetyConfig\(threshold=0.5\)\]_\#     

Filters applied to the moderation chain, defaults to \[ModerationPiiConfig\(\), ModerationToxicityConfig\(\), ModerationPromptSafetyConfig\(\)\]

__On this page