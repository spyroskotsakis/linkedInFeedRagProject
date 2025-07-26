# ZenGuardInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.zenguard.tool.ZenGuardInput.html
**Word Count:** 62
**Links Count:** 414
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# ZenGuardInput\#

_class _langchain\_community.tools.zenguard.tool.ZenGuardInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/zenguard/tool.html#ZenGuardInput)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _detectors _: List\[[Detector](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.zenguard.tool.Detector.html#langchain_community.tools.zenguard.tool.Detector "langchain_community.tools.zenguard.tool.Detector")\]__\[Required\]_\#     

List of detectors by which you want to check the prompt

Constraints:     

  * **min\_length** = 1

_param _in\_parallel _: bool_ _ = True_\#     

Run prompt detection by the detector in parallel or sequentially

_param _prompts _: List\[str\]__\[Required\]_\#     

Prompt to check

Constraints:     

  * **min\_length** = 1

__On this page