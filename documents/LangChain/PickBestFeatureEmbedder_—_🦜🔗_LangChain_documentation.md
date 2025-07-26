# PickBestFeatureEmbedder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestFeatureEmbedder.html
**Word Count:** 59
**Links Count:** 162
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# PickBestFeatureEmbedder\#

_class _langchain\_experimental.rl\_chain.pick\_best\_chain.PickBestFeatureEmbedder\(

    _auto\_embed : bool_,     _model : Any | None = None_,     _\* args: Any_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder)\#     

Embed the BasedOn and ToSelectFrom inputs into a format that can be used by the learning policy.

Parameters:     

  * **auto\_embed** \(_bool_\)

  * **model** \(_Optional_ _\[__Any_ _\]_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

model name     

The type of embeddings to be used for feature representation. Defaults to BERT SentenceTransformer.

Type:     

Any, optional

Methods

`__init__`\(auto\_embed\[, model\]\) |    ---|---   `format`\(event\) |    `format_auto_embed_off`\(event\) | Converts the BasedOn and ToSelectFrom into a format that can be used by VW   `format_auto_embed_on`\(event\) |    `get_context_and_action_embeddings`\(event\) |    `get_indexed_dot_product`\(context\_emb, action\_embs\) |    `get_label`\(event\) |       \_\_init\_\_\(

    _auto\_embed : bool_,     _model : Any | None = None_,     _\* args: Any_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.__init__)\#     

Parameters:     

  * **auto\_embed** \(_bool_\)

  * **model** \(_Any_ _|__None_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

format\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.format)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

str

format\_auto\_embed\_off\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.format_auto_embed_off)\#     

Converts the BasedOn and ToSelectFrom into a format that can be used by VW

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

str

format\_auto\_embed\_on\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.format_auto_embed_on)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

str

get\_context\_and\_action\_embeddings\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → tuple[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.get_context_and_action_embeddings)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

tuple

get\_indexed\_dot\_product\(

    _context\_emb : List_,     _action\_embs : List_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.get_indexed_dot_product)\#     

Parameters:     

  * **context\_emb** \(_List_\)

  * **action\_embs** \(_List_\)

Return type:     

_Dict_

get\_label\(

    _event : [PickBestEvent](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")_, \) → tuple[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/pick_best_chain.html#PickBestFeatureEmbedder.get_label)\#     

Parameters:     

**event** \([_PickBestEvent_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.pick_best_chain.PickBestEvent.html#langchain_experimental.rl_chain.pick_best_chain.PickBestEvent "langchain_experimental.rl_chain.pick_best_chain.PickBestEvent")\)

Return type:     

tuple

__On this page