# format_xml — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.xml.format_xml.html
**Word Count:** 42
**Links Count:** 161
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# format\_xml\#

langchain.agents.format\_scratchpad.xml.format\_xml\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _\*_ ,     _escape\_format : Literal\['minimal'\] | None = 'minimal'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/xml.html#format_xml)\#     

Format the intermediate steps as XML.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – The intermediate steps.

  * **escape\_format** \(_Literal_ _\[__'minimal'__\]__|__None_\) – The escaping format to use. Currently only ‘minimal’ is supported, which replaces XML tags with custom delimiters to prevent conflicts.

Returns:     

The intermediate steps as XML.

Return type:     

str

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)