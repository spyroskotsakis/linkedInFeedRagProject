# Node — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html
**Word Count:** 44
**Links Count:** 144
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# Node\#

_class _langchain\_community.graphs.graph\_document.Node[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/graph_document.html#Node)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Represents a node in a graph with associated properties.

id\#     

A unique identifier for the node.

Type:     

Union\[str, int\]

type\#     

The type or label of the node, default is “Node”.

Type:     

str

properties\#     

Additional properties and metadata associated with the node.

Type:     

dict

_param _id _: str | int_ _\[Required\]_\#     

_param _properties _: dict_ _\[Optional\]_\#     

_param _type _: str_ _ = 'Node'_\#     

Examples using Node

  * [Azure Cosmos DB for Apache Gremlin](https://python.langchain.com/docs/integrations/graphs/azure_cosmosdb_gremlin/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page