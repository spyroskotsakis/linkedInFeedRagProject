# GPT4AllEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.gpt4all.GPT4AllEmbeddings.html
**Word Count:** 106
**Links Count:** 228
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# GPT4AllEmbeddings\#

_class _langchain\_community.embeddings.gpt4all.GPT4AllEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gpt4all.html#GPT4AllEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

GPT4All embedding models.

To use, you should have the gpt4all python package installed

Example               from langchain_community.embeddings import GPT4AllEmbeddings          model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf"     gpt4all_kwargs = {'allow_download': 'True'}     embeddings = GPT4AllEmbeddings(         model_name=model_name,         gpt4all_kwargs=gpt4all_kwargs     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _device _: str | None_ _ = 'cpu'_\#     

_param _gpt4all\_kwargs _: dict | None_ _ = \{\}_\#     

_param _model\_name _: str | None_ _ = None_\#     

_param _n\_threads _: int | None_ _ = None_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gpt4all.html#GPT4AllEmbeddings.embed_documents)\#     

Embed a list of documents using GPT4All.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gpt4all.html#GPT4AllEmbeddings.embed_query)\#     

Embed a query using GPT4All.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using GPT4AllEmbeddings

  * [GPT4All](https://python.langchain.com/docs/integrations/text_embedding/gpt4all/)

  * [ManticoreSearch VectorStore](https://python.langchain.com/docs/integrations/vectorstores/manticore_search/)

__On this page