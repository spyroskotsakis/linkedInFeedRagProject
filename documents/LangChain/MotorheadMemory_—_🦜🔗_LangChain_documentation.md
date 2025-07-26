# MotorheadMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/memory/langchain_community.memory.motorhead_memory.MotorheadMemory.html
**Word Count:** 89
**Links Count:** 147
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# MotorheadMemory\#

_class _langchain\_community.memory.motorhead\_memory.MotorheadMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/motorhead_memory.html#MotorheadMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")

Chat message memory backed by Motorhead service.

_param _api\_key _: str | None_ _ = None_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _client\_id _: str | None_ _ = None_\#     

_param _context _: str | None_ _ = None_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _memory\_key _: str_ _ = 'history'_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _return\_messages _: bool_ _ = False_\#     

_param _session\_id _: str_ _\[Required\]_\#     

_param _timeout _: int_ _ = 3000_\#     

_param _url _: str_ _ = 'https://api.getmetal.io/v1/motorhead'_\#     

_async _aclear\(\) → None\#     

Clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Async return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

dict\[str, _Any_\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None\#     

Clear memory contents.

Return type:     

None

delete\_session\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/motorhead_memory.html#MotorheadMemory.delete_session)\#     

Delete a session

Return type:     

None

_async _init\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/motorhead_memory.html#MotorheadMemory.init)\#     

Return type:     

None

load\_memory\_variables\(

    _values : Dict\[str, Any\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/motorhead_memory.html#MotorheadMemory.load_memory_variables)\#     

Return key-value pairs given the text input to the chain.

Parameters:     

  * **inputs** – The inputs to the chain.

  * **values** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Returns:     

A dictionary of key-value pairs.

Return type:     

_Dict_\[str, _Any_\]

save\_context\(

    _inputs : Dict\[str, Any\]_,     _outputs : Dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/motorhead_memory.html#MotorheadMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: List\[str\]_\#     

The string keys this memory class will add to chain inputs.

Examples using MotorheadMemory

  * [Motörhead](https://python.langchain.com/docs/integrations/memory/motorhead_memory/)

__On this page