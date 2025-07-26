# EmbeddingsIntegrationTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.embeddings.EmbeddingsIntegrationTests.html
**Word Count:** 204
**Links Count:** 104
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# EmbeddingsIntegrationTests\#

_class _langchain\_tests.integration\_tests.embeddings.EmbeddingsIntegrationTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/embeddings.html#EmbeddingsIntegrationTests)\#     

Base class for embeddings integration tests.

Test subclasses must implement the `embeddings_class` property to specify the embeddings model to be tested. You can also override the `embedding_model_params` property to specify initialization parameters.

Example:               from typing import Type          from langchain_tests.integration_tests import EmbeddingsIntegrationTests     from my_package.embeddings import MyEmbeddingsModel               class TestMyEmbeddingsModelIntegration(EmbeddingsIntegrationTests):         @property         def embeddings_class(self) -> Type[MyEmbeddingsModel]:             # Return the embeddings model class to test here             return MyEmbeddingsModel              @property         def embedding_model_params(self) -> dict:             # Return initialization parameters for the model.             return {"model": "model-001"}     

Note

API references for individual test methods include troubleshooting tips.

Attributes

`embedding_model_params` |    ---|---   `embeddings_class` |       Methods

`model`\(\) |    ---|---   `test_aembed_documents`\(model\) | Test embedding a list of strings async.   `test_aembed_query`\(model\) | Test embedding a string query async.   `test_embed_documents`\(model\) | Test embedding a list of strings.   `test_embed_query`\(model\) | Test embedding a string query.      model\(\) → [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\#     

Return type:     

[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

_async _test\_aembed\_documents\(

    _model : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/embeddings.html#EmbeddingsIntegrationTests.test_aembed_documents)\#     

Test embedding a list of strings async.

Troubleshooting

If this test fails, check that:

  1. The model will generate a list of lists of floats when calling `.aembed_documents` on a list of strings.

  2. The length of each list is the same.

Parameters:     

**model** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

Return type:     

None

_async _test\_aembed\_query\(

    _model : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/embeddings.html#EmbeddingsIntegrationTests.test_aembed_query)\#     

Test embedding a string query async.

Troubleshooting

If this test fails, check that:

  1. The model will generate a list of floats when calling `.aembed_query` on a string.

  2. The length of the list is consistent across different inputs.

Parameters:     

**model** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

Return type:     

None

test\_embed\_documents\(

    _model : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/embeddings.html#EmbeddingsIntegrationTests.test_embed_documents)\#     

Test embedding a list of strings.

Troubleshooting

If this test fails, check that:

  1. The model will generate a list of lists of floats when calling `.embed_documents` on a list of strings.

  2. The length of each list is the same.

Parameters:     

**model** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

Return type:     

None

test\_embed\_query\(

    _model : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/embeddings.html#EmbeddingsIntegrationTests.test_embed_query)\#     

Test embedding a string query.

Troubleshooting

If this test fails, check that:

  1. The model will generate a list of floats when calling `.embed_query` on a string.

  2. The length of the list is consistent across different inputs.

Parameters:     

**model** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

Return type:     

None

__On this page