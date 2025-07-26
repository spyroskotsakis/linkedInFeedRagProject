# validate_tools_single_input — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.utils.validate_tools_single_input.html
**Word Count:** 31
**Links Count:** 161
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# validate\_tools\_single\_input\#

langchain.agents.utils.validate\_tools\_single\_input\(

    _class\_name : str_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/utils.html#validate_tools_single_input)\#     

Validate tools for single input.

Parameters:     

  * **class\_name** \(_str_\) – Name of the class.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – List of tools to validate.

Raises:     

**ValueError** – If a multi-input tool is found in tools.

Return type:     

None

__On this page