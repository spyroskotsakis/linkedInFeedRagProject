# MlflowAIGatewayEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.mlflow_gateway.MlflowAIGatewayEmbeddings.html
**Word Count:** 79
**Links Count:** 224
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# MlflowAIGatewayEmbeddings\#

_class _langchain\_community.embeddings.mlflow\_gateway.MlflowAIGatewayEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow_gateway.html#MlflowAIGatewayEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

MLflow AI Gateway embeddings.

To use, you should have the `mlflow[gateway]` python package installed. For more information, see <https://mlflow.org/docs/latest/gateway/index.html>.

Example               from langchain_community.embeddings import MlflowAIGatewayEmbeddings          embeddings = MlflowAIGatewayEmbeddings(         gateway_uri="<your-mlflow-ai-gateway-uri>",         route="<your-mlflow-ai-gateway-embeddings-route>"     )     

_param _gateway\_uri _: str | None_ _ = None_\#     

The URI for the MLflow AI Gateway API.

_param _route _: str_ _\[Required\]_\#     

The route to use for the MLflow AI Gateway API.

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

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow_gateway.html#MlflowAIGatewayEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mlflow_gateway.html#MlflowAIGatewayEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using MlflowAIGatewayEmbeddings

  * [MLflow AI Gateway](https://python.langchain.com/docs/integrations/providers/mlflow_ai_gateway/)

__On this page