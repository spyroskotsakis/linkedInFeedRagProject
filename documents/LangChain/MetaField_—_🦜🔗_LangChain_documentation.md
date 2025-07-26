# MetaField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.tencentvectordb.MetaField.html
**Word Count:** 48
**Links Count:** 325
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# MetaField\#

_class _langchain\_community.vectorstores.tencentvectordb.MetaField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/tencentvectordb.html#MetaField)\#     

Bases: `BaseModel`

MetaData Field for Tencent vector DB.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _data\_type _: str | Enum_ _\[Required\]_\#     

_param _description _: str | None_ _\[Required\]_\#     

_param _index _: bool_ _ = False_\#     

_param _name _: str_ _\[Required\]_\#     

Examples using MetaField

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

__On this page