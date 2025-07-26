# create_stuff_documents_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html
**Word Count:** 244
**Links Count:** 220
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# create\_stuff\_documents\_chain\#

langchain.chains.combine\_documents.stuff.create\_stuff\_documents\_chain\(

    _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | str\]_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_,     _\*_ ,     _output\_parser : [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | None = None_,     _document\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _document\_separator : str = '\n\n'_,     _document\_variable\_name : str = 'context'_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[dict\[str, Any\], Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/combine_documents/stuff.html#create_stuff_documents_chain)\#     

Create a chain for passing a list of Documents to a model.

Parameters:     

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[_[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") _|__str_ _|__Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__\]__,_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__str_ _\]_\) – Language model.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – Prompt template. Must contain input variable “context” \(override by setting document\_variable\), which will be used for passing in the formatted documents.

  * **output\_parser** \([_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") _|__None_\) – Output parser. Defaults to StrOutputParser.

  * **document\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – Prompt used for formatting each document into a string. Input variables can be “page\_content” or any metadata keys that are in all documents. “page\_content” will automatically retrieve the Document.page\_content, and all other inputs variables will be automatically retrieved from the Document.metadata dictionary. Default to a prompt that only contains Document.page\_content.

  * **document\_separator** \(_str_\) – String separator to use between formatted document strings.

  * **document\_variable\_name** \(_str_\) – Variable name to use for the formatted documents in the prompt. Defaults to “context”.

Returns:     

An LCEL Runnable. The input is a dictionary that must have a “context” key that maps to a List\[Document\], and any other input variables expected in the prompt. The Runnable return type depends on output\_parser used.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[dict\[str, _Any_\], _Any_\]

Example               # pip install -U langchain langchain-community          from langchain_community.chat_models import ChatOpenAI     from langchain_core.documents import Document     from langchain_core.prompts import ChatPromptTemplate     from langchain.chains.combine_documents import create_stuff_documents_chain          prompt = ChatPromptTemplate.from_messages(         [("system", "What are everyone's favorite colors:\n\n{context}")]     )     llm = ChatOpenAI(model="gpt-3.5-turbo")     chain = create_stuff_documents_chain(llm, prompt)          docs = [         Document(page_content="Jesse loves red but not yellow"),         Document(page_content = "Jamal loves green but not as much as he loves orange")     ]          chain.invoke({"context": docs})     

Examples using create\_stuff\_documents\_chain

  * [\# Example](https://python.langchain.com/docs/versions/migrating_chains/stuff_docs_chain/)

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to reorder retrieved results to mitigate the “lost in the middle” effect](https://python.langchain.com/docs/how_to/long_context_reorder/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to summarize text in a single LLM call](https://python.langchain.com/docs/how_to/summarize_stuff/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/retrievers/ragatouille/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)