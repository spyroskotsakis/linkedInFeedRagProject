# RetrieversIntegrationTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.retrievers.RetrieversIntegrationTests.html
**Word Count:** 260
**Links Count:** 98
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# RetrieversIntegrationTests\#

_class _langchain\_tests.integration\_tests.retrievers.RetrieversIntegrationTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/retrievers.html#RetrieversIntegrationTests)\#     

Base class for retrievers integration tests.

Attributes

`retriever_constructor` | A BaseRetriever subclass to be tested.   ---|---   `retriever_constructor_params` | Returns a dictionary of parameters to pass to the retriever constructor.   `retriever_query_example` | Returns a str representing the "query" of an example retriever call.      Methods

`test_ainvoke_returns_documents`\(retriever\) | If ainvoked with the example params, the retriever should return a list of Documents.   ---|---   `test_invoke_returns_documents`\(retriever\) | If invoked with the example params, the retriever should return a list of Documents.   `test_invoke_with_k_kwarg`\(retriever\) | Test that the invoke method accepts a k parameter, representing the number of documents to return.   `test_k_constructor_param`\(\) | Test that the retriever constructor accepts a k parameter, representing the number of documents to return.      _async _test\_ainvoke\_returns\_documents\(

    _retriever : [BaseRetriever](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/retrievers.html#RetrieversIntegrationTests.test_ainvoke_returns_documents)\#     

If ainvoked with the example params, the retriever should return a list of Documents.

See `test_invoke_returns_documents()` for more information on troubleshooting.

Parameters:     

**retriever** \([_BaseRetriever_](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")\)

Return type:     

None

test\_invoke\_returns\_documents\(

    _retriever : [BaseRetriever](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/retrievers.html#RetrieversIntegrationTests.test_invoke_returns_documents)\#     

If invoked with the example params, the retriever should return a list of Documents.

Troubleshooting

If this test fails, the retriever’s invoke method does not return a list of langchain\_core.document.Document objects. Please confirm that your \_get\_relevant\_documents method returns a list of Document objects.

Parameters:     

**retriever** \([_BaseRetriever_](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")\)

Return type:     

None

test\_invoke\_with\_k\_kwarg\(

    _retriever : [BaseRetriever](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/retrievers.html#RetrieversIntegrationTests.test_invoke_with_k_kwarg)\#     

Test that the invoke method accepts a k parameter, representing the number of documents to return.

Troubleshooting

If this test fails, the retriever’s invoke method does not accept a k parameter, or the retriever does not return the correct number of documents \(k\) when it is set.

For example, a retriever like               MyRetriever().invoke("query", k=3)     

should return 3 documents when invoked with a query.

Parameters:     

**retriever** \([_BaseRetriever_](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")\)

Return type:     

None

test\_k\_constructor\_param\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/retrievers.html#RetrieversIntegrationTests.test_k_constructor_param)\#     

Test that the retriever constructor accepts a k parameter, representing the number of documents to return.

Troubleshooting

If this test fails, either the retriever constructor does not accept a k parameter, or the retriever does not return the correct number of documents \(k\) when it is set.

For example, a retriever like               MyRetriever(k=3).invoke("query")     

should return 3 documents when invoked with a query.

Return type:     

None

__On this page