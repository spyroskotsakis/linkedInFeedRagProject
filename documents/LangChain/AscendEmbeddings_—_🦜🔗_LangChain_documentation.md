# AscendEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.ascend.AscendEmbeddings.html
**Word Count:** 89
**Links Count:** 244
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# AscendEmbeddings\#

_class _langchain\_community.embeddings.ascend.AscendEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ascend.html#AscendEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

Ascend NPU accelerate Embedding model

Please ensure that you have installed CANN and torch\_npu.

Example:

from langchain\_community.embeddings import AscendEmbeddings model = AscendEmbeddings\(model\_path=<path\_to\_model>,

> device\_id=0, query\_instruction=”Represent this sentence for searching relevant passages: “

\)

_param _batch\_size _: int_ _ = 32_\#     

_param _device\_id _: int_ _ = 0_\#     

Unstruntion to used for embedding query.

_param _document\_instruction _: str_ _ = ''_\#     

_param _model _: Any_ _\[Required\]_\#     

_param _model\_path _: str_ _\[Required\]_\#     

Ascend NPU device id.

_param _pooling\_method _: str | None_ _ = 'cls'_\#     

_param _query\_instruction _: str_ _ = ''_\#     

Unstruntion to used for embedding document.

_param _tokenizer _: Any_ _\[Required\]_\#     

_param _use\_fp16 _: bool_ _ = True_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ascend.html#AscendEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ascend.html#AscendEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

encode\(

    _sentences : Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ascend.html#AscendEmbeddings.encode)\#     

Parameters:     

**sentences** \(_Any_\)

Return type:     

_Any_

pooling\(

    _last\_hidden\_state : Any_,     _attention\_mask : Any = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ascend.html#AscendEmbeddings.pooling)\#     

Parameters:     

  * **last\_hidden\_state** \(_Any_\)

  * **attention\_mask** \(_Any_\)

Return type:     

_Any_

Examples using AscendEmbeddings

  * [\# Related](https://python.langchain.com/docs/integrations/text_embedding/ascend/)

  * [Ascend](https://python.langchain.com/docs/integrations/providers/ascend/)

__On this page