# read_schema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.read_schema.html
**Word Count:** 46
**Links Count:** 102
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# read\_schema\#

langchain\_aws.vectorstores.inmemorydb.schema.read\_schema\(

    _index\_schema : Dict\[str, List\[Any\]\] | str | PathLike | None_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#read_schema)\#     

Read in the index schema from a dict or yaml file.

Check if it is a dict and return RedisModel otherwise, check if it’s a path and read in the file assuming it’s a yaml file and return a RedisModel

Parameters:     

**index\_schema** \(_Dict_ _\[__str_ _,__List_ _\[__Any_ _\]__\]__|__str_ _|__PathLike_ _|__None_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page