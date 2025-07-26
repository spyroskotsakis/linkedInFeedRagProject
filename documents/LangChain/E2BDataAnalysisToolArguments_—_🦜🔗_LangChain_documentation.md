# E2BDataAnalysisToolArguments — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.e2b_data_analysis.tool.E2BDataAnalysisToolArguments.html
**Word Count:** 60
**Links Count:** 409
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# E2BDataAnalysisToolArguments\#

_class _langchain\_community.tools.e2b\_data\_analysis.tool.E2BDataAnalysisToolArguments[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/tool.html#E2BDataAnalysisToolArguments)\#     

Bases: `BaseModel`

Arguments for the E2BDataAnalysisTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _python\_code _: str_ _\[Required\]_\#     

The python script to be evaluated. The contents will be in main.py. It should not be in markdown format.

__On this page