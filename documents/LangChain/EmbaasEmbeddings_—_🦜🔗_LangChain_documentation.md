# EmbaasEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.embaas.EmbaasEmbeddings.html
**Word Count:** 170
**Links Count:** 234
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# EmbaasEmbeddings\#

_class _langchain\_community.embeddings.embaas.EmbaasEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/embaas.html#EmbaasEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Embaas’s embedding service.

To use, you should have the environment variable `EMBAAS_API_KEY` set with your API key, or pass it as a named parameter to the constructor.

Example               # initialize with default model and instruction     from langchain_community.embeddings import EmbaasEmbeddings     emb = EmbaasEmbeddings()          # initialize with custom model and instruction     from langchain_community.embeddings import EmbaasEmbeddings     emb_model = "instructor-large"     emb_inst = "Represent the Wikipedia document for retrieval"     emb = EmbaasEmbeddings(         model=emb_model,         instruction=emb_inst     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_url _: str_ _ = 'https://api.embaas.io/v1/embeddings/'_\#     

The URL for the embaas embeddings API.

_param _embaas\_api\_key _: SecretStr | None_ _ = None_\#     

max number of retries for requests

_param _instruction _: str | None_ _ = None_\#     

Instruction used for domain-specific embeddings.

_param _max\_retries _: int | None_ _ = 3_\#     

request timeout in seconds

_param _model _: str_ _ = 'e5-large-v2'_\#     

The model used for embeddings.

_param _timeout _: int | None_ _ = 30_\#     

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/embaas.html#EmbaasEmbeddings.validate_environment)\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/embaas.html#EmbaasEmbeddings.embed_documents)\#     

Get embeddings for a list of texts.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to get embeddings for.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/embaas.html#EmbaasEmbeddings.embed_query)\#     

Get embeddings for a single text.

Parameters:     

**text** \(_str_\) – The text to get embeddings for.

Returns:     

List of embeddings.

Return type:     

_List_\[float\]

Examples using EmbaasEmbeddings

  * [Embaas](https://python.langchain.com/docs/integrations/text_embedding/embaas/)

__On this page