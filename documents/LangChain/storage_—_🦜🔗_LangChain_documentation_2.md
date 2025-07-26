# storage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/storage.html
**Word Count:** 51
**Links Count:** 83
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# `storage`\#

Implementations of key-value stores and storage helpers.

Module provides implementations of various key-value stores that conform to a simple key-value interface.

The primary goal of these storages is to support implementation of caching.

**Classes**

[`storage.encoder_backed.EncoderBackedStore`](https://python.langchain.com/api_reference/langchain/storage/langchain.storage.encoder_backed.EncoderBackedStore.html#langchain.storage.encoder_backed.EncoderBackedStore "langchain.storage.encoder_backed.EncoderBackedStore")\(...\) | Wraps a store with key and value encoders/decoders.   ---|---   [`storage.file_system.LocalFileStore`](https://python.langchain.com/api_reference/langchain/storage/langchain.storage.file_system.LocalFileStore.html#langchain.storage.file_system.LocalFileStore "langchain.storage.file_system.LocalFileStore")\(root\_path, \*\) | BaseStore interface that works on the local file system.