# langchain-neo4j: 0.4.0 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/index.html
**Word Count:** 120
**Links Count:** 94
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# langchain-neo4j: 0.4.0\#

## [chains](https://python.langchain.com/api_reference/neo4j/chains.html#langchain-neo4j-chains)\#

**Classes**

[`chains.graph_qa.cypher.GraphCypherQAChain`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain.html#langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain "langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain") | Chain for question-answering against a graph by generating Cypher statements.   ---|---   [`chains.graph_qa.cypher_utils.CypherQueryCorrector`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector")\(schemas\) | Used to correct relationship direction in generated Cypher statements.   [`chains.graph_qa.cypher_utils.Schema`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")\(...\) | Create new instance of Schema\(left\_node, relation, right\_node\)      **Functions**

[`chains.graph_qa.cypher.construct_schema`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.construct_schema.html#langchain_neo4j.chains.graph_qa.cypher.construct_schema "langchain_neo4j.chains.graph_qa.cypher.construct_schema")\(...\) | Filter the schema based on included or excluded types   ---|---   [`chains.graph_qa.cypher.get_function_response`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.get_function_response.html#langchain_neo4j.chains.graph_qa.cypher.get_function_response "langchain_neo4j.chains.graph_qa.cypher.get_function_response")\(...\) |       ## [chat\_message\_histories](https://python.langchain.com/api_reference/neo4j/chat_message_histories.html#langchain-neo4j-chat-message-histories)\#

**Classes**

[`chat_message_histories.neo4j.Neo4jChatMessageHistory`](https://python.langchain.com/api_reference/neo4j/chat_message_histories/langchain_neo4j.chat_message_histories.neo4j.Neo4jChatMessageHistory.html#langchain_neo4j.chat_message_histories.neo4j.Neo4jChatMessageHistory "langchain_neo4j.chat_message_histories.neo4j.Neo4jChatMessageHistory")\(...\) | Chat message history stored in a Neo4j database.   ---|---      ## [graphs](https://python.langchain.com/api_reference/neo4j/graphs.html#langchain-neo4j-graphs)\#

**Classes**

[`graphs.graph_document.GraphDocument`](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument") | Represents a graph document consisting of nodes and relationships.   ---|---   [`graphs.graph_document.Node`](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Node.html#langchain_neo4j.graphs.graph_document.Node "langchain_neo4j.graphs.graph_document.Node") | Represents a node in a graph with associated properties.   [`graphs.graph_document.Relationship`](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Relationship.html#langchain_neo4j.graphs.graph_document.Relationship "langchain_neo4j.graphs.graph_document.Relationship") | Represents a directed relationship between two nodes in a graph.   [`graphs.graph_store.GraphStore`](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_store.GraphStore.html#langchain_neo4j.graphs.graph_store.GraphStore "langchain_neo4j.graphs.graph_store.GraphStore")\(\*args, \*\*kwargs\) | Abstract class for graph operations.   [`graphs.neo4j_graph.Neo4jGraph`](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html#langchain_neo4j.graphs.neo4j_graph.Neo4jGraph "langchain_neo4j.graphs.neo4j_graph.Neo4jGraph")\(\[url, ...\]\) | Neo4j database wrapper for various graph operations.      ## [query\_constructors](https://python.langchain.com/api_reference/neo4j/query_constructors.html#langchain-neo4j-query-constructors)\#

**Classes**

[`query_constructors.neo4j.Neo4jTranslator`](https://python.langchain.com/api_reference/neo4j/query_constructors/langchain_neo4j.query_constructors.neo4j.Neo4jTranslator.html#langchain_neo4j.query_constructors.neo4j.Neo4jTranslator "langchain_neo4j.query_constructors.neo4j.Neo4jTranslator")\(\) | Translate Neo4j internal query language elements to valid filters.   ---|---      ## [vectorstores](https://python.langchain.com/api_reference/neo4j/vectorstores.html#langchain-neo4j-vectorstores)\#

**Classes**

[`vectorstores.neo4j_vector.Neo4jVector`](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.neo4j_vector.Neo4jVector.html#langchain_neo4j.vectorstores.neo4j_vector.Neo4jVector "langchain_neo4j.vectorstores.neo4j_vector.Neo4jVector")\(...\[, ...\]\) | Neo4j vector index.   ---|---   [`vectorstores.utils.DistanceStrategy`](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.utils.DistanceStrategy.html#langchain_neo4j.vectorstores.utils.DistanceStrategy "langchain_neo4j.vectorstores.utils.DistanceStrategy")\(value\) | Enumerator of the Distance strategies for calculating distances between vectors.      **Functions**

[`vectorstores.neo4j_vector.check_if_not_null`](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.neo4j_vector.check_if_not_null.html#langchain_neo4j.vectorstores.neo4j_vector.check_if_not_null "langchain_neo4j.vectorstores.neo4j_vector.check_if_not_null")\(...\) | Check if the values are not None or empty string   ---|---   [`vectorstores.neo4j_vector.dict_to_yaml_str`](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.neo4j_vector.dict_to_yaml_str.html#langchain_neo4j.vectorstores.neo4j_vector.dict_to_yaml_str "langchain_neo4j.vectorstores.neo4j_vector.dict_to_yaml_str")\(...\) | Convert a dictionary to a YAML-like string without using external libraries.   [`vectorstores.neo4j_vector.remove_lucene_chars`](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.neo4j_vector.remove_lucene_chars.html#langchain_neo4j.vectorstores.neo4j_vector.remove_lucene_chars "langchain_neo4j.vectorstores.neo4j_vector.remove_lucene_chars")\(text\) | Remove Lucene special characters