# PowerBIToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit.html
**Word Count:** 138
**Links Count:** 186
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# PowerBIToolkit\#

_class _langchain\_community.agent\_toolkits.powerbi.toolkit.PowerBIToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/powerbi/toolkit.html#PowerBIToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Power BI dataset.

_Security Note_ : This toolkit interacts with an external service.

> Control access to who can use this toolkit. >  > Make sure that the capabilities given by this toolkit to the calling code are appropriately scoped to the application. >  > See <https://python.langchain.com/docs/security> for more information.

Parameters:     

  * **powerbi** – The Power BI dataset.

  * **llm** – The language model to use.

  * **examples** – Optional. The examples for the prompt. Default is None.

  * **max\_iterations** – Optional. The maximum iterations to run. Default is 5.

  * **callback\_manager** – Optional. The callback manager. Default is None.

  * **output\_token\_limit** – The output token limit. Default is 4000.

  * **tiktoken\_model\_name** – Optional. The TikToken model name. Default is None.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _callback\_manager _: [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None_ _ = None_\#     

_param _examples _: str | None_ _ = None_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_ _\[Required\]_\#     

_param _max\_iterations _: int_ _ = 5_\#     

_param _output\_token\_limit _: int_ _ = 4000_\#     

_param _powerbi _: [PowerBIDataset](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html#langchain_community.utilities.powerbi.PowerBIDataset "langchain_community.utilities.powerbi.PowerBIDataset")_ _\[Required\]_\#     

_param _tiktoken\_model\_name _: str | None_ _ = None_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/powerbi/toolkit.html#PowerBIToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using PowerBIToolkit

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [PowerBI Toolkit](https://python.langchain.com/docs/integrations/tools/powerbi/)

__On this page