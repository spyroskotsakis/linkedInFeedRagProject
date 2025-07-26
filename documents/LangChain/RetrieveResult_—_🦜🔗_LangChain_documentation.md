# RetrieveResult — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.RetrieveResult.html
**Word Count:** 60
**Links Count:** 103
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# RetrieveResult\#

_class _langchain\_aws.retrievers.kendra.RetrieveResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#RetrieveResult)\#     

Bases: `BaseModel`

Amazon Kendra Retrieve API search result.

It is composed of:     

  * relevant passages or text excerpts given an input query.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _QueryId _: str_ _\[Required\]_\#     

The ID of the query.

_param _ResultItems _: List\[[RetrieveResultItem](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.RetrieveResultItem.html#langchain_aws.retrievers.kendra.RetrieveResultItem "langchain_aws.retrievers.kendra.RetrieveResultItem")\]__\[Required\]_\#     

The result items.

__On this page