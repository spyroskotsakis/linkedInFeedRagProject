# GraphQLAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.graphql.GraphQLAPIWrapper.html
**Word Count:** 67
**Links Count:** 258
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# GraphQLAPIWrapper\#

_class _langchain\_community.utilities.graphql.GraphQLAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/graphql.html#GraphQLAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around GraphQL API.

To use, you should have the `gql` python package installed. This wrapper will use the GraphQL API to conduct queries.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _custom\_headers _: Dict\[str, str\] | None_ _ = None_\#     

_param _fetch\_schema\_from\_transport _: bool | None_ _ = None_\#     

_param _graphql\_endpoint _: str_ _\[Required\]_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/graphql.html#GraphQLAPIWrapper.run)\#     

Run a GraphQL query and get the results.

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page