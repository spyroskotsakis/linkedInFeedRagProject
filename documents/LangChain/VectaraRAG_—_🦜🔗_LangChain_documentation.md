# VectaraRAG — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRAG.html
**Word Count:** 36
**Links Count:** 328
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# VectaraRAG\#

_class _langchain\_community.vectorstores.vectara.VectaraRAG\(

    _vectara : [Vectara](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.Vectara.html#langchain_community.vectorstores.vectara.Vectara "langchain_community.vectorstores.vectara.Vectara")_,     _config : [VectaraQueryConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")_,     _chat : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#VectaraRAG)\#     

Vectara RAG runnable.

Parameters:     

  * **vectara** \([_Vectara_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.Vectara.html#langchain_community.vectorstores.vectara.Vectara "langchain_community.vectorstores.vectara.Vectara")\) – Vectara object

  * **config** \([_VectaraQueryConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")\) – VectaraQueryConfig object

  * **chat** \(_bool_\) – bool, default False

Note

VectaraRAG implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

> The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

Attributes

Methods

`__init__`\(\*args, \*\*kwargs\) | Initialize self.   ---|---     

__On this page