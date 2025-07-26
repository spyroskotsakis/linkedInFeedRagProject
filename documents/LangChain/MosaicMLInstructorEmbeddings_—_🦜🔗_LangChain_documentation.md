# MosaicMLInstructorEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.mosaicml.MosaicMLInstructorEmbeddings.html
**Word Count:** 147
**Links Count:** 229
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# MosaicMLInstructorEmbeddings\#

_class _langchain\_community.embeddings.mosaicml.MosaicMLInstructorEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mosaicml.html#MosaicMLInstructorEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

MosaicML embedding service.

To use, you should have the environment variable `MOSAICML_API_TOKEN` set with your API token, or pass it as a named parameter to the constructor.

Example               from langchain_community.llms import MosaicMLInstructorEmbeddings     endpoint_url = (         "https://models.hosted-on.mosaicml.hosting/instructor-large/v1/predict"     )     mosaic_llm = MosaicMLInstructorEmbeddings(         endpoint_url=endpoint_url,         mosaicml_api_token="my-api-key"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _embed\_instruction _: str_ _ = 'Represent the document for retrieval: '_\#     

Instruction used to embed documents.

_param _endpoint\_url _: str_ _ = 'https://models.hosted-on.mosaicml.hosting/instructor-xl/v1/predict'_\#     

Endpoint URL to use.

_param _mosaicml\_api\_token _: str | None_ _ = None_\#     

_param _query\_instruction _: str_ _ = 'Represent the question for retrieving supporting documents: '_\#     

Instruction used to embed the query.

_param _retry\_sleep _: float_ _ = 1.0_\#     

How long to try sleeping for if a rate limit is encountered

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mosaicml.html#MosaicMLInstructorEmbeddings.embed_documents)\#     

Embed documents using a MosaicML deployed instructor embedding model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/mosaicml.html#MosaicMLInstructorEmbeddings.embed_query)\#     

Embed a query using a MosaicML deployed instructor embedding model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using MosaicMLInstructorEmbeddings

  * [MosaicML](https://python.langchain.com/docs/integrations/text_embedding/mosaicml/)

__On this page