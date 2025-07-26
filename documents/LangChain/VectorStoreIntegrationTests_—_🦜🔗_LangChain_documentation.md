# VectorStoreIntegrationTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.vectorstores.VectorStoreIntegrationTests.html
**Word Count:** 1310
**Links Count:** 231
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# VectorStoreIntegrationTests\#

_class _langchain\_tests.integration\_tests.vectorstores.VectorStoreIntegrationTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests)\#     

Base class for vector store integration tests.

Implementers should subclass this test suite and provide a fixture that returns an empty vector store for each test.

The fixture should use the `get_embeddings` method to get a pre-defined embeddings model that should be used for this test suite.

Here is a template:               from typing import Generator          import pytest     from langchain_core.vectorstores import VectorStore     from langchain_parrot_link.vectorstores import ParrotVectorStore     from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests               class TestParrotVectorStore(VectorStoreIntegrationTests):         @pytest.fixture()         def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore             """Get an empty vectorstore."""             store = ParrotVectorStore(self.get_embeddings())             # note: store should be EMPTY at this point             # if you need to delete data, you may do so here             try:                 yield store             finally:                 # cleanup operations, or deleting data                 pass     

In the fixture, before the `yield` we instantiate an empty vector store. In the `finally` block, we call whatever logic is necessary to bring the vector store to a clean state.

Example:               from typing import Generator          import pytest     from langchain_core.vectorstores import VectorStore     from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests          from langchain_chroma import Chroma               class TestChromaStandard(VectorStoreIntegrationTests):         @pytest.fixture()         def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore             """Get an empty vectorstore for unit tests."""             store = Chroma(embedding_function=self.get_embeddings())             try:                 yield store             finally:                 store.delete_collection()                 pass     

Note that by default we enable both sync and async tests. To disable either, override the `has_sync` or `has_async` properties to `False` in the subclass. For example:               class TestParrotVectorStore(VectorStoreIntegrationTests):          @pytest.fixture()          def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore              ...               @property          def has_async(self) -> bool:              return False     

Note

API references for individual test methods include troubleshooting tips.

Attributes

`has_async` | Configurable property to enable or disable async tests.   ---|---   `has_sync` | Configurable property to enable or disable sync tests.      Methods

`get_embeddings`\(\) | A pre-defined embeddings model that should be used for this test.   ---|---   `test_add_documents`\(vectorstore\) | Test adding documents into the vectorstore.   `test_add_documents_async`\(vectorstore\) | Test adding documents into the vectorstore.   `test_add_documents_by_id_with_mutation`\(...\) | Test that we can overwrite by ID using add\_documents.   `test_add_documents_by_id_with_mutation_async`\(...\) | Test that we can overwrite by ID using add\_documents.   `test_add_documents_documents`\(vectorstore\) | Run add\_documents tests.   `test_add_documents_documents_async`\(vectorstore\) | Run add\_documents tests.   `test_add_documents_with_existing_ids`\(vectorstore\) | Test that add\_documents with existing IDs is idempotent.   `test_add_documents_with_existing_ids_async`\(...\) | Test that add\_documents with existing IDs is idempotent.   `test_add_documents_with_ids_is_idempotent`\(...\) | Adding by ID should be idempotent.   `test_add_documents_with_ids_is_idempotent_async`\(...\) | Adding by ID should be idempotent.   `test_delete_missing_content`\(vectorstore\) | Deleting missing content should not raise an exception.   `test_delete_missing_content_async`\(vectorstore\) | Deleting missing content should not raise an exception.   `test_deleting_bulk_documents`\(vectorstore\) | Test that we can delete several documents at once.   `test_deleting_bulk_documents_async`\(vectorstore\) | Test that we can delete several documents at once.   `test_deleting_documents`\(vectorstore\) | Test deleting documents from the vectorstore.   `test_deleting_documents_async`\(vectorstore\) | Test deleting documents from the vectorstore.   `test_get_by_ids`\(vectorstore\) | Test get by IDs.   `test_get_by_ids_async`\(vectorstore\) | Test get by IDs.   `test_get_by_ids_missing`\(vectorstore\) | Test get by IDs with missing IDs.   `test_get_by_ids_missing_async`\(vectorstore\) | Test get by IDs with missing IDs.   `test_vectorstore_is_empty`\(vectorstore\) | Test that the vectorstore is empty.   `test_vectorstore_is_empty_async`\(vectorstore\) | Test that the vectorstore is empty.   `test_vectorstore_still_empty`\(vectorstore\) | This test should follow a test that adds documents.   `test_vectorstore_still_empty_async`\(vectorstore\) | This test should follow a test that adds documents.   `vectorstore`\(\) | Get the vectorstore class to test.      _static _get\_embeddings\(\) → [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.get_embeddings)\#     

