# UpstageGroundednessCheckInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/tools/langchain_upstage.tools.groundedness_check.UpstageGroundednessCheckInput.html
**Word Count:** 61
**Links Count:** 80
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# UpstageGroundednessCheckInput\#

_class _langchain\_upstage.tools.groundedness\_check.UpstageGroundednessCheckInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/tools/groundedness_check.html#UpstageGroundednessCheckInput)\#     

Bases: `BaseModel`

Input for the Groundedness Check tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _answer _: str_ _\[Required\]_\#     

assistant’s reply or a text that is subject to groundedness check

_param _context _: str | List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]__\[Required\]_\#     

context in which the answer should be verified

__On this page