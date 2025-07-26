# RetrieveResultItem — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.RetrieveResultItem.html
**Word Count:** 104
**Links Count:** 205
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# RetrieveResultItem\#

_class _langchain\_community.retrievers.kendra.RetrieveResultItem[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#RetrieveResultItem)\#     

Bases: [`ResultItem`](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.ResultItem.html#langchain_community.retrievers.kendra.ResultItem "langchain_community.retrievers.kendra.ResultItem")

Retrieve API result item.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _Content _: str | None_ _\[Required\]_\#     

The content of the item.

_param _DocumentAttributes _: List\[[DocumentAttribute](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttribute.html#langchain_community.retrievers.kendra.DocumentAttribute "langchain_community.retrievers.kendra.DocumentAttribute")\] | None_ _ = \[\]_\#     

The document attributes.

_param _DocumentId _: str | None_ _\[Required\]_\#     

The document ID.

_param _DocumentTitle _: str | None_ _\[Required\]_\#     

The document title.

_param _DocumentURI _: str | None_ _\[Required\]_\#     

The document URI.

_param _Id _: str | None_ _\[Required\]_\#     

The ID of the relevant result item.

_param _ScoreAttributes _: dict | None_ _\[Required\]_\#     

The kendra score confidence

get\_additional\_metadata\(\) → dict\#     

Document additional metadata dict. This returns any extra metadata except these:

>   * result\_id >  >   * document\_id >  >   * source >  >   * title >  >   * excerpt >  >   * document\_attributes >  > 

Return type:     

dict

get\_document\_attributes\_dict\(\) → Dict\[str, str | int | List\[str\] | None\]\#     

Document attributes dict.

Return type:     

_Dict_\[str, str | int | _List_\[str\] | None\]

get\_excerpt\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#RetrieveResultItem.get_excerpt)\#     

Document excerpt or passage original content as retrieved by Kendra.

Return type:     

str

get\_score\_attribute\(\) → str\#     

Document Score Confidence

Return type:     

str

get\_title\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#RetrieveResultItem.get_title)\#     

Document title.

Return type:     

str

to\_doc\(_page\_content\_formatter: ~typing.Callable\[\[~langchain\_community.retrievers.kendra.ResultItem\], str\] = <function combined\_text>_\) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\#     

Converts this item to a Document.

Parameters:     

**page\_content\_formatter** \(_Callable_ _\[__\[_[_ResultItem_](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.ResultItem.html#langchain_community.retrievers.kendra.ResultItem "langchain_community.retrievers.kendra.ResultItem") _\]__,__str_ _\]_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

__On this page