# MWDumpLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mediawikidump.MWDumpLoader.html
**Word Count:** 153
**Links Count:** 420
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# MWDumpLoader\#

_class _langchain\_community.document\_loaders.mediawikidump.MWDumpLoader\(

    _file\_path : str | Path_,     _encoding : str | None = 'utf8'_,     _namespaces : Sequence\[int\] | None = None_,     _skip\_redirects : bool | None = False_,     _stop\_on\_error : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mediawikidump.html#MWDumpLoader)\#     

Load MediaWiki dump from an XML file.

Example               from langchain_text_splitters import RecursiveCharacterTextSplitter     from langchain_community.document_loaders import MWDumpLoader          loader = MWDumpLoader(         file_path="myWiki.xml",         encoding="utf8"     )     docs = loader.load()     text_splitter = RecursiveCharacterTextSplitter(         chunk_size=1000, chunk_overlap=0     )     texts = text_splitter.split_documents(docs)     

Parameters:     

  * **file\_path** \(_str_\) – XML local file path

  * **encoding** \(_str_ _,__optional_\) – Charset encoding, defaults to “utf8”

  * **namespaces** \(_List_ _\[__int_ _\]__,__optional_\) – The namespace of pages you want to parse. See <https://www.mediawiki.org/wiki/Help:Namespaces#Localisation> for a list of all common namespaces

  * **skip\_redirects** \(_bool_ _,__optional_\) – TR=rue to skip pages that redirect to other pages, False to keep them. False by default

  * **stop\_on\_error** \(_bool_ _,__optional_\) – False to skip over pages that cause parsing errors, True to stop. True by default

Methods

`__init__`\(file\_path\[, encoding, namespaces, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load from a file path.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _encoding : str | None = 'utf8'_,     _namespaces : Sequence\[int\] | None = None_,     _skip\_redirects : bool | None = False_,     _stop\_on\_error : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mediawikidump.html#MWDumpLoader.__init__)\#     

Parameters:     

  * **file\_path** \(_str_ _|__Path_\)

  * **encoding** \(_str_ _|__None_\)

  * **namespaces** \(_Sequence_ _\[__int_ _\]__|__None_\)

  * **skip\_redirects** \(_bool_ _|__None_\)

  * **stop\_on\_error** \(_bool_ _|__None_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mediawikidump.html#MWDumpLoader.lazy_load)\#     

Lazy load from a file path.

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

Examples using MWDumpLoader

  * [MediaWiki Dump](https://python.langchain.com/docs/integrations/document_loaders/mediawikidump/)

  * [MediaWikiDump](https://python.langchain.com/docs/integrations/providers/mediawikidump/)

__On this page