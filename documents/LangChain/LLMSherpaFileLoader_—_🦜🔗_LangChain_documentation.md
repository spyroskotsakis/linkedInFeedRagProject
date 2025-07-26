# LLMSherpaFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.llmsherpa.LLMSherpaFileLoader.html
**Word Count:** 138
**Links Count:** 419
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# LLMSherpaFileLoader\#

_class _langchain\_community.document\_loaders.llmsherpa.LLMSherpaFileLoader\(

    _file\_path : str | Path_,     _new\_indent\_parser : bool = True_,     _apply\_ocr : bool = True_,     _strategy : str = 'chunks'_,     _llmsherpa\_api\_url : str = 'https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/llmsherpa.html#LLMSherpaFileLoader)\#     

Load Documents using LLMSherpa.

LLMSherpaFileLoader use LayoutPDFReader, which is part of the LLMSherpa library. This tool is designed to parse PDFs while preserving their layout information, which is often lost when using most PDF to text parsers.

Examples

from langchain\_community.document\_loaders.llmsherpa import LLMSherpaFileLoader

loader = LLMSherpaFileLoader\(     

“example.pdf”, strategy=”chunks”, llmsherpa\_api\_url=”<http://localhost:5010/api/parseDocument?renderFormat=all>”,

\) docs = loader.load\(\)

Initialize with a file path.

Methods

`__init__`\(file\_path\[, new\_indent\_parser, ...\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **file\_path** \(_str_ _|__Path_\)

  * **new\_indent\_parser** \(_bool_\)

  * **apply\_ocr** \(_bool_\)

  * **strategy** \(_str_\)

  * **llmsherpa\_api\_url** \(_str_\)

\_\_init\_\_\(

    _file\_path : str | Path_,     _new\_indent\_parser : bool = True_,     _apply\_ocr : bool = True_,     _strategy : str = 'chunks'_,     _llmsherpa\_api\_url : str = 'https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/llmsherpa.html#LLMSherpaFileLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\)

  * **new\_indent\_parser** \(_bool_\)

  * **apply\_ocr** \(_bool_\)

  * **strategy** \(_str_\)

  * **llmsherpa\_api\_url** \(_str_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/llmsherpa.html#LLMSherpaFileLoader.lazy_load)\#     

Load file.

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

Examples using LLMSherpaFileLoader

  * [LLM Sherpa](https://python.langchain.com/docs/integrations/document_loaders/llmsherpa/)

__On this page