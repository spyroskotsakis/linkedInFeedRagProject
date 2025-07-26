# langchain-tests: 0.3.20 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/index.html
**Word Count:** 80
**Links Count:** 82
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# langchain-tests: 0.3.20\#

Base Test classes for standard testing.

To learn how to use these classes, see the [Integration standard testing](https://python.langchain.com/docs/contributing/how_to/integrations/standard_tests/) guide.

## [conftest](https://python.langchain.com/api_reference/standard_tests/conftest.html#langchain-tests-conftest)\#

**Classes**

[`conftest.CustomPersister`](https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomPersister.html#langchain_tests.conftest.CustomPersister "langchain_tests.conftest.CustomPersister")\(\) | A custom persister for VCR that uses the CustomSerializer.   ---|---   [`conftest.CustomSerializer`](https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomSerializer.html#langchain_tests.conftest.CustomSerializer "langchain_tests.conftest.CustomSerializer")\(\) | Custom serializer for VCR cassettes using YAML and gzip.      ## [integration\_tests](https://python.langchain.com/api_reference/standard_tests/integration_tests.html#langchain-tests-integration-tests)\#

**Classes**

[`integration_tests.chat_models.ChatModelIntegrationTests`](https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.chat_models.ChatModelIntegrationTests.html#langchain_tests.integration_tests.chat_models.ChatModelIntegrationTests "langchain_tests.integration_tests.chat_models.ChatModelIntegrationTests")\(\) | Base class for chat model integration tests.   ---|---   [`integration_tests.embeddings.EmbeddingsIntegrationTests`](https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.embeddings.EmbeddingsIntegrationTests.html#langchain_tests.integration_tests.embeddings.EmbeddingsIntegrationTests "langchain_tests.integration_tests.embeddings.EmbeddingsIntegrationTests")\(\) | Base class for embeddings integration tests.   [`integration_tests.retrievers.RetrieversIntegrationTests`](https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.retrievers.RetrieversIntegrationTests.html#langchain_tests.integration_tests.retrievers.RetrieversIntegrationTests "langchain_tests.integration_tests.retrievers.RetrieversIntegrationTests")\(\) | Base class for retrievers integration tests.   [`integration_tests.tools.ToolsIntegrationTests`](https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.tools.ToolsIntegrationTests.html#langchain_tests.integration_tests.tools.ToolsIntegrationTests "langchain_tests.integration_tests.tools.ToolsIntegrationTests")\(\) | Base class for tools integration tests.   [`integration_tests.vectorstores.VectorStoreIntegrationTests`](https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.vectorstores.VectorStoreIntegrationTests.html#langchain_tests.integration_tests.vectorstores.VectorStoreIntegrationTests "langchain_tests.integration_tests.vectorstores.VectorStoreIntegrationTests")\(\) | Base class for vector store integration tests.      ## [unit\_tests](https://python.langchain.com/api_reference/standard_tests/unit_tests.html#langchain-tests-unit-tests)\#

**Classes**

[`unit_tests.chat_models.ChatModelUnitTests`](https://python.langchain.com/api_reference/standard_tests/unit_tests/langchain_tests.unit_tests.chat_models.ChatModelUnitTests.html#langchain_tests.unit_tests.chat_models.ChatModelUnitTests "langchain_tests.unit_tests.chat_models.ChatModelUnitTests")\(\) | Base class for chat model unit tests.   ---|---   [`unit_tests.embeddings.EmbeddingsUnitTests`](https://python.langchain.com/api_reference/standard_tests/unit_tests/langchain_tests.unit_tests.embeddings.EmbeddingsUnitTests.html#langchain_tests.unit_tests.embeddings.EmbeddingsUnitTests "langchain_tests.unit_tests.embeddings.EmbeddingsUnitTests")\(\) | Base class for embeddings unit tests.   [`unit_tests.tools.ToolsUnitTests`](https://python.langchain.com/api_reference/standard_tests/unit_tests/langchain_tests.unit_tests.tools.ToolsUnitTests.html#langchain_tests.unit_tests.tools.ToolsUnitTests "langchain_tests.unit_tests.tools.ToolsUnitTests")\(\) | Base class for tools unit tests.