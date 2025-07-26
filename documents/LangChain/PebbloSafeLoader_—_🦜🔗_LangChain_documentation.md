# PebbloSafeLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pebblo.PebbloSafeLoader.html
**Word Count:** 147
**Links Count:** 430
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# PebbloSafeLoader\#

_class _langchain\_community.document\_loaders.pebblo.PebbloSafeLoader\(

    _langchain\_loader : [BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")_,     _name : str_,     _owner : str = ''_,     _description : str = ''_,     _api\_key : str | None = None_,     _load\_semantic : bool = False_,     _classifier\_url : str | None = None_,     _\*_ ,     _classifier\_location : str = 'local'_,     _anonymize\_snippets : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloSafeLoader)\#     

Pebblo Safe Loader class is a wrapper around document loaders enabling the data to be scrutinized.

Methods

`__init__`\(langchain\_loader, name\[, owner, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `classify_in_batches`\(\) | Classify documents in batches.   `lazy_load`\(\) | Load documents in lazy fashion.   `load`\(\) | Load Documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `set_discover_sent`\(\) |       Parameters:     

  * **langchain\_loader** \([_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\)

  * **name** \(_str_\)

  * **owner** \(_str_\)

  * **description** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **load\_semantic** \(_bool_\)

  * **classifier\_url** \(_str_ _|__None_\)

  * **classifier\_location** \(_str_\)

  * **anonymize\_snippets** \(_bool_\)

\_\_init\_\_\(

    _langchain\_loader : [BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")_,     _name : str_,     _owner : str = ''_,     _description : str = ''_,     _api\_key : str | None = None_,     _load\_semantic : bool = False_,     _classifier\_url : str | None = None_,     _\*_ ,     _classifier\_location : str = 'local'_,     _anonymize\_snippets : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloSafeLoader.__init__)\#     

Parameters:     

  * **langchain\_loader** \([_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\)

  * **name** \(_str_\)

  * **owner** \(_str_\)

  * **description** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **load\_semantic** \(_bool_\)

  * **classifier\_url** \(_str_ _|__None_\)

  * **classifier\_location** \(_str_\)

  * **anonymize\_snippets** \(_bool_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

classify\_in\_batches\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloSafeLoader.classify_in_batches)\#     

Classify documents in batches. This is to avoid API timeouts when sending large number of documents. Batches are generated based on the page\_content size.

Return type:     

None

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloSafeLoader.lazy_load)\#     

Load documents in lazy fashion.

Raises:     

  * **NotImplementedError** – raised when lazy\_load id not implemented

  * **within wrapped loader.** – 

Yields:     

_list_ – Documents from loader’s lazy loading.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloSafeLoader.load)\#     

Load Documents.

Returns:     

Documents fetched from load method of the wrapped loader.

Return type:     

list

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

_classmethod _set\_discover\_sent\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloSafeLoader.set_discover_sent)\#     

Return type:     

None

Examples using PebbloSafeLoader

  * [Pebblo Safe DocumentLoader](https://python.langchain.com/docs/integrations/document_loaders/pebblo/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)