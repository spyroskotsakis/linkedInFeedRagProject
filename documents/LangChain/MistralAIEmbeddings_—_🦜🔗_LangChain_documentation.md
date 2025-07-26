# MistralAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/mistralai/embeddings/langchain_mistralai.embeddings.MistralAIEmbeddings.html
**Word Count:** 233
**Links Count:** 106
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# MistralAIEmbeddings\#

_class _langchain\_mistralai.embeddings.MistralAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_mistralai/embeddings.html#MistralAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

MistralAI embedding model integration.

Setup:     

Install `langchain_mistralai` and set environment variable `MISTRAL_API_KEY`.               pip install -U langchain_mistralai     export MISTRAL_API_KEY="your-api-key"     

Key init args — completion params:     

model: str     

Name of MistralAI model to use.

Key init args — client params:     

api\_key: Optional\[SecretStr\]     

The API key for the MistralAI API. If not provided, it will be read from the environment variable `MISTRAL_API_KEY`.

max\_retries: int     

The number of times to retry a request if it fails.

timeout: int     

The number of seconds to wait for a response before timing out.

wait\_time: int     

The number of seconds to wait before retrying a request in case of 429 error.

max\_concurrent\_requests: int     

The maximum number of concurrent requests to make to the Mistral API.

See full list of supported init args and their descriptions in the params section.

Instantiate:

>  >     from __module_name__ import MistralAIEmbeddings >      >     embed = MistralAIEmbeddings( >         model="mistral-embed", >         # api_key="...", >         # other params... >     ) >     

Embed single text:

>  >     input_text = "The meaning of life is 42" >     vector = embed.embed_query(input_text) >     print(vector[:3]) >      >      >      >     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915] >     

Embed multiple text:

>  >     input_texts = ["Document 1...", "Document 2..."] >     vectors = embed.embed_documents(input_texts) >     print(len(vectors)) >     # The first 3 coordinates for the first vector >     print(vectors[0][:3]) >      >      >      >     2 >     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915] >     

Async:

>  >     vector = await embed.aembed_query(input_text) >     print(vector[:3]) >      >     # multiple: >     # await embed.aembed_documents(input_texts) >      >      >      >     [-0.009100092574954033, 0.005071679595857859, -0.0029193938244134188] >     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _async\_client _: AsyncClient_ _ = None_\#     

_param _client _: Client_ _ = None_\#     

_param _endpoint _: str_ _ = 'https://api.mistral.ai/v1/'_\#     

_param _max\_concurrent\_requests _: int_ _ = 64_\#     

_param _max\_retries _: int_ _ = 5_\#     

_param _mistral\_api\_key _: SecretStr_ _\[Optional\]__\(alias 'api\_key'\)_\#     

_param _model _: str_ _ = 'mistral-embed'_\#     

_param _timeout _: int_ _ = 120_\#     

_param _tokenizer _: Tokenizer_ _ = None_\#     

_param _wait\_time _: int_ _ = 30_\#     

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_mistralai/embeddings.html#MistralAIEmbeddings.aembed_documents)\#     

Embed a list of document texts.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_mistralai/embeddings.html#MistralAIEmbeddings.aembed_query)\#     

Embed a single query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_mistralai/embeddings.html#MistralAIEmbeddings.embed_documents)\#     

Embed a list of document texts.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_mistralai/embeddings.html#MistralAIEmbeddings.embed_query)\#     

Embed a single query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

list\[float\]

Examples using MistralAIEmbeddings

  * [MistralAI](https://python.langchain.com/docs/integrations/providers/mistralai/)

  * [MistralAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/mistralai/)

__On this page