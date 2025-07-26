# NomicEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nomic/embeddings/langchain_nomic.embeddings.NomicEmbeddings.html
**Word Count:** 228
**Links Count:** 95
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# NomicEmbeddings\#

_class _langchain\_nomic.embeddings.NomicEmbeddings\(

    _\*_ ,     _model : str_,     _nomic\_api\_key : str | None = ..._,     _dimensionality : int | None = ..._,     _inference\_mode : Literal\['remote'\] = ..._, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nomic/embeddings.html#NomicEmbeddings)\# _class _langchain\_nomic.embeddings.NomicEmbeddings\(

    _\*_ ,     _model : str_,     _nomic\_api\_key : str | None = ..._,     _dimensionality : int | None = ..._,     _inference\_mode : Literal\['local', 'dynamic'\]_,     _device : str | None = ..._, \) _class _langchain\_nomic.embeddings.NomicEmbeddings\(

    _\*_ ,     _model : str_,     _nomic\_api\_key : str | None = ..._,     _dimensionality : int | None = ..._,     _inference\_mode : str_,     _device : str | None = ..._, \)     

NomicEmbeddings embedding model.

Example               from langchain_nomic import NomicEmbeddings          model = NomicEmbeddings()     

Initialize NomicEmbeddings model.

Parameters:     

  * **model** \(_str_\) – model name

  * **nomic\_api\_key** \(_Optional_ _\[__str_ _\]_\) – optionally, set the Nomic API key. Uses the `NOMIC_API_KEY` environment variable by default.

  * **dimensionality** \(_Optional_ _\[__int_ _\]_\) – The embedding dimension, for use with Matryoshka-capable models. Defaults to full-size.

  * **inference\_mode** \(_str_\) – How to generate embeddings. One of `'remote'`, `'local'` \(Embed4All\), or `'dynamic'` \(automatic\). Defaults to `'remote'`.

  * **device** \(_Optional_ _\[__str_ _\]_\) – The device to use for local embeddings. Choices include `'cpu'`, `'gpu'`, `'nvidia'`, `'amd'`, or a specific device name. See the docstring for `GPT4All.__init__` for more info. Typically defaults to `'cpu'`. Do not use on macOS.

  * **vision\_model** \(_Optional_ _\[__str_ _\]_\) – The vision model to use for image embeddings.

Methods

`__init__`\(\) | Initialize NomicEmbeddings model.   ---|---   `aembed_documents`\(texts\) | Asynchronous Embed search docs.   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed`\(texts, \*, task\_type\) | Embed texts.   `embed_documents`\(texts\) | Embed search docs.   `embed_image`\(uris\) |    `embed_query`\(text\) | Embed query text.      \_\_init\_\_\(

    _\*_ ,     _model : str_,     _nomic\_api\_key : str | None = None_,     _dimensionality : int | None = None_,     _inference\_mode : Literal\['remote'\] = 'remote'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nomic/embeddings.html#NomicEmbeddings.__init__)\# \_\_init\_\_\(

    _\*_ ,     _model : str_,     _nomic\_api\_key : str | None = None_,     _dimensionality : int | None = None_,     _inference\_mode : Literal\['local', 'dynamic'\]_,     _device : str | None = None_, \) \_\_init\_\_\(

    _\*_ ,     _model : str_,     _nomic\_api\_key : str | None = None_,     _dimensionality : int | None = None_,     _inference\_mode : str_,     _device : str | None = None_, \)     

Initialize NomicEmbeddings model.

Parameters:     

  * **model** – model name

  * **nomic\_api\_key** – optionally, set the Nomic API key. Uses the `NOMIC_API_KEY` environment variable by default.

  * **dimensionality** – The embedding dimension, for use with Matryoshka-capable models. Defaults to full-size.

  * **inference\_mode** – How to generate embeddings. One of `'remote'`, `'local'` \(Embed4All\), or `'dynamic'` \(automatic\). Defaults to `'remote'`.

  * **device** – The device to use for local embeddings. Choices include `'cpu'`, `'gpu'`, `'nvidia'`, `'amd'`, or a specific device name. See the docstring for `GPT4All.__init__` for more info. Typically defaults to `'cpu'`. Do not use on macOS.

  * **vision\_model** – The vision model to use for image embeddings.

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

    _texts : list\[str\]_,     _\*_ ,     _task\_type : str_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nomic/embeddings.html#NomicEmbeddings.embed)\#     

Embed texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – list of texts to embed

  * **task\_type** \(_str_\) – the task type to use when embedding. One of `'search_query'`, `'search_document'`, `'classification'`, `'clustering'`

Return type:     

list\[list\[float\]\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nomic/embeddings.html#NomicEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – list of texts to embed as documents

Return type:     

list\[list\[float\]\]

embed\_image\(

    _uris : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nomic/embeddings.html#NomicEmbeddings.embed_image)\#     

Parameters:     

**uris** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nomic/embeddings.html#NomicEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – query text

Return type:     

list\[float\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)