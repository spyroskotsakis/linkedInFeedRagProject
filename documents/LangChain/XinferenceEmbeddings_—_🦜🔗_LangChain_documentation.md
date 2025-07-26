# XinferenceEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.xinference.XinferenceEmbeddings.html
**Word Count:** 199
**Links Count:** 227
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# XinferenceEmbeddings\#

_class _langchain\_community.embeddings.xinference.XinferenceEmbeddings\(

    _server\_url : str | None = None_,     _model\_uid : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/xinference.html#XinferenceEmbeddings)\#     

Xinference embedding models.

To use, you should have the xinference library installed:               pip install xinference     

If you’re simply using the services provided by Xinference, you can utilize the xinference\_client package:               pip install xinference_client     

Check out: [xorbitsai/inference](https://github.com/xorbitsai/inference) To run, you need to start a Xinference supervisor on one server and Xinference workers on the other servers.

Example

To start a local instance of Xinference, run               $ xinference     

You can also deploy Xinference in a distributed cluster. Here are the steps:

Starting the supervisor:               $ xinference-supervisor     

If you’re simply using the services provided by Xinference, you can utilize the xinference\_client package:               pip install xinference_client     

Starting the worker:               $ xinference-worker     

Then, launch a model using command line interface \(CLI\).

Example:               $ xinference launch -n orca -s 3 -q q4_0     

It will return a model UID. Then you can use Xinference Embedding with LangChain.

Example:               from langchain_community.embeddings import XinferenceEmbeddings          xinference = XinferenceEmbeddings(         server_url="http://0.0.0.0:9997",         model_uid = {model_uid} # replace model_uid with the model UID return from launching the model     )     

Attributes

Methods

`__init__`\(\[server\_url, model\_uid\]\) |    ---|---   `aembed_documents`\(texts\) | Asynchronous Embed search docs.   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed a list of documents using Xinference.   `embed_query`\(text\) | Embed a query of documents using Xinference.      Parameters:     

  * **server\_url** \(_str_ _|__None_\)

  * **model\_uid** \(_str_ _|__None_\)

\_\_init\_\_\(

    _server\_url : str | None = None_,     _model\_uid : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/xinference.html#XinferenceEmbeddings.__init__)\#     

Parameters:     

  * **server\_url** \(_str_ _|__None_\)

  * **model\_uid** \(_str_ _|__None_\)

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/xinference.html#XinferenceEmbeddings.embed_documents)\#     

Embed a list of documents using Xinference. :param texts: The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/xinference.html#XinferenceEmbeddings.embed_query)\#     

Embed a query of documents using Xinference. :param text: The text to embed.

Returns:     

Embeddings for the text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using XinferenceEmbeddings

  * [Xorbits inference \(Xinference\)](https://python.langchain.com/docs/integrations/text_embedding/xinference/)

__On this page