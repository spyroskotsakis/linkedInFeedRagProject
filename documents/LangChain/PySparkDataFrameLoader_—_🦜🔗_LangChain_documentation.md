# PySparkDataFrameLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pyspark_dataframe.PySparkDataFrameLoader.html
**Word Count:** 184
**Links Count:** 423
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# PySparkDataFrameLoader\#

_class _langchain\_community.document\_loaders.pyspark\_dataframe.PySparkDataFrameLoader\(

    _spark\_session : SparkSession | None = None_,     _df : Any | None = None_,     _page\_content\_column : str = 'text'_,     _fraction\_of\_memory : float = 0.1_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pyspark_dataframe.html#PySparkDataFrameLoader)\#     

Load PySpark DataFrames.

Initialize with a Spark DataFrame object.

Parameters:     

  * **spark\_session** \(_SparkSession_ _|__None_\) – The SparkSession object.

  * **df** \(_Any_ _|__None_\) – The Spark DataFrame object.

  * **page\_content\_column** \(_str_\) – The name of the column containing the page content. Defaults to “text”.

  * **fraction\_of\_memory** \(_float_\) – The fraction of memory to use. Defaults to 0.1.

Methods

`__init__`\(\[spark\_session, df, ...\]\) | Initialize with a Spark DataFrame object.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `get_num_rows`\(\) | Gets the number of "feasible" rows for the DataFrame   `lazy_load`\(\) | A lazy loader for document content.   `load`\(\) | Load from the dataframe.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _spark\_session : SparkSession | None = None_,     _df : Any | None = None_,     _page\_content\_column : str = 'text'_,     _fraction\_of\_memory : float = 0.1_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pyspark_dataframe.html#PySparkDataFrameLoader.__init__)\#     

Initialize with a Spark DataFrame object.

Parameters:     

  * **spark\_session** \(_SparkSession_ _|__None_\) – The SparkSession object.

  * **df** \(_Any_ _|__None_\) – The Spark DataFrame object.

  * **page\_content\_column** \(_str_\) – The name of the column containing the page content. Defaults to “text”.

  * **fraction\_of\_memory** \(_float_\) – The fraction of memory to use. Defaults to 0.1.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_num\_rows\(\) → Tuple\[int, int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pyspark_dataframe.html#PySparkDataFrameLoader.get_num_rows)\#     

Gets the number of “feasible” rows for the DataFrame

Return type:     

_Tuple_\[int, int\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pyspark_dataframe.html#PySparkDataFrameLoader.lazy_load)\#     

A lazy loader for document content.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pyspark_dataframe.html#PySparkDataFrameLoader.load)\#     

Load from the dataframe.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using PySparkDataFrameLoader

  * [PySpark](https://python.langchain.com/docs/integrations/document_loaders/pyspark_dataframe/)

__On this page