# MiniMaxEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.minimax.MiniMaxEmbeddings.html
**Word Count:** 197
**Links Count:** 238
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# MiniMaxEmbeddings\#

_class _langchain\_community.embeddings.minimax.MiniMaxEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/minimax.html#MiniMaxEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

MiniMax embedding model integration.

Setup:     

To use, you should have the environment variable `MINIMAX_GROUP_ID` and `MINIMAX_API_KEY` set with your API token.               export MINIMAX_API_KEY="your-api-key"     export MINIMAX_GROUP_ID="your-group-id"     

Key init args — completion params:     

model: Optional\[str\]     

Name of ZhipuAI model to use.

api\_key: Optional\[str\]     

Automatically inferred from env var MINIMAX\_GROUP\_ID if not provided.

group\_id: Optional\[str\]     

Automatically inferred from env var MINIMAX\_GROUP\_ID if not provided.

See full list of supported init args and their descriptions in the params section.

Instantiate:

>  >     from langchain_community.embeddings import MiniMaxEmbeddings >      >     embed = MiniMaxEmbeddings( >         model="embo-01", >         # api_key="...", >         # group_id="...", >         # other >     ) >     

Embed single text:                    input_text = "The meaning of life is 42"     embed.embed_query(input_text)                    [0.03016241, 0.03617699, 0.0017198119, -0.002061239, -0.00029994643, -0.0061320597, -0.0043635326, ...]     

Embed multiple text:                    input_texts = ["This is a test query1.", "This is a test query2."]     embed.embed_documents(input_texts)                    [         [-0.0021588828, -0.007608119, 0.029349545, -0.0038194496, 0.008031177, -0.004529633, -0.020150753, ...],         [ -0.00023150232, -0.011122423, 0.016930554, 0.0083089275, 0.012633711, 0.019683322, -0.005971041, ...]     ]     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _embed\_type\_db _: str_ _ = 'db'_\#     

For embed\_documents

_param _embed\_type\_query _: str_ _ = 'query'_\#     

For embed\_query

_param _endpoint\_url _: str_ _ = 'https://api.minimax.chat/v1/embeddings'_\#     

Endpoint URL to use.

_param _minimax\_api\_key _: SecretStr | None_ _ = None_ _\(alias 'api\_key'\)_\#     

API Key for MiniMax API.

_param _minimax\_group\_id _: str | None_ _ = None_ _\(alias 'group\_id'\)_\#     

Group ID for MiniMax API.

_param _model _: str_ _ = 'embo-01'_\#     

Embeddings model name to use.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/minimax.html#MiniMaxEmbeddings.validate_environment)\#     

Validate that group id and api key exists in environment.

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

    _texts : List\[str\]_,     _embed\_type : str_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/minimax.html#MiniMaxEmbeddings.embed)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embed\_type** \(_str_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/minimax.html#MiniMaxEmbeddings.embed_documents)\#     

Embed documents using a MiniMax embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/minimax.html#MiniMaxEmbeddings.embed_query)\#     

Embed a query using a MiniMax embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using MiniMaxEmbeddings

  * [MiniMax](https://python.langchain.com/docs/integrations/text_embedding/minimax/)

  * [Minimax](https://python.langchain.com/docs/integrations/providers/minimax/)

__On this page