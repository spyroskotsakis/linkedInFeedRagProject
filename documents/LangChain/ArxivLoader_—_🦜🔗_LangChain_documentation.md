# ArxivLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.arxiv.ArxivLoader.html
**Word Count:** 284
**Links Count:** 425
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# ArxivLoader\#

_class _langchain\_community.document\_loaders.arxiv.ArxivLoader\(

    _query : str_,     _doc\_content\_chars\_max : int | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arxiv.html#ArxivLoader)\#     

Load a query result from Arxiv. The loader converts the original PDF format into the text.

Setup:     

Install `arxiv` and `PyMuPDF` packages. `PyMuPDF` transforms PDF files downloaded from the arxiv.org site into the text format.               pip install -U arxiv pymupdf     

Instantiate:                    from langchain_community.document_loaders import ArxivLoader          loader = ArxivLoader(         query="reasoning",         # load_max_docs=2,         # load_all_available_meta=False     )     

Load:                    docs = loader.load()     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Understanding the Reasoning Ability of Language Models     From the Perspective of Reasoning Paths Aggre     {         'Published': '2024-02-29',         'Title': 'Understanding the Reasoning Ability of Language Models From the                 Perspective of Reasoning Paths Aggregation',         'Authors': 'Xinyi Wang, Alfonso Amayuelas, Kexun Zhang, Liangming Pan,                 Wenhu Chen, William Yang Wang',         'Summary': 'Pre-trained language models (LMs) are able to perform complex reasoning                 without explicit fine-tuning...'     }     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Understanding the Reasoning Ability of Language Models     From the Perspective of Reasoning Paths Aggre     {         'Published': '2024-02-29',         'Title': 'Understanding the Reasoning Ability of Language Models From the                 Perspective of Reasoning Paths Aggregation',         'Authors': 'Xinyi Wang, Alfonso Amayuelas, Kexun Zhang, Liangming Pan,                 Wenhu Chen, William Yang Wang',         'Summary': 'Pre-trained language models (LMs) are able to perform complex reasoning                 without explicit fine-tuning...'     }     

Use summaries of articles as docs:                    from langchain_community.document_loaders import ArxivLoader          loader = ArxivLoader(         query="reasoning"     )          docs = loader.get_summaries_as_docs()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Pre-trained language models (LMs) are able to perform complex reasoning     without explicit fine-tuning     {         'Entry ID': 'http://arxiv.org/abs/2402.03268v2',         'Published': datetime.date(2024, 2, 29),         'Title': 'Understanding the Reasoning Ability of Language Models From the                 Perspective of Reasoning Paths Aggregation',         'Authors': 'Xinyi Wang, Alfonso Amayuelas, Kexun Zhang, Liangming Pan,                 Wenhu Chen, William Yang Wang'     }     

Initialize with search query to find documents in the Arxiv. Supports all arguments of ArxivAPIWrapper.

Parameters:     

  * **query** \(_str_\) – free text which used to find documents in the Arxiv

  * **doc\_content\_chars\_max** \(_int_ _|__None_\) – cut limit for the length of a document’s content

  * **kwargs** \(_Any_\)

Methods

`__init__`\(query\[, doc\_content\_chars\_max\]\) | Initialize with search query to find documents in the Arxiv.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `get_summaries_as_docs`\(\) | Uses papers summaries as documents rather than source Arvix papers   `lazy_load`\(\) | Lazy load Arvix documents   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _doc\_content\_chars\_max : int | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arxiv.html#ArxivLoader.__init__)\#     

Initialize with search query to find documents in the Arxiv. Supports all arguments of ArxivAPIWrapper.

Parameters:     

  * **query** \(_str_\) – free text which used to find documents in the Arxiv

  * **doc\_content\_chars\_max** \(_int_ _|__None_\) – cut limit for the length of a document’s content

  * **kwargs** \(_Any_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_summaries\_as\_docs\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arxiv.html#ArxivLoader.get_summaries_as_docs)\#     

Uses papers summaries as documents rather than source Arvix papers

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arxiv.html#ArxivLoader.lazy_load)\#     

Lazy load Arvix documents

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

Examples using ArxivLoader

  * [Arxiv](https://python.langchain.com/docs/integrations/providers/arxiv/)

  * [ArxivLoader](https://python.langchain.com/docs/integrations/document_loaders/arxiv/)

__On this page