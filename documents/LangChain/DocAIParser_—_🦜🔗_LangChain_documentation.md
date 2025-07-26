# DocAIParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParser.html
**Word Count:** 517
**Links Count:** 457
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# DocAIParser\#

_class _langchain\_community.document\_loaders.parsers.docai.DocAIParser\(

    _\*_ ,     _client : DocumentProcessorServiceClient | None = None_,     _location : str | None = None_,     _gcs\_output\_path : str | None = None_,     _processor\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser)\#     

Deprecated since version 0.0.32: Use `:class:`~langchain_google_community.DocAIParser`` instead. It will not be removed until langchain-community==1.0.

Google Cloud Document AI parser.

For a detailed explanation of Document AI, refer to the product documentation. <https://cloud.google.com/document-ai/docs/overview>

Initializes the parser.

Parameters:     

  * **client** \(_DocumentProcessorServiceClient_ _|__None_\) – a DocumentProcessorServiceClient to use

  * **location** \(_str_ _|__None_\) – a Google Cloud location where a Document AI processor is located

  * **gcs\_output\_path** \(_str_ _|__None_\) – a path on Google Cloud Storage to store parsing results

  * **processor\_name** \(_str_ _|__None_\) – full resource name of a Document AI processor or processor version

You should provide either a client or location \(and then a client     

would be instantiated\).

Methods

`__init__`\(\*\[, client, location, ...\]\) | Initializes the parser.   ---|---   `batch_parse`\(blobs\[, gcs\_output\_path, ...\]\) | Parses a list of blobs lazily.   `docai_parse`\(blobs, \*\[, gcs\_output\_path, ...\]\) | Runs Google Document AI PDF Batch Processing on a list of blobs.   `get_results`\(operations\) |    `is_running`\(operations\) |    `lazy_parse`\(blob\) | Parses a blob lazily.   `online_process`\(blob\[, ...\]\) | Parses a blob lazily using online processing.   `operations_from_names`\(operation\_names\) | Initializes Long-Running Operations from their names.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.   `parse_from_results`\(results\) |       \_\_init\_\_\(

    _\*_ ,     _client : DocumentProcessorServiceClient | None = None_,     _location : str | None = None_,     _gcs\_output\_path : str | None = None_,     _processor\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.__init__)\#     

Initializes the parser.

Parameters:     

  * **client** \(_DocumentProcessorServiceClient_ _|__None_\) – a DocumentProcessorServiceClient to use

  * **location** \(_str_ _|__None_\) – a Google Cloud location where a Document AI processor is located

  * **gcs\_output\_path** \(_str_ _|__None_\) – a path on Google Cloud Storage to store parsing results

  * **processor\_name** \(_str_ _|__None_\) – full resource name of a Document AI processor or processor version

You should provide either a client or location \(and then a client     

would be instantiated\).

batch\_parse\(

    _blobs : Sequence\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\]_,     _gcs\_output\_path : str | None = None_,     _timeout\_sec : int = 3600_,     _check\_in\_interval\_sec : int = 60_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.batch_parse)\#     

Parses a list of blobs lazily.

