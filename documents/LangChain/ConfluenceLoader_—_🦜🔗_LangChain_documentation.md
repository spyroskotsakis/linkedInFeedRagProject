# ConfluenceLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ConfluenceLoader.html
**Word Count:** 671
**Links Count:** 478
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# ConfluenceLoader\#

_class _langchain\_community.document\_loaders.confluence.ConfluenceLoader\(

    _url : str_,     _api\_key : str | None = None_,     _username : str | None = None_,     _session : Session | None = None_,     _oauth2 : dict | None = None_,     _token : str | None = None_,     _cloud : bool | None = True_,     _number\_of\_retries : int | None = 3_,     _min\_retry\_seconds : int | None = 2_,     _max\_retry\_seconds : int | None = 10_,     _confluence\_kwargs : dict | None = None_,     _\*_ ,     _cookies : dict | None = None_,     _space\_key : str | None = None_,     _page\_ids : List\[str\] | None = None_,     _label : str | None = None_,     _cql : str | None = None_,     _include\_restricted\_content : bool = False_,     _include\_archived\_content : bool = False_,     _include\_attachments : bool = False_,     _include\_comments : bool = False_,     _include\_labels : bool = False_,     _content\_format : [ContentFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat") = ContentFormat.STORAGE_,     _limit : int | None = 50_,     _max\_pages : int | None = 1000_,     _ocr\_languages : str | None = None_,     _keep\_markdown\_format : bool = False_,     _keep\_newlines : bool = False_,     _attachment\_filter\_func : Callable\[\[dict\], bool\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader)\#     

Load Confluence pages.

Port of <https://llamahub.ai/l/confluence> This currently supports username/api\_key, Oauth2 login, personal access token or cookies authentication.

Specify a list page\_ids and/or space\_key to load in the corresponding pages into Document objects, if both are specified the union of both sets will be returned.

You can also specify a boolean include\_attachments to include attachments, this is set to False by default, if set to True all attachments will be downloaded and ConfluenceLoader will extract the text from the attachments and add it to the Document object. Currently supported attachment types are: PDF, PNG, JPEG/JPG, SVG, Word and Excel.

Confluence API supports difference format of page content. The storage format is the raw XML representation for storage. The view format is the HTML representation for viewing with macros are rendered as though it is viewed by users. You can pass a enum content\_format argument to specify the content format, this is set to ContentFormat.STORAGE by default, the supported values are: ContentFormat.EDITOR, ContentFormat.EXPORT\_VIEW, ContentFormat.ANONYMOUS\_EXPORT\_VIEW, ContentFormat.STORAGE, and ContentFormat.VIEW.

Hint: space\_key and page\_id can both be found in the URL of a page in Confluence \- <https://yoursite.atlassian.com/wiki/spaces>/<space\_key>/pages/<page\_id>

Example               from langchain_community.document_loaders import ConfluenceLoader          loader = ConfluenceLoader(         url="https://yoursite.atlassian.com/wiki",         username="me",         api_key="12345",         space_key="SPACE",         limit=50,     )     documents = loader.load()          # Server on perm     loader = ConfluenceLoader(         url="https://confluence.yoursite.com/",         username="me",         api_key="your_password",         cloud=False,         space_key="SPACE",         limit=50,     )     documents = loader.load()     

Parameters:     

  * **url** \(_str_\) – \_description\_

  * **api\_key** \(_str_ _,__optional_\) – \_description\_, defaults to None

  * **username** \(_str_ _,__optional_\) – \_description\_, defaults to None

  * **oauth2** \(_dict_ _,__optional_\) – \_description\_, defaults to \{\}

  * **token** \(_str_ _,__optional_\) – \_description\_, defaults to None

  * **cloud** \(_bool_ _,__optional_\) – \_description\_, defaults to True

  * **number\_of\_retries** \(_Optional_ _\[__int_ _\]__,__optional_\) – How many times to retry, defaults to 3

  * **min\_retry\_seconds** \(_Optional_ _\[__int_ _\]__,__optional_\) – defaults to 2

  * **max\_retry\_seconds** \(_Optional_ _\[__int_ _\]__,__optional_\) – defaults to 10

  * **confluence\_kwargs** \(_dict_ _,__optional_\) – additional kwargs to initialize confluence with

  * **cookies** \(_dict_ _,__optional_\) – \_description\_, defaults to \{\}

  * **space\_key** \(_Optional_ _\[__str_ _\]__,__optional_\) – Space key retrieved from a confluence URL, defaults to None

  * **page\_ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]__,__optional_\) – List of specific page IDs to load, defaults to None

  * **label** \(_Optional_ _\[__str_ _\]__,__optional_\) – Get all pages with this label, defaults to None

  * **cql** \(_Optional_ _\[__str_ _\]__,__optional_\) – CQL Expression, defaults to None

  * **include\_restricted\_content** \(_bool_ _,__optional_\) – defaults to False

  * **include\_archived\_content** \(_bool_ _,__optional_\) – Whether to include archived content, defaults to False

  * **include\_attachments** \(_bool_ _,__optional_\) – defaults to False

  * **attachment\_filter\_func** \(_Callable_ _\[__\[__dict_ _\]__,__bool_ _\]__|__None_\) – A function that takes the attachment information from Confluence and decides whether or not the attachment is processed.

  * **include\_comments** \(_bool_ _,__optional_\) – defaults to False

  * **content\_format** \([_ContentFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat")\) – Specify content format, defaults to ContentFormat.STORAGE, the supported values are: ContentFormat.EDITOR, ContentFormat.EXPORT\_VIEW, ContentFormat.ANONYMOUS\_EXPORT\_VIEW, ContentFormat.STORAGE, and ContentFormat.VIEW.

  * **limit** \(_int_ _,__optional_\) – Maximum number of pages to retrieve per request, defaults to 50

  * **max\_pages** \(_int_ _,__optional_\) – Maximum number of pages to retrieve in total, defaults 1000

  * **ocr\_languages** \(_str_ _,__optional_\) – The languages to use for the Tesseract agent. To use a language, you’ll first need to install the appropriate Tesseract language pack.

  * **keep\_markdown\_format** \(_bool_\) – Whether to keep the markdown format, defaults to False

  * **keep\_newlines** \(_bool_\) – Whether to keep the newlines format, defaults to False

  * **session** \(_Session_ _|__None_\)

  * **include\_labels** \(_bool_\)

Raises:     

  * **ValueError** – Errors while validating input

  * **ImportError** – Required dependencies not installed.

Methods

`__init__`\(url\[, api\_key, username, session, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `is_public_page`\(page\) | Check if a page is publicly accessible.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\*\*kwargs\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `paginate_request`\(retrieval\_method, \*\*kwargs\) | Paginate the various methods to retrieve groups of pages.   `process_attachment`\(page\_id\[, ocr\_languages\]\) |    `process_doc`\(link\) |    `process_image`\(link\[, ocr\_languages\]\) |    `process_page`\(page, include\_attachments, ...\) |    `process_pages`\(pages, ...\[, ocr\_languages, ...\]\) | Process a list of pages into a list of documents.   `process_pdf`\(link\[, ocr\_languages\]\) |    `process_svg`\(link\[, ocr\_languages\]\) |    `process_xls`\(link\) |    `validate_init_args`\(\[url, api\_key, username, ...\]\) | Validates proper combinations of init arguments      \_\_init\_\_\(

    _url : str_,     _api\_key : str | None = None_,     _username : str | None = None_,     _session : Session | None = None_,     _oauth2 : dict | None = None_,     _token : str | None = None_,     _cloud : bool | None = True_,     _number\_of\_retries : int | None = 3_,     _min\_retry\_seconds : int | None = 2_,     _max\_retry\_seconds : int | None = 10_,     _confluence\_kwargs : dict | None = None_,     _\*_ ,     _cookies : dict | None = None_,     _space\_key : str | None = None_,     _page\_ids : List\[str\] | None = None_,     _label : str | None = None_,     _cql : str | None = None_,     _include\_restricted\_content : bool = False_,     _include\_archived\_content : bool = False_,     _include\_attachments : bool = False_,     _include\_comments : bool = False_,     _include\_labels : bool = False_,     _content\_format : [ContentFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat") = ContentFormat.STORAGE_,     _limit : int | None = 50_,     _max\_pages : int | None = 1000_,     _ocr\_languages : str | None = None_,     _keep\_markdown\_format : bool = False_,     _keep\_newlines : bool = False_,     _attachment\_filter\_func : Callable\[\[dict\], bool\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.__init__)\#     

Parameters:     

  * **url** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **session** \(_Session_ _|__None_\)

  * **oauth2** \(_dict_ _|__None_\)

  * **token** \(_str_ _|__None_\)

  * **cloud** \(_bool_ _|__None_\)

  * **number\_of\_retries** \(_int_ _|__None_\)

  * **min\_retry\_seconds** \(_int_ _|__None_\)

  * **max\_retry\_seconds** \(_int_ _|__None_\)

  * **confluence\_kwargs** \(_dict_ _|__None_\)

  * **cookies** \(_dict_ _|__None_\)

  * **space\_key** \(_str_ _|__None_\)

  * **page\_ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **label** \(_str_ _|__None_\)

  * **cql** \(_str_ _|__None_\)

  * **include\_restricted\_content** \(_bool_\)

  * **include\_archived\_content** \(_bool_\)

  * **include\_attachments** \(_bool_\)

  * **include\_comments** \(_bool_\)

  * **include\_labels** \(_bool_\)

  * **content\_format** \([_ContentFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat")\)

  * **limit** \(_int_ _|__None_\)

  * **max\_pages** \(_int_ _|__None_\)

  * **ocr\_languages** \(_str_ _|__None_\)

  * **keep\_markdown\_format** \(_bool_\)

  * **keep\_newlines** \(_bool_\)

  * **attachment\_filter\_func** \(_Callable_ _\[__\[__dict_ _\]__,__bool_ _\]__|__None_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

is\_public\_page\(_page : dict_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.is_public_page)\#     

Check if a page is publicly accessible.

Parameters:     

**page** \(_dict_\)

Return type:     

bool

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(

    _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.load)\#     

Load data into Document objects.

Parameters:     

**kwargs** \(_Any_\)

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

paginate\_request\(

    _retrieval\_method : Callable_,     _\*\* kwargs: Any_, \) → List[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.paginate_request)\#     

Paginate the various methods to retrieve groups of pages.

Unfortunately, due to page size, sometimes the Confluence API doesn’t match the limit value. If limit is >100 confluence seems to cap the response to 100. Also, due to the Atlassian Python package, we don’t get the “next” values from the “\_links” key because they only return the value from the result key. So here, the pagination starts from 0 and goes until the max\_pages, getting the limit number of pages with each request. We have to manually check if there are more docs based on the length of the returned list of pages, rather than just checking for the presence of a next key in the response like this page would have you do: <https://developer.atlassian.com/server/confluence/pagination-in-the-rest-api/>

Parameters:     

  * **retrieval\_method** \(_callable_\) – Function used to retrieve docs

  * **kwargs** \(_Any_\)

Returns:     

List of documents

Return type:     

List

process\_attachment\(

    _page\_id : str_,     _ocr\_languages : str | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_attachment)\#     

Parameters:     

  * **page\_id** \(_str_\)

  * **ocr\_languages** \(_str_ _|__None_\)

Return type:     

_List_\[str\]

process\_doc\(_link : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_doc)\#     

Parameters:     

**link** \(_str_\)

Return type:     

str

process\_image\(

    _link : str_,     _ocr\_languages : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_image)\#     

Parameters:     

  * **link** \(_str_\)

  * **ocr\_languages** \(_str_ _|__None_\)

Return type:     

str

process\_page\(

    _page : dict_,     _include\_attachments : bool_,     _include\_comments : bool_,     _include\_labels : bool_,     _content\_format : [ContentFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat")_,     _ocr\_languages : str | None = None_,     _keep\_markdown\_format : bool | None = False_,     _keep\_newlines : bool = False_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_page)\#     

Parameters:     

  * **page** \(_dict_\)

  * **include\_attachments** \(_bool_\)

  * **include\_comments** \(_bool_\)

  * **include\_labels** \(_bool_\)

  * **content\_format** \([_ContentFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat")\)

  * **ocr\_languages** \(_str_ _|__None_\)

  * **keep\_markdown\_format** \(_bool_ _|__None_\)

  * **keep\_newlines** \(_bool_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

process\_pages\(

    _pages : List\[dict\]_,     _include\_restricted\_content : bool_,     _include\_attachments : bool_,     _include\_comments : bool_,     _include\_labels : bool_,     _content\_format : [ContentFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat")_,     _ocr\_languages : str | None = None_,     _keep\_markdown\_format : bool | None = False_,     _keep\_newlines : bool = False_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_pages)\#     

Process a list of pages into a list of documents.

Parameters:     

  * **pages** \(_List_ _\[__dict_ _\]_\)

  * **include\_restricted\_content** \(_bool_\)

  * **include\_attachments** \(_bool_\)

  * **include\_comments** \(_bool_\)

  * **include\_labels** \(_bool_\)

  * **content\_format** \([_ContentFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html#langchain_community.document_loaders.confluence.ContentFormat "langchain_community.document_loaders.confluence.ContentFormat")\)

  * **ocr\_languages** \(_str_ _|__None_\)

  * **keep\_markdown\_format** \(_bool_ _|__None_\)

  * **keep\_newlines** \(_bool_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

process\_pdf\(

    _link : str_,     _ocr\_languages : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_pdf)\#     

Parameters:     

  * **link** \(_str_\)

  * **ocr\_languages** \(_str_ _|__None_\)

Return type:     

str

process\_svg\(

    _link : str_,     _ocr\_languages : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_svg)\#     

Parameters:     

  * **link** \(_str_\)

  * **ocr\_languages** \(_str_ _|__None_\)

Return type:     

str

process\_xls\(_link : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.process_xls)\#     

Parameters:     

**link** \(_str_\)

Return type:     

str

_static _validate\_init\_args\(

    _url : str | None = None_,     _api\_key : str | None = None_,     _username : str | None = None_,     _session : Session | None = None_,     _oauth2 : dict | None = None_,     _token : str | None = None_,     _cookies : dict | None = None_, \) → List | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/confluence.html#ConfluenceLoader.validate_init_args)\#     

Validates proper combinations of init arguments

Parameters:     

  * **url** \(_str_ _|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **session** \(_Session_ _|__None_\)

  * **oauth2** \(_dict_ _|__None_\)

  * **token** \(_str_ _|__None_\)

  * **cookies** \(_dict_ _|__None_\)

Return type:     

_List_ | None

Examples using ConfluenceLoader

  * [Confluence](https://python.langchain.com/docs/integrations/document_loaders/confluence/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)