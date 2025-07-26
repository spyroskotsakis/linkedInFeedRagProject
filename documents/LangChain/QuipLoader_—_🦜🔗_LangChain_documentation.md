# QuipLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.quip.QuipLoader.html
**Word Count:** 328
**Links Count:** 447
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# QuipLoader\#

_class _langchain\_community.document\_loaders.quip.QuipLoader\(

    _api\_url : str_,     _access\_token : str_,     _request\_timeout : int | None = 60_,     _\*_ ,     _allow\_dangerous\_xml\_parsing : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader)\#     

Load Quip pages.

Port of [quip/quip-api](https://github.com/quip/quip-api/tree/master/samples/baqup)

Parameters:     

  * **api\_url** \(_str_\) – <https://platform.quip.com>

  * **access\_token** \(_str_\) – token of access quip API. Please refer: [https://quip.com/dev/automation/documentation/current\#section/Authentication/Get-Access-to-Quip’s-APIs](https://quip.com/dev/automation/documentation/current#section/Authentication/Get-Access-to-Quip's-APIs)

  * **request\_timeout** \(_int_ _|__None_\) – timeout of request, default 60s.

  * **allow\_dangerous\_xml\_parsing** \(_bool_\) – Allow dangerous XML parsing, defaults to False

Methods

`__init__`\(api\_url, access\_token\[, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `get_thread_ids_by_folder_id`\(folder\_id, ...\) | Get thread ids by folder id and update in thread\_ids   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\[folder\_ids, thread\_ids, max\_docs, ...\]\) | :param : param folder\_ids: List of specific folder IDs to load, defaults to None :param : param thread\_ids: List of specific thread IDs to load, defaults to None :param : param max\_docs: Maximum number of docs to retrieve in total, defaults 1000 :param : param include\_all\_folders: Include all folders that your access\_token can access, but doesn't include your private folder :param : param include\_comments: Include comments, defaults to False :param : param include\_images: Include images, defaults to False   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `process_thread`\(thread\_id, include\_images, ...\) |    `process_thread_images`\(tree\) |    `process_thread_messages`\(thread\_id\) |    `process_threads`\(thread\_ids, include\_images, ...\) | Process a list of thread into a list of documents.      \_\_init\_\_\(

    _api\_url : str_,     _access\_token : str_,     _request\_timeout : int | None = 60_,     _\*_ ,     _allow\_dangerous\_xml\_parsing : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.__init__)\#     

Parameters:     

  * **api\_url** \(_str_\) – <https://platform.quip.com>

  * **access\_token** \(_str_\) – token of access quip API. Please refer: [https://quip.com/dev/automation/documentation/current\#section/Authentication/Get-Access-to-Quip’s-APIs](https://quip.com/dev/automation/documentation/current#section/Authentication/Get-Access-to-Quip's-APIs)

  * **request\_timeout** \(_int_ _|__None_\) – timeout of request, default 60s.

  * **allow\_dangerous\_xml\_parsing** \(_bool_\) – Allow dangerous XML parsing, defaults to False

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_thread\_ids\_by\_folder\_id\(

    _folder\_id : str_,     _depth : int_,     _thread\_ids : List\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.get_thread_ids_by_folder_id)\#     

Get thread ids by folder id and update in thread\_ids

Parameters:     

  * **folder\_id** \(_str_\)

  * **depth** \(_int_\)

  * **thread\_ids** \(_List_ _\[__str_ _\]_\)

Return type:     

None

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(

    _folder\_ids : List\[str\] | None = None_,     _thread\_ids : List\[str\] | None = None_,     _max\_docs : int | None = 1000_,     _include\_all\_folders : bool = False_,     _include\_comments : bool = False_,     _include\_images : bool = False_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.load)\#     

:param : param folder\_ids: List of specific folder IDs to load, defaults to None :param : param thread\_ids: List of specific thread IDs to load, defaults to None :param : param max\_docs: Maximum number of docs to retrieve in total, defaults 1000 :param : param include\_all\_folders: Include all folders that your access\_token

> can access, but doesn’t include your private folder

:param : param include\_comments: Include comments, defaults to False :param : param include\_images: Include images, defaults to False

Parameters:     

  * **folder\_ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **thread\_ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **max\_docs** \(_int_ _|__None_\)

  * **include\_all\_folders** \(_bool_\)

  * **include\_comments** \(_bool_\)

  * **include\_images** \(_bool_\)

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

process\_thread\(

    _thread\_id : str_,     _include\_images : bool_,     _include\_messages : bool_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.process_thread)\#     

Parameters:     

  * **thread\_id** \(_str_\)

  * **include\_images** \(_bool_\)

  * **include\_messages** \(_bool_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None

process\_thread\_images\(

    _tree : ElementTree_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.process_thread_images)\#     

Parameters:     

**tree** \(_ElementTree_\)

Return type:     

str

process\_thread\_messages\(_thread\_id : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.process_thread_messages)\#     

Parameters:     

**thread\_id** \(_str_\)

Return type:     

str

process\_threads\(

    _thread\_ids : Sequence\[str\]_,     _include\_images : bool_,     _include\_messages : bool_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/quip.html#QuipLoader.process_threads)\#     

Process a list of thread into a list of documents.

Parameters:     

  * **thread\_ids** \(_Sequence_ _\[__str_ _\]_\)

  * **include\_images** \(_bool_\)

  * **include\_messages** \(_bool_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using QuipLoader

  * [Quip](https://python.langchain.com/docs/integrations/document_loaders/quip/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)