# MlflowEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.mlflow.MlflowEmbeddings.html
**Word Count:** 77
**Links Count:** 231
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# MlflowEmbeddings\#

_class _langchain\_community.embeddings.mlflow.MlflowEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow.html#MlflowEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

Embedding LLMs in MLflow.

To use, you should have the mlflow\[genai\] python package installed. For more information, see <https://mlflow.org/docs/latest/llms/deployments>.

Example               from langchain_community.embeddings import MlflowEmbeddings          embeddings = MlflowEmbeddings(         target_uri="http://localhost:5000",         endpoint="embeddings",     )     

_param _documents\_params _: Dict\[str, str\]__ = \{\}_\#     

_param _endpoint _: str_ _\[Required\]_\#     

The endpoint to use.

_param _query\_params _: Dict\[str, str\]__ = \{\}_\#     

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

_async _aembed\_query\(_text : str_\) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\(

    _texts : List\[str\]_,     _params : Dict\[str, str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow.html#MlflowEmbeddings.embed)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **params** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow.html#MlflowEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow.html#MlflowEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using MlflowEmbeddings

  * [MLflow Deployments for LLMs](https://python.langchain.com/docs/integrations/providers/mlflow/)

__On this page