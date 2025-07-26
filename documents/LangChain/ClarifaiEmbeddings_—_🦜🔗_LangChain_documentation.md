# ClarifaiEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.clarifai.ClarifaiEmbeddings.html
**Word Count:** 149
**Links Count:** 235
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# ClarifaiEmbeddings\#

_class _langchain\_community.embeddings.clarifai.ClarifaiEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/clarifai.html#ClarifaiEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Clarifai embedding models.

To use, you should have the `clarifai` python package installed, and the environment variable `CLARIFAI_PAT` set with your personal access token or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import ClarifaiEmbeddings     clarifai = ClarifaiEmbeddings(user_id=USER_ID,                                   app_id=APP_ID,                                   model_id=MODEL_ID)                      (or)     Example_URL = "https://clarifai.com/clarifai/main/models/BAAI-bge-base-en-v15"     clarifai = ClarifaiEmbeddings(model_url=EXAMPLE_URL)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_base _: str_ _ = 'https://api.clarifai.com'_\#     

_param _app\_id _: str | None_ _ = None_\#     

Clarifai application id to use.

_param _model\_id _: str | None_ _ = None_\#     

Model id to use.

_param _model\_url _: str | None_ _ = None_\#     

Model url to use.

_param _model\_version\_id _: str | None_ _ = None_\#     

Model version id to use.

_param _pat _: str | None_ _ = None_\#     

Clarifai personal access token to use.

_param _token _: str | None_ _ = None_\#     

Clarifai session token to use.

_param _user\_id _: str | None_ _ = None_\#     

Clarifai user id to use.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/clarifai.html#ClarifaiEmbeddings.embed_documents)\#     

Call out to Clarifai’s embedding models.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/clarifai.html#ClarifaiEmbeddings.embed_query)\#     

Call out to Clarifai’s embedding models.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using ClarifaiEmbeddings

  * [Clarifai](https://python.langchain.com/docs/integrations/providers/clarifai/)

__On this page