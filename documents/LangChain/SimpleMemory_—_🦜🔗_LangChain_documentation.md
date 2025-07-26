# SimpleMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html
**Word Count:** 119
**Links Count:** 122
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# SimpleMemory\#

_class _langchain.memory.simple.SimpleMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/simple.html#SimpleMemory)\#     

Bases: `BaseMemory`

Simple memory for storing context or other information that shouldn’t ever change between prompts.

_param _memories _: dict\[str, Any\]__ = \{\}_\#     

_async _aclear\(\) → None\#     

Async clear memory contents.

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

Async save the context of this chain run to memory.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\) – The outputs of the chain.

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/simple.html#SimpleMemory.clear)\#     

Nothing to clear, got a memory like a vault.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/simple.html#SimpleMemory.load_memory_variables)\#     

Return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

dict\[str, str\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/simple.html#SimpleMemory.save_context)\#     

Nothing should be saved or changed, my memory is set in stone.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: list\[str\]_\#     

The string keys this memory class will add to chain inputs.

__On this page