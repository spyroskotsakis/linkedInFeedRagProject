# chains — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/chains.html
**Word Count:** 36
**Links Count:** 78
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# `chains`\#

**Classes**

[`chains.graph_qa.cypher.GraphCypherQAChain`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain.html#langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain "langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain") | Chain for question-answering against a graph by generating Cypher statements.   ---|---   [`chains.graph_qa.cypher_utils.CypherQueryCorrector`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector")\(schemas\) | Used to correct relationship direction in generated Cypher statements.   [`chains.graph_qa.cypher_utils.Schema`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")\(...\) | Create new instance of Schema\(left\_node, relation, right\_node\)      **Functions**

[`chains.graph_qa.cypher.construct_schema`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.construct_schema.html#langchain_neo4j.chains.graph_qa.cypher.construct_schema "langchain_neo4j.chains.graph_qa.cypher.construct_schema")\(...\) | Filter the schema based on included or excluded types   ---|---   [`chains.graph_qa.cypher.get_function_response`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.get_function_response.html#langchain_neo4j.chains.graph_qa.cypher.get_function_response "langchain_neo4j.chains.graph_qa.cypher.get_function_response")\(...\) |