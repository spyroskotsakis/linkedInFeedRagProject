# try_neq_default — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.try_neq_default.html
**Word Count:** 43
**Links Count:** 111
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# try\_neq\_default\#

langchain\_core.load.serializable.try\_neq\_default\(

    _value : Any_,     _key : str_,     _model : BaseModel_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/serializable.html#try_neq_default)\#     

Try to determine if a value is different from the default.

Parameters:     

  * **value** \(_Any_\) – The value.

  * **key** \(_str_\) – The key.

  * **model** \(_BaseModel_\) – The pydantic model.

Returns:     

Whether the value is different from the default.

Raises:     

**Exception** – If the key is not in the model.

Return type:     

bool

__On this page