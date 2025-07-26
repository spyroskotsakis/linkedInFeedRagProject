# VwPolicy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.VwPolicy.html
**Word Count:** 15
**Links Count:** 156
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# VwPolicy\#

_class _langchain\_experimental.rl\_chain.base.VwPolicy\(

    _model\_repo : [ModelRepository](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.model_repository.ModelRepository.html#langchain_experimental.rl_chain.model_repository.ModelRepository "langchain_experimental.rl_chain.model_repository.ModelRepository")_,     _vw\_cmd : List\[str\]_,     _feature\_embedder : [Embedder](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")_,     _vw\_logger : [VwLogger](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger "langchain_experimental.rl_chain.vw_logger.VwLogger")_,     _\* args: Any_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#VwPolicy)\#     

Vowpal Wabbit policy.

Methods

`__init__`\(model\_repo, vw\_cmd, ...\) |    ---|---   `learn`\(event\) |    `log`\(event\) |    `predict`\(event\) |    `save`\(\) |       Parameters:     

  * **model\_repo** \([_ModelRepository_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.model_repository.ModelRepository.html#langchain_experimental.rl_chain.model_repository.ModelRepository "langchain_experimental.rl_chain.model_repository.ModelRepository")\)

  * **vw\_cmd** \(_List_ _\[__str_ _\]_\)

  * **feature\_embedder** \([_Embedder_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")\)

  * **vw\_logger** \([_VwLogger_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger "langchain_experimental.rl_chain.vw_logger.VwLogger")\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _model\_repo : [ModelRepository](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.model_repository.ModelRepository.html#langchain_experimental.rl_chain.model_repository.ModelRepository "langchain_experimental.rl_chain.model_repository.ModelRepository")_,     _vw\_cmd : List\[str\]_,     _feature\_embedder : [Embedder](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")_,     _vw\_logger : [VwLogger](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger "langchain_experimental.rl_chain.vw_logger.VwLogger")_,     _\* args: Any_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#VwPolicy.__init__)\#     

Parameters:     

  * **model\_repo** \([_ModelRepository_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.model_repository.ModelRepository.html#langchain_experimental.rl_chain.model_repository.ModelRepository "langchain_experimental.rl_chain.model_repository.ModelRepository")\)

  * **vw\_cmd** \(_List_ _\[__str_ _\]_\)

  * **feature\_embedder** \([_Embedder_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")\)

  * **vw\_logger** \([_VwLogger_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger "langchain_experimental.rl_chain.vw_logger.VwLogger")\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

learn\(

    _event : TEvent_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#VwPolicy.learn)\#     

Parameters:     

**event** \(_TEvent_\)

Return type:     

None

log\(

    _event : TEvent_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#VwPolicy.log)\#     

Parameters:     

**event** \(_TEvent_\)

Return type:     

None

predict\(

    _event : TEvent_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#VwPolicy.predict)\#     

Parameters:     

**event** \(_TEvent_\)

Return type:     

_Any_

save\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#VwPolicy.save)\#     

Return type:     

None

__On this page