# FireworksEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/fireworks/embeddings/langchain_fireworks.embeddings.FireworksEmbeddings.html
**Word Count:** 136
**Links Count:** 89
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# FireworksEmbeddings\#

_class _langchain\_fireworks.embeddings.FireworksEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_fireworks/embeddings.html#FireworksEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Fireworks embedding model integration.

Setup:

> Install `langchain_fireworks` and set environment variable `FIREWORKS_API_KEY`. >      >      >     pip install -U langchain_fireworks >     export FIREWORKS_API_KEY="your-api-key" >     

Key init args — completion params:     

model: str     

Name of Fireworks model to use.

Key init args — client params:     

fireworks\_api\_key: SecretStr     

Fireworks API key.

See full list of supported init args and their descriptions in the params section.

Instantiate:

>  >     from langchain_fireworks import FireworksEmbeddings >      >     model = FireworksEmbeddings( >         model='nomic-ai/nomic-embed-text-v1.5' >         # Use FIREWORKS_API_KEY env var or pass it in directly >         # fireworks_api_key="..." >     ) >     

Embed multiple texts:

>  >     vectors = embeddings.embed_documents(['hello', 'goodbye']) >     # Showing only the first 3 coordinates >     print(len(vectors)) >     print(vectors[0][:3]) >      >      >      >     2 >     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915] >     

Embed single text:

>  >     input_text = "The meaning of life is 42" >     vector = embeddings.embed_query('hello') >     print(vector[:3]) >      >      >      >     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915] >     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: [OpenAI](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.OpenAI.html#langchain_community.llms.openai.OpenAI "langchain_community.llms.openai.OpenAI")_ _ = None_\#     

_param _fireworks\_api\_key _: SecretStr_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Fireworks API key.

Automatically read from env variable `FIREWORKS_API_KEY` if not provided.

_param _model _: str_ _ = 'nomic-ai/nomic-embed-text-v1.5'_\#     

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

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_fireworks/embeddings.html#FireworksEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_fireworks/embeddings.html#FireworksEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

list\[float\]

__On this page