Parameters:     

  * **blobs** \(_Sequence_ _\[_[_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob") _\]_\) – a list of blobs to parse.

  * **gcs\_output\_path** \(_str_ _|__None_\) – a path on Google Cloud Storage to store parsing results.

  * **timeout\_sec** \(_int_\) – a timeout to wait for Document AI to complete, in seconds.

  * **check\_in\_interval\_sec** \(_int_\) – an interval to wait until next check whether parsing operations have been completed, in seconds

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

This is a long-running operation. A recommended way is to decouple     

parsing from creating LangChain Documents: >>> operations = parser.docai\_parse\(blobs, gcs\_path\) >>> parser.is\_running\(operations\) You can get operations names and save them: >>> names = \[op.operation.name for op in operations\] And when all operations are finished, you can use their results: >>> operations = parser.operations\_from\_names\(operation\_names\) >>> results = parser.get\_results\(operations\) >>> docs = parser.parse\_from\_results\(results\)

docai\_parse\(

    _blobs : Sequence\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\]_,     _\*_ ,     _gcs\_output\_path : str | None = None_,     _processor\_name : str | None = None_,     _batch\_size : int = 1000_,     _enable\_native\_pdf\_parsing : bool = True_,     _field\_mask : str | None = None_, \) → List\[[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.docai_parse)\#     

Runs Google Document AI PDF Batch Processing on a list of blobs.

Parameters:     

  * **blobs** \(_Sequence_ _\[_[_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob") _\]_\) – a list of blobs to be parsed

  * **gcs\_output\_path** \(_str_ _|__None_\) – a path \(folder\) on GCS to store results

  * **processor\_name** \(_str_ _|__None_\) – name of a Document AI processor.

  * **batch\_size** \(_int_\) – amount of documents per batch

  * **enable\_native\_pdf\_parsing** \(_bool_\) – a config option for the parser

  * **field\_mask** \(_str_ _|__None_\) – a comma-separated list of which fields to include in the Document AI response. suggested: “text,pages.pageNumber,pages.layout”

Return type:     

_List_\[[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\]

Document AI has a 1000 file limit per batch, so batches larger than that need to be split into multiple requests. Batch processing is an async long-running operation and results are stored in a output GCS bucket.

get\_results\(

    _operations : List\[[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\]_, \) → List\[[DocAIParsingResults](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParsingResults.html#langchain_community.document_loaders.parsers.docai.DocAIParsingResults "langchain_community.document_loaders.parsers.docai.DocAIParsingResults")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.get_results)\#     

Parameters:     

**operations** \(_List_ _\[_[_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation") _\]_\)

Return type:     

_List_\[[_DocAIParsingResults_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParsingResults.html#langchain_community.document_loaders.parsers.docai.DocAIParsingResults "langchain_community.document_loaders.parsers.docai.DocAIParsingResults")\]

is\_running\(

    _operations : List\[[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\]_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.is_running)\#     

Parameters:     

**operations** \(_List_ _\[_[_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation") _\]_\)

Return type:     

bool

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.lazy_parse)\#     

Parses a blob lazily.

Parameters:     

  * **blobs** – a Blob to parse

  * **blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

This is a long-running operation. A recommended way is to batch     

documents together and use the batch\_parse\(\) method.

online\_process\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_,     _enable\_native\_pdf\_parsing : bool = True_,     _field\_mask : str | None = None_,     _page\_range : List\[int\] | None = None_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.online_process)\#     

Parses a blob lazily using online processing.

Parameters:     

  * **blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – a blob to parse.

  * **enable\_native\_pdf\_parsing** \(_bool_\) – enable pdf embedded text extraction

  * **field\_mask** \(_str_ _|__None_\) – a comma-separated list of which fields to include in the Document AI response. suggested: “text,pages.pageNumber,pages.layout”

  * **page\_range** \(_List_ _\[__int_ _\]__|__None_\) – list of page numbers to parse. If None, entire document will be parsed.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

operations\_from\_names\(

    _operation\_names : List\[str\]_, \) → List\[[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.operations_from_names)\#     

Initializes Long-Running Operations from their names.

Parameters:     

**operation\_names** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\_from\_results\(

    _results : List\[[DocAIParsingResults](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParsingResults.html#langchain_community.document_loaders.parsers.docai.DocAIParsingResults "langchain_community.document_loaders.parsers.docai.DocAIParsingResults")\]_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/docai.html#DocAIParser.parse_from_results)\#     

Parameters:     

**results** \(_List_ _\[_[_DocAIParsingResults_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParsingResults.html#langchain_community.document_loaders.parsers.docai.DocAIParsingResults "langchain_community.document_loaders.parsers.docai.DocAIParsingResults") _\]_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)