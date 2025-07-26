# dumps — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/load/langchain_core.load.dump.dumps.html
**Word Count:** 75
**Links Count:** 112
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# dumps\#

langchain\_core.load.dump.dumps\(

    _obj : Any_,     _\*_ ,     _pretty : bool = False_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/dump.html#dumps)\#     

Return a json string representation of an object.

Parameters:     

  * **obj** \(_Any_\) – The object to dump.

  * **pretty** \(_bool_\) – Whether to pretty print the json. If true, the json will be indented with 2 spaces \(if no indent is provided as part of kwargs\). Default is False.

  * **kwargs** \(_Any_\) – Additional arguments to pass to json.dumps

Returns:     

A json string representation of the object.

Raises:     

**ValueError** – If default is passed as a kwarg.

Return type:     

str

Examples using dumps

  * [How to save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)