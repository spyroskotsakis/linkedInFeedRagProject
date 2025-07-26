# YandexGPTEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.yandex.YandexGPTEmbeddings.html
**Word Count:** 232
**Links Count:** 248
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# YandexGPTEmbeddings\#

_class _langchain\_community.embeddings.yandex.YandexGPTEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/yandex.html#YandexGPTEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

YandexGPT Embeddings models.

To use, you should have the `yandexcloud` python package installed.

There are two authentication options for the service account with the `ai.languageModels.user` role:

>   * You can specify the token in a constructor parameter iam\_token >  > 

>  > or in an environment variable YC\_IAM\_TOKEN. \- You can specify the key in a constructor parameter api\_key or in an environment variable YC\_API\_KEY.

To use the default model specify the folder ID in a parameter folder\_id or in an environment variable YC\_FOLDER\_ID.

Example               from langchain_community.embeddings.yandex import YandexGPTEmbeddings     embeddings = YandexGPTEmbeddings(iam_token="t1.9eu...", folder_id=<folder-id>)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: SecretStr_ _ = ''_\#     

Yandex Cloud Api Key for service account with the ai.languageModels.user role

_param _disable\_request\_logging _: bool_ _ = False_\#     

YandexGPT API logs all request data by default. If you provide personal data, confidential information, disable logging.

_param _doc\_model\_name _: str_ _ = 'text-search-doc'_\#     

Doc model name to use.

_param _doc\_model\_uri _: str_ _ = ''_\#     

Doc model uri to use.

_param _folder\_id _: str_ _ = ''_\#     

Yandex Cloud folder ID

_param _grpc\_metadata _: Sequence_ _\[Required\]_\#     

_param _iam\_token _: SecretStr_ _ = ''_\#     

Yandex Cloud IAM token for service account with the ai.languageModels.user role

_param _max\_retries _: int_ _ = 6_\#     

Maximum number of retries to make when generating.

_param _model\_name _: str_ _ = 'text-search-query'__\(alias 'query\_model\_name'\)_\#     

Query model name to use.

_param _model\_uri _: str_ _ = ''__\(alias 'query\_model\_uri'\)_\#     

Query model uri to use.

_param _model\_version _: str_ _ = 'latest'_\#     

Model version to use.

_param _sleep\_interval _: float_ _ = 0.0_\#     

Delay between API requests

_param _url _: str_ _ = 'llm.api.cloud.yandex.net:443'_\#     

The url of the API.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/yandex.html#YandexGPTEmbeddings.validate_environment)\#     

Validate that iam token exists in environment.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/yandex.html#YandexGPTEmbeddings.embed_documents)\#     

Embed documents using a YandexGPT embeddings models.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/yandex.html#YandexGPTEmbeddings.embed_query)\#     

Embed a query using a YandexGPT embeddings models.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using YandexGPTEmbeddings

  * [YandexGPT](https://python.langchain.com/docs/integrations/text_embedding/yandex/)

__On this page