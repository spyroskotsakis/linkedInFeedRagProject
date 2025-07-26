# PlayWrightBrowserToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.playwright.toolkit.PlayWrightBrowserToolkit.html
**Word Count:** 223
**Links Count:** 177
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# PlayWrightBrowserToolkit\#

_class _langchain\_community.agent\_toolkits.playwright.toolkit.PlayWrightBrowserToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/playwright/toolkit.html#PlayWrightBrowserToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for PlayWright browser tools.

**Security Note** : This toolkit provides code to control a web-browser.

> Careful if exposing this toolkit to end-users. The tools in the toolkit are capable of navigating to arbitrary webpages, clicking on arbitrary elements, and extracting arbitrary text and hyperlinks from webpages. >  > Specifically, by default this toolkit allows navigating to: >  >   * Any URL \(including any internal network URLs\) >  >   * And local files >  > 

>  > If exposing to end-users, consider limiting network access to the server that hosts the agent; in addition, consider it is advised to create a custom NavigationTool wht an args\_schema that limits the URLs that can be navigated to \(e.g., only allow navigating to URLs that start with a particular prefix\). >  > Remember to scope permissions to the minimal permissions necessary for the application. If the default tool selection is not appropriate for the application, consider creating a custom toolkit with the appropriate tools. >  > See <https://python.langchain.com/docs/security> for more information.

Parameters:     

  * **sync\_browser** – Optional. The sync browser. Default is None.

  * **async\_browser** – Optional. The async browser. Default is None.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _async\_browser _: 'AsyncBrowser' | None_ _ = None_\#     

_param _sync\_browser _: 'SyncBrowser' | None_ _ = None_\#     

_classmethod _from\_browser\(

    _sync\_browser : SyncBrowser | None = None_,     _async\_browser : AsyncBrowser | None = None_, \) → PlayWrightBrowserToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/playwright/toolkit.html#PlayWrightBrowserToolkit.from_browser)\#     

Instantiate the toolkit.

Parameters:     

  * **sync\_browser** \(_Optional_ _\[__SyncBrowser_ _\]_\) – Optional. The sync browser. Default is None.

  * **async\_browser** \(_Optional_ _\[__AsyncBrowser_ _\]_\) – Optional. The async browser. Default is None.

Returns:     

The toolkit.

Return type:     

PlayWrightBrowserToolkit

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/playwright/toolkit.html#PlayWrightBrowserToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using PlayWrightBrowserToolkit

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [PlayWright Browser Toolkit](https://python.langchain.com/docs/integrations/tools/playwright/)

__On this page