# LLMRailsEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.llm_rails.LLMRailsEmbeddings.html
**Word Count:** 134
**Links Count:** 226
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# LLMRailsEmbeddings\#

_class _langchain\_community.embeddings.llm\_rails.LLMRailsEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llm_rails.html#LLMRailsEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

LLMRails embedding models.

To use, you should have the environment variable `LLM_RAILS_API_KEY` set with your API key or pass it as a named parameter to the constructor.

Model can be one of \[“embedding-english-v1”,”embedding-multi-v1”\]

Example               from langchain_community.embeddings import LLMRailsEmbeddings     cohere = LLMRailsEmbeddings(         model="embedding-english-v1", api_key="my-api-key"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: SecretStr | None_ _ = None_\#     

LLMRails API key.

_param _model _: str_ _ = 'embedding-english-v1'_\#     

Model name to use.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llm_rails.html#LLMRailsEmbeddings.validate_environment)\#     

Validate that api key exists in environment.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llm_rails.html#LLMRailsEmbeddings.embed_documents)\#     

Call out to Cohere’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llm_rails.html#LLMRailsEmbeddings.embed_query)\#     

Call out to Cohere’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using LLMRailsEmbeddings

  * [LLMRails](https://python.langchain.com/docs/integrations/text_embedding/llm_rails/)

__On this page