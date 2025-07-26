# openapi_spec_to_openai_fn — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.openapi_spec_to_openai_fn.html
**Word Count:** 46
**Links Count:** 190
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# openapi\_spec\_to\_openai\_fn\#

langchain.chains.openai\_functions.openapi.openapi\_spec\_to\_openai\_fn\(

    _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")_, \) → tuple\[list\[dict\[str, Any\]\], Callable\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/openapi.html#openapi_spec_to_openai_fn)\#     

Convert a valid OpenAPI spec to the JSON Schema format expected for OpenAI     

functions.

Parameters:     

**spec** \([_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")\) – OpenAPI spec to convert.

Returns:     

Tuple of the OpenAI functions JSON schema and a default function for executing     

a request based on the OpenAI function schema.

Return type:     

tuple\[list\[dict\[str, Any\]\], Callable\]

__On this page