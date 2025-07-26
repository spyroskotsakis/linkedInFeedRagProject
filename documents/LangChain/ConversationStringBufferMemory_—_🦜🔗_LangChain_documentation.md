# ConversationStringBufferMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationStringBufferMemory.html
**Word Count:** 129
**Links Count:** 137
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# ConversationStringBufferMemory\#

_class _langchain.memory.buffer.ConversationStringBufferMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory)\#     

Bases: `BaseMemory`

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

A basic memory implementation that simply stores the conversation history.

This stores the entire conversation history in memory without any additional processing.

Equivalent to ConversationBufferMemory but tailored more specifically for string-based conversations rather than chat models.

Note that additional processing may be required in some situations when the conversation history is too large to fit in the context window of the model.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

Prefix to use for AI generated responses.

_param _buffer _: str_ _ = ''_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _output\_key _: str | None_ _ = None_\#     

_classmethod _validate\_chains\(

    _values : dict_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.validate_chains)\#     

Validate that return messages is not True.

Parameters:     

**values** \(_dict_\)

Return type:     

dict

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.aclear)\#     

Async clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.aload_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, str\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.asave_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.clear)\#     

Clear memory contents.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.load_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, str\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationStringBufferMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: list\[str\]_\#     

Will always return list of memory variables. :meta private:

__On this page