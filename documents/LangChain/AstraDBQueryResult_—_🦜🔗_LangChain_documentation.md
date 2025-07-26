# AstraDBQueryResult — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html
**Word Count:** 147
**Links Count:** 98
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBQueryResult\#

_class _langchain\_astradb.vectorstores.AstraDBQueryResult\(

    _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_,     _id : str_,     _embedding : list\[float\] | None_,     _similarity : float | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBQueryResult)\#     

The complete information contained in a vector store entry.

This class represents all that can be returned from the collection when running a query, which goes beyond just the corresponding Document.

Parameters:     

  * **document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\)

  * **id** \(_str_\)

  * **embedding** \(_list_ _\[__float_ _\]__|__None_\)

  * **similarity** \(_float_ _|__None_\)

document\#     

a `langchain.schema.Document` object representing the query result.

Type:     

[langchain\_core.documents.base.Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

id\#     

the ID of the returned document.

Type:     

str

embedding\#     

the embedding vector associated to the document. This may be None, depending on whether the embeddings were requested in the query or not.

Type:     

list\[float\] | None

similarity\#     

the numeric similarity score of the document in the query. In case this quantity was not requested by the query, it will be set to None.

Type:     

float | None

Create new instance of AstraDBQueryResult\(document, id, embedding, similarity\)

Attributes

`document` | Alias for field number 0   ---|---   `embedding` | Alias for field number 2   `id` | Alias for field number 1   `similarity` | Alias for field number 3      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)