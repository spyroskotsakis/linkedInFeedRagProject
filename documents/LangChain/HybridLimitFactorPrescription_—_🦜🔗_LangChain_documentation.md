# HybridLimitFactorPrescription — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.HybridLimitFactorPrescription.html
**Word Count:** 159
**Links Count:** 89
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# HybridLimitFactorPrescription\#

_class _langchain\_astradb.vectorstores.HybridLimitFactorPrescription\(_vector : float_, _lexical : float_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#HybridLimitFactorPrescription)\#     

A per-subsearch setting for the hybrid-search ‘limit’ factors.

This structure is to be used to set different values for the vector and the lexical portions of the hybrid search.

Each of the attributes is a floating-point number, representing the multiplicative factor applied to a search final ‘k’ to calculate the “limit” value for the associated sub-search. For instance, if vector=1.5 and lexical=3.0, a hybrid search called by asking a final set of k=4 results will be executed with limits of 6 for vector and 12 for lexical. \(The results are approximated to an integer.\)

Parameters:     

  * **vector** \(_float_\)

  * **lexical** \(_float_\)

vector\#     

the multiplicative factor for the “vector” part of the hybrid search.

Type:     

float

lexical\#     

the multiplicative factor for the “lexical” part of the hybrid search.

Type:     

float

Create new instance of HybridLimitFactorPrescription\(vector, lexical\)

Attributes

`lexical` | Alias for field number 1   ---|---   `vector` | Alias for field number 0      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)