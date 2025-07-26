# SambaStudioEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.sambanova.SambaStudioEmbeddings.html
**Word Count:** 192
**Links Count:** 236
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# SambaStudioEmbeddings\#

_class _langchain\_community.embeddings.sambanova.SambaStudioEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sambanova.html#SambaStudioEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.3.16: Use `:class:`~langchain_sambanova.SambaStudioEmbeddings`` instead. It will not be removed until langchain-community==1.0.

SambaNova embedding models.

To use, you should have the environment variables `SAMBASTUDIO_EMBEDDINGS_BASE_URL`, `SAMBASTUDIO_EMBEDDINGS_BASE_URI` `SAMBASTUDIO_EMBEDDINGS_PROJECT_ID`, `SAMBASTUDIO_EMBEDDINGS_ENDPOINT_ID`, `SAMBASTUDIO_EMBEDDINGS_API_KEY` set with your personal sambastudio variable or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import SambaStudioEmbeddings          embeddings = SambaStudioEmbeddings(sambastudio_embeddings_base_url=base_url,                                   sambastudio_embeddings_base_uri=base_uri,                                   sambastudio_embeddings_project_id=project_id,                                   sambastudio_embeddings_endpoint_id=endpoint_id,                                   sambastudio_embeddings_api_key=api_key,                                   batch_size=32)     (or)          embeddings = SambaStudioEmbeddings(batch_size=32)          (or)          # CoE example     embeddings = SambaStudioEmbeddings(         batch_size=1,         model_kwargs={             'select_expert':'e5-mistral-7b-instruct'         }     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _batch\_size _: int_ _ = 32_\#     

Batch size for the embedding models

_param _model\_kwargs _: dict_ _ = \{\}_\#     

Key word arguments to pass to the model.

_param _sambastudio\_embeddings\_api\_key _: str_ _ = ''_\#     

sambastudio api key

_param _sambastudio\_embeddings\_base\_uri _: str_ _ = ''_\#     

endpoint base uri

_param _sambastudio\_embeddings\_base\_url _: str_ _ = ''_\#     

Base url to use

_param _sambastudio\_embeddings\_endpoint\_id _: str_ _ = ''_\#     

endpoint id on sambastudio for model

_param _sambastudio\_embeddings\_project\_id _: str_ _ = ''_\#     

Project id on sambastudio for model

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sambanova.html#SambaStudioEmbeddings.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

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

    _texts : List\[str\]_,     _batch\_size : int | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sambanova.html#SambaStudioEmbeddings.embed_documents)\#     

Returns a list of embeddings for the given sentences. :param texts: List of texts to encode :type texts: List\[str\] :param batch\_size: Batch size for the encoding :type batch\_size: int

Returns:     

List of embeddings for the given sentences

Return type:     

List\[np.ndarray\] or List\[tensor\]

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **batch\_size** \(_int_ _|__None_\)

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sambanova.html#SambaStudioEmbeddings.embed_query)\#     

Returns a list of embeddings for the given sentences. :param sentences: List of sentences to encode :type sentences: List\[str\]

Returns:     

List of embeddings for the given sentences

Return type:     

List\[np.ndarray\] or List\[tensor\]

Parameters:     

**text** \(_str_\)

Examples using SambaStudioEmbeddings

  * [SambaNova](https://python.langchain.com/docs/integrations/text_embedding/sambanova/)

__On this page