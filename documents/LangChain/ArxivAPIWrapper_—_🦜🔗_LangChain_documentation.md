# ArxivAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arxiv.ArxivAPIWrapper.html
**Word Count:** 357
**Links Count:** 304
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# ArxivAPIWrapper\#

_class _langchain\_community.utilities.arxiv.ArxivAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arxiv.html#ArxivAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around ArxivAPI.

To use, you should have the `arxiv` python package installed. <https://lukasschwab.me/arxiv.py/index.html> This wrapper will use the Arxiv API to conduct searches and fetch document summaries. By default, it will return the document summaries of the top-k results. If the query is in the form of arxiv identifier \(see <https://info.arxiv.org/help/find/index.html>\), it will return the paper corresponding to the arxiv identifier. It limits the Document content by doc\_content\_chars\_max. Set doc\_content\_chars\_max=None if you don’t want to limit the content size.

top\_k\_results\#     

number of the top-scored document used for the arxiv tool

ARXIV\_MAX\_QUERY\_LENGTH\#     

the cut limit on the query used for the arxiv tool.

continue\_on\_failure\#     

If True, continue loading other URLs on failure.

Type:     

bool

load\_max\_docs\#     

a limit to the number of loaded documents

load\_all\_available\_meta\#     

if True: the metadata of the loaded Documents contains all available meta info \(see <https://lukasschwab.me/arxiv.py/index.html#Result>\), if False: the metadata contains only the published date, title, authors and summary.

doc\_content\_chars\_max\#     

an optional cut limit for the length of a document’s content

Example               from langchain_community.utilities.arxiv import ArxivAPIWrapper     arxiv = ArxivAPIWrapper(         top_k_results = 3,         ARXIV_MAX_QUERY_LENGTH = 300,         load_max_docs = 3,         load_all_available_meta = False,         doc_content_chars_max = 40000     )     arxiv.run("tree of thought llm")     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _ARXIV\_MAX\_QUERY\_LENGTH _: int_ _ = 300_\#     

_param _arxiv\_exceptions _: Any_ _\[Required\]_\#     

_param _continue\_on\_failure _: bool_ _ = False_\#     

_param _doc\_content\_chars\_max _: int | None_ _ = 4000_\#     

_param _load\_all\_available\_meta _: bool_ _ = False_\#     

_param _load\_max\_docs _: int_ _ = 100_\#     

_param _top\_k\_results _: int_ _ = 3_\#     

get\_summaries\_as\_docs\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arxiv.html#ArxivAPIWrapper.get_summaries_as_docs)\#     

Performs an arxiv search and returns list of documents, with summaries as the content.

If an error occurs or no documents found, error text is returned instead. Wrapper for <https://lukasschwab.me/arxiv.py/index.html#Search>

Parameters:     

**query** \(_str_\) – a plaintext search query

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

is\_arxiv\_identifier\(_query : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arxiv.html#ArxivAPIWrapper.is_arxiv_identifier)\#     

Check if a query is an arxiv identifier.

Parameters:     

**query** \(_str_\)

Return type:     

bool

lazy\_load\(

    _query : str_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arxiv.html#ArxivAPIWrapper.lazy_load)\#     

Run Arxiv search and get the article texts plus the article meta information. See <https://lukasschwab.me/arxiv.py/index.html#Search>

Returns: documents with the document.page\_content in text format

Performs an arxiv search, downloads the top k results as PDFs, loads them as Documents, and returns them.

Parameters:     

**query** \(_str_\) – a plaintext search query

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arxiv.html#ArxivAPIWrapper.load)\#     

Run Arxiv search and get the article texts plus the article meta information. See <https://lukasschwab.me/arxiv.py/index.html#Search>

Returns: a list of documents with the document.page\_content in text format

Performs an arxiv search, downloads the top k results as PDFs, loads them as Documents, and returns them in a List.

Parameters:     

**query** \(_str_\) – a plaintext search query

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arxiv.html#ArxivAPIWrapper.run)\#     

Performs an arxiv search and A single string with the publish date, title, authors, and summary for each article separated by two newlines.

If an error occurs or no documents found, error text is returned instead. Wrapper for <https://lukasschwab.me/arxiv.py/index.html#Search>

Parameters:     

**query** \(_str_\) – a plaintext search query

Return type:     

str

Examples using ArxivAPIWrapper

  * [ArXiv](https://python.langchain.com/docs/integrations/tools/arxiv/)

__On this page