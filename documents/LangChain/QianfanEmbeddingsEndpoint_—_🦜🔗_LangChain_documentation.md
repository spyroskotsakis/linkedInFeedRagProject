# QianfanEmbeddingsEndpoint — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.baidu_qianfan_endpoint.QianfanEmbeddingsEndpoint.html
**Word Count:** 280
**Links Count:** 245
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# QianfanEmbeddingsEndpoint\#

_class _langchain\_community.embeddings.baidu\_qianfan\_endpoint.QianfanEmbeddingsEndpoint[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baidu_qianfan_endpoint.html#QianfanEmbeddingsEndpoint)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Baidu Qianfan Embeddings embedding models.

Setup:     

To use, you should have the `qianfan` python package installed, and set environment variables `QIANFAN_AK`, `QIANFAN_SK`.               pip install qianfan     export QIANFAN_AK="your-api-key"     export QIANFAN_SK="your-secret_key"     

Instantiate:     

>  >     from langchain_community.embeddings import QianfanEmbeddingsEndpoint >      >     embeddings = QianfanEmbeddingsEndpoint() >     

Embed:                    # embed the documents     vectors = embeddings.embed_documents([text1, text2, ...])          # embed the query     vectors = embeddings.embed_query(text)          # embed the documents with async     vectors = await embeddings.aembed_documents([text1, text2, ...])          # embed the query with async     vectors = await embeddings.aembed_query(text)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _chunk\_size _: int_ _ = 16_\#     

Chunk size when multiple texts are input

_param _client _: Any_ _ = None_\#     

Qianfan client

_param _endpoint _: str_ _ = ''_\#     

Endpoint of the Qianfan Embedding, required if custom model used.

_param _init\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

init kwargs for qianfan client init, such as query\_per\_second which is associated with qianfan resource object to limit QPS

_param _model _: str | None_ _ = None_\#     

Model name you could get from <https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu>

for now, we support Embedding-V1 and \- Embedding-V1 （默认模型） \- bge-large-en \- bge-large-zh

preset models are mapping to an endpoint. model will be ignored if endpoint is set

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

extra params for model invoke using with do.

_param _qianfan\_ak _: SecretStr | None_ _ = None_ _\(alias 'api\_key'\)_\#     

Qianfan application apikey

_param _qianfan\_sk _: SecretStr | None_ _ = None_ _\(alias 'secret\_key'\)_\#     

Qianfan application secretkey

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baidu_qianfan_endpoint.html#QianfanEmbeddingsEndpoint.validate_environment)\#     

Validate whether qianfan\_ak and qianfan\_sk in the environment variables or configuration file are available or not.

init qianfan embedding client with ak, sk, model, endpoint

Parameters:     

  * **values** \(_Dict_\) – a dictionary containing configuration information, must include the

  * **qianfan\_sk** \(_fields_ _of_ _qianfan\_ak and_\)

Returns:     

a dictionary containing configuration information. If qianfan\_ak and qianfan\_sk are not provided in the environment variables or configuration file,the original values will be returned; otherwise, values containing qianfan\_ak and qianfan\_sk will be returned.

Raises:     

  * **ValueError** – qianfan package not found, please install it with \`pip install

  * **qianfan\`** – 

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baidu_qianfan_endpoint.html#QianfanEmbeddingsEndpoint.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baidu_qianfan_endpoint.html#QianfanEmbeddingsEndpoint.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baidu_qianfan_endpoint.html#QianfanEmbeddingsEndpoint.embed_documents)\#     

Embeds a list of text documents using the AutoVOT algorithm.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – A list of text documents to embed.

Returns:     

A list of embeddings for each document in the input list.     

Each embedding is represented as a list of float values.

Return type:     

List\[List\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baidu_qianfan_endpoint.html#QianfanEmbeddingsEndpoint.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using QianfanEmbeddingsEndpoint

  * [Baidu](https://python.langchain.com/docs/integrations/providers/baidu/)

  * [Baidu Cloud ElasticSearch VectorSearch](https://python.langchain.com/docs/integrations/vectorstores/baiducloud_vector_search/)

  * [Baidu Qianfan](https://python.langchain.com/docs/integrations/text_embedding/baidu_qianfan_endpoint/)

  * [ERNIE](https://python.langchain.com/docs/integrations/text_embedding/ernie/)

__On this page