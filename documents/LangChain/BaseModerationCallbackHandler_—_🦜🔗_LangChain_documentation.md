# BaseModerationCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation_callbacks.BaseModerationCallbackHandler.html
**Word Count:** 52
**Links Count:** 123
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# BaseModerationCallbackHandler\#

_class _langchain\_experimental.comprehend\_moderation.base\_moderation\_callbacks.BaseModerationCallbackHandler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_callbacks.html#BaseModerationCallbackHandler)\#     

Base class for moderation callback handlers.

Attributes

`pii_callback` |    ---|---   `prompt_safety_callback` |    `toxicity_callback` |       Methods

`__init__`\(\) |    ---|---   `on_after_pii`\(moderation\_beacon, unique\_id, ...\) | Run after PII validation is complete.   `on_after_prompt_safety`\(moderation\_beacon, ...\) | Run after Prompt Safety validation is complete.   `on_after_toxicity`\(moderation\_beacon, ...\) | Run after Toxicity validation is complete.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_callbacks.html#BaseModerationCallbackHandler.__init__)\#     

Return type:     

None

_async _on\_after\_pii\(

    _moderation\_beacon : Dict\[str, Any\]_,     _unique\_id : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_callbacks.html#BaseModerationCallbackHandler.on_after_pii)\#     

Run after PII validation is complete.

Parameters:     

  * **moderation\_beacon** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **unique\_id** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_async _on\_after\_prompt\_safety\(

    _moderation\_beacon : Dict\[str, Any\]_,     _unique\_id : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_callbacks.html#BaseModerationCallbackHandler.on_after_prompt_safety)\#     

Run after Prompt Safety validation is complete.

Parameters:     

  * **moderation\_beacon** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **unique\_id** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_async _on\_after\_toxicity\(

    _moderation\_beacon : Dict\[str, Any\]_,     _unique\_id : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation_callbacks.html#BaseModerationCallbackHandler.on_after_toxicity)\#     

Run after Toxicity validation is complete.

Parameters:     

  * **moderation\_beacon** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **unique\_id** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

__On this page