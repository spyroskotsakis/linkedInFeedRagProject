# BaiduBOSFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.baiducloud_bos_file.BaiduBOSFileLoader.html
**Word Count:** 129
**Links Count:** 417
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# BaiduBOSFileLoader\#

_class _langchain\_community.document\_loaders.baiducloud\_bos\_file.BaiduBOSFileLoader\(_conf : Any_, _bucket : str_, _key : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/baiducloud_bos_file.html#BaiduBOSFileLoader)\#     

Load from Baidu Cloud BOS file.

Initialize with BOS config, bucket and key name. :param conf\(BceClientConfiguration\): BOS config. :param bucket\(str\): BOS bucket. :param key\(str\): BOS file key.

Methods

`__init__`\(conf, bucket, key\) | Initialize with BOS config, bucket and key name.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **conf** \(_Any_\)

  * **bucket** \(_str_\)

  * **key** \(_str_\)

\_\_init\_\_\(

    _conf : Any_,     _bucket : str_,     _key : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/baiducloud_bos_file.html#BaiduBOSFileLoader.__init__)\#     

Initialize with BOS config, bucket and key name. :param conf\(BceClientConfiguration\): BOS config. :param bucket\(str\): BOS bucket. :param key\(str\): BOS file key.

Parameters:     

  * **conf** \(_Any_\)

  * **bucket** \(_str_\)

  * **key** \(_str_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/baiducloud_bos_file.html#BaiduBOSFileLoader.lazy_load)\#     

Load documents.

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

__On this page