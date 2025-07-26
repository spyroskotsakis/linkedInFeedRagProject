# ValueSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.value.ValueSchema.html
**Word Count:** 50
**Links Count:** 414
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# ValueSchema\#

_class _langchain\_community.tools.ainetwork.value.ValueSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/ainetwork/value.html#ValueSchema)\#     

Bases: `BaseModel`

Schema for value operations.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _path _: str_ _\[Required\]_\#     

Blockchain reference path

_param _type _: [OperationType](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.base.OperationType.html#langchain_community.tools.ainetwork.base.OperationType "langchain_community.tools.ainetwork.base.OperationType")_ _\[Required\]_\#     

_param _value _: int | str | float | dict | None_ _ = None_\#     

Value to be set at the path

__On this page