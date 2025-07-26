# LarkSuiteDocLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.larksuite.LarkSuiteDocLoader.html
**Word Count:** 147
**Links Count:** 419
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# LarkSuiteDocLoader\#

_class _langchain\_community.document\_loaders.larksuite.LarkSuiteDocLoader\(

    _domain : str_,     _access\_token : str_,     _document\_id : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/larksuite.html#LarkSuiteDocLoader)\#     

Load from LarkSuite \(FeiShu\).

Initialize with domain, access\_token \(tenant / user\), and document\_id.

Parameters:     

  * **domain** \(_str_\) – The domain to load the LarkSuite.

  * **access\_token** \(_str_\) – The access\_token to use.

  * **document\_id** \(_str_\) – The document\_id to load.

Methods

`__init__`\(domain, access\_token, document\_id\) | Initialize with domain, access\_token \(tenant / user\), and document\_id.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load LarkSuite \(FeiShu\) document.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _domain : str_,     _access\_token : str_,     _document\_id : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/larksuite.html#LarkSuiteDocLoader.__init__)\#     

Initialize with domain, access\_token \(tenant / user\), and document\_id.

Parameters:     

  * **domain** \(_str_\) – The domain to load the LarkSuite.

  * **access\_token** \(_str_\) – The access\_token to use.

  * **document\_id** \(_str_\) – The document\_id to load.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/larksuite.html#LarkSuiteDocLoader.lazy_load)\#     

Lazy load LarkSuite \(FeiShu\) document.

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

Examples using LarkSuiteDocLoader

  * [ByteDance](https://python.langchain.com/docs/integrations/providers/byte_dance/)

  * [LarkSuite \(FeiShu\)](https://python.langchain.com/docs/integrations/document_loaders/larksuite/)

__On this page