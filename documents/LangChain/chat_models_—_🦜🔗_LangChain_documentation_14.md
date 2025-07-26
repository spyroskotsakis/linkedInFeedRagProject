# chat_models — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chat_models.html
**Word Count:** 61
**Links Count:** 81
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# `chat_models`\#

**Chat Models** are a variation on language models.

While Chat Models use language models under the hood, the interface they expose is a bit different. Rather than expose a “text in, text out” API, they expose an interface where “chat messages” are the inputs and outputs.

**Class hierarchy:**               BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm     

**Main helpers:**               AIMessage, BaseMessage, HumanMessage     

**Functions**

[`chat_models.base.init_chat_model`](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html#langchain.chat_models.base.init_chat_model "langchain.chat_models.base.init_chat_model")\(\) | Initialize a ChatModel from the model name and provider.   ---|---