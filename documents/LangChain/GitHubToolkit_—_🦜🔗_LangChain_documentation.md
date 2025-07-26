# GitHubToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.GitHubToolkit.html
**Word Count:** 309
**Links Count:** 178
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# GitHubToolkit\#

_class _langchain\_community.agent\_toolkits.github.toolkit.GitHubToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#GitHubToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

GitHub Toolkit.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by creating, deleting, or updating, reading underlying data.

For example, this toolkit can be used to create issues, pull requests, and comments on GitHub.

See \[Security\]\(<https://python.langchain.com/docs/security>\) for more information.

Setup:     

See detailed installation instructions here: <https://python.langchain.com/docs/integrations/tools/github/#installation>

You will need to install `pygithub` and set the following environment variables:               pip install -U pygithub     export GITHUB_APP_ID="your-app-id"     export GITHUB_APP_PRIVATE_KEY="path-to-private-key"     export GITHUB_REPOSITORY="your-github-repository"     

Instantiate:                    from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit     from langchain_community.utilities.github import GitHubAPIWrapper          github = GitHubAPIWrapper()     toolkit = GitHubToolkit.from_github_api_wrapper(github)     

Tools:                    tools = toolkit.get_tools()     for tool in tools:         print(tool.name)                    Get Issues     Get Issue     Comment on Issue     List open pull requests (PRs)     Get Pull Request     Overview of files included in PR     Create Pull Request     List Pull Requests' Files     Create File     Read File     Update File     Delete File     Overview of existing files in Main branch     Overview of files in current working branch     List branches in this repository     Set active branch     Create a new branch     Get files from a directory     Search issues and pull requests     Search code     Create review request     

Include release tools:     

By default, the toolkit does not include release-related tools. You can include them by setting `include_release_tools=True` when initializing the toolkit:               toolkit = GitHubToolkit.from_github_api_wrapper(         github, include_release_tools=True     )     

Setting `include_release_tools=True` will include the following tools:               Get latest release     Get releases     Get release     

Use within an agent:                    from langchain_openai import ChatOpenAI     from langgraph.prebuilt import create_react_agent          # Select example tool     tools = [tool for tool in toolkit.get_tools() if tool.name == "Get Issue"]     assert len(tools) == 1     tools[0].name = "get_issue"          llm = ChatOpenAI(model="gpt-4o-mini")     agent_executor = create_react_agent(llm, tools)          example_query = "What is the title of issue 24888?"          events = agent_executor.stream(         {"messages": [("user", example_query)]},         stream_mode="values",     )     for event in events:         event["messages"][-1].pretty_print()                     ================================[1m Human Message [0m=================================          What is the title of issue 24888?     ==================================[1m Ai Message [0m==================================     Tool Calls:     get_issue (call_iSYJVaM7uchfNHOMJoVPQsOi)     Call ID: call_iSYJVaM7uchfNHOMJoVPQsOi     Args:         issue_number: 24888     =================================[1m Tool Message [0m=================================     Name: get_issue          {"number": 24888, "title": "Standardize KV-Store Docs", "body": "..."     ==================================[1m Ai Message [0m==================================          The title of issue 24888 is "Standardize KV-Store Docs".     

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_github\_api\_wrapper\(

    _github\_api\_wrapper : [GitHubAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.github.GitHubAPIWrapper.html#langchain_community.utilities.github.GitHubAPIWrapper "langchain_community.utilities.github.GitHubAPIWrapper")_,     _include\_release\_tools : bool = False_, \) → GitHubToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#GitHubToolkit.from_github_api_wrapper)\#     

Create a GitHubToolkit from a GitHubAPIWrapper.

Parameters:     

  * **github\_api\_wrapper** \([_GitHubAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.github.GitHubAPIWrapper.html#langchain_community.utilities.github.GitHubAPIWrapper "langchain_community.utilities.github.GitHubAPIWrapper")\) – GitHubAPIWrapper. The GitHub API wrapper.

  * **include\_release\_tools** \(_bool_\) – bool. Whether to include release-related tools. Defaults to False.

Returns:     

GitHubToolkit. The GitHub toolkit.

Return type:     

_GitHubToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#GitHubToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using GitHubToolkit

  * [Github Toolkit](https://python.langchain.com/docs/integrations/tools/github/)

__On this page