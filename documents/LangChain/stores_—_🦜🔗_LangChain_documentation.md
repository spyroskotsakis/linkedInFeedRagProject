# stores — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/stores.html
**Word Count:** 65
**Links Count:** 104
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# `stores`\#

**Store** implements the key-value stores and storage helpers.

Module provides implementations of various key-value stores that conform to a simple key-value interface.

The primary goal of these storages is to support implementation of caching.

**Classes**

[`stores.BaseStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\(\) | Abstract interface for a key-value store.   ---|---   [`stores.InMemoryBaseStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryBaseStore.html#langchain_core.stores.InMemoryBaseStore "langchain_core.stores.InMemoryBaseStore")\(\) | In-memory implementation of the BaseStore using a dictionary.   [`stores.InMemoryByteStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryByteStore.html#langchain_core.stores.InMemoryByteStore "langchain_core.stores.InMemoryByteStore")\(\) | In-memory store for bytes.   [`stores.InMemoryStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryStore.html#langchain_core.stores.InMemoryStore "langchain_core.stores.InMemoryStore")\(\) | In-memory store for any type of data.   [`stores.InvalidKeyException`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InvalidKeyException.html#langchain_core.stores.InvalidKeyException "langchain_core.stores.InvalidKeyException") | Raised when a key is invalid; e.g., uses incorrect characters.