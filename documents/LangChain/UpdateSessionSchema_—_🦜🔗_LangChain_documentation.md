# UpdateSessionSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.multion.update_session.UpdateSessionSchema.html
**Word Count:** 68
**Links Count:** 414
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# UpdateSessionSchema\#

_class _langchain\_community.tools.multion.update\_session.UpdateSessionSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/multion/update_session.html#UpdateSessionSchema)\#     

Bases: `BaseModel`

Input for UpdateSessionTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

The query to run in multion agent.

_param _sessionId _: str_ _\[Required\]_\#     

The sessionID, received from one of the createSessions run before

_param _url _: str_ _ = 'https://www.google.com/'_\#     

The Url to run the agent at. Note: accepts only secure links having <https://>

__On this page