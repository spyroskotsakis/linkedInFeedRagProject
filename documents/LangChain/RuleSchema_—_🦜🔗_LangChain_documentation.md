# RuleSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.owner.RuleSchema.html
**Word Count:** 69
**Links Count:** 422
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# RuleSchema\#

_class _langchain\_community.tools.ainetwork.owner.RuleSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/ainetwork/owner.html#RuleSchema)\#     

Bases: `BaseModel`

Schema for owner operations.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _address _: str | List\[str\] | None_ _ = None_\#     

A single address or a list of addresses

_param _branch\_owner _: bool | None_ _ = False_\#     

Authority to initialize owner of sub-paths

_param _path _: str_ _\[Required\]_\#     

Blockchain reference path

_param _type _: [OperationType](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.base.OperationType.html#langchain_community.tools.ainetwork.base.OperationType "langchain_community.tools.ainetwork.base.OperationType")_ _\[Required\]_\#     

_param _write\_function _: bool | None_ _ = False_\#     

Authority to set function for the path

_param _write\_owner _: bool | None_ _ = False_\#     

Authority to edit the owner property of the path

_param _write\_rule _: bool | None_ _ = False_\#     

Authority to edit write rule for the path

__On this page