# ExtractHyperlinksToolInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.playwright.extract_hyperlinks.ExtractHyperlinksToolInput.html
**Word Count:** 47
**Links Count:** 409
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# ExtractHyperlinksToolInput\#

_class _langchain\_community.tools.playwright.extract\_hyperlinks.ExtractHyperlinksToolInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/playwright/extract_hyperlinks.html#ExtractHyperlinksToolInput)\#     

Bases: `BaseModel`

Input for ExtractHyperlinksTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _absolute\_urls _: bool_ _ = False_\#     

Return absolute URLs instead of relative URLs

__On this page