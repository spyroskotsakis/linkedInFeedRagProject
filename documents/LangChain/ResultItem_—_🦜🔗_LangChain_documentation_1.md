# ResultItem — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.ResultItem.html
**Word Count:** 100
**Links Count:** 204
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# ResultItem\#

_class _langchain\_community.retrievers.kendra.ResultItem[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem)\#     

Bases: `BaseModel`, `ABC`

Base class of a result item.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _DocumentAttributes _: List\[[DocumentAttribute](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttribute.html#langchain_community.retrievers.kendra.DocumentAttribute "langchain_community.retrievers.kendra.DocumentAttribute")\] | None_ _ = \[\]_\#     

The document attributes.

_param _DocumentId _: str | None_ _\[Required\]_\#     

The document ID.

_param _DocumentURI _: str | None_ _\[Required\]_\#     

The document URI.

_param _Id _: str | None_ _\[Required\]_\#     

The ID of the relevant result item.

_param _ScoreAttributes _: dict | None_ _\[Required\]_\#     

The kendra score confidence

get\_additional\_metadata\(\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem.get_additional_metadata)\#     

Document additional metadata dict. This returns any extra metadata except these:

>   * result\_id >  >   * document\_id >  >   * source >  >   * title >  >   * excerpt >  >   * document\_attributes >  > 

Return type:     

dict

get\_document\_attributes\_dict\(\) → Dict\[str, str | int | List\[str\] | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem.get_document_attributes_dict)\#     

Document attributes dict.

Return type:     

_Dict_\[str, str | int | _List_\[str\] | None\]

_abstractmethod _get\_excerpt\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem.get_excerpt)\#     

Document excerpt or passage original content as retrieved by Kendra.

Return type:     

str

get\_score\_attribute\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem.get_score_attribute)\#     

Document Score Confidence

Return type:     

str

_abstractmethod _get\_title\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem.get_title)\#     

Document title.

Return type:     

str

to\_doc\(_page\_content\_formatter: ~typing.Callable\[\[~langchain\_community.retrievers.kendra.ResultItem\], str\] = <function combined\_text>_\) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#ResultItem.to_doc)\#     

Converts this item to a Document.

Parameters:     

**page\_content\_formatter** \(_Callable_ _\[__\[__ResultItem_ _\]__,__str_ _\]_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

__On this page