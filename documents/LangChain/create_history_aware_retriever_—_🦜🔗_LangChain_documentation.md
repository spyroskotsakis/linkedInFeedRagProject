# create_history_aware_retriever — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.history_aware_retriever.create_history_aware_retriever.html
**Word Count:** 143
**Links Count:** 210
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# create\_history\_aware\_retriever\#

langchain.chains.history\_aware\_retriever.create\_history\_aware\_retriever\(

    _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | str\]_,     _retriever : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[str, list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Any, list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/history_aware_retriever.html#create_history_aware_retriever)\#     

Create a chain that takes conversation history and returns documents.

If there is no chat\_history, then the input is just passed directly to the retriever. If there is chat\_history, then the prompt and LLM will be used to generate a search query. That search query is then passed to the retriever.

Parameters:     

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[_[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") _|__str_ _|__Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__\]__,_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__str_ _\]_\) – Language model to use for generating a search term given chat history

  * **retriever** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__str_ _,__list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__\]_\) – RetrieverLike object that takes a string as input and outputs a list of Documents.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – The prompt used to generate the search query for the retriever.

Returns:     

An LCEL Runnable. The runnable input must take in input, and if there is chat history should take it in the form of chat\_history. The Runnable output is a list of Documents

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Any_ , list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]

Example               # pip install -U langchain langchain-community          from langchain_community.chat_models import ChatOpenAI     from langchain.chains import create_history_aware_retriever     from langchain import hub          rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")     llm = ChatOpenAI()     retriever = ...     chat_retriever_chain = create_history_aware_retriever(         llm, retriever, rephrase_prompt     )          chain.invoke({"input": "...", "chat_history": })     

Examples using create\_history\_aware\_retriever

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/)

__On this page