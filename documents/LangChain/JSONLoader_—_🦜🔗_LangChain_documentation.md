# JSONLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.json_loader.JSONLoader.html
**Word Count:** 475
**Links Count:** 420
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# JSONLoader\#

_class _langchain\_community.document\_loaders.json\_loader.JSONLoader\(

    _file\_path : str | PathLike_,     _jq\_schema : str_,     _content\_key : str | None = None_,     _is\_content\_key\_jq\_parsable : bool | None = False_,     _metadata\_func : Callable\[\[Dict, Dict\], Dict\] | None = None_,     _text\_content : bool = True_,     _json\_lines : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/json_loader.html#JSONLoader)\#     

Load a JSON file using a jq schema.

Setup:                    pip install -U jq     

Instantiate:                    from langchain_community.document_loaders import JSONLoader     import json     from pathlib import Path          file_path='./sample_quiz.json'     data = json.loads(Path(file_path).read_text())     loader = JSONLoader(              file_path=file_path,              jq_schema='.quiz',              text_content=False)     

Load:                    docs = loader.load()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    {"sport": {"q1": {"question": "Which one is correct team name in     NBA?", "options": ["New York Bulls"     {'source': '/sample_quiz     .json', 'seq_num': 1}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    {"sport": {"q1": {"question": "Which one is correct team name in     NBA?", "options": ["New York Bulls"     {'source': '/sample_quizg     .json', 'seq_num': 1}     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    {"sport": {"q1": {"question": "Which one is correct team name in     NBA?", "options": ["New York Bulls"     {'source': '/sample_quiz     .json', 'seq_num': 1}     

Initialize the JSONLoader.

Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__PathLike_ _\]_\) – The path to the JSON or JSON Lines file.

  * **jq\_schema** \(_str_\) – The jq schema to use to extract the data or text from the JSON.

  * **content\_key** \(_str_\) – The key to use to extract the content from the JSON if the jq\_schema results to a list of objects \(dict\). If is\_content\_key\_jq\_parsable is True, this has to be a jq compatible schema. If is\_content\_key\_jq\_parsable is False, this should be a simple string key.

  * **is\_content\_key\_jq\_parsable** \(_bool_\) – A flag to determine if content\_key is parsable by jq or not. If True, content\_key is treated as a jq schema and compiled accordingly. If False or if content\_key is None, content\_key is used as a simple string. Default is False.

  * **metadata\_func** \(_Callable_ _\[__Dict_ _,__Dict_ _\]_\) – A function that takes in the JSON object extracted by the jq\_schema and the default metadata and returns a dict of the updated metadata.

  * **text\_content** \(_bool_\) – Boolean flag to indicate whether the content is in string format, default to True.

  * **json\_lines** \(_bool_\) – Boolean flag to indicate whether the input is in JSON Lines format.

Methods

`__init__`\(file\_path, jq\_schema\[, ...\]\) | Initialize the JSONLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load and return documents from the JSON file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | PathLike_,     _jq\_schema : str_,     _content\_key : str | None = None_,     _is\_content\_key\_jq\_parsable : bool | None = False_,     _metadata\_func : Callable\[\[Dict, Dict\], Dict\] | None = None_,     _text\_content : bool = True_,     _json\_lines : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/json_loader.html#JSONLoader.__init__)\#     

Initialize the JSONLoader.

Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__PathLike_ _\]_\) – The path to the JSON or JSON Lines file.

  * **jq\_schema** \(_str_\) – The jq schema to use to extract the data or text from the JSON.

  * **content\_key** \(_str_\) – The key to use to extract the content from the JSON if the jq\_schema results to a list of objects \(dict\). If is\_content\_key\_jq\_parsable is True, this has to be a jq compatible schema. If is\_content\_key\_jq\_parsable is False, this should be a simple string key.

  * **is\_content\_key\_jq\_parsable** \(_bool_\) – A flag to determine if content\_key is parsable by jq or not. If True, content\_key is treated as a jq schema and compiled accordingly. If False or if content\_key is None, content\_key is used as a simple string. Default is False.

  * **metadata\_func** \(_Callable_ _\[__Dict_ _,__Dict_ _\]_\) – A function that takes in the JSON object extracted by the jq\_schema and the default metadata and returns a dict of the updated metadata.

  * **text\_content** \(_bool_\) – Boolean flag to indicate whether the content is in string format, default to True.

  * **json\_lines** \(_bool_\) – Boolean flag to indicate whether the input is in JSON Lines format.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/json_loader.html#JSONLoader.lazy_load)\#     

Load and return documents from the JSON file.

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

Examples using JSONLoader

  * [How to load JSON](https://python.langchain.com/docs/how_to/document_loader_json/)

  * [JSONLoader](https://python.langchain.com/docs/integrations/document_loaders/json/)

  * [Timescale Vector \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/timescalevector/)

__On this page