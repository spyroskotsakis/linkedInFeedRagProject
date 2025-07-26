# dumpd — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/load/langchain_core.load.dump.dumpd.html
**Word Count:** 63
**Links Count:** 112
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# dumpd\#

langchain\_core.load.dump.dumpd\(_obj : Any_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/dump.html#dumpd)\#     

Return a dict representation of an object.

Note

Unfortunately this function is not as efficient as it could be because it first dumps the object to a json string and then loads it back into a dictionary.

Parameters:     

**obj** \(_Any_\) – The object to dump.

Returns:     

dictionary that can be serialized to json using json.dumps

Return type:     

_Any_

Examples using dumpd

  * [How to save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)

__On this page