# value_sanitize — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.neo4j_graph.value_sanitize.html
**Word Count:** 81
**Links Count:** 129
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# value\_sanitize\#

langchain\_community.graphs.neo4j\_graph.value\_sanitize\(_d : Any_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/neo4j_graph.html#value_sanitize)\#     

Deprecated since version 0.3.8: Use `:meth:`~langchain_neo4j.graphs.neo4j_graph.value_sanitize`` instead. It will not be removed until langchain-community==1.0.

Sanitize the input dictionary or list.

Sanitizes the input by removing embedding-like values, lists with more than 128 elements, that are mostly irrelevant for generating answers in a LLM context. These properties, if left in results, can occupy significant context space and detract from the LLM’s performance by introducing unnecessary noise and cost.

Parameters:     

**d** \(_Any_\) – The input dictionary or list to sanitize.

Returns:     

The sanitized dictionary or list.

Return type:     

Any

__On this page