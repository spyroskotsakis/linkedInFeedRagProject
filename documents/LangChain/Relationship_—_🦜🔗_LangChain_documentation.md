# Relationship — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Relationship.html
**Word Count:** 42
**Links Count:** 152
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# Relationship\#

_class _langchain\_community.graphs.graph\_document.Relationship[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/graph_document.html#Relationship)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Represents a directed relationship between two nodes in a graph.

source\#     

The source node of the relationship.

Type:     

[Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")

target\#     

The target node of the relationship.

Type:     

[Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")

type\#     

The type of the relationship.

Type:     

str

properties\#     

Additional properties associated with the relationship.

Type:     

dict

_param _properties _: dict_ _\[Optional\]_\#     

_param _source _: [Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")_ _\[Required\]_\#     

_param _target _: [Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")_ _\[Required\]_\#     

_param _type _: str_ _\[Required\]_\#     

Examples using Relationship

  * [Azure Cosmos DB for Apache Gremlin](https://python.langchain.com/docs/integrations/graphs/azure_cosmosdb_gremlin/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page