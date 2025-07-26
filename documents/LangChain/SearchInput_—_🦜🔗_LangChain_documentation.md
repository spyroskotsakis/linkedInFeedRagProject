# SearchInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.asknews.tool.SearchInput.html
**Word Count:** 109
**Links Count:** 411
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# SearchInput\#

_class _langchain\_community.tools.asknews.tool.SearchInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/asknews/tool.html#SearchInput)\#     

Bases: `BaseModel`

Input for the AskNews Search tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _hours\_back _: int | None_ _ = 0_\#     

If the Assistant deems that the event may have occurred more than 48 hours ago, it estimates the number of hours back to search. For example, if the event was one month ago, the Assistant may set this to 720. One week would be 168. The Assistant can estimate up to on year back \(8760\).

_param _query _: str_ _\[Required\]_\#     

Search query to be used for finding real-time or historical news information.

__On this page