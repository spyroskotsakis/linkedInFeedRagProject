# nodes_to_documents — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.nodes_to_documents.html
**Word Count:** 34
**Links Count:** 122
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# nodes\_to\_documents\#

langchain\_community.graph\_vectorstores.base.nodes\_to\_documents\(

    _nodes : Iterable\[[Node](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node")\]_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#nodes_to_documents)\#     

Deprecated since version 0.3.21: See <https://datastax.github.io/graph-rag/guide/migration/#from-langchain-graphvectorstore> for migration instructions. It will be removed in langchain-community==0.5.

Convert nodes to documents.

Parameters:     

**nodes** \(_Iterable_ _\[_[_Node_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") _\]_\) – The nodes to convert to documents.

Returns:     

The documents generated from the nodes.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page