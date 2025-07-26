# HunyuanEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.hunyuan.HunyuanEmbeddings.html
**Word Count:** 94
**Links Count:** 235
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# HunyuanEmbeddings\#

_class _langchain\_community.embeddings.hunyuan.HunyuanEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/hunyuan.html#HunyuanEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

Tencent Hunyuan embedding models API by Tencent.

For more information, see <https://cloud.tencent.com/document/product/1729>

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

The tencentcloud client.

_param _embedding\_ctx\_length _: int_ _ = 1024_\#     

The max embedding context length of hunyuan embedding \(defaults to 1024\).

_param _hunyuan\_secret\_id _: SecretStr | None_ _ = None_ _\(alias 'secret\_id'\)_\#     

Hunyuan Secret ID

_param _hunyuan\_secret\_key _: SecretStr | None_ _ = None_ _\(alias 'secret\_key'\)_\#     

Hunyuan Secret Key

_param _region _: Literal\['ap-guangzhou', 'ap-beijing'\]__ = 'ap-guangzhou'_\#     

The region of hunyuan service.

_param _request\_cls _: Type | None_ _ = None_\#     

The request class of tencentcloud sdk.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Show progress bar when embedding. Default is False.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/hunyuan.html#HunyuanEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/hunyuan.html#HunyuanEmbeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/hunyuan.html#HunyuanEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/hunyuan.html#HunyuanEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

__On this page