# CypherQueryCorrector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html
**Word Count:** 112
**Links Count:** 123
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# CypherQueryCorrector\#

_class _langchain\_neo4j.chains.graph\_qa.cypher\_utils.CypherQueryCorrector\(

    _schemas : List\[[Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector)\#     

Used to correct relationship direction in generated Cypher statements. This code is copied from the winner’s submission to the Cypher competition: [sakusaku-rich/cypher-direction-competition](https://github.com/sakusaku-rich/cypher-direction-competition)

Parameters:     

**schemas** \(_List_ _\[_[_Schema_](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema") _\]_\) – list of schemas

Attributes

`node_pattern` |    ---|---   `node_relation_node_pattern` |    `path_pattern` |    `property_pattern` |    `relation_type_pattern` |       Methods

`__init__`\(schemas\) |    ---|---   `clean_node`\(node\) |    `correct_query`\(query\) |    `detect_labels`\(str\_node, node\_variable\_dict\) |    `detect_node_variables`\(query\) |    `detect_relation_types`\(str\_relation\) |    `extract_node_variable`\(part\) |    `extract_paths`\(query\) |    `judge_direction`\(relation\) |    `verify_schema`\(from\_node\_labels, ...\) |       \_\_init\_\_\(

    _schemas : List\[[Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.__init__)\#     

Parameters:     

**schemas** \(_List_ _\[_[_Schema_](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema") _\]_\) – list of schemas

clean\_node\(_node : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.clean_node)\#     

Parameters:     

**node** \(_str_\) – node in string format

Return type:     

str

correct\_query\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.correct_query)\#     

Parameters:     

**query** \(_str_\) – cypher query

Return type:     

str

detect\_labels\(

    _str\_node : str_,     _node\_variable\_dict : Dict\[str, Any\]_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.detect_labels)\#     

Parameters:     

  * **str\_node** \(_str_\) – node in string format

  * **node\_variable\_dict** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – dictionary of node variables

Return type:     

_List_\[str\]

detect\_node\_variables\(

    _query : str_, \) → Dict\[str, List\[str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.detect_node_variables)\#     

Parameters:     

**query** \(_str_\) – cypher query

Return type:     

_Dict_\[str, _List_\[str\]\]

detect\_relation\_types\(

    _str\_relation : str_, \) → Tuple\[str, List\[str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.detect_relation_types)\#     

Parameters:     

**str\_relation** \(_str_\) – relation in string format

Return type:     

_Tuple_\[str, _List_\[str\]\]

extract\_node\_variable\(

    _part : str_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.extract_node_variable)\#     

Parameters:     

**part** \(_str_\) – node in string format

Return type:     

str | None

extract\_paths\(

    _query : str_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.extract_paths)\#     

Parameters:     

**query** \(_str_\) – cypher query

Return type:     

_List_\[str\]

judge\_direction\(_relation : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.judge_direction)\#     

Parameters:     

**relation** \(_str_\) – relation in string format

Return type:     

str

verify\_schema\(

    _from\_node\_labels : List\[str\]_,     _relation\_types : List\[str\]_,     _to\_node\_labels : List\[str\]_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.verify_schema)\#     

Parameters:     

  * **from\_node\_labels** \(_List_ _\[__str_ _\]_\) – labels of the from node

  * **relation\_type** – type of the relation

  * **to\_node\_labels** \(_List_ _\[__str_ _\]_\) – labels of the to node

  * **relation\_types** \(_List_ _\[__str_ _\]_\)

Return type:     

bool

Examples using CypherQueryCorrector

  * [How to map values to a graph database](https://python.langchain.com/docs/how_to/graph_mapping/)

__On this page