# langchain_community.tools.graphql.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/graphql/tool.html
**Word Count:** 86
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:23
**Status:** completed

---

# Source code for langchain\_community.tools.graphql.tool               import json     from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool     from pydantic import ConfigDict          from langchain_community.utilities.graphql import GraphQLAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.graphql.tool.BaseGraphQLTool.html#langchain_community.tools.graphql.tool.BaseGraphQLTool)     class BaseGraphQLTool(BaseTool):         """Base tool for querying a GraphQL API."""              graphql_wrapper: GraphQLAPIWrapper              name: str = "query_graphql"         description: str = """\         Input to this tool is a detailed and correct GraphQL query, output is a result from the API.         If the query is not correct, an error message will be returned.         If an error is returned with 'Bad request' in it, rewrite the query and try again.         If an error is returned with 'Unauthorized' in it, do not try again, but tell the user to change their authentication.              Example Input: query {{ allUsers {{ id, name, email }} }}\         """  # noqa: E501              model_config = ConfigDict(             arbitrary_types_allowed=True,         )              def _run(             self,             tool_input: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             result = self.graphql_wrapper.run(tool_input)             return json.dumps(result, indent=2)