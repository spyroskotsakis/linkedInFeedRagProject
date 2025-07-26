# AppSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.app.AppSchema.html
**Word Count:** 59
**Links Count:** 414
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# AppSchema\#

_class _langchain\_community.tools.ainetwork.app.AppSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/ainetwork/app.html#AppSchema)\#     

Bases: `BaseModel`

Schema for app operations.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _address _: str | List\[str\] | None_ _ = None_\#     

A single address or a list of addresses. Default: current session’s address

_param _appName _: str_ _\[Required\]_\#     

Name of the application on the blockchain

_param _type _: [AppOperationType](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.app.AppOperationType.html#langchain_community.tools.ainetwork.app.AppOperationType "langchain_community.tools.ainetwork.app.AppOperationType")_ _\[Required\]_\#     

__On this page