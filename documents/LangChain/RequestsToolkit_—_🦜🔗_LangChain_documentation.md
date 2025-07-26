# RequestsToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.RequestsToolkit.html
**Word Count:** 336
**Links Count:** 172
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# RequestsToolkit\#

_class _langchain\_community.agent\_toolkits.openapi.toolkit.RequestsToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/toolkit.html#RequestsToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for making REST requests.

_Security Note_ : This toolkit contains tools to make GET, POST, PATCH, PUT,     

and DELETE requests to an API.

Exercise care in who is allowed to use this toolkit. If exposing to end users, consider that users will be able to make arbitrary requests on behalf of the server hosting the code. For example, users could ask the server to make a request to a private API that is only accessible from the server.

Control access to who can submit issue requests using this toolkit and what network access it has.

See <https://python.langchain.com/docs/security> for more information.

Setup:     

Install `langchain-community`.               pip install -U langchain-community     

Key init args:     

requests\_wrapper: langchain\_community.utilities.requests.GenericRequestsWrapper     

wrapper for executing requests.

allow\_dangerous\_requests: bool     

Defaults to False. Must “opt-in” to using dangerous requests by setting to True.

Instantiate:                    from langchain_community.agent_toolkits.openapi.toolkit import RequestsToolkit     from langchain_community.utilities.requests import TextRequestsWrapper          toolkit = RequestsToolkit(         requests_wrapper=TextRequestsWrapper(headers={}),         allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST,     )     

Tools:                    tools = toolkit.get_tools()     tools                    [RequestsGetTool(requests_wrapper=TextRequestsWrapper(headers={}, aiosession=None, auth=None, response_content_type='text', verify=True), allow_dangerous_requests=True),     RequestsPostTool(requests_wrapper=TextRequestsWrapper(headers={}, aiosession=None, auth=None, response_content_type='text', verify=True), allow_dangerous_requests=True),     RequestsPatchTool(requests_wrapper=TextRequestsWrapper(headers={}, aiosession=None, auth=None, response_content_type='text', verify=True), allow_dangerous_requests=True),     RequestsPutTool(requests_wrapper=TextRequestsWrapper(headers={}, aiosession=None, auth=None, response_content_type='text', verify=True), allow_dangerous_requests=True),     RequestsDeleteTool(requests_wrapper=TextRequestsWrapper(headers={}, aiosession=None, auth=None, response_content_type='text', verify=True), allow_dangerous_requests=True)]     

Use within an agent:                    from langchain_openai import ChatOpenAI     from langgraph.prebuilt import create_react_agent               api_spec = """     openapi: 3.0.0     info:       title: JSONPlaceholder API       version: 1.0.0     servers:       - url: https://jsonplaceholder.typicode.com     paths:       /posts:         get:           summary: Get posts           parameters: &id001             - name: _limit               in: query               required: false               schema:                 type: integer               example: 2               description: Limit the number of results     """          system_message = """     You have access to an API to help answer user queries.     Here is documentation on the API:     {api_spec}     """.format(api_spec=api_spec)          llm = ChatOpenAI(model="gpt-4o-mini")     agent_executor = create_react_agent(llm, tools, state_modifier=system_message)          example_query = "Fetch the top two posts. What are their titles?"          events = agent_executor.stream(         {"messages": [("user", example_query)]},         stream_mode="values",     )     for event in events:         event["messages"][-1].pretty_print()                     ================================[1m Human Message [0m=================================          Fetch the top two posts. What are their titles?     ==================================[1m Ai Message [0m==================================     Tool Calls:     requests_get (call_RV2SOyzCnV5h2sm4WPgG8fND)     Call ID: call_RV2SOyzCnV5h2sm4WPgG8fND     Args:         url: https://jsonplaceholder.typicode.com/posts?_limit=2     =================================[1m Tool Message [0m=================================     Name: requests_get          [     {         "userId": 1,         "id": 1,         "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",         "body": "quia et suscipit..."     },     {         "userId": 1,         "id": 2,         "title": "qui est esse",         "body": "est rerum tempore vitae..."     }     ]     ==================================[1m Ai Message [0m==================================          The titles of the top two posts are:     1. "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"     2. "qui est esse"     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allow\_dangerous\_requests _: bool_ _ = False_\#     

Allow dangerous requests. See documentation for details.

_param _requests\_wrapper _: [TextRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html#langchain_community.utilities.requests.TextRequestsWrapper "langchain_community.utilities.requests.TextRequestsWrapper")_ _\[Required\]_\#     

The requests wrapper.

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/toolkit.html#RequestsToolkit.get_tools)\#     

Return a list of tools.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using RequestsToolkit

  * [Requests Toolkit](https://python.langchain.com/docs/integrations/tools/requests/)

__On this page