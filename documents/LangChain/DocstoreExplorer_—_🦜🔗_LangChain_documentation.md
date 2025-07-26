# DocstoreExplorer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.react.base.DocstoreExplorer.html
**Word Count:** 141
**Links Count:** 178
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# DocstoreExplorer\#

_class _langchain.agents.react.base.DocstoreExplorer\(_docstore : [Docstore](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/react/base.html#DocstoreExplorer)\#     

Deprecated since version 0.1.0: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) as well as guides for [Migrating from AgentExecutor](https://python.langchain.com/docs/how_to/migrate_agent/) and LangGraph’s [Pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). It will not be removed until langchain==1.0.

Class to assist with exploration of a document store.

Initialize with a docstore, and set initial document to None.

Methods

`__init__`\(docstore\) | Initialize with a docstore, and set initial document to None.   ---|---   `lookup`\(term\) | Lookup a term in document \(if saved\).   `search`\(term\) | Search for a term in the docstore, and if found save.      Parameters:     

**docstore** \([_Docstore_](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")\)

\_\_init\_\_\(_docstore : [Docstore](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/react/base.html#DocstoreExplorer.__init__)\#     

Initialize with a docstore, and set initial document to None.

Parameters:     

**docstore** \([_Docstore_](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")\)

lookup\(_term : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/react/base.html#DocstoreExplorer.lookup)\#     

Lookup a term in document \(if saved\).

Parameters:     

**term** \(_str_\)

Return type:     

str

search\(_term : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/react/base.html#DocstoreExplorer.search)\#     

Search for a term in the docstore, and if found save.

Parameters:     

**term** \(_str_\)

Return type:     

str

__On this page