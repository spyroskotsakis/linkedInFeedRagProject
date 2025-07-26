# AmadeusToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.amadeus.toolkit.AmadeusToolkit.html
**Word Count:** 73
**Links Count:** 171
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# AmadeusToolkit\#

_class _langchain\_community.agent\_toolkits.amadeus.toolkit.AmadeusToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/amadeus/toolkit.html#AmadeusToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Amadeus which offers APIs for travel.

Parameters:     

  * **client** – Optional. The Amadeus client. Default is None.

  * **llm** – Optional. The language model to use. Default is None.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Client_ _\[Optional\]_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/amadeus/toolkit.html#AmadeusToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using AmadeusToolkit

  * [Amadeus Toolkit](https://python.langchain.com/docs/integrations/tools/amadeus/)

__On this page