A pre-defined embeddings model that should be used for this test.

This currently uses `DeterministicFakeEmbedding` from `langchain-core`, which uses numpy to generate random numbers based on a hash of the input text.

The resulting embeddings are not meaningful, but they are deterministic.

Return type:     

[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

test\_add\_documents\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents)\#     

Test adding documents into the vectorstore.

Troubleshooting

If this test fails, check that:

  1. We correctly initialize an empty vector store in the `vectorestore` fixture.

  2. Calling `.similarity_search` for the top `k` similar documents does not threshold by score.

  3. We do not mutate the original document object when adding it to the vector store \(e.g., by adding an ID\).

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_add\_documents\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_async)\#     

Test adding documents into the vectorstore.

Troubleshooting

If this test fails, check that:

  1. We correctly initialize an empty vector store in the `vectorestore` fixture.

  2. Calling `.asimilarity_search` for the top `k` similar documents does not threshold by score.

  3. We do not mutate the original document object when adding it to the vector store \(e.g., by adding an ID\).

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_add\_documents\_by\_id\_with\_mutation\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_by_id_with_mutation)\#     

Test that we can overwrite by ID using add\_documents.

Troubleshooting

If this test fails, check that when `add_documents` is called with an ID that already exists in the vector store, the content is updated rather than duplicated.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_add\_documents\_by\_id\_with\_mutation\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_by_id_with_mutation_async)\#     

Test that we can overwrite by ID using add\_documents.

Troubleshooting

If this test fails, check that when `aadd_documents` is called with an ID that already exists in the vector store, the content is updated rather than duplicated.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_add\_documents\_documents\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_documents)\#     

Run add\_documents tests.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and returns documents in the same order as the IDs passed in.

Check also that `add_documents` will correctly generate string IDs if none are provided.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     def test_add_documents_documents(self, vectorstore: VectorStore) -> None:         super().test_add_documents_documents(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_add\_documents\_documents\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_documents_async)\#     

Run add\_documents tests.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and returns documents in the same order as the IDs passed in.

Check also that `aadd_documents` will correctly generate string IDs if none are provided.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     async def test_add_documents_documents(self, vectorstore: VectorStore) -> None:         await super().test_add_documents_documents(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_add\_documents\_with\_existing\_ids\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_with_existing_ids)\#     

Test that add\_documents with existing IDs is idempotent.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and returns documents in the same order as the IDs passed in.

This test also verifies that:

  1. IDs specified in the `Document.id` field are assigned when adding documents.

  2. If some documents include IDs and others don’t string IDs are generated for the latter.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     def test_add_documents_with_existing_ids(self, vectorstore: VectorStore) -> None:         super().test_add_documents_with_existing_ids(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_add\_documents\_with\_existing\_ids\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_with_existing_ids_async)\#     

Test that add\_documents with existing IDs is idempotent.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and returns documents in the same order as the IDs passed in.

This test also verifies that:

  1. IDs specified in the `Document.id` field are assigned when adding documents.

  2. If some documents include IDs and others don’t string IDs are generated for the latter.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     async def test_add_documents_with_existing_ids(self, vectorstore: VectorStore) -> None:         await super().test_add_documents_with_existing_ids(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_add\_documents\_with\_ids\_is\_idempotent\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_with_ids_is_idempotent)\#     

Adding by ID should be idempotent.

Troubleshooting

If this test fails, check that adding the same document twice with the same IDs has the same effect as adding it once \(i.e., it does not duplicate the documents\).

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_add\_documents\_with\_ids\_is\_idempotent\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_add_documents_with_ids_is_idempotent_async)\#     

Adding by ID should be idempotent.

Troubleshooting

If this test fails, check that adding the same document twice with the same IDs has the same effect as adding it once \(i.e., it does not duplicate the documents\).

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_delete\_missing\_content\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_delete_missing_content)\#     

Deleting missing content should not raise an exception.

Troubleshooting

