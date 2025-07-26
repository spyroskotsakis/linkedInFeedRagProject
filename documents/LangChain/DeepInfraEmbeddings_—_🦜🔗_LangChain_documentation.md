# DeepInfraEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.deepinfra.DeepInfraEmbeddings.html
**Word Count:** 224
**Links Count:** 237
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# DeepInfraEmbeddings\#

_class _langchain\_community.embeddings.deepinfra.DeepInfraEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/deepinfra.html#DeepInfraEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deep Infra’s embedding inference service.

To use, you should have the environment variable `DEEPINFRA_API_TOKEN` set with your API token, or pass it as a named parameter to the constructor. There are multiple embeddings models available, see <https://deepinfra.com/models?type=embeddings>.

Example               from langchain_community.embeddings import DeepInfraEmbeddings     deepinfra_emb = DeepInfraEmbeddings(         model_id="sentence-transformers/clip-ViT-B-32",         deepinfra_api_token="my-api-key"     )     r1 = deepinfra_emb.embed_documents(         [             "Alpha is the first letter of Greek alphabet",             "Beta is the second letter of Greek alphabet",         ]     )     r2 = deepinfra_emb.embed_query(         "What is the second letter of Greek alphabet"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _batch\_size _: int_ _ = 1024_\#     

Batch size for embedding requests.

_param _deepinfra\_api\_token _: str | None_ _ = None_\#     

API token for Deep Infra. If not provided, the token is fetched from the environment variable ‘DEEPINFRA\_API\_TOKEN’.

_param _embed\_instruction _: str_ _ = 'passage: '_\#     

Instruction used to embed documents.

_param _model\_id _: str_ _ = 'sentence-transformers/clip-ViT-B-32'_\#     

Embeddings model to use.

_param _model\_kwargs _: dict | None_ _ = None_\#     

Other model keyword args

_param _normalize _: bool_ _ = False_\#     

whether to normalize the computed embeddings

_param _query\_instruction _: str_ _ = 'query: '_\#     

Instruction used to embed the query.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/deepinfra.html#DeepInfraEmbeddings.validate_environment)\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/deepinfra.html#DeepInfraEmbeddings.embed_documents)\#     

Embed documents using a Deep Infra deployed embedding model. For larger batches, the input list of texts is chunked into smaller batches to avoid exceeding the maximum request size.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/deepinfra.html#DeepInfraEmbeddings.embed_query)\#     

Embed a query using a Deep Infra deployed embedding model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using DeepInfraEmbeddings

  * [DeepInfra](https://python.langchain.com/docs/integrations/providers/deepinfra/)

__On this page