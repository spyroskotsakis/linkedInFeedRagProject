# RecursiveJsonSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/json/langchain_text_splitters.json.RecursiveJsonSplitter.html
**Word Count:** 304
**Links Count:** 111
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# RecursiveJsonSplitter\#

_class _langchain\_text\_splitters.json.RecursiveJsonSplitter\(

    _max\_chunk\_size : int = 2000_,     _min\_chunk\_size : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/json.html#RecursiveJsonSplitter)\#     

Splits JSON data into smaller, structured chunks while preserving hierarchy.

This class provides methods to split JSON data into smaller dictionaries or JSON-formatted strings based on configurable maximum and minimum chunk sizes. It supports nested JSON structures, optionally converts lists into dictionaries for better chunking, and allows the creation of document objects for further use.

max\_chunk\_size\#     

The maximum size for each chunk. Defaults to 2000.

Type:     

int

min\_chunk\_size\#     

The minimum size for each chunk, derived from max\_chunk\_size if not explicitly provided.

Type:     

int

Initialize the chunk size configuration for text processing.

This constructor sets up the maximum and minimum chunk sizes, ensuring that the min\_chunk\_size defaults to a value slightly smaller than the max\_chunk\_size if not explicitly provided.

Parameters:     

  * **max\_chunk\_size** \(_int_\) – The maximum size for a chunk. Defaults to 2000.

  * **min\_chunk\_size** \(_Optional_ _\[__int_ _\]_\) – The minimum size for a chunk. If None, defaults to the maximum chunk size minus 200, with a lower bound of 50.

max\_chunk\_size\#     

The configured maximum size for each chunk.

Type:     

int

min\_chunk\_size\#     

The configured minimum size for each chunk, derived from max\_chunk\_size if not explicitly provided.

Type:     

int

Methods

`__init__`\(\[max\_chunk\_size, min\_chunk\_size\]\) | Initialize the chunk size configuration for text processing.   ---|---   `create_documents`\(texts\[, convert\_lists, ...\]\) | Create documents from a list of json objects \(Dict\).   `split_json`\(json\_data\[, convert\_lists\]\) | Splits JSON into a list of JSON chunks.   `split_text`\(json\_data\[, convert\_lists, ...\]\) | Splits JSON into a list of JSON formatted strings.      \_\_init\_\_\(

    _max\_chunk\_size : int = 2000_,     _min\_chunk\_size : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/json.html#RecursiveJsonSplitter.__init__)\#     

Initialize the chunk size configuration for text processing.

This constructor sets up the maximum and minimum chunk sizes, ensuring that the min\_chunk\_size defaults to a value slightly smaller than the max\_chunk\_size if not explicitly provided.

Parameters:     

  * **max\_chunk\_size** \(_int_\) – The maximum size for a chunk. Defaults to 2000.

  * **min\_chunk\_size** \(_Optional_ _\[__int_ _\]_\) – The minimum size for a chunk. If None, defaults to the maximum chunk size minus 200, with a lower bound of 50.

max\_chunk\_size\#     

The configured maximum size for each chunk.

Type:     

int

min\_chunk\_size\#     

The configured minimum size for each chunk, derived from max\_chunk\_size if not explicitly provided.

Type:     

int

create\_documents\(

    _texts : list\[dict\[str, Any\]\]_,     _convert\_lists : bool = False_,     _ensure\_ascii : bool = True_,     _metadatas : list\[dict\[Any, Any\]\] | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/json.html#RecursiveJsonSplitter.create_documents)\#     

Create documents from a list of json objects \(Dict\).

Parameters:     

  * **texts** \(_list_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **convert\_lists** \(_bool_\)

  * **ensure\_ascii** \(_bool_\)

  * **metadatas** \(_list_ _\[__dict_ _\[__Any_ _,__Any_ _\]__\]__|__None_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_json\(

    _json\_data : dict\[str, Any\]_,     _convert\_lists : bool = False_, \) → list\[dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/json.html#RecursiveJsonSplitter.split_json)\#     

Splits JSON into a list of JSON chunks.

Parameters:     

  * **json\_data** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **convert\_lists** \(_bool_\)

Return type:     

list\[dict\[str, _Any_\]\]

split\_text\(

    _json\_data : dict\[str, Any\]_,     _convert\_lists : bool = False_,     _ensure\_ascii : bool = True_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/json.html#RecursiveJsonSplitter.split_text)\#     

Splits JSON into a list of JSON formatted strings.

Parameters:     

  * **json\_data** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **convert\_lists** \(_bool_\)

  * **ensure\_ascii** \(_bool_\)

Return type:     

list\[str\]

Examples using RecursiveJsonSplitter

  * [How to split JSON data](https://python.langchain.com/docs/how_to/recursive_json_splitter/)

__On this page