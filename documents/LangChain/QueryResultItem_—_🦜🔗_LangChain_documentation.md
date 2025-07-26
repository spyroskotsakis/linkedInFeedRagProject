# QueryResultItem — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.QueryResultItem.html
**Word Count:** 149
**Links Count:** 146
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# QueryResultItem\#

_class _langchain\_aws.retrievers.kendra.QueryResultItem[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#QueryResultItem)\#     

Bases: [`ResultItem`](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.ResultItem.html#langchain_aws.retrievers.kendra.ResultItem "langchain_aws.retrievers.kendra.ResultItem")

Query API result item.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _AdditionalAttributes _: List\[[AdditionalResultAttribute](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.AdditionalResultAttribute.html#langchain_aws.retrievers.kendra.AdditionalResultAttribute "langchain_aws.retrievers.kendra.AdditionalResultAttribute")\] | None_ _ = \[\]_\#     

One or more additional attributes associated with the result.

_param _DocumentAttributes _: List\[[DocumentAttribute](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.DocumentAttribute.html#langchain_aws.retrievers.kendra.DocumentAttribute "langchain_aws.retrievers.kendra.DocumentAttribute")\] | None_ _ = \[\]_\#     

The document attributes.

_param _DocumentExcerpt _: [TextWithHighLights](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.TextWithHighLights.html#langchain_aws.retrievers.kendra.TextWithHighLights "langchain_aws.retrievers.kendra.TextWithHighLights") | None_ _ = None_\#     

Excerpt of the document text.

_param _DocumentId _: str | None_ _ = None_\#     

The document ID.

_param _DocumentTitle _: [TextWithHighLights](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.TextWithHighLights.html#langchain_aws.retrievers.kendra.TextWithHighLights "langchain_aws.retrievers.kendra.TextWithHighLights")_ _\[Required\]_\#     

The document title.

_param _DocumentURI _: str | None_ _ = None_\#     

The document URI.

_param _FeedbackToken _: str | None_ _ = None_\#     

Identifies a particular result from a particular query.

_param _Format _: str | None_ _ = None_\#     

If the Type is ANSWER, then format is either:     

  * TABLE: a table excerpt is returned in TableExcerpt;

  * TEXT: a text excerpt is returned in DocumentExcerpt.

_param _Id _: str | None_ _ = None_\#     

The ID of the relevant result item.

_param _ScoreAttributes _: dict | None_ _ = None_\#     

The kendra score confidence

_param _Type _: str | None_ _ = None_\#     

Type of result: DOCUMENT or QUESTION\_ANSWER or ANSWER

get\_additional\_metadata\(\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#QueryResultItem.get_additional_metadata)\#     

Document additional metadata dict. This returns any extra metadata except these:

>   * result\_id >  >   * document\_id >  >   * source >  >   * title >  >   * excerpt >  >   * document\_attributes >  > 

Return type:     

dict

get\_attribute\_value\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#QueryResultItem.get_attribute_value)\#     

Return type:     

str

get\_document\_attributes\_dict\(\) → Dict\[str, str | int | List\[str\] | None\]\#     

Document attributes dict.

Return type:     

_Dict_\[str, str | int | _List_\[str\] | None\]

get\_excerpt\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#QueryResultItem.get_excerpt)\#     

Document excerpt or passage original content as retrieved by Kendra.

Return type:     

str

get\_score\_attribute\(\) → str\#     

Document Score Confidence

Return type:     

str

get\_title\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#QueryResultItem.get_title)\#     

Document title.

Return type:     

str

to\_doc\(_page\_content\_formatter: ~typing.Callable\[\[~langchain\_aws.retrievers.kendra.ResultItem\], str\] = <function combined\_text>_\) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\#     

Converts this item to a Document.

Parameters:     

**page\_content\_formatter** \(_Callable_ _\[__\[_[_ResultItem_](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.ResultItem.html#langchain_aws.retrievers.kendra.ResultItem "langchain_aws.retrievers.kendra.ResultItem") _\]__,__str_ _\]_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

__On this page