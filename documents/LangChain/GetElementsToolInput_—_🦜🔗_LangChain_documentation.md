# GetElementsToolInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.playwright.get_elements.GetElementsToolInput.html
**Word Count:** 57
**Links Count:** 411
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# GetElementsToolInput\#

_class _langchain\_community.tools.playwright.get\_elements.GetElementsToolInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/playwright/get_elements.html#GetElementsToolInput)\#     

Bases: `BaseModel`

Input for GetElementsTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _attributes _: List\[str\]__\[Optional\]_\#     

Set of attributes to retrieve for each element

_param _selector _: str_ _\[Required\]_\#     

CSS selector, such as ‘\*’, ‘div’, ‘p’, ‘a’, \#id, .classname

__On this page