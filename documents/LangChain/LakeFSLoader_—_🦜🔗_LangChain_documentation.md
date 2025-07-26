# LakeFSLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.lakefs.LakeFSLoader.html
**Word Count:** 184
**Links Count:** 432
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# LakeFSLoader\#

_class _langchain\_community.document\_loaders.lakefs.LakeFSLoader\(

    _lakefs\_access\_key : str_,     _lakefs\_secret\_key : str_,     _lakefs\_endpoint : str_,     _repo : str | None = None_,     _ref : str | None = 'main'_,     _path : str | None = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSLoader)\#     

Load from lakeFS.

Parameters:     

  * **lakefs\_access\_key** \(_str_\) – \[required\] lakeFS server’s access key

  * **lakefs\_secret\_key** \(_str_\) – \[required\] lakeFS server’s secret key

  * **lakefs\_endpoint** \(_str_\) – \[required\] lakeFS server’s endpoint address, ex: <https://example.my-lakefs.com>

  * **repo** \(_str_\) – \[optional, default = ‘’\] target repository

  * **ref** \(_str_\) – \[optional, default = ‘main’\] target ref \(branch name, tag, or commit ID\)

  * **path** \(_str_\) – \[optional, default = ‘’\] target path

Attributes

Methods

`__init__`\(lakefs\_access\_key, ...\[, repo, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `set_path`\(path\) |    `set_ref`\(ref\) |    `set_repo`\(repo\) |       \_\_init\_\_\(

    _lakefs\_access\_key : str_,     _lakefs\_secret\_key : str_,     _lakefs\_endpoint : str_,     _repo : str | None = None_,     _ref : str | None = 'main'_,     _path : str | None = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSLoader.__init__)\#     

Parameters:     

  * **lakefs\_access\_key** \(_str_\) – \[required\] lakeFS server’s access key

  * **lakefs\_secret\_key** \(_str_\) – \[required\] lakeFS server’s secret key

  * **lakefs\_endpoint** \(_str_\) – \[required\] lakeFS server’s endpoint address, ex: <https://example.my-lakefs.com>

  * **repo** \(_str_ _|__None_\) – \[optional, default = ‘’\] target repository

  * **ref** \(_str_ _|__None_\) – \[optional, default = ‘main’\] target ref \(branch name, tag, or commit ID\)

  * **path** \(_str_ _|__None_\) – \[optional, default = ‘’\] target path

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSLoader.load)\#     

Load data into Document objects.

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

set\_path\(_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSLoader.set_path)\#     

Parameters:     

**path** \(_str_\)

Return type:     

None

set\_ref\(_ref : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSLoader.set_ref)\#     

Parameters:     

**ref** \(_str_\)

Return type:     

None

set\_repo\(_repo : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSLoader.set_repo)\#     

Parameters:     

**repo** \(_str_\)

Return type:     

None

Examples using LakeFSLoader

  * [lakeFS](https://python.langchain.com/docs/integrations/document_loaders/lakefs/)

__On this page