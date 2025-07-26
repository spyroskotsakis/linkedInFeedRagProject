# RocksetLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rocksetdb.RocksetLoader.html
**Word Count:** 320
**Links Count:** 418
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# RocksetLoader\#

_class _langchain\_community.document\_loaders.rocksetdb.RocksetLoader\(_client: ~typing.Any, query: ~typing.Any, content\_keys: ~typing.List\[str\], metadata\_keys: ~typing.List\[str\] | None = None, content\_columns\_joiner: ~typing.Callable\[\[~typing.List\[~typing.Tuple\[str, ~typing.Any\]\]\], str\] = <function default\_joiner>_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rocksetdb.html#RocksetLoader)\#     

Load from a Rockset database.

To use, you should have the rockset python package installed.

Example               # This code will load 3 records from the "langchain_demo"     # collection as Documents, with the `text` column used as     # the content          from langchain_community.document_loaders import RocksetLoader     from rockset import RocksetClient, Regions, models          loader = RocksetLoader(         RocksetClient(Regions.usw2a1, "<api key>"),         models.QueryRequestSql(             query="select * from langchain_demo limit 3"         ),         ["text"]     )     

\)

Initialize with Rockset client.

Parameters:     

  * **client** \(_Any_\) – Rockset client object.

  * **query** \(_Any_\) – Rockset query object.

  * **content\_keys** \(_List_ _\[__str_ _\]_\) – The collection columns to be written into the page\_content of the Documents.

  * **metadata\_keys** \(_List_ _\[__str_ _\]__|__None_\) – The collection columns to be written into the metadata of the Documents. By default, this is all the keys in the document.

  * **content\_columns\_joiner** \(_Callable_ _\[__\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]__,__str_ _\]_\) – Method that joins content\_keys and its values into a string. It’s method that takes in a List\[Tuple\[str, Any\]\]\], representing a list of tuples of \(column name, column value\). By default, this is a method that joins each column value with a new line. This method is only relevant if there are multiple content\_keys.

Methods

`__init__`\(client, query, content\_keys\[, ...\]\) | Initialize with Rockset client.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(_client: ~typing.Any, query: ~typing.Any, content\_keys: ~typing.List\[str\], metadata\_keys: ~typing.List\[str\] | None = None, content\_columns\_joiner: ~typing.Callable\[\[~typing.List\[~typing.Tuple\[str, ~typing.Any\]\]\], str\] = <function default\_joiner>_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rocksetdb.html#RocksetLoader.__init__)\#     

Initialize with Rockset client.

Parameters:     

  * **client** \(_Any_\) – Rockset client object.

  * **query** \(_Any_\) – Rockset query object.

  * **content\_keys** \(_List_ _\[__str_ _\]_\) – The collection columns to be written into the page\_content of the Documents.

  * **metadata\_keys** \(_List_ _\[__str_ _\]__|__None_\) – The collection columns to be written into the metadata of the Documents. By default, this is all the keys in the document.

  * **content\_columns\_joiner** \(_Callable_ _\[__\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]__,__str_ _\]_\) – Method that joins content\_keys and its values into a string. It’s method that takes in a List\[Tuple\[str, Any\]\]\], representing a list of tuples of \(column name, column value\). By default, this is a method that joins each column value with a new line. This method is only relevant if there are multiple content\_keys.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rocksetdb.html#RocksetLoader.lazy_load)\#     

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

Examples using RocksetLoader

  * [Rockset](https://python.langchain.com/docs/integrations/document_loaders/rockset/)

__On this page