# GmailToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.gmail.toolkit.GmailToolkit.html
**Word Count:** 262
**Links Count:** 170
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# GmailToolkit\#

_class _langchain\_community.agent\_toolkits.gmail.toolkit.GmailToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/gmail/toolkit.html#GmailToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Gmail.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by reading, creating, updating, deleting data associated with this service.

For example, this toolkit can be used to send emails on behalf of the associated account.

See <https://python.langchain.com/docs/security> for more information.

Setup:     

You will need a Google credentials.json file to use this toolkit. See instructions here: <https://python.langchain.com/docs/integrations/tools/gmail/#setup>

Key init args:     

api\_resource: Optional. The Google API resource. Default is None.

Instantiate:                    from langchain_google_community import GmailToolkit          toolkit = GmailToolkit()     

Tools:                    toolkit.get_tools()                    [GmailCreateDraft(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),     GmailSendMessage(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),     GmailSearch(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),     GmailGetMessage(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),     GmailGetThread(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>)]     

Use within an agent:                    from langchain_openai import ChatOpenAI     from langgraph.prebuilt import create_react_agent          llm = ChatOpenAI(model="gpt-4o-mini")          agent_executor = create_react_agent(llm, tools)          example_query = "Draft an email to fake@fake.com thanking them for coffee."          events = agent_executor.stream(         {"messages": [("user", example_query)]},         stream_mode="values",     )     for event in events:         event["messages"][-1].pretty_print()                     ================================[1m Human Message [0m=================================          Draft an email to fake@fake.com thanking them for coffee.     ==================================[1m Ai Message [0m==================================     Tool Calls:     create_gmail_draft (call_slGkYKZKA6h3Mf1CraUBzs6M)     Call ID: call_slGkYKZKA6h3Mf1CraUBzs6M     Args:         message: Dear Fake,          I wanted to take a moment to thank you for the coffee yesterday. It was a pleasure catching up with you. Let's do it again soon!          Best regards,     [Your Name]         to: ['fake@fake.com']         subject: Thank You for the Coffee     =================================[1m Tool Message [0m=================================     Name: create_gmail_draft          Draft created. Draft Id: r-7233782721440261513     ==================================[1m Ai Message [0m==================================          I have drafted an email to fake@fake.com thanking them for the coffee. You can review and send it from your email draft with the subject "Thank You for the Coffee".     

Parameters:     

**api\_resource** – Optional. The Google API resource. Default is None.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_resource _: [Resource](https://python.langchain.com/api_reference/google_community/gmail/langchain_google_community.gmail.search.Resource.html#langchain_google_community.gmail.search.Resource "langchain_google_community.gmail.search.Resource")_ _\[Optional\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/gmail/toolkit.html#GmailToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

__On this page