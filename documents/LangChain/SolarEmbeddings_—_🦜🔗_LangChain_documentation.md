# SolarEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.solar.SolarEmbeddings.html
**Word Count:** 157
**Links Count:** 231
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# SolarEmbeddings\#

_class _langchain\_community.embeddings.solar.SolarEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/solar.html#SolarEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.0.34: Use `:class:`~langchain_upstage.ChatUpstage`` instead. It will not be removed until langchain-community==1.0.

Solar’s embedding service.

To use, you should have the environment variable\`\`SOLAR\_API\_KEY\`\` set with your API token, or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import SolarEmbeddings     embeddings = SolarEmbeddings()          query_text = "This is a test query."     query_result = embeddings.embed_query(query_text)          document_text = "This is a test document."     document_result = embeddings.embed_documents([document_text])     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _endpoint\_url _: str_ _ = 'https://api.upstage.ai/v1/solar/embeddings'_\#     

Endpoint URL to use.

_param _model _: str_ _ = 'embedding-query'_\#     

Embeddings model name to use.

_param _solar\_api\_key _: SecretStr | None_ _ = None_\#     

API Key for Solar API.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/solar.html#SolarEmbeddings.validate_environment)\#     

Validate api key exists in environment.

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

embed\(

    _text : str_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/solar.html#SolarEmbeddings.embed)\#     

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/solar.html#SolarEmbeddings.embed_documents)\#     

Embed documents using a Solar embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/solar.html#SolarEmbeddings.embed_query)\#     

Embed a query using a Solar embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using SolarEmbeddings

  * [Solar](https://python.langchain.com/docs/integrations/text_embedding/solar/)

__On this page