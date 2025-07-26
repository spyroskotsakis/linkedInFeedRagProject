# documents_to_networkx — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.networkx.documents_to_networkx.html
**Word Count:** 54
**Links Count:** 119
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# documents\_to\_networkx\#

langchain\_community.graph\_vectorstores.networkx.documents\_to\_networkx\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _tag\_nodes : bool = True_, \) → nx.DiGraph[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/networkx.html#documents_to_networkx)\#     

Return the networkx directed graph corresponding to the documents.

Parameters:     

  * **documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The documents to convenrt to networkx.

  * **tag\_nodes** \(_bool_\) – If True, each tag will be rendered as a node, with edges to/from the corresponding documents. If False, edges will be between documents, with a label corresponding to the tag\(s\) connecting them.

Return type:     

nx.DiGraph

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)