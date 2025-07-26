# retrievers — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/retrievers.html
**Word Count:** 69
**Links Count:** 98
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# `retrievers`\#

**Retriever** class returns Documents given a text **query**.

It is more general than a vector store. A retriever does not need to be able to store documents, only to return \(or retrieve\) it. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.

**Class hierarchy:**               BaseRetriever --> <name>Retriever  # Examples: ArxivRetriever, MergerRetriever     

**Main helpers:**               RetrieverInput, RetrieverOutput, RetrieverLike, RetrieverOutputLike,     Document, Serializable, Callbacks,     CallbackManagerForRetrieverRun, AsyncCallbackManagerForRetrieverRun     

**Classes**

[`retrievers.BaseRetriever`](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever") | Abstract base class for a Document retrieval system.   ---|---   [`retrievers.LangSmithRetrieverParams`](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.LangSmithRetrieverParams.html#langchain_core.retrievers.LangSmithRetrieverParams "langchain_core.retrievers.LangSmithRetrieverParams") | LangSmith parameters for tracing.