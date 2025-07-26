# collapse_docs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.collapse_docs.html
**Word Count:** 98
**Links Count:** 194
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# collapse\_docs\#

langchain.chains.combine\_documents.reduce.collapse\_docs\(

    _docs : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _combine\_document\_func : [CombineDocsProtocol](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.CombineDocsProtocol.html#langchain.chains.combine_documents.reduce.CombineDocsProtocol "langchain.chains.combine_documents.reduce.CombineDocsProtocol")_,     _\*\* kwargs: Any_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/combine_documents/reduce.html#collapse_docs)\#     

Execute a collapse function on a set of documents and merge their metadatas.

Parameters:     

  * **docs** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A list of Documents to combine.

  * **combine\_document\_func** \([_CombineDocsProtocol_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.CombineDocsProtocol.html#langchain.chains.combine_documents.reduce.CombineDocsProtocol "langchain.chains.combine_documents.reduce.CombineDocsProtocol")\) – A function that takes in a list of Documents and optionally addition keyword parameters and combines them into a single string.

  * **\*\*kwargs** \(_Any_\) – Arbitrary additional keyword params to pass to the combine\_document\_func.

Returns:     

A single Document with the output of combine\_document\_func for the page content     

and the combined metadata’s of all the input documents. All metadata values are strings, and where there are overlapping keys across documents the values are joined by “, “.

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

__On this page