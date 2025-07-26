# EdenAiEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.edenai.EdenAiEmbeddings.html
**Word Count:** 141
**Links Count:** 233
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# EdenAiEmbeddings\#

_class _langchain\_community.embeddings.edenai.EdenAiEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/edenai.html#EdenAiEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

EdenAI embedding. environment variable `EDENAI_API_KEY` set with your API key, or pass it as a named parameter.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _edenai\_api\_key _: SecretStr | None_ _ = None_\#     

EdenAI API Token

_param _model _: str | None_ _ = None_\#     

model name for above provider \(eg: ‘gpt-3.5-turbo-instruct’ for openai\) available models are shown on <https://docs.edenai.co/> under ‘available providers’

_param _provider _: str_ _ = 'openai'_\#     

embedding provider to use \(eg: openai,google etc.\)

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/edenai.html#EdenAiEmbeddings.validate_environment)\#     

Validate that api key exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_static _get\_user\_agent\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/edenai.html#EdenAiEmbeddings.get_user_agent)\#     

Return type:     

str

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/edenai.html#EdenAiEmbeddings.embed_documents)\#     

Embed a list of documents using EdenAI.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/edenai.html#EdenAiEmbeddings.embed_query)\#     

Embed a query using EdenAI.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using EdenAiEmbeddings

  * [EDEN AI](https://python.langchain.com/docs/integrations/text_embedding/edenai/)

  * [Eden AI](https://python.langchain.com/docs/integrations/providers/edenai/)

__On this page