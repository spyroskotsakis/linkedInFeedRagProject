# VolcanoEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.volcengine.VolcanoEmbeddings.html
**Word Count:** 213
**Links Count:** 243
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# VolcanoEmbeddings\#

_class _langchain\_community.embeddings.volcengine.VolcanoEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/volcengine.html#VolcanoEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Volcengine Embeddings embedding models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _chunk\_size _: int_ _ = 100_\#     

Chunk size when multiple texts are input

_param _client _: Any_ _\[Required\]_\#     

volcano client

_param _host _: str_ _ = 'maas-api.ml-platform-cn-beijing.volces.com'_\#     

host learn more from <https://www.volcengine.com/docs/82379/1174746>

_param _model _: str_ _ = 'bge-large-zh'_\#     

Model name you could get from <https://www.volcengine.com/docs/82379/1174746> for now, we support bge\_large\_zh

_param _region _: str_ _ = 'cn-beijing'_\#     

region learn more from <https://www.volcengine.com/docs/82379/1174746>

_param _version _: str_ _ = '1.0'_\#     

model version

_param _volcano\_ak _: str | None_ _ = None_\#     

volcano access key learn more from: <https://www.volcengine.com/docs/6459/76491#ak-sk>

_param _volcano\_sk _: str | None_ _ = None_\#     

volcano secret key learn more from: <https://www.volcengine.com/docs/6459/76491#ak-sk>

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/volcengine.html#VolcanoEmbeddings.validate_environment)\#     

Validate whether volcano\_ak and volcano\_sk in the environment variables or configuration file are available or not.

init volcano embedding client with ak, sk, host, region

Parameters:     

  * **values** \(_Dict_\) – a dictionary containing configuration information, must include the

  * **volcano\_sk** \(_fields_ _of_ _volcano\_ak and_\)

Returns:     

a dictionary containing configuration information. If volcano\_ak and volcano\_sk are not provided in the environment variables or configuration file,the original values will be returned; otherwise, values containing volcano\_ak and volcano\_sk will be returned.

Raises:     

  * **ValueError** – volcengine package not found, please install it with

  * **pip install volcengine** – 

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/volcengine.html#VolcanoEmbeddings.embed_documents)\#     

Embeds a list of text documents using the AutoVOT algorithm.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – A list of text documents to embed.

Returns:     

A list of embeddings for each document in the input list.     

Each embedding is represented as a list of float values.

Return type:     

List\[List\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/volcengine.html#VolcanoEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using VolcanoEmbeddings

  * [Volc Engine](https://python.langchain.com/docs/integrations/text_embedding/volcengine/)

__On this page