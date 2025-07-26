# BaseModeration — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.base_moderation.BaseModeration.html
**Word Count:** 19
**Links Count:** 119
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# BaseModeration\#

_class _langchain\_experimental.comprehend\_moderation.base\_moderation.BaseModeration\(

    _client : Any_,     _config : Any | None = None_,     _moderation\_callback : Any | None = None_,     _unique\_id : str | None = None_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation.html#BaseModeration)\#     

Base class for moderation.

Methods

`__init__`\(client\[, config, ...\]\) |    ---|---   `moderate`\(prompt\) | Moderate the input prompt.      Parameters:     

  * **client** \(_Any_\)

  * **config** \(_Any_ _|__None_\)

  * **moderation\_callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|__None_\)

\_\_init\_\_\(

    _client : Any_,     _config : Any | None = None_,     _moderation\_callback : Any | None = None_,     _unique\_id : str | None = None_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation.html#BaseModeration.__init__)\#     

Parameters:     

  * **client** \(_Any_\)

  * **config** \(_Any_ _|__None_\)

  * **moderation\_callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|__None_\)

moderate\(_prompt : Any_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/base_moderation.html#BaseModeration.moderate)\#     

Moderate the input prompt.

Parameters:     

**prompt** \(_Any_\)

Return type:     

str

__On this page