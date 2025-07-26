# TransferSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.transfer.TransferSchema.html
**Word Count:** 50
**Links Count:** 411
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# TransferSchema\#

_class _langchain\_community.tools.ainetwork.transfer.TransferSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/ainetwork/transfer.html#TransferSchema)\#     

Bases: `BaseModel`

Schema for transfer operations.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _address _: str_ _\[Required\]_\#     

Address to transfer AIN to

_param _amount _: int_ _\[Required\]_\#     

Amount of AIN to transfer

__On this page