# dereference_refs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.json_schema.dereference_refs.html
**Word Count:** 51
**Links Count:** 166
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# dereference\_refs\#

langchain\_core.utils.json\_schema.dereference\_refs\(

    _schema\_obj : dict_,     _\*_ ,     _full\_schema : dict | None = None_,     _skip\_keys : Sequence\[str\] | None = None_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/json_schema.html#dereference_refs)\#     

Try to substitute $refs in JSON Schema.

Parameters:     

  * **schema\_obj** \(_dict_\) – The fragment to dereference.

  * **full\_schema** \(_Optional_ _\[__dict_ _\]_\) – The complete schema \(defaults to schema\_obj\).

  * **skip\_keys** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) –      * If None \(the default\), we skip recursion under ‘$defs’ _and_ only     

shallow-inline refs.

    * If provided \(even as an empty list\), we will recurse under every key and     

deep-inline all refs.

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)