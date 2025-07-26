# PremAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.PremAIEmbeddings.html
**Word Count:** 132
**Links Count:** 236
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# PremAIEmbeddings\#

_class _langchain\_community.embeddings.premai.PremAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/premai.html#PremAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Prem’s Embedding APIs

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _\[Required\]_\#     

_param _max\_retries _: int_ _ = 1_\#     

Max number of retries for tenacity

_param _model _: str_ _\[Required\]_\#     

The Embedding model to choose from

_param _premai\_api\_key _: SecretStr | None_ _ = None_\#     

Prem AI API Key. Get it here: <https://app.premai.io/api_keys/>

_param _project\_id _: int_ _\[Required\]_\#     

The project ID in which the experiments or deployments are carried out. You can find all your projects here: <https://app.premai.io/projects/>

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a tqdm progress bar. Must have tqdm installed.

_classmethod _validate\_environments\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/premai.html#PremAIEmbeddings.validate_environments)\#     

Validate that the package is installed and that the API token is valid

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/premai.html#PremAIEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/premai.html#PremAIEmbeddings.embed_query)\#     

Embed query text

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using PremAIEmbeddings

  * [PremAI](https://python.langchain.com/docs/integrations/text_embedding/premai/)

__On this page