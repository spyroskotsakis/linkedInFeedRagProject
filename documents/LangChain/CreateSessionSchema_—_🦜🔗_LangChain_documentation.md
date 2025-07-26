# CreateSessionSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.multion.create_session.CreateSessionSchema.html
**Word Count:** 59
**Links Count:** 412
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# CreateSessionSchema\#

_class _langchain\_community.tools.multion.create\_session.CreateSessionSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/multion/create_session.html#CreateSessionSchema)\#     

Bases: `BaseModel`

Input for CreateSessionTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

The query to run in multion agent.

_param _url _: str_ _ = 'https://www.google.com/'_\#     

The Url to run the agent at. Note: accepts only secure links having <https://>

__On this page