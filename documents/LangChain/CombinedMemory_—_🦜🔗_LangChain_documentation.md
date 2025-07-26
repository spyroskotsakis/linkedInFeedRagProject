# CombinedMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.combined.CombinedMemory.html
**Word Count:** 95
**Links Count:** 122
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# CombinedMemory\#

_class _langchain.memory.combined.CombinedMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/combined.html#CombinedMemory)\#     

Bases: `BaseMemory`

Combining multiple memories’ data together.

_param _memories _: list\[BaseMemory\]__\[Required\]_\#     

For tracking all the memories that should be accessed.

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/combined.html#CombinedMemory.clear)\#     

Clear context from this session for every memory.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/combined.html#CombinedMemory.load_memory_variables)\#     

Load all vars from sub-memories.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, str\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/combined.html#CombinedMemory.save_context)\#     

Save context from this session for every memory.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: list\[str\]_\#     

All the memory variables that this instance provides.

__On this page