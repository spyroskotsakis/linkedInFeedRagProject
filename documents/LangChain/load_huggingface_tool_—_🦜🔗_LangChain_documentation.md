# load_huggingface_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_huggingface_tool.html
**Word Count:** 65
**Links Count:** 163
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# load\_huggingface\_tool\#

langchain\_community.agent\_toolkits.load\_tools.load\_huggingface\_tool\(

    _task\_or\_repo\_id : str_,     _model\_repo\_id : str | None = None_,     _token : str | None = None_,     _remote : bool = False_,     _\*\* kwargs: Any_, \) → [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/load_tools.html#load_huggingface_tool)\#     

Loads a tool from the HuggingFace Hub.

Parameters:     

  * **task\_or\_repo\_id** \(_str_\) – Task or model repo id.

  * **model\_repo\_id** \(_str_ _|__None_\) – Optional model repo id. Defaults to None.

  * **token** \(_str_ _|__None_\) – Optional token. Defaults to None.

  * **remote** \(_bool_\) – Optional remote. Defaults to False.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

A tool.

Raises:     

  * **ImportError** – If the required libraries are not installed.

  * **NotImplementedError** – If multimodal outputs or inputs are not supported.

Return type:     

[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")

Examples using load\_huggingface\_tool

  * [Hugging Face](https://python.langchain.com/docs/integrations/providers/huggingface/)

  * [HuggingFace Hub Tools](https://python.langchain.com/docs/integrations/tools/huggingface_tools/)

__On this page