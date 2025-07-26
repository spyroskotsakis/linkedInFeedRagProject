# langchain-mistralai: 0.2.11 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/mistralai/index.html
**Word Count:** 34
**Links Count:** 72
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# langchain-mistralai: 0.2.11\#

## [chat\_models](https://python.langchain.com/api_reference/mistralai/chat_models.html#langchain-mistralai-chat-models)\#

**Classes**

[`chat_models.ChatMistralAI`](https://python.langchain.com/api_reference/mistralai/chat_models/langchain_mistralai.chat_models.ChatMistralAI.html#langchain_mistralai.chat_models.ChatMistralAI "langchain_mistralai.chat_models.ChatMistralAI") | A chat model that uses the MistralAI API.   ---|---      **Functions**

[`chat_models.acompletion_with_retry`](https://python.langchain.com/api_reference/mistralai/chat_models/langchain_mistralai.chat_models.acompletion_with_retry.html#langchain_mistralai.chat_models.acompletion_with_retry "langchain_mistralai.chat_models.acompletion_with_retry")\(llm\[, ...\]\) | Use tenacity to retry the async completion call.   ---|---      ## [embeddings](https://python.langchain.com/api_reference/mistralai/embeddings.html#langchain-mistralai-embeddings)\#

**Classes**

[`embeddings.DummyTokenizer`](https://python.langchain.com/api_reference/mistralai/embeddings/langchain_mistralai.embeddings.DummyTokenizer.html#langchain_mistralai.embeddings.DummyTokenizer "langchain_mistralai.embeddings.DummyTokenizer")\(\) | Dummy tokenizer for when tokenizer cannot be accessed \(e.g., via Huggingface\).   ---|---   [`embeddings.MistralAIEmbeddings`](https://python.langchain.com/api_reference/mistralai/embeddings/langchain_mistralai.embeddings.MistralAIEmbeddings.html#langchain_mistralai.embeddings.MistralAIEmbeddings "langchain_mistralai.embeddings.MistralAIEmbeddings") | MistralAI embedding model integration.