# DataheraldTextToSQLInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.dataherald.tool.DataheraldTextToSQLInput.html
**Word Count:** 48
**Links Count:** 409
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# DataheraldTextToSQLInput\#

_class _langchain\_community.tools.dataherald.tool.DataheraldTextToSQLInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/dataherald/tool.html#DataheraldTextToSQLInput)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _prompt _: str_ _\[Required\]_\#     

Natural language query to be translated to a SQL query.

__On this page