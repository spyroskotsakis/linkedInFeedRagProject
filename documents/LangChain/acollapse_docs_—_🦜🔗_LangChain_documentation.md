# acollapse_docs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.acollapse_docs.html
**Word Count:** 110
**Links Count:** 197
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# acollapse\_docs\#

_async _langchain.chains.combine\_documents.reduce.acollapse\_docs\(

    _docs : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _combine\_document\_func : [AsyncCombineDocsProtocol](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol.html#langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol "langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol")_,     _\*\* kwargs: Any_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/combine_documents/reduce.html#acollapse_docs)\#     

Execute a collapse function on a set of documents and merge their metadatas.

Parameters:     

  * **docs** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A list of Documents to combine.

  * **combine\_document\_func** \([_AsyncCombineDocsProtocol_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol.html#langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol "langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol")\) – A function that takes in a list of Documents and optionally addition keyword parameters and combines them into a single string.

  * **\*\*kwargs** \(_Any_\) – Arbitrary additional keyword params to pass to the combine\_document\_func.

Returns:     

A single Document with the output of combine\_document\_func for the page content     

and the combined metadata’s of all the input documents. All metadata values are strings, and where there are overlapping keys across documents the values are joined by “, “.

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

Examples using acollapse\_docs

  * [\# Basic example \(short documents\)](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)

  * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

__On this page