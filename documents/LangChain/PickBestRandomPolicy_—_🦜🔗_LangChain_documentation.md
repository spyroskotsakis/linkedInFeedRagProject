# PickBestRandomPolicy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestRandomPolicy.html
**Word Count:** 17
**Links Count:** 153
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# PickBestRandomPolicy\#

_class _langchain\_experimental.rl\_chain.pick\_best\_chain.PickBestRandomPolicy\(

    _feature\_embedder : [Embedder](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestRandomPolicy)\#     

Random policy for PickBest chain.

Methods

`__init__`\(feature\_embedder, \*\*kwargs\) |    ---|---   `learn`\(event\) |    `log`\(event\) |    `predict`\(event\) |    `save`\(\) |       Parameters:     

  * **feature\_embedder** \([_base.Embedder_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _feature\_embedder : [Embedder](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestRandomPolicy.__init__)\#     

Parameters:     

  * **feature\_embedder** \([_Embedder_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Embedder.html#langchain_experimental.rl_chain.base.Embedder "langchain_experimental.rl_chain.base.Embedder")\)

  * **kwargs** \(_Any_\)

learn\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestRandomPolicy.learn)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

None

log\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestRandomPolicy.log)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

None

predict\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → List\[Tuple\[int, float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestRandomPolicy.predict)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

_List_\[_Tuple_\[int, float\]\]

save\(\) → None\#     

Return type:     

None

__On this page