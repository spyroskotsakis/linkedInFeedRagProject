# FileManagementToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.file_management.toolkit.FileManagementToolkit.html
**Word Count:** 224
**Links Count:** 171
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# FileManagementToolkit\#

_class _langchain\_community.agent\_toolkits.file\_management.toolkit.FileManagementToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/file_management/toolkit.html#FileManagementToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with local files.

_Security Notice_ : This toolkit provides methods to interact with local files.     

If providing this toolkit to an agent on an LLM, ensure you scope the agent’s permissions to only include the necessary permissions to perform the desired operations.

By **default** the agent will have access to all files within the root dir and will be able to Copy, Delete, Move, Read, Write and List files in that directory.

Consider the following: \- Limit access to particular directories using root\_dir. \- Use filesystem permissions to restrict access and permissions to only

> the files and directories required by the agent.

  * Limit the tools available to the agent to only the file operations necessary for the agent’s intended use.

  * Sandbox the agent by running it in a container.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

  * **root\_dir** – Optional. The root directory to perform file operations. If not provided, file operations are performed relative to the current working directory.

  * **selected\_tools** – Optional. The tools to include in the toolkit. If not provided, all tools are included.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _root\_dir _: str | None_ _ = None_\#     

If specified, all file operations are made relative to root\_dir.

_param _selected\_tools _: List\[str\] | None_ _ = None_\#     

If provided, only provide the selected tools. Defaults to all.

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/file_management/toolkit.html#FileManagementToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using FileManagementToolkit

  * [File System](https://python.langchain.com/docs/integrations/tools/filesystem/)

__On this page