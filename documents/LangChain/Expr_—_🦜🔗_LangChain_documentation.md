# Expr — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Expr.html
**Word Count:** 52
**Links Count:** 111
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# Expr\#

_class _langchain\_core.structured\_query.Expr[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Expr)\#     

Bases: `BaseModel`

Base class for all expressions.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

accept\(

    _visitor : [Visitor](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Expr.accept)\#     

Accept a visitor.

Parameters:     

**visitor** \([_Visitor_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")\) – visitor to accept.

Returns:     

result of visiting.

Return type:     

_Any_

__On this page