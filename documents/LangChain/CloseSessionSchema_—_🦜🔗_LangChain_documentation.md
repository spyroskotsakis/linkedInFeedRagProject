# CloseSessionSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.multion.close_session.CloseSessionSchema.html
**Word Count:** 52
**Links Count:** 409
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# CloseSessionSchema\#

_class _langchain\_community.tools.multion.close\_session.CloseSessionSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/multion/close_session.html#CloseSessionSchema)\#     

Bases: `BaseModel`

Input for UpdateSessionTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _sessionId _: str_ _\[Required\]_\#     

The sessionId, received from one of the createSessions or updateSessions run before

__On this page