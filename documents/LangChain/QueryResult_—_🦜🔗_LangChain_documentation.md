# QueryResult — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.QueryResult.html
**Word Count:** 73
**Links Count:** 101
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# QueryResult\#

_class _langchain\_aws.retrievers.kendra.QueryResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#QueryResult)\#     

Bases: `BaseModel`

Amazon Kendra Query API search result.

It is composed of:     

  * Relevant suggested answers: either a text excerpt or table excerpt.

  * Matching FAQs or questions-answer from your FAQ file.

  * Documents including an excerpt of each document with its title.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _ResultItems _: List\[[QueryResultItem](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.QueryResultItem.html#langchain_aws.retrievers.kendra.QueryResultItem "langchain_aws.retrievers.kendra.QueryResultItem")\]__\[Required\]_\#     

The result items.

__On this page