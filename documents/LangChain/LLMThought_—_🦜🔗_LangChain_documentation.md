# LLMThought — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThought.html
**Word Count:** 131
**Links Count:** 233
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# LLMThought\#

_class _langchain\_community.callbacks.streamlit.streamlit\_callback\_handler.LLMThought\(

    _parent\_container : DeltaGenerator_,     _labeler : [LLMThoughtLabeler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler.html#langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler "langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler")_,     _expanded : bool_,     _collapse\_on\_complete : bool_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought)\#     

A thought in the LLM’s thought stream.

Initialize the LLMThought.

Parameters:     

  * **parent\_container** \(_DeltaGenerator_\) – The container we’re writing into.

  * **labeler** \([_LLMThoughtLabeler_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler.html#langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler "langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler")\) – The labeler to use for this thought.

  * **expanded** \(_bool_\) – Whether the thought should be expanded by default.

  * **collapse\_on\_complete** \(_bool_\) – Whether the thought should be collapsed.

Attributes

`container` | The container we're writing into.   ---|---   `last_tool` | The last tool executed by this thought      Methods

`__init__`\(parent\_container, labeler, ...\) | Initialize the LLMThought.   ---|---   `clear`\(\) | Remove the thought from the screen.   `complete`\(\[final\_label\]\) | Finish the thought.   `on_agent_action`\(action\[, color\]\) |    `on_llm_end`\(response, \*\*kwargs\) |    `on_llm_error`\(error, \*\*kwargs\) |    `on_llm_new_token`\(token, \*\*kwargs\) |    `on_llm_start`\(serialized, prompts\) |    `on_tool_end`\(output\[, color, ...\]\) |    `on_tool_error`\(error, \*\*kwargs\) |    `on_tool_start`\(serialized, input\_str, \*\*kwargs\) |       \_\_init\_\_\(

    _parent\_container : DeltaGenerator_,     _labeler : [LLMThoughtLabeler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler.html#langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler "langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler")_,     _expanded : bool_,     _collapse\_on\_complete : bool_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.__init__)\#     

Initialize the LLMThought.

Parameters:     

  * **parent\_container** \(_DeltaGenerator_\) – The container we’re writing into.

  * **labeler** \([_LLMThoughtLabeler_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler.html#langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler "langchain_community.callbacks.streamlit.streamlit_callback_handler.LLMThoughtLabeler")\) – The labeler to use for this thought.

  * **expanded** \(_bool_\) – Whether the thought should be expanded by default.

  * **collapse\_on\_complete** \(_bool_\) – Whether the thought should be collapsed.

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.clear)\#     

Remove the thought from the screen. A cleared thought can’t be reused.

Return type:     

None

complete\(_final\_label : str | None = None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.complete)\#     

Finish the thought.

Parameters:     

**final\_label** \(_str_ _|__None_\)

Return type:     

None

on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _color : str | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_agent_action)\#     

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\)

  * **color** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

on\_llm\_end\(

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_llm_end)\#     

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_llm_error)\#     

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_new\_token\(

    _token : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_llm_new_token)\#     

Parameters:     

  * **token** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_start\(

    _serialized : Dict\[str, Any\]_,     _prompts : List\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_llm_start)\#     

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **prompts** \(_List_ _\[__str_ _\]_\)

Return type:     

None

on\_tool\_end\(

    _output : Any_,     _color : str | None = None_,     _observation\_prefix : str | None = None_,     _llm\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_tool_end)\#     

Parameters:     

  * **output** \(_Any_\)

  * **color** \(_str_ _|__None_\)

  * **observation\_prefix** \(_str_ _|__None_\)

  * **llm\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_tool_error)\#     

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_start\(

    _serialized : Dict\[str, Any\]_,     _input\_str : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#LLMThought.on_tool_start)\#     

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **input\_str** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

__On this page