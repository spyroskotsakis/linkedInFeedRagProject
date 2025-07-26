# SearchArgsSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gmail.search.SearchArgsSchema.html
**Word Count:** 94
**Links Count:** 414
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# SearchArgsSchema\#

_class _langchain\_community.tools.gmail.search.SearchArgsSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/gmail/search.html#SearchArgsSchema)\#     

Bases: `BaseModel`

Input for SearchGmailTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _max\_results _: int_ _ = 10_\#     

The maximum number of results to return.

_param _query _: str_ _\[Required\]_\#     

The Gmail query. Example filters include from:sender, to:recipient, subject:subject, -filtered\_term, in:folder, is:important|read|starred, after:year/mo/date, before:year/mo/date, label:label\_name “exact phrase”. Search newer/older than using d \(day\), m \(month\), and y \(year\): newer\_than:2d, older\_than:1y. Attachments with extension example: filename:pdf. Multiple term matching example: from:amy OR from:david.

_param _resource _: [Resource](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gmail.search.Resource.html#langchain_community.tools.gmail.search.Resource "langchain_community.tools.gmail.search.Resource")_ _ = Resource.MESSAGES_\#     

Whether to search for threads or messages.

__On this page