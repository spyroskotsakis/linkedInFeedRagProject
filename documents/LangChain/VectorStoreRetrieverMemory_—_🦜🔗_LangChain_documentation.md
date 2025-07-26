# VectorStoreRetrieverMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore.VectorStoreRetrieverMemory.html
**Word Count:** 124
**Links Count:** 139
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# VectorStoreRetrieverMemory\#

_class _langchain.memory.vectorstore.VectorStoreRetrieverMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory)\#     

Bases: `BaseMemory`

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Store the conversation history in a vector store and retrieves the relevant parts of past conversation based on the input.

_param _exclude\_input\_keys _: Sequence\[str\]__\[Optional\]_\#     

Input keys to exclude in addition to memory key when constructing the document

_param _input\_key _: str | None_ _ = None_\#     

Key name to index the inputs to load\_memory\_variables.

_param _memory\_key _: str_ _ = 'history'_\#     

Key name to locate the memories in the result of load\_memory\_variables.

_param _retriever _: [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_ _\[Required\]_\#     

VectorStoreRetriever object to connect to.

_param _return\_docs _: bool_ _ = False_\#     

Whether or not to return the result of querying the database directly.

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory.aclear)\#     

Nothing to clear.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory.aload_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | str\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory.asave_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory.clear)\#     

Nothing to clear.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory.load_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | str\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore.html#VectorStoreRetrieverMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: list\[str\]_\#     

The list of keys emitted from the load\_memory\_variables method.

__On this page