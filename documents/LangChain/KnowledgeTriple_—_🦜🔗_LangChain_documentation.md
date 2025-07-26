# KnowledgeTriple — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html
**Word Count:** 67
**Links Count:** 142
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# KnowledgeTriple\#

_class _langchain\_community.graphs.networkx\_graph.KnowledgeTriple\(_subject : str_, _predicate : str_, _object\_ : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#KnowledgeTriple)\#     

Knowledge triple in the graph.

Create new instance of KnowledgeTriple\(subject, predicate, object\_\)

Attributes

`object_` | Alias for field number 2   ---|---   `predicate` | Alias for field number 1   `subject` | Alias for field number 0      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `from_string`\(triple\_string\) | Create a KnowledgeTriple from a string.   `index`\(value\[, start, stop\]\) | Return first index of value.      Parameters:     

  * **subject** \(_str_\)

  * **predicate** \(_str_\)

  * **object\_** \(_str_\)

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

_classmethod _from\_string\(

    _triple\_string : str_, \) → KnowledgeTriple[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#KnowledgeTriple.from_string)\#     

Create a KnowledgeTriple from a string.

Parameters:     

**triple\_string** \(_str_\)

Return type:     

_KnowledgeTriple_

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)