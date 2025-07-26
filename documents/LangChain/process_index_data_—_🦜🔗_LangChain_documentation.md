# process_index_data — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.falkordb_vector.process_index_data.html
**Word Count:** 184
**Links Count:** 316
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# process\_index\_data\#

langchain\_community.vectorstores.falkordb\_vector.process\_index\_data\(

    _data : List\[List\[Any\]\]_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/falkordb_vector.html#process_index_data)\#     

Processes a nested list of entity data to extract information about labels, entity types, properties, index types, and index details \(if applicable\).

Parameters:     

  * **data** \(_List_ _\[__List_ _\[__Any_ _\]__\]_\) – A nested list containing

  * **entitys** \(_details about_\)

  * **properties** \(_their_\)

  * **index**

  * **types**

  * **information.** \(_and configuration_\)

Returns:     

A list of dictionaries where each dictionary contains:

>   * entity\_label \(str\): The label or name of the entity or relationship \(e.g., ‘Person’, ‘Song’\). >  >   * entity\_property \(str\): The property of the entity or relationship on which an index was created \(e.g., ‘first\_name’\). >  >   * index\_type \(str or List\[str\]\): The type\(s\) of index applied to the property \(e.g., ‘FULLTEXT’, ‘VECTOR’\). >  >   * index\_status \(str\): The status of the index \(e.g., ‘OPERATIONAL’, ‘PENDING’\). >  >   * index\_dimension \(Optional\[int\]\): The dimension of the vector index, if applicable. >  >   * index\_similarityFunction \(Optional\[str\]\): The similarity function used by the vector index, if applicable. >  >   * entity\_type \(str\): The type of entity. That is either entity or relationship >  > 

Return type:     

List\[Dict\[str, Any\]\]

Notes

  * The entity label is extracted from the first element of each entity list.

  * The entity property and associated index types are extracted from the second element.

  * If the index type includes ‘VECTOR’, additional details such as dimension and similarity function are extracted from the entity configuration.

  * The function handles cases where entitys have multiple index types \(e.g., both ‘FULLTEXT’ and ‘VECTOR’\).

__On this page