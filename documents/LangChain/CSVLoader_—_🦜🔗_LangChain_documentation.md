# CSVLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.csv_loader.CSVLoader.html
**Word Count:** 389
**Links Count:** 424
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# CSVLoader\#

_class _langchain\_community.document\_loaders.csv\_loader.CSVLoader\(

    _file\_path : str | Path_,     _source\_column : str | None = None_,     _metadata\_columns : Sequence\[str\] = \(\)_,     _csv\_args : Dict | None = None_,     _encoding : str | None = None_,     _autodetect\_encoding : bool = False_,     _\*_ ,     _content\_columns : Sequence\[str\] = \(\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/csv_loader.html#CSVLoader)\#     

Load a CSV file into a list of Documents.

Each document represents one row of the CSV file. Every row is converted into a key/value pair and outputted to a new line in the document’s page\_content.

The source for each document loaded from csv is set to the value of the file\_path argument for all documents by default. You can override this by setting the source\_column argument to the name of a column in the CSV file. The source of each document will then be set to the value of the column with the name specified in source\_column.

Output Example:                    column1: value1     column2: value2     column3: value3     

Instantiate:                    from langchain_community.document_loaders import CSVLoader          loader = CSVLoader(file_path='./hw_200.csv',         csv_args={         'delimiter': ',',         'quotechar': '"',         'fieldnames': ['Index', 'Height', 'Weight']     })     

Load:                    docs = loader.load()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Index: Index     Height: Height(Inches)"     Weight: "Weight(Pounds)"     {'source': './hw_200.csv', 'row': 0}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Index: Index     Height: Height(Inches)"     Weight: "Weight(Pounds)"     {'source': './hw_200.csv', 'row': 0}     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Index: Index     Height: Height(Inches)"     Weight: "Weight(Pounds)"     {'source': './hw_200.csv', 'row': 0}     

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the CSV file.

  * **source\_column** \(_str_ _|__None_\) – The name of the column in the CSV file to use as the source. Optional. Defaults to None.

  * **metadata\_columns** \(_Sequence_ _\[__str_ _\]_\) – A sequence of column names to use as metadata. Optional.

  * **csv\_args** \(_Dict_ _|__None_\) – A dictionary of arguments to pass to the csv.DictReader. Optional. Defaults to None.

  * **encoding** \(_str_ _|__None_\) – The encoding of the CSV file. Optional. Defaults to None.

  * **autodetect\_encoding** \(_bool_\) – Whether to try to autodetect the file encoding.

  * **content\_columns** \(_Sequence_ _\[__str_ _\]_\) – A sequence of column names to use for the document content. If not present, use all columns that are not part of the metadata.

Methods

`__init__`\(file\_path\[, source\_column, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _source\_column : str | None = None_,     _metadata\_columns : Sequence\[str\] = \(\)_,     _csv\_args : Dict | None = None_,     _encoding : str | None = None_,     _autodetect\_encoding : bool = False_,     _\*_ ,     _content\_columns : Sequence\[str\] = \(\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/csv_loader.html#CSVLoader.__init__)\#     

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the CSV file.

  * **source\_column** \(_str_ _|__None_\) – The name of the column in the CSV file to use as the source. Optional. Defaults to None.

  * **metadata\_columns** \(_Sequence_ _\[__str_ _\]_\) – A sequence of column names to use as metadata. Optional.

  * **csv\_args** \(_Dict_ _|__None_\) – A dictionary of arguments to pass to the csv.DictReader. Optional. Defaults to None.

  * **encoding** \(_str_ _|__None_\) – The encoding of the CSV file. Optional. Defaults to None.

  * **autodetect\_encoding** \(_bool_\) – Whether to try to autodetect the file encoding.

  * **content\_columns** \(_Sequence_ _\[__str_ _\]_\) – A sequence of column names to use for the document content. If not present, use all columns that are not part of the metadata.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/csv_loader.html#CSVLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using CSVLoader

  * [Aerospike](https://python.langchain.com/docs/integrations/vectorstores/aerospike/)

  * [CSV](https://python.langchain.com/docs/integrations/document_loaders/csv/)

  * [ChatGPT plugin](https://python.langchain.com/docs/integrations/retrievers/chatgpt-plugin/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [Document loaders](https://python.langchain.com/docs/integrations/document_loaders/index/)

  * [How to load CSVs](https://python.langchain.com/docs/how_to/document_loader_csv/)

  * [Pebblo Safe DocumentLoader](https://python.langchain.com/docs/integrations/document_loaders/pebblo/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)