# SparkLLMTextEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.sparkllm.SparkLLMTextEmbeddings.html
**Word Count:** 260
**Links Count:** 230
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# SparkLLMTextEmbeddings\#

_class _langchain\_community.embeddings.sparkllm.SparkLLMTextEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sparkllm.html#SparkLLMTextEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

SparkLLM embedding model integration.

Setup:     

To use, you should have the environment variable “SPARK\_APP\_ID”,”SPARK\_API\_KEY” and “SPARK\_API\_SECRET” set your APP\_ID, API\_KEY and API\_SECRET or pass it as a name parameter to the constructor.               export SPARK_APP_ID="your-api-id"     export SPARK_API_KEY="your-api-key"     export SPARK_API_SECRET="your-api-secret"     

Key init args — completion params:     

api\_key: Optional\[str\]     

Automatically inferred from env var SPARK\_API\_KEY if not provided.

app\_id: Optional\[str\]     

Automatically inferred from env var SPARK\_APP\_ID if not provided.

api\_secret: Optional\[str\]     

Automatically inferred from env var SPARK\_API\_SECRET if not provided.

base\_url: Optional\[str\]     

Base URL path for API requests.

See full list of supported init args and their descriptions in the params section.

Instantiate:

>  >     from langchain_community.embeddings import SparkLLMTextEmbeddings >      >     embed = SparkLLMTextEmbeddings( >         api_key="...", >         app_id="...", >         api_secret="...", >         # other >     ) >     

Embed single text:                    input_text = "The meaning of life is 42"     embed.embed_query(input_text)                    [-0.4912109375, 0.60595703125, 0.658203125, 0.3037109375, 0.6591796875, 0.60302734375, ...]     

Embed multiple text:                    input_texts = ["This is a test query1.", "This is a test query2."]     embed.embed_documents(input_texts)                    [         [-0.1962890625, 0.94677734375, 0.7998046875, -0.1971435546875, 0.445556640625, 0.54638671875, ...],         [  -0.44970703125, 0.06585693359375, 0.7421875, -0.474609375, 0.62353515625, 1.0478515625, ...],     ]     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _base\_url _: str_ _ = 'https://emb-cn-huabei-1.xf-yun.com/'_\#     

Base URL path for API requests

_param _domain _: Literal\['para', 'query'\]__ = 'para'_\#     

This parameter is used for which Embedding this time belongs to. If “para”\(default\), it belongs to document Embedding. If “query”, it belongs to query Embedding.

_param _spark\_api\_key _: SecretStr | None_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically inferred from env var SPARK\_API\_KEY if not provided.

_param _spark\_api\_secret _: SecretStr | None_ _\[Optional\]__\(alias 'api\_secret'\)_\#     

Automatically inferred from env var SPARK\_API\_SECRET if not provided.

_param _spark\_app\_id _: SecretStr_ _\[Optional\]__\(alias 'app\_id'\)_\#     

Automatically inferred from env var SPARK\_APP\_ID if not provided.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sparkllm.html#SparkLLMTextEmbeddings.embed_documents)\#     

Public method to get embeddings for a list of documents.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

A list of embeddings, one for each text, or None if an error occurs.

Return type:     

_List_\[_List_\[float\]\] | None

embed\_query\(

    _text : str_, \) → List\[float\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sparkllm.html#SparkLLMTextEmbeddings.embed_query)\#     

Public method to get embedding for a single query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text, or None if an error occurs.

Return type:     

_List_\[float\] | None

Examples using SparkLLMTextEmbeddings

  * [SparkLLM Text Embeddings](https://python.langchain.com/docs/integrations/text_embedding/sparkllm/)

  * [iFlytek](https://python.langchain.com/docs/integrations/providers/iflytek/)

__On this page