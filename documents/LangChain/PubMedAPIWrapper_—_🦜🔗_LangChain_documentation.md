# PubMedAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pubmed.PubMedAPIWrapper.html
**Word Count:** 201
**Links Count:** 290
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# PubMedAPIWrapper\#

_class _langchain\_community.utilities.pubmed.PubMedAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around PubMed API.

This wrapper will use the PubMed API to conduct searches and fetch document summaries. By default, it will return the document summaries of the top-k results of an input search.

Parameters:     

  * **top\_k\_results** – number of the top-scored document used for the PubMed tool

  * **MAX\_QUERY\_LENGTH** – maximum length of the query. Default is 300 characters.

  * **doc\_content\_chars\_max** – maximum length of the document content. Content will be truncated if it exceeds this length. Default is 2000 characters.

  * **max\_retry** – maximum number of retries for a request. Default is 5.

  * **sleep\_time** – time to wait between retries. Default is 0.2 seconds.

  * **email** – email address to be used for the PubMed API.

  * **api\_key** – API key to be used for the PubMed API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _MAX\_QUERY\_LENGTH _: int_ _ = 300_\#     

_param _api\_key _: str_ _ = ''_\#     

_param _base\_url\_efetch _: str_ _ = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'_\#     

_param _base\_url\_esearch _: str_ _ = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?'_\#     

_param _doc\_content\_chars\_max _: int_ _ = 2000_\#     

_param _email _: str_ _ = 'your\_email@example.com'_\#     

_param _max\_retry _: int_ _ = 5_\#     

_param _sleep\_time _: float_ _ = 0.2_\#     

_param _top\_k\_results _: int_ _ = 3_\#     

lazy\_load\(

    _query : str_, \) → Iterator\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper.lazy_load)\#     

Search PubMed for documents matching the query. Return an iterator of dictionaries containing the document metadata.

Parameters:     

**query** \(_str_\)

Return type:     

_Iterator_\[dict\]

lazy\_load\_docs\(

    _query : str_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper.lazy_load_docs)\#     

Parameters:     

**query** \(_str_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(_query : str_\) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper.load)\#     

Search PubMed for documents matching the query. Return a list of dictionaries containing the document metadata.

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[dict\]

load\_docs\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper.load_docs)\#     

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

retrieve\_article\(

    _uid : str_,     _webenv : str_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper.retrieve_article)\#     

Parameters:     

  * **uid** \(_str_\)

  * **webenv** \(_str_\)

Return type:     

dict

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pubmed.html#PubMedAPIWrapper.run)\#     

Run PubMed search and get the article meta information. See <https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch> It uses only the most informative fields of article meta information.

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page