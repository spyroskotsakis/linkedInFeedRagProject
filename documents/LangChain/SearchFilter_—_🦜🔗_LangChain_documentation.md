# SearchFilter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.bedrock.SearchFilter.html
**Word Count:** 42
**Links Count:** 126
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# SearchFilter\#

_class _langchain\_aws.retrievers.bedrock.SearchFilter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/bedrock.html#SearchFilter)\#     

Bases: `BaseModel`

Filter configuration for retrieval.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _andAll _: List\[SearchFilter\] | None_ _ = None_\#     

_param _equals _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _greaterThan _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _greaterThanOrEquals _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _in\__: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_ _\(alias 'in'\)_\#     

_param _lessThan _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _lessThanOrEquals _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _listContains _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _notEquals _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _notIn _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _orAll _: List\[SearchFilter\] | None_ _ = None_\#     

_param _startsWith _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

_param _stringContains _: Dict\[str, Dict\[str, Any\] | List\[Any\] | int | float | str | bool | None\] | None_ _ = None_\#     

__On this page