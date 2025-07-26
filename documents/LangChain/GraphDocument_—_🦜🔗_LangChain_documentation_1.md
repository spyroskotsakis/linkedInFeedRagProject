# GraphDocument — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html
**Word Count:** 42
**Links Count:** 98
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# GraphDocument\#

_class _langchain\_neo4j.graphs.graph\_document.GraphDocument[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/graph_document.html#GraphDocument)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Represents a graph document consisting of nodes and relationships.

nodes\#     

A list of nodes in the graph.

Type:     

List\[[Node](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Node.html#langchain_neo4j.graphs.graph_document.Node "langchain_neo4j.graphs.graph_document.Node")\]

relationships\#     

A list of relationships in the graph.

Type:     

List\[[Relationship](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Relationship.html#langchain_neo4j.graphs.graph_document.Relationship "langchain_neo4j.graphs.graph_document.Relationship")\]

source\#     

The document from which the graph information is derived.

Type:     

Optional\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_param _nodes _: List\[[Node](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Node.html#langchain_neo4j.graphs.graph_document.Node "langchain_neo4j.graphs.graph_document.Node")\]__\[Required\]_\#     

_param _relationships _: List\[[Relationship](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Relationship.html#langchain_neo4j.graphs.graph_document.Relationship "langchain_neo4j.graphs.graph_document.Relationship")\]__\[Required\]_\#     

_param _source _: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None_ _ = None_\#     

Examples using GraphDocument

  * [Azure Cosmos DB for Apache Gremlin](https://python.langchain.com/docs/integrations/graphs/azure_cosmosdb_gremlin/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page