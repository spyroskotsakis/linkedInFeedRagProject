# init_embeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/embeddings/langchain.embeddings.base.init_embeddings.html
**Word Count:** 138
**Links Count:** 89
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# init\_embeddings\#

langchain.embeddings.base.init\_embeddings\(

    _model : str_,     _\*_ ,     _provider : str | None = None_,     _\*\* kwargs: Any_, \) → [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Any, list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/base.html#init_embeddings)\#     

Initialize an embeddings model from a model name and optional provider.

**Note:** Must have the integration package corresponding to the model provider installed.

Parameters:     

  * **model** \(_str_\) – Name of the model to use. Can be either: \- A model string like “openai:text-embedding-3-small” \- Just the model name if provider is specified

  * **provider** \(_str_ _|__None_\) – 

Optional explicit provider name. If not specified, will attempt to parse from the model string. Supported providers and their required packages:

\{\_get\_provider\_list\(\)\}

  * **\*\*kwargs** \(_Any_\) – Additional model-specific parameters passed to the embedding model. These vary by provider, see the provider-specific documentation for details.

Returns:     

An Embeddings instance that can generate embeddings for text.

Raises:     

  * **ValueError** – If the model provider is not supported or cannot be determined

  * **ImportError** – If the required provider package is not installed

Return type:     

[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | [_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Any_ , list\[float\]\]

Example Usage               # Using a model string     model = init_embeddings("openai:text-embedding-3-small")     model.embed_query("Hello, world!")          # Using explicit provider     model = init_embeddings(         model="text-embedding-3-small",         provider="openai"     )     model.embed_documents(["Hello, world!", "Goodbye, world!"])          # With additional parameters     model = init_embeddings(         "openai:text-embedding-3-small",         api_key="sk-..."     )     

Added in version 0.3.9.

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)