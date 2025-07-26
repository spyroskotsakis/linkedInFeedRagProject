# CloudflareWorkersAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.cloudflare_workersai.CloudflareWorkersAIEmbeddings.html
**Word Count:** 101
**Links Count:** 234
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# CloudflareWorkersAIEmbeddings\#

_class _langchain\_community.embeddings.cloudflare\_workersai.CloudflareWorkersAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cloudflare_workersai.html#CloudflareWorkersAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.3.23: Use `:class:`~langchain_cloudflare.CloudflareWorkersAIEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Cloudflare Workers AI embedding model.

To use, you need to provide an API token and account ID to access Cloudflare Workers AI.

Example               from langchain_community.embeddings import CloudflareWorkersAIEmbeddings          account_id = "my_account_id"     api_token = "my_secret_api_token"     model_name =  "@cf/baai/bge-small-en-v1.5"          cf = CloudflareWorkersAIEmbeddings(         account_id=account_id,         api_token=api_token,         model_name=model_name     )     

Initialize the Cloudflare Workers AI client.

_param _account\_id _: str_ _\[Required\]_\#     

_param _api\_base\_url _: str_ _ = 'https://api.cloudflare.com/client/v4/accounts'_\#     

_param _api\_token _: str_ _\[Required\]_\#     

_param _batch\_size _: int_ _ = 50_\#     

_param _headers _: Dict\[str, str\]__ = \{'Authorization': 'Bearer '\}_\#     

_param _model\_name _: str_ _ = '@cf/baai/bge-base-en-v1.5'_\#     

_param _strip\_new\_lines _: bool_ _ = True_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cloudflare_workersai.html#CloudflareWorkersAIEmbeddings.embed_documents)\#     

Compute doc embeddings using Cloudflare Workers AI.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cloudflare_workersai.html#CloudflareWorkersAIEmbeddings.embed_query)\#     

Compute query embeddings using Cloudflare Workers AI.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using CloudflareWorkersAIEmbeddings

  * [Cloudflare](https://python.langchain.com/docs/integrations/providers/cloudflare/)

  * [Cloudflare Workers AI](https://python.langchain.com/docs/integrations/text_embedding/cloudflare_workersai/)

__On this page