# KineticaLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.kinetica_loader.KineticaLoader.html
**Word Count:** 183
**Links Count:** 419
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# KineticaLoader\#

_class _langchain\_community.document\_loaders.kinetica\_loader.KineticaLoader\(

    _query : str_,     _host : str_,     _username : str_,     _password : str_,     _parameters : Dict\[str, Any\] | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/kinetica_loader.html#KineticaLoader)\#     

Load from Kinetica API.

Each document represents one row of the result. The page\_content\_columns are written into the page\_content of the document. The metadata\_columns are written into the metadata of the document. By default, all columns are written into the page\_content and none into the metadata.

Initialize Kinetica document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in Kinetica.

  * **parameters** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional. Parameters to pass to the query.

  * **page\_content\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. Columns written to Document page\_content.

  * **metadata\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. Columns written to Document metadata.

  * **host** \(_str_\)

  * **username** \(_str_\)

  * **password** \(_str_\)

Methods

`__init__`\(query, host, username, password\[, ...\]\) | Initialize Kinetica document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _host : str_,     _username : str_,     _password : str_,     _parameters : Dict\[str, Any\] | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/kinetica_loader.html#KineticaLoader.__init__)\#     

Initialize Kinetica document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in Kinetica.

  * **parameters** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Parameters to pass to the query.

  * **page\_content\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document page\_content.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document metadata.

  * **host** \(_str_\)

  * **username** \(_str_\)

  * **password** \(_str_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/kinetica_loader.html#KineticaLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/kinetica_loader.html#KineticaLoader.load)\#     

Load data into document objects.

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

Examples using KineticaLoader

  * [Kinetica](https://python.langchain.com/docs/integrations/document_loaders/kinetica/)

__On this page