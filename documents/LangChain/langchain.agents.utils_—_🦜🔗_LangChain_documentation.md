# langchain.agents.utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/agents/utils.html
**Word Count:** 30
**Links Count:** 13
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# Source code for langchain.agents.utils               from collections.abc import Sequence          from langchain_core.tools import BaseTool                              [[docs]](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.utils.validate_tools_single_input.html#langchain.agents.utils.validate_tools_single_input)     def validate_tools_single_input(class_name: str, tools: Sequence[BaseTool]) -> None:         """Validate tools for single input.              Args:             class_name: Name of the class.             tools: List of tools to validate.              Raises:             ValueError: If a multi-input tool is found in tools.         """         for tool in tools:             if not tool.is_single_input:                 msg = f"{class_name} does not support multi-input tool {tool.name}."                 raise ValueError(msg)