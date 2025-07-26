# BookendEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.bookend.BookendEmbeddings.html
**Word Count:** 150
**Links Count:** 229
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# BookendEmbeddings\#

_class _langchain\_community.embeddings.bookend.BookendEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bookend.html#BookendEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Bookend AI sentence\_transformers embedding models.

Example               from langchain_community.embeddings import BookendEmbeddings          bookend = BookendEmbeddings(         domain={domain}         api_token={api_token}         model_id={model_id}     )     bookend.embed_documents([         "Please put on these earmuffs because I can't you hear.",         "Baby wipes are made of chocolate stardust.",     ])     bookend.embed_query(         "She only paints with bold colors; she does not like pastels."     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_token _: str_ _\[Required\]_\#     

Request for an API token at <https://bookend.ai/> to use this embeddings module.

_param _auth\_header _: dict_ _\[Optional\]_\#     

_param _domain _: str_ _\[Required\]_\#     

Request for a domain at <https://bookend.ai/> to use this embeddings module.

_param _model\_id _: str_ _\[Required\]_\#     

Embeddings model ID to use.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bookend.html#BookendEmbeddings.embed_documents)\#     

Embed documents using a Bookend deployed embeddings model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bookend.html#BookendEmbeddings.embed_query)\#     

Embed a query using a Bookend deployed embeddings model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using BookendEmbeddings

  * [Bookend AI](https://python.langchain.com/docs/integrations/text_embedding/bookend/)

__On this page