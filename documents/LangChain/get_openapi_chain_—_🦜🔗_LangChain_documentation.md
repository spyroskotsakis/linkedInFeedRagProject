# get_openapi_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.get_openapi_chain.html
**Word Count:** 148
**Links Count:** 199
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# get\_openapi\_chain\#

langchain.chains.openai\_functions.openapi.get\_openapi\_chain\(

    _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec") | str_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _request\_chain : [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") | None = None_,     _llm\_chain\_kwargs : dict | None = None_,     _verbose : bool = False_,     _headers : dict | None = None_,     _params : dict | None = None_,     _\*\* kwargs: Any_, \) → [SequentialChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SequentialChain.html#langchain.chains.sequential.SequentialChain "langchain.chains.sequential.SequentialChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/openapi.html#get_openapi_chain)\#     

Deprecated since version 0.2.13: This function is deprecated and will be removed in langchain 1.0. See API reference for replacement: <https://api.python.langchain.com/en/latest/chains/langchain.chains.openai_functions.openapi.get_openapi_chain.html> It will not be removed until langchain==1.0.

Create a chain for querying an API from a OpenAPI spec.

Note: this class is deprecated. See below for a replacement implementation.     

The benefits of this implementation are:

  * Uses LLM tool calling features to encourage properly-formatted API requests;

  * Includes async support.

              from typing import Any          from langchain.chains.openai_functions.openapi import openapi_spec_to_openai_fn     from langchain_community.utilities.openapi import OpenAPISpec     from langchain_core.prompts import ChatPromptTemplate     from langchain_openai import ChatOpenAI          # Define API spec. Can be JSON or YAML     api_spec = """     {     "openapi": "3.1.0",     "info": {         "title": "JSONPlaceholder API",         "version": "1.0.0"     },     "servers": [         {         "url": "https://jsonplaceholder.typicode.com"         }     ],     "paths": {         "/posts": {         "get": {             "summary": "Get posts",             "parameters": [             {                 "name": "_limit",                 "in": "query",                 "required": false,                 "schema": {                 "type": "integer",                 "example": 2                 },                 "description": "Limit the number of results"             }             ]         }         }     }     }     """          parsed_spec = OpenAPISpec.from_text(api_spec)     openai_fns, call_api_fn = openapi_spec_to_openai_fn(parsed_spec)     tools = [         {"type": "function", "function": fn}         for fn in openai_fns     ]          prompt = ChatPromptTemplate.from_template(         "Use the provided APIs to respond to this user query:\n\n{query}"     )     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)          def _execute_tool(message) -> Any:         if tool_calls := message.tool_calls:             tool_call = message.tool_calls[0]             response = call_api_fn(name=tool_call["name"], fn_args=tool_call["args"])             response.raise_for_status()             return response.json()         else:             return message.content          chain = prompt | llm | _execute_tool                    response = chain.invoke({"query": "Get me top two posts."})     

Parameters:     

  * **spec** \(_Union_ _\[_[_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec") _,__str_ _\]_\) – OpenAPISpec or url/file/text string corresponding to one.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – language model, should be an OpenAI function-calling model, e.g. ChatOpenAI\(model=”gpt-3.5-turbo-0613”\).

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\) – Main prompt template to use.

  * **request\_chain** \(_Optional_ _\[_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") _\]_\) – Chain for taking the functions output and executing the request.

  * **llm\_chain\_kwargs** \(_Optional_ _\[__dict_ _\]_\)

  * **verbose** \(_bool_\)

  * **headers** \(_Optional_ _\[__dict_ _\]_\)

  * **params** \(_Optional_ _\[__dict_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

[SequentialChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SequentialChain.html#langchain.chains.sequential.SequentialChain "langchain.chains.sequential.SequentialChain")

__On this page