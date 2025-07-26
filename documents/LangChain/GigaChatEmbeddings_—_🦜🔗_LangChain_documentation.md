# GigaChatEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.gigachat.GigaChatEmbeddings.html
**Word Count:** 167
**Links Count:** 253
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# GigaChatEmbeddings\#

_class _langchain\_community.embeddings.gigachat.GigaChatEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gigachat.html#GigaChatEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.3.5: Use `:class:`~langchain_gigachat.GigaChatEmbeddings`` instead. It will not be removed until langchain-community==1.0.

GigaChat Embeddings models.

Example

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str | None_ _ = None_\#     

Access token for GigaChat

_param _auth\_url _: str | None_ _ = None_\#     

Auth URL

_param _base\_url _: str | None_ _ = None_\#     

Base API URL

_param _ca\_bundle\_file _: str | None_ _ = None_\#     

_param _cert\_file _: str | None_ _ = None_\#     

_param _credentials _: str | None_ _ = None_\#     

Auth Token

_param _key\_file _: str | None_ _ = None_\#     

_param _key\_file\_password _: str | None_ _ = None_\#     

_param _model _: str | None_ _ = None_\#     

Model name to use.

_param _password _: str | None_ _ = None_\#     

Password for authenticate

_param _scope _: str | None_ _ = None_\#     

Permission scope for access token

_param _timeout _: float | None_ _ = 600_\#     

Timeout for request. By default it works for long requests.

_param _user _: str | None_ _ = None_\#     

Username for authenticate

_param _verify\_ssl\_certs _: bool | None_ _ = None_\#     

Check certificates for all requests

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gigachat.html#GigaChatEmbeddings.validate_environment)\#     

Validate authenticate data in environment and python package is installed.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gigachat.html#GigaChatEmbeddings.aembed_documents)\#     

Embed documents using a GigaChat embeddings models.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gigachat.html#GigaChatEmbeddings.aembed_query)\#     

Embed a query using a GigaChat embeddings models.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gigachat.html#GigaChatEmbeddings.embed_documents)\#     

Embed documents using a GigaChat embeddings models.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/gigachat.html#GigaChatEmbeddings.embed_query)\#     

Embed a query using a GigaChat embeddings models.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using GigaChatEmbeddings

  * [GigaChat](https://python.langchain.com/docs/integrations/text_embedding/gigachat/)

  * [Salute Devices](https://python.langchain.com/docs/integrations/providers/salute_devices/)

__On this page