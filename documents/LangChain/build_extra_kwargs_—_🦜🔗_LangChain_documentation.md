# build_extra_kwargs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.build_extra_kwargs.html
**Word Count:** 55
**Links Count:** 166
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# build\_extra\_kwargs\#

langchain\_core.utils.utils.build\_extra\_kwargs\(

    _extra\_kwargs : dict\[str, Any\]_,     _values : dict\[str, Any\]_,     _all\_required\_field\_names : set\[str\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#build_extra_kwargs)\#     

Build extra kwargs from values and extra\_kwargs.

Parameters:     

  * **extra\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Extra kwargs passed in by user.

  * **values** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Values passed in by user.

  * **all\_required\_field\_names** \(_set_ _\[__str_ _\]_\) – All required field names for the pydantic class.

Returns:     

Extra kwargs.

Return type:     

dict\[str, Any\]

Raises:     

  * **ValueError** – If a field is specified in both values and extra\_kwargs.

  * **ValueError** – If a field is specified in model\_kwargs.

__On this page