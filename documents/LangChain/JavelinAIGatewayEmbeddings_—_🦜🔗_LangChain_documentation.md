# JavelinAIGatewayEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.javelin_ai_gateway.JavelinAIGatewayEmbeddings.html
**Word Count:** 91
**Links Count:** 231
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# JavelinAIGatewayEmbeddings\#

_class _langchain\_community.embeddings.javelin\_ai\_gateway.JavelinAIGatewayEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/javelin_ai_gateway.html#JavelinAIGatewayEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

Javelin AI Gateway embeddings.

To use, you should have the `javelin_sdk` python package installed. For more information, see <https://docs.getjavelin.io>

Example               from langchain_community.embeddings import JavelinAIGatewayEmbeddings          embeddings = JavelinAIGatewayEmbeddings(         gateway_uri="<javelin-ai-gateway-uri>",         route="<your-javelin-gateway-embeddings-route>"     )     

_param _client _: Any_ _\[Required\]_\#     

javelin client.

_param _gateway\_uri _: str | None_ _ = None_\#     

The URI for the Javelin AI Gateway API.

_param _javelin\_api\_key _: str | None_ _ = None_\#     

The API key for the Javelin AI Gateway API.

_param _route _: str_ _\[Required\]_\#     

The route to use for the Javelin AI Gateway API.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/javelin_ai_gateway.html#JavelinAIGatewayEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/javelin_ai_gateway.html#JavelinAIGatewayEmbeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/javelin_ai_gateway.html#JavelinAIGatewayEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/javelin_ai_gateway.html#JavelinAIGatewayEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using JavelinAIGatewayEmbeddings

  * [Javelin AI Gateway](https://python.langchain.com/docs/integrations/providers/javelin_ai_gateway/)

  * [Javelin AI Gateway Tutorial](https://python.langchain.com/docs/integrations/llms/javelin/)

__On this page