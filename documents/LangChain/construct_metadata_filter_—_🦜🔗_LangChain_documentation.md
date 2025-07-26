# construct_metadata_filter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.falkordb_vector.construct_metadata_filter.html
**Word Count:** 36
**Links Count:** 316
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# construct\_metadata\_filter\#

langchain\_community.vectorstores.falkordb\_vector.construct\_metadata\_filter\(

    _filter : Dict\[str, Any\] | None = None_, \) → Tuple\[str, Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/falkordb_vector.html#construct_metadata_filter)\#     

Construct a metadata filter by directly injecting the filter values into the query.

Parameters:     

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Dictionary

  * **condition.** \(_representing the filter_\)

Returns:     

Filter snippet and an empty dictionary \(since we don’t need parameters\).

Return type:     

Tuple\[str, Dict\[str, Any\]\]

__On this page