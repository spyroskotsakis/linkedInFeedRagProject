# SemantscholarInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.semanticscholar.tool.SemantscholarInput.html
**Word Count:** 47
**Links Count:** 409
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# SemantscholarInput\#

_class _langchain\_community.tools.semanticscholar.tool.SemantscholarInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/semanticscholar/tool.html#SemantscholarInput)\#     

Bases: `BaseModel`

Input for the SemanticScholar tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

search query to look up

__On this page