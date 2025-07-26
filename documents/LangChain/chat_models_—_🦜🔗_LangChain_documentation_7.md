# chat_models — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/chat_models.html
**Word Count:** 65
**Links Count:** 101
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# `chat_models`\#

**Chat Models** are a variation on language models.

While Chat Models use language models under the hood, the interface they expose is a bit different. Rather than expose a “text in, text out” API, they expose an interface where “chat messages” are the inputs and outputs.

**Class hierarchy:**               BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm     

**Main helpers:**               AIMessage, BaseMessage, HumanMessage     

**Classes**

[`chat_models.llm_wrapper.ChatWrapper`](https://python.langchain.com/api_reference/experimental/chat_models/langchain_experimental.chat_models.llm_wrapper.ChatWrapper.html#langchain_experimental.chat_models.llm_wrapper.ChatWrapper "langchain_experimental.chat_models.llm_wrapper.ChatWrapper") | Wrapper for chat LLMs.   ---|---   [`chat_models.llm_wrapper.Llama2Chat`](https://python.langchain.com/api_reference/experimental/chat_models/langchain_experimental.chat_models.llm_wrapper.Llama2Chat.html#langchain_experimental.chat_models.llm_wrapper.Llama2Chat "langchain_experimental.chat_models.llm_wrapper.Llama2Chat") | Wrapper for Llama-2-chat model.   [`chat_models.llm_wrapper.Mixtral`](https://python.langchain.com/api_reference/experimental/chat_models/langchain_experimental.chat_models.llm_wrapper.Mixtral.html#langchain_experimental.chat_models.llm_wrapper.Mixtral "langchain_experimental.chat_models.llm_wrapper.Mixtral") | See <https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1#instruction-format>   [`chat_models.llm_wrapper.Orca`](https://python.langchain.com/api_reference/experimental/chat_models/langchain_experimental.chat_models.llm_wrapper.Orca.html#langchain_experimental.chat_models.llm_wrapper.Orca "langchain_experimental.chat_models.llm_wrapper.Orca") | Wrapper for Orca-style models.   [`chat_models.llm_wrapper.Vicuna`](https://python.langchain.com/api_reference/experimental/chat_models/langchain_experimental.chat_models.llm_wrapper.Vicuna.html#langchain_experimental.chat_models.llm_wrapper.Vicuna "langchain_experimental.chat_models.llm_wrapper.Vicuna") | Wrapper for Vicuna-style models.