# MlflowCohereEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.mlflow.MlflowCohereEmbeddings.html
**Word Count:** 62
**Links Count:** 226
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# MlflowCohereEmbeddings\#

_class _langchain\_community.embeddings.mlflow.MlflowCohereEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow.html#MlflowCohereEmbeddings)\#     

Bases: [`MlflowEmbeddings`](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.mlflow.MlflowEmbeddings.html#langchain_community.embeddings.mlflow.MlflowEmbeddings "langchain_community.embeddings.mlflow.MlflowEmbeddings")

Cohere embedding LLMs in MLflow.

_param _documents\_params _: Dict\[str, str\]__ = \{'input\_type': 'search\_document'\}_\#     

_param _endpoint _: str_ _\[Required\]_\#     

The endpoint to use.

_param _query\_params _: Dict\[str, str\]__ = \{'input\_type': 'search\_query'\}_\#     

The parameters to use for documents.

_param _target\_uri _: str_ _\[Required\]_\#     

The target URI to use.

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\(

    _texts : List\[str\]_,     _params : Dict\[str, str\]_, \) → List\[List\[float\]\]\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **params** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\]\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\]\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

__On this page