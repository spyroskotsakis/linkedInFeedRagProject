# split_list_of_docs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.split_list_of_docs.html
**Word Count:** 72
**Links Count:** 195
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# split\_list\_of\_docs\#

langchain.chains.combine\_documents.reduce.split\_list\_of\_docs\(

    _docs : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _length\_func : Callable_,     _token\_max : int_,     _\*\* kwargs: Any_, \) → list\[list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/combine_documents/reduce.html#split_list_of_docs)\#     

Split Documents into subsets that each meet a cumulative length constraint.

Parameters:     

  * **docs** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The full list of Documents.

  * **length\_func** \(_Callable_\) – Function for computing the cumulative length of a set of Documents.

  * **token\_max** \(_int_\) – The maximum cumulative length of any subset of Documents.

  * **\*\*kwargs** \(_Any_\) – Arbitrary additional keyword params to pass to each call of the length\_func.

Returns:     

A List\[List\[Document\]\].

Return type:     

list\[list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]

Examples using split\_list\_of\_docs

  * [\# Basic example \(short documents\)](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)

  * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

__On this page