If this test fails, check that `delete` does not raise an exception when deleting IDs that do not exist.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_delete\_missing\_content\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_delete_missing_content_async)\#     

Deleting missing content should not raise an exception.

Troubleshooting

If this test fails, check that `adelete` does not raise an exception when deleting IDs that do not exist.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_deleting\_bulk\_documents\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_deleting_bulk_documents)\#     

Test that we can delete several documents at once.

Troubleshooting

If this test fails, check that `delete` correctly removes multiple documents when given a list of IDs.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_deleting\_bulk\_documents\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_deleting_bulk_documents_async)\#     

Test that we can delete several documents at once.

Troubleshooting

If this test fails, check that `adelete` correctly removes multiple documents when given a list of IDs.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_deleting\_documents\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_deleting_documents)\#     

Test deleting documents from the vectorstore.

Troubleshooting

If this test fails, check that `add_documents` preserves identifiers passed in through `ids`, and that `delete` correctly removes documents.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_deleting\_documents\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_deleting_documents_async)\#     

Test deleting documents from the vectorstore.

Troubleshooting

If this test fails, check that `aadd_documents` preserves identifiers passed in through `ids`, and that `delete` correctly removes documents.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_get\_by\_ids\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_get_by_ids)\#     

Test get by IDs.

This test requires that `get_by_ids` be implemented on the vector store.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and returns documents in the same order as the IDs passed in.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     def test_get_by_ids(self, vectorstore: VectorStore) -> None:         super().test_get_by_ids(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_get\_by\_ids\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_get_by_ids_async)\#     

Test get by IDs.

This test requires that `get_by_ids` be implemented on the vector store.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and returns documents in the same order as the IDs passed in.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     async def test_get_by_ids(self, vectorstore: VectorStore) -> None:         await super().test_get_by_ids(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_get\_by\_ids\_missing\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_get_by_ids_missing)\#     

Test get by IDs with missing IDs.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and does not raise an exception when given IDs that do not exist.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     def test_get_by_ids_missing(self, vectorstore: VectorStore) -> None:         super().test_get_by_ids_missing(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_get\_by\_ids\_missing\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_get_by_ids_missing_async)\#     

Test get by IDs with missing IDs.

Troubleshooting

If this test fails, check that `get_by_ids` is implemented and does not raise an exception when given IDs that do not exist.

Note

`get_by_ids` was added to the `VectorStore` interface in `langchain-core` version 0.2.11. If difficult to implement, this test can be skipped using a pytest `xfail` on the test class:               @pytest.mark.xfail(reason=("get_by_ids not implemented."))     async def test_get_by_ids_missing(self, vectorstore: VectorStore) -> None:         await super().test_get_by_ids_missing(vectorstore)     

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_vectorstore\_is\_empty\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_vectorstore_is_empty)\#     

Test that the vectorstore is empty.

Troubleshooting

If this test fails, check that the test class \(i.e., sub class of `VectorStoreIntegrationTests`\) initializes an empty vector store in the `vectorestore` fixture.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_vectorstore\_is\_empty\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_vectorstore_is_empty_async)\#     

Test that the vectorstore is empty.

Troubleshooting

If this test fails, check that the test class \(i.e., sub class of `VectorStoreIntegrationTests`\) initializes an empty vector store in the `vectorestore` fixture.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

test\_vectorstore\_still\_empty\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_vectorstore_still_empty)\#     

This test should follow a test that adds documents.

This just verifies that the fixture is set up properly to be empty after each test.

Troubleshooting

If this test fails, check that the test class \(i.e., sub class of `VectorStoreIntegrationTests`\) correctly clears the vector store in the `finally` block.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_async _test\_vectorstore\_still\_empty\_async\(

    _vectorstore : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.test_vectorstore_still_empty_async)\#     

This test should follow a test that adds documents.

This just verifies that the fixture is set up properly to be empty after each test.

Troubleshooting

If this test fails, check that the test class \(i.e., sub class of `VectorStoreIntegrationTests`\) correctly clears the vector store in the `finally` block.

Parameters:     

**vectorstore** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\)

Return type:     

None

_abstractmethod _vectorstore\(\) → [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/vectorstores.html#VectorStoreIntegrationTests.vectorstore)\#     

Get the vectorstore class to test.

The returned vectorstore should be EMPTY.

Return type:     

[_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")

__On this page