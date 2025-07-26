# DriaAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dria_index.DriaAPIWrapper.html
**Word Count:** 127
**Links Count:** 279
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# DriaAPIWrapper\#

_class _langchain\_community.utilities.dria\_index.DriaAPIWrapper\(

    _api\_key : str_,     _contract\_id : str | None = None_,     _top\_n : int = 10_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper)\#     

Wrapper around Dria API.

This wrapper facilitates interactions with Dria’s vector search and retrieval services, including creating knowledge bases, inserting data, and fetching search results.

Parameters:     

  * **api\_key** \(_str_\)

  * **contract\_id** \(_str_ _|__None_\)

  * **top\_n** \(_int_\)

api\_key\#     

Your API key for accessing Dria.

contract\_id\#     

The contract ID of the knowledge base to interact with.

top\_n\#     

Number of top results to fetch for a search.

Methods

`__init__`\(api\_key\[, contract\_id, top\_n\]\) |    ---|---   `create_knowledge_base`\(name, description, ...\) | Create a new knowledge base.   `insert_data`\(data\) | Insert data into the knowledge base.   `query_with_vector`\(vector\) | Perform a vector-based query.   `run`\(query\) | Method to handle both text-based searches and vector-based queries.   `search`\(query\) | Perform a text-based search.      \_\_init\_\_\(

    _api\_key : str_,     _contract\_id : str | None = None_,     _top\_n : int = 10_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper.__init__)\#     

Parameters:     

  * **api\_key** \(_str_\)

  * **contract\_id** \(_str_ _|__None_\)

  * **top\_n** \(_int_\)

create\_knowledge\_base\(

    _name : str_,     _description : str_,     _category : str_,     _embedding : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper.create_knowledge_base)\#     

Create a new knowledge base.

Parameters:     

  * **name** \(_str_\)

  * **description** \(_str_\)

  * **category** \(_str_\)

  * **embedding** \(_str_\)

Return type:     

str

insert\_data\(

    _data : List\[Dict\[str, Any\]\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper.insert_data)\#     

Insert data into the knowledge base.

Parameters:     

**data** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

Return type:     

str

query\_with\_vector\(

    _vector : List\[float\]_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper.query_with_vector)\#     

Perform a vector-based query.

Parameters:     

**vector** \(_List_ _\[__float_ _\]_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

run\(

    _query : str | List\[float\]_, \) → List\[Dict\[str, Any\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper.run)\#     

Method to handle both text-based searches and vector-based queries.

Parameters:     

  * **query** \(_str_ _|__List_ _\[__float_ _\]_\) – A string for text-based search or a list of floats for

  * **query.** \(_vector-based_\)

Returns:     

The search or query results from Dria.

Return type:     

_List_\[_Dict_\[str, _Any_\]\] | None

search\(

    _query : str_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dria_index.html#DriaAPIWrapper.search)\#     

Perform a text-based search.

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

__On this page