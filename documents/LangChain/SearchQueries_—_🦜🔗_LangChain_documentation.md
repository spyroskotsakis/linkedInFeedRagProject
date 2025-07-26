# SearchQueries — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.web_research.SearchQueries.html
**Word Count:** 54
**Links Count:** 174
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# SearchQueries\#

_class _langchain\_community.retrievers.web\_research.SearchQueries[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/web_research.html#SearchQueries)\#     

Bases: `BaseModel`

Search queries to research for the user’s goal.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _queries _: List\[str\]__\[Required\]_\#     

List of search queries to look up on Google

__On this page