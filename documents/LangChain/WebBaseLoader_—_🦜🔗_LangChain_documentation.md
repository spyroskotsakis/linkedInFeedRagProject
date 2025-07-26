# WebBaseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html
**Word Count:** 541
**Links Count:** 457
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# WebBaseLoader\#

_class _langchain\_community.document\_loaders.web\_base.WebBaseLoader\(

    _web\_path : str | Sequence\[str\] = ''_,     _header\_template : dict | None = None_,     _verify\_ssl : bool = True_,     _proxies : dict | None = None_,     _continue\_on\_failure : bool = False_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _web\_paths : Sequence\[str\] = \(\)_,     _requests\_per\_second : int = 2_,     _default\_parser : str = 'html.parser'_,     _requests\_kwargs : Dict\[str, Any\] | None = None_,     _raise\_for\_status : bool = False_,     _bs\_get\_text\_kwargs : Dict\[str, Any\] | None = None_,     _bs\_kwargs : Dict\[str, Any\] | None = None_,     _session : Any = None_,     _\*_ ,     _show\_progress : bool = True_,     _trust\_env : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader)\#     

WebBaseLoader document loader integration

Setup:     

Install `langchain_community`.               pip install -U langchain_community     

Instantiate:                    from langchain_community.document_loaders import WebBaseLoader          loader = WebBaseLoader(         web_path = "https://www.espn.com/"         # header_template = None,         # verify_ssl = True,         # proxies = None,         # continue_on_failure = False,         # autoset_encoding = True,         # encoding = None,         # web_paths = (),         # requests_per_second = 2,         # default_parser = "html.parser",         # requests_kwargs = None,         # raise_for_status = False,         # bs_get_text_kwargs = None,         # bs_kwargs = None,         # session = None,         # show_progress = True,         # trust_env = False,     )     

Lazy load:                    docs = []     for doc in loader.lazy_load():         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    ESPN - Serving Sports Fans. Anytime. Anywhere.          {'source': 'https://www.espn.com/', 'title': 'ESPN - Serving Sports Fans. Anytime. Anywhere.', 'description': 'Visit ESPN for live scores, highlights and sports news. Stream exclusive games on ESPN+ and play fantasy sports.', 'language': 'en'}     

Async load:                    docs = []     async for doc in loader.alazy_load():         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    ESPN - Serving Sports Fans. Anytime. Anywhere.          {'source': 'https://www.espn.com/', 'title': 'ESPN - Serving Sports Fans. Anytime. Anywhere.', 'description': 'Visit ESPN for live scores, highlights and sports news. Stream exclusive games on ESPN+ and play fantasy sports.', 'language': 'en'}     

Changed in version 0.3.14: Deprecated `aload` \(which was not async\) and implemented a native async `alazy_load`. Expand below for more details.

How to update `aload`

Instead of using `aload`, you can use `load` for synchronous loading or `alazy_load` for asynchronous lazy loading.

Example using `load` \(synchronous\):               docs: List[Document] = loader.load()     

Example using `alazy_load` \(asynchronous\):               docs: List[Document] = []     async for doc in loader.alazy_load():         docs.append(doc)     

This is in preparation for accommodating an asynchronous `aload` in the future:               docs: List[Document] = await loader.aload()     

Initialize loader.

Parameters:     

  * **web\_paths** \(_Sequence_ _\[__str_ _\]_\) – Web paths to load from.

  * **requests\_per\_second** \(_int_\) – Max number of concurrent requests to make.

  * **default\_parser** \(_str_\) – Default parser to use for BeautifulSoup.

  * **requests\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for requests

  * **raise\_for\_status** \(_bool_\) – Raise an exception if http status code denotes an error.

  * **bs\_get\_text\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 get\_text

  * **bs\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 web page parsing

  * **show\_progress** \(_bool_\) – Show progress bar when loading pages.

  * **trust\_env** \(_bool_\) – set to True if using proxy to make web requests, for example using http\(s\)\_proxy environment variables. Defaults to False.

  * **web\_path** \(_str_ _|__Sequence_ _\[__str_ _\]_\)

  * **header\_template** \(_dict_ _|__None_\)

  * **verify\_ssl** \(_bool_\)

  * **proxies** \(_dict_ _|__None_\)

  * **continue\_on\_failure** \(_bool_\)

  * **autoset\_encoding** \(_bool_\)

  * **encoding** \(_str_ _|__None_\)

  * **session** \(_Any_\)

Attributes

`web_path` |    ---|---      Methods

`__init__`\(\[web\_path, header\_template, ...\]\) | Initialize loader.   ---|---   `alazy_load`\(\) | Async lazy load text from the url\(s\) in web\_path.   `aload`\(\) |    `ascrape_all`\(urls\[, parser\]\) | Async fetch all urls, then return soups for all results.   `fetch_all`\(urls\) | Fetch all urls concurrently with rate limiting.   `lazy_load`\(\) | Lazy load text from the url\(s\) in web\_path.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `scrape`\(\[parser\]\) | Scrape data from webpage and return it in BeautifulSoup format.   `scrape_all`\(urls\[, parser\]\) | Fetch all urls, then return soups for all results.      \_\_init\_\_\(

    _web\_path : str | Sequence\[str\] = ''_,     _header\_template : dict | None = None_,     _verify\_ssl : bool = True_,     _proxies : dict | None = None_,     _continue\_on\_failure : bool = False_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _web\_paths : Sequence\[str\] = \(\)_,     _requests\_per\_second : int = 2_,     _default\_parser : str = 'html.parser'_,     _requests\_kwargs : Dict\[str, Any\] | None = None_,     _raise\_for\_status : bool = False_,     _bs\_get\_text\_kwargs : Dict\[str, Any\] | None = None_,     _bs\_kwargs : Dict\[str, Any\] | None = None_,     _session : Any = None_,     _\*_ ,     _show\_progress : bool = True_,     _trust\_env : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.__init__)\#     

Initialize loader.

Parameters:     

  * **web\_paths** \(_Sequence_ _\[__str_ _\]_\) – Web paths to load from.

  * **requests\_per\_second** \(_int_\) – Max number of concurrent requests to make.

  * **default\_parser** \(_str_\) – Default parser to use for BeautifulSoup.

  * **requests\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for requests

  * **raise\_for\_status** \(_bool_\) – Raise an exception if http status code denotes an error.

  * **bs\_get\_text\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 get\_text

  * **bs\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 web page parsing

  * **show\_progress** \(_bool_\) – Show progress bar when loading pages.

  * **trust\_env** \(_bool_\) – set to True if using proxy to make web requests, for example using http\(s\)\_proxy environment variables. Defaults to False.

  * **web\_path** \(_str_ _|__Sequence_ _\[__str_ _\]_\)

  * **header\_template** \(_dict_ _|__None_\)

  * **verify\_ssl** \(_bool_\)

  * **proxies** \(_dict_ _|__None_\)

  * **continue\_on\_failure** \(_bool_\)

  * **autoset\_encoding** \(_bool_\)

  * **encoding** \(_str_ _|__None_\)

  * **session** \(_Any_\)

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.alazy_load)\#     

Async lazy load text from the url\(s\) in web\_path.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

aload\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.aload)\#     

Deprecated since version 0.3.14: See API reference for updated usage: <https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html> It will not be removed until langchain-community==1.0.

Load text from the urls in web\_path async into Documents.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ascrape\_all\(

    _urls : List\[str\]_,     _parser : str | None = None_, \) → List\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.ascrape_all)\#     

Async fetch all urls, then return soups for all results.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **parser** \(_str_ _|__None_\)

Return type:     

_List_\[_Any_\]

_async _fetch\_all\(

    _urls : List\[str\]_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.fetch_all)\#     

Fetch all urls concurrently with rate limiting.

Parameters:     

**urls** \(_List_ _\[__str_ _\]_\)

Return type:     

_Any_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.lazy_load)\#     

Lazy load text from the url\(s\) in web\_path.

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

scrape\(

    _parser : str | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.scrape)\#     

Scrape data from webpage and return it in BeautifulSoup format.

Parameters:     

**parser** \(_str_ _|__None_\)

Return type:     

_Any_

scrape\_all\(

    _urls : List\[str\]_,     _parser : str | None = None_, \) → List\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/web_base.html#WebBaseLoader.scrape_all)\#     

Fetch all urls, then return soups for all results.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **parser** \(_str_ _|__None_\)

Return type:     

_List_\[_Any_\]

Examples using WebBaseLoader

  * [\# Basic example \(short documents\)](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [Build a Local RAG Application](https://python.langchain.com/docs/tutorials/local_rag/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Google Cloud Vertex AI Reranker](https://python.langchain.com/docs/integrations/document_transformers/google_cloud_vertexai_rerank/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)

  * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

  * [Infino](https://python.langchain.com/docs/integrations/callbacks/infino/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [Merge Documents Loader](https://python.langchain.com/docs/integrations/document_loaders/merge_doc/)

  * [RePhraseQuery](https://python.langchain.com/docs/integrations/retrievers/re_phrase/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

  * [WebBaseLoader](https://python.langchain.com/docs/integrations/document_loaders/web_base/)

  * [Zep](https://python.langchain.com/docs/integrations/vectorstores/zep/)

  * [Zep Cloud](https://python.langchain.com/docs/integrations/vectorstores/zep_cloud/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)