# LarkSuiteWikiLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.larksuite.LarkSuiteWikiLoader.html
**Word Count:** 150
**Links Count:** 418
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# LarkSuiteWikiLoader\#

_class _langchain\_community.document\_loaders.larksuite.LarkSuiteWikiLoader\(

    _domain : str_,     _access\_token : str_,     _wiki\_id : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/larksuite.html#LarkSuiteWikiLoader)\#     

Load from LarkSuite \(FeiShu\) wiki.

Initialize with domain, access\_token \(tenant / user\), and wiki\_id.

Parameters:     

  * **domain** \(_str_\) – The domain to load the LarkSuite.

  * **access\_token** \(_str_\) – The access\_token to use.

  * **wiki\_id** \(_str_\) – The wiki\_id to load.

Methods

`__init__`\(domain, access\_token, wiki\_id\) | Initialize with domain, access\_token \(tenant / user\), and wiki\_id.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load LarkSuite \(FeiShu\) wiki document.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _domain : str_,     _access\_token : str_,     _wiki\_id : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/larksuite.html#LarkSuiteWikiLoader.__init__)\#     

Initialize with domain, access\_token \(tenant / user\), and wiki\_id.

Parameters:     

  * **domain** \(_str_\) – The domain to load the LarkSuite.

  * **access\_token** \(_str_\) – The access\_token to use.

  * **wiki\_id** \(_str_\) – The wiki\_id to load.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/larksuite.html#LarkSuiteWikiLoader.lazy_load)\#     

Lazy load LarkSuite \(FeiShu\) wiki document.

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

Examples using LarkSuiteWikiLoader

  * [LarkSuite \(FeiShu\)](https://python.langchain.com/docs/integrations/document_loaders/larksuite/)

__On this page