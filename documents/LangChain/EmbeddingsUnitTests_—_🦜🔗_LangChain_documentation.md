# EmbeddingsUnitTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/unit_tests/langchain_tests.unit_tests.embeddings.EmbeddingsUnitTests.html
**Word Count:** 190
**Links Count:** 86
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# EmbeddingsUnitTests\#

_class _langchain\_tests.unit\_tests.embeddings.EmbeddingsUnitTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/embeddings.html#EmbeddingsUnitTests)\#     

Base class for embeddings unit tests.

Test subclasses must implement the `embeddings_class` property to specify the embeddings model to be tested. You can also override the `embedding_model_params` property to specify initialization parameters.

Example:               from typing import Type          from langchain_tests.unit_tests import EmbeddingsUnitTests     from my_package.embeddings import MyEmbeddingsModel               class TestMyEmbeddingsModelUnit(EmbeddingsUnitTests):         @property         def embeddings_class(self) -> Type[MyEmbeddingsModel]:             # Return the embeddings model class to test here             return MyEmbeddingsModel              @property         def embedding_model_params(self) -> dict:             # Return initialization parameters for the model.             return {"model": "model-001"}     

Note

API references for individual test methods include troubleshooting tips.

Testing initialization from environment variables     

Overriding the `init_from_env_params` property will enable additional tests for initialization from environment variables. See below for details.

init\_from\_env\_params

This property is used in unit tests to test initialization from environment variables. It should return a tuple of three dictionaries that specify the environment variables, additional initialization args, and expected instance attributes to check.

Defaults to empty dicts. If not overridden, the test is skipped.

Example:               @property     def init_from_env_params(self) -> Tuple[dict, dict, dict]:         return (             {                 "MY_API_KEY": "api_key",             },             {                 "model": "model-001",             },             {                 "my_api_key": "api_key",             },         )     

Attributes

`embedding_model_params` |    ---|---   `embeddings_class` |    `init_from_env_params` | This property is used in unit tests to test initialization from environment variables.      Methods

`model`\(\) |    ---|---   `test_init`\(\) | Test model initialization.   `test_init_from_env`\(\) | Test initialization from environment variables.      model\(\) → [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\#     

Return type:     

[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

test\_init\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/embeddings.html#EmbeddingsUnitTests.test_init)\#     

Test model initialization.

Troubleshooting

If this test fails, ensure that `embedding_model_params` is specified and the model can be initialized from those params.

Return type:     

None

test\_init\_from\_env\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/embeddings.html#EmbeddingsUnitTests.test_init_from_env)\#     

Test initialization from environment variables. Relies on the `init_from_env_params` property. Test is skipped if that property is not set.

Troubleshooting

If this test fails, ensure that `init_from_env_params` is specified correctly and that model parameters are properly set from environment variables during initialization.

Return type:     

None

__On this page