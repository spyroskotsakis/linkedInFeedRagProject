# ReadOnlySharedMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html
**Word Count:** 88
**Links Count:** 123
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# ReadOnlySharedMemory\#

_class _langchain.memory.readonly.ReadOnlySharedMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/readonly.html#ReadOnlySharedMemory)\#     

Bases: `BaseMemory`

Memory wrapper that is read-only and cannot be changed.

_param _memory _: BaseMemory_ _\[Required\]_\#     

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/readonly.html#ReadOnlySharedMemory.clear)\#     

Nothing to clear, got a memory like a vault.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/readonly.html#ReadOnlySharedMemory.load_memory_variables)\#     

Load memory variables from memory.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, str\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/readonly.html#ReadOnlySharedMemory.save_context)\#     

Nothing should be saved or changed

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: list\[str\]_\#     

Return memory variables.

Examples using ReadOnlySharedMemory

  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)

__On this page