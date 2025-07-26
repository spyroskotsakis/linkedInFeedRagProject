# CubeSemanticLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.cube_semantic.CubeSemanticLoader.html
**Word Count:** 181
**Links Count:** 420
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# CubeSemanticLoader\#

_class _langchain\_community.document\_loaders.cube\_semantic.CubeSemanticLoader\(

    _cube\_api\_url : str_,     _cube\_api\_token : str_,     _load\_dimension\_values : bool = True_,     _dimension\_values\_limit : int = 10000_,     _dimension\_values\_max\_retries : int = 10_,     _dimension\_values\_retry\_delay : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cube_semantic.html#CubeSemanticLoader)\#     

Load Cube semantic layer metadata.

Parameters:     

  * **cube\_api\_url** \(_str_\) – REST API endpoint. Use the REST API of your Cube’s deployment. Please find out more information here: <https://cube.dev/docs/http-api/rest#configuration-base-path>

  * **cube\_api\_token** \(_str_\) – Cube API token. Authentication tokens are generated based on your Cube’s API secret. Please find out more information here: <https://cube.dev/docs/security#generating-json-web-tokens-jwt>

  * **load\_dimension\_values** \(_bool_\) – Whether to load dimension values for every string dimension or not.

  * **dimension\_values\_limit** \(_int_\) – Maximum number of dimension values to load.

  * **dimension\_values\_max\_retries** \(_int_\) – Maximum number of retries to load dimension values.

  * **dimension\_values\_retry\_delay** \(_int_\) – Delay between retries to load dimension values.

Methods

`__init__`\(cube\_api\_url, cube\_api\_token\[, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Makes a call to Cube's REST API metadata endpoint.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _cube\_api\_url : str_,     _cube\_api\_token : str_,     _load\_dimension\_values : bool = True_,     _dimension\_values\_limit : int = 10000_,     _dimension\_values\_max\_retries : int = 10_,     _dimension\_values\_retry\_delay : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cube_semantic.html#CubeSemanticLoader.__init__)\#     

Parameters:     

  * **cube\_api\_url** \(_str_\)

  * **cube\_api\_token** \(_str_\)

  * **load\_dimension\_values** \(_bool_\)

  * **dimension\_values\_limit** \(_int_\)

  * **dimension\_values\_max\_retries** \(_int_\)

  * **dimension\_values\_retry\_delay** \(_int_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cube_semantic.html#CubeSemanticLoader.lazy_load)\#     

Makes a call to Cube’s REST API metadata endpoint.

Returns:     

  * page\_content=column\_title + column\_description

  * metadata          * table\_name

    * column\_name

    * column\_data\_type

    * column\_member\_type

    * column\_title

    * column\_description

    * column\_values

    * cube\_data\_obj\_type

Return type:     

A list of documents with attributes

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

Examples using CubeSemanticLoader

  * [Cube](https://python.langchain.com/docs/integrations/providers/cube/)

  * [Cube Semantic Layer](https://python.langchain.com/docs/integrations/document_loaders/cube_semantic/)

__On this page