# ClovaXEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.naver.ClovaXEmbeddings.html
**Word Count:** 124
**Links Count:** 237
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# ClovaXEmbeddings\#

_class _langchain\_community.embeddings.naver.ClovaXEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/naver.html#ClovaXEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

NCP ClovaStudio Embedding API.

following environment variables set or passed in constructor in lower case: \- `NCP_CLOVASTUDIO_API_KEY` \- `NCP_APIGW_API_KEY` \- `NCP_CLOVASTUDIO_APP_ID`

Example               from langchain_community import ClovaXEmbeddings          model = ClovaXEmbeddings(model="clir-emb-dolphin")     output = embedding.embed_documents(documents)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _app\_id _: str | None_ _ = None_\#     

_param _base\_url _: str | None_ _ = None_\#     

Automatically inferred from env are NCP\_CLOVASTUDIO\_API\_BASE\_URL if not provided.

_param _model\_name _: str_ _ = 'clir-emb-dolphin'_\#     

NCP ClovaStudio embedding model name

_param _ncp\_apigw\_api\_key _: SecretStr | None_ _ = None_ _\(alias 'apigw\_api\_key'\)_\#     

Automatically inferred from env are NCP\_APIGW\_API\_KEY if not provided.

_param _ncp\_clovastudio\_api\_key _: SecretStr | None_ _ = None_ _\(alias 'api\_key'\)_\#     

Automatically inferred from env are NCP\_CLOVASTUDIO\_API\_KEY if not provided.

_param _service\_app _: bool_ _ = False_\#     

false: use testapp, true: use service app on NCP Clova Studio

_param _timeout _: int_ _ = 60_\#     

Constraints:     

  * **gt** = 0

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/naver.html#ClovaXEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/naver.html#ClovaXEmbeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

default\_headers\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/naver.html#ClovaXEmbeddings.default_headers)\#     

Return type:     

_Dict_\[str, _Any_\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/naver.html#ClovaXEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/naver.html#ClovaXEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

__On this page