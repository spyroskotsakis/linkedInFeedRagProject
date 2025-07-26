# ClovaEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.clova.ClovaEmbeddings.html
**Word Count:** 189
**Links Count:** 229
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# ClovaEmbeddings\#

_class _langchain\_community.embeddings.clova.ClovaEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/clova.html#ClovaEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.3.4: Use `:class:`~langchain_community.ClovaXEmbeddings`` instead. It will not be removed until langchain-community==1.0.0.

Clova’s embedding service.

To use this service,

you should have the following environment variables set with your API tokens and application ID, or pass them as named parameters to the constructor:

  * `CLOVA_EMB_API_KEY`: API key for accessing Clova’s embedding service.

  * `CLOVA_EMB_APIGW_API_KEY`: API gateway key for enhanced security.

  * `CLOVA_EMB_APP_ID`: Application ID for identifying your application.

Example               from langchain_community.embeddings import ClovaEmbeddings     embeddings = ClovaEmbeddings(         clova_emb_api_key='your_clova_emb_api_key',         clova_emb_apigw_api_key='your_clova_emb_apigw_api_key',         app_id='your_app_id'     )          query_text = "This is a test query."     query_result = embeddings.embed_query(query_text)          document_text = "This is a test document."     document_result = embeddings.embed_documents([document_text])     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _app\_id _: SecretStr | None_ _ = None_\#     

Application ID for identifying your application.

_param _clova\_emb\_api\_key _: SecretStr | None_ _ = None_\#     

API key for accessing Clova’s embedding service.

_param _clova\_emb\_apigw\_api\_key _: SecretStr | None_ _ = None_\#     

API gateway key for enhanced security.

_param _endpoint\_url _: str_ _ = 'https://clovastudio.apigw.ntruss.com/testapp/v1/api-tools/embedding'_\#     

Endpoint URL to use.

_param _model _: str_ _ = 'clir-emb-dolphin'_\#     

Embedding model name to use.

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

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/clova.html#ClovaEmbeddings.embed_documents)\#     

Embed a list of texts and return their embeddings.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/clova.html#ClovaEmbeddings.embed_query)\#     

Embed a single query text and return its embedding.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using ClovaEmbeddings

  * [Clova Embeddings](https://python.langchain.com/docs/integrations/text_embedding/clova/)

__On this page