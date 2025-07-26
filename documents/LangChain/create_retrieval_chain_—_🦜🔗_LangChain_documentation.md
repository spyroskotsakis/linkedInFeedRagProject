# create_retrieval_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval.create_retrieval_chain.html
**Word Count:** 198
**Links Count:** 209
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# create\_retrieval\_chain\#

langchain.chains.retrieval.create\_retrieval\_chain\(

    _retriever : [BaseRetriever](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever") | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[dict, list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]_,     _combine\_docs\_chain : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[dict\[str, Any\], str\]_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/retrieval.html#create_retrieval_chain)\#     

Create retrieval chain that retrieves documents and then passes them on.

Parameters:     

  * **retriever** \([_BaseRetriever_](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever") _|_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__dict_ _,__list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__\]_\) – Retriever-like object that returns list of documents. Should either be a subclass of BaseRetriever or a Runnable that returns a list of documents. If a subclass of BaseRetriever, then it is expected that an input key be passed in - this is what is will be used to pass into the retriever. If this is NOT a subclass of BaseRetriever, then all the inputs will be passed into this runnable, meaning that runnable should take a dictionary as input.

  * **combine\_docs\_chain** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__dict_ _\[__str_ _,__Any_ _\]__,__str_ _\]_\) – Runnable that takes inputs and produces a string output. The inputs to this will be any original inputs to this chain, a new context key with the retrieved documents, and chat\_history \(if not present in the inputs\) with a value of \[\] \(to easily enable conversational retrieval.

Returns:     

An LCEL Runnable. The Runnable return is a dictionary containing at the very least a context and answer key.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               # pip install -U langchain langchain-community          from langchain_community.chat_models import ChatOpenAI     from langchain.chains.combine_documents import create_stuff_documents_chain     from langchain.chains import create_retrieval_chain     from langchain import hub          retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")     llm = ChatOpenAI()     retriever = ...     combine_docs_chain = create_stuff_documents_chain(         llm, retrieval_qa_chat_prompt     )     retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)          retrieval_chain.invoke({"input": "..."})     

Examples using create\_retrieval\_chain

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/retrievers/ragatouille/)

__On this page