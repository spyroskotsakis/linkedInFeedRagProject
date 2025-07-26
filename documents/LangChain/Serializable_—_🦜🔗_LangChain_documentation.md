# Serializable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html
**Word Count:** 120
**Links Count:** 111
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# Serializable\#

_class _langchain\_core.load.serializable.Serializable[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/serializable.html#Serializable)\#     

Bases: `BaseModel`, `ABC`

Serializable base class.

This class is used to serialize objects to JSON.

It relies on the following methods and properties:

  * is\_lc\_serializable: Is this class serializable?     

By design, even if a class inherits from Serializable, it is not serializable by default. This is to prevent accidental serialization of objects that should not be serialized.

  * get\_lc\_namespace: Get the namespace of the langchain object.     

During deserialization, this namespace is used to identify the correct class to instantiate. Please see the Reviver class in langchain\_core.load.load for more details. During deserialization an additional mapping is handle classes that have moved or been renamed across package versions.

  * lc\_secrets: A map of constructor argument names to secret ids.

  * lc\_attributes: List of additional attribute names that should be included     

as part of the serialized representation.

__On this page