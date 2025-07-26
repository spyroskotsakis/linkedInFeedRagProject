# ClickToolInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.playwright.click.ClickToolInput.html
**Word Count:** 47
**Links Count:** 409
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# ClickToolInput\#

_class _langchain\_community.tools.playwright.click.ClickToolInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/playwright/click.html#ClickToolInput)\#     

Bases: `BaseModel`

Input for ClickTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _selector _: str_ _\[Required\]_\#     

CSS selector for the element to click

__On this page