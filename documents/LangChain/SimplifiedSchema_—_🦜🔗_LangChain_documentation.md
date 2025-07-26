# SimplifiedSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.SimplifiedSchema.html
**Word Count:** 82
**Links Count:** 121
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# SimplifiedSchema\#

_class _langchain\_experimental.graph\_transformers.diffbot.SimplifiedSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#SimplifiedSchema)\#     

Simplified schema mapping.

schema\#     

A dictionary containing the mapping to simplified schema types.

Type:     

Dict

Initializes the schema dictionary based on the predefined list.

Methods

`__init__`\(\) | Initializes the schema dictionary based on the predefined list.   ---|---   `get_type`\(type\) | Retrieves the simplified schema type for a given original type.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#SimplifiedSchema.__init__)\#     

Initializes the schema dictionary based on the predefined list.

Return type:     

None

get\_type\(_type : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#SimplifiedSchema.get_type)\#     

Retrieves the simplified schema type for a given original type.

Parameters:     

**type** \(_str_\) – The original schema type to find the simplified type for.

Returns:     

The simplified schema type if it exists;     

otherwise, returns the original type.

Return type:     

str

__On this page