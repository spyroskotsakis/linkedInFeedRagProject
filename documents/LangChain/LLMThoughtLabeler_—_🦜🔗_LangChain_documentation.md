# LLMThoughtLabeler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler.html
**Word Count:** 170
**Links Count:** 199
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# LLMThoughtLabeler\#

_class _langchain\_community.callbacks.streamlit.streamlit\_callback\_handler.LLMThoughtLabeler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThoughtLabeler)\#     

Generates markdown labels for LLMThought containers. Pass a custom subclass of this to StreamlitCallbackHandler to override its default labeling logic.

Methods

`get_final_agent_thought_label`\(\) | Return the markdown label for the agent's final thought - the "Now I have the answer" thought, that doesn't involve a tool.   ---|---   `get_history_label`\(\) | Return a markdown label for the special 'history' container that contains overflow thoughts.   `get_initial_label`\(\) | Return the markdown label for a new LLMThought that doesn't have an associated tool yet.   `get_tool_label`\(tool, is\_complete\) | Return the label for an LLMThought that has an associated tool.      _static _get\_final\_agent\_thought\_label\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThoughtLabeler.get_final_agent_thought_label)\#     

Return the markdown label for the agent’s final thought - the “Now I have the answer” thought, that doesn’t involve a tool.

Return type:     

str

_static _get\_history\_label\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThoughtLabeler.get_history_label)\#     

Return a markdown label for the special ‘history’ container that contains overflow thoughts.

Return type:     

str

_static _get\_initial\_label\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThoughtLabeler.get_initial_label)\#     

Return the markdown label for a new LLMThought that doesn’t have an associated tool yet.

Return type:     

str

_static _get\_tool\_label\(

    _tool : [ToolRecord](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord.html#langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord "langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord")_,     _is\_complete : bool_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThoughtLabeler.get_tool_label)\#     

Return the label for an LLMThought that has an associated tool.

Parameters:     

  * **tool** \([_ToolRecord_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord.html#langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord "langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord")\) – The tool’s ToolRecord

  * **is\_complete** \(_bool_\) – True if the thought is complete; False if the thought is still receiving input.

Return type:     

The markdown label for the thought’s container.

__On this page