# SlackToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.slack.toolkit.SlackToolkit.html
**Word Count:** 122
**Links Count:** 169
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# SlackToolkit\#

_class _langchain\_community.agent\_toolkits.slack.toolkit.SlackToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/slack/toolkit.html#SlackToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Slack.

Parameters:     

**client** – The Slack client.

Setup:     

Install `slack_sdk` and set environment variable `SLACK_USER_TOKEN`.               pip install -U slack_sdk     export SLACK_USER_TOKEN="your-user-token"     

Key init args:     

client: slack\_sdk.WebClient     

The Slack client.

Instantiate:                    from langchain_community.agent_toolkits import SlackToolkit          toolkit = SlackToolkit()     

Tools:                    tools = toolkit.get_tools()     tools                    [SlackGetChannel(client=<slack_sdk.web.client.WebClient object at 0x113caa8c0>),     SlackGetMessage(client=<slack_sdk.web.client.WebClient object at 0x113caa4d0>),     SlackScheduleMessage(client=<slack_sdk.web.client.WebClient object at 0x113caa440>),     SlackSendMessage(client=<slack_sdk.web.client.WebClient object at 0x113caa410>)]     

Use within an agent:                    from langchain_openai import ChatOpenAI     from langgraph.prebuilt import create_react_agent          llm = ChatOpenAI(model="gpt-4o-mini")     agent_executor = create_react_agent(llm, tools)          example_query = "When was the #general channel created?"          events = agent_executor.stream(         {"messages": [("user", example_query)]},         stream_mode="values",     )     for event in events:         message = event["messages"][-1]         if message.type != "tool":  # mask sensitive information             event["messages"][-1].pretty_print()                     ================================[1m Human Message [0m=================================          When was the #general channel created?     ==================================[1m Ai Message [0m==================================     Tool Calls:     get_channelid_name_dict (call_NXDkALjoOx97uF1v0CoZTqtJ)     Call ID: call_NXDkALjoOx97uF1v0CoZTqtJ     Args:     ==================================[1m Ai Message [0m==================================          The #general channel was created on timestamp 1671043305.     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: WebClient_ _\[Optional\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/slack/toolkit.html#SlackToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using SlackToolkit

  * [Slack](https://python.langchain.com/docs/integrations/providers/slack/)

  * [Slack Toolkit](https://python.langchain.com/docs/integrations/tools/slack/)

__On this page