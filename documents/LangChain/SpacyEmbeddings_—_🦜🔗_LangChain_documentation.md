# SpacyEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.spacy_embeddings.SpacyEmbeddings.html
**Word Count:** 178
**Links Count:** 231
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# SpacyEmbeddings\#

_class _langchain\_community.embeddings.spacy\_embeddings.SpacyEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/spacy_embeddings.html#SpacyEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Embeddings by spaCy models.

model\_name\#     

Name of a spaCy model.

Type:     

str

nlp\#     

The spaCy model loaded into memory.

Type:     

Any

embed\_documents\(texts     

List\[str\]\) -> List\[List\[float\]\]: Generates embeddings for a list of documents.

embed\_query\(text     

str\) -> List\[float\]: Generates an embedding for a single piece of text.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _model\_name _: str_ _ = 'en\_core\_web\_sm'_\#     

_param _nlp _: Any | None_ _ = None_\#     

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/spacy_embeddings.html#SpacyEmbeddings.aembed_documents)\#     

Asynchronously generates embeddings for a list of documents. This method is not implemented and raises a NotImplementedError.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The documents to generate embeddings for.

Raises:     

**NotImplementedError** – This method is not implemented.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/spacy_embeddings.html#SpacyEmbeddings.aembed_query)\#     

Asynchronously generates an embedding for a single piece of text. This method is not implemented and raises a NotImplementedError.

Parameters:     

**text** \(_str_\) – The text to generate an embedding for.

Raises:     

**NotImplementedError** – This method is not implemented.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/spacy_embeddings.html#SpacyEmbeddings.embed_documents)\#     

Generates embeddings for a list of documents.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The documents to generate embeddings for.

Returns:     

A list of embeddings, one for each document.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/spacy_embeddings.html#SpacyEmbeddings.embed_query)\#     

Generates an embedding for a single piece of text.

Parameters:     

**text** \(_str_\) – The text to generate an embedding for.

Returns:     

The embedding for the text.

Return type:     

_List_\[float\]

Examples using SpacyEmbeddings

  * [NanoPQ \(Product Quantization\)](https://python.langchain.com/docs/integrations/retrievers/nanopq/)

  * [SpaCy](https://python.langchain.com/docs/integrations/text_embedding/spacy_embedding/)

  * [spaCy](https://python.langchain.com/docs/integrations/providers/spacy/)

__On this page