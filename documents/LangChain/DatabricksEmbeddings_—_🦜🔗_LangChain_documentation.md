# DatabricksEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.databricks.DatabricksEmbeddings.html
**Word Count:** 84
**Links Count:** 228
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# DatabricksEmbeddings\#

_class _langchain\_community.embeddings.databricks.DatabricksEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/databricks.html#DatabricksEmbeddings)\#     

Bases: [`MlflowEmbeddings`](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.mlflow.MlflowEmbeddings.html#langchain_community.embeddings.mlflow.MlflowEmbeddings "langchain_community.embeddings.mlflow.MlflowEmbeddings")

Deprecated since version 0.3.3: Use `:class:`~databricks_langchain.DatabricksEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Databricks embeddings.

To use, you should have the `mlflow` python package installed. For more information, see <https://mlflow.org/docs/latest/llms/deployments>.

Example               from langchain_community.embeddings import DatabricksEmbeddings          embeddings = DatabricksEmbeddings(         target_uri="databricks",         endpoint="embeddings",     )     

_param _documents\_params _: Dict\[str, str\]__ = \{\}_\#     

_param _endpoint _: str_ _\[Required\]_\#     

The endpoint to use.

_param _query\_params _: Dict\[str, str\]__ = \{\}_\#     

The parameters to use for documents.

_param _target\_uri _: str_ _ = 'databricks'_\#     

The target URI to use. Defaults to `databricks`.

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

Examples using DatabricksEmbeddings

  * [Databricks](https://python.langchain.com/docs/integrations/text_embedding/databricks/)

__On this page