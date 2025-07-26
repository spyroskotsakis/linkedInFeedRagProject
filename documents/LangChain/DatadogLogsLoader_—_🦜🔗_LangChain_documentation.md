# DatadogLogsLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.datadog_logs.DatadogLogsLoader.html
**Word Count:** 282
**Links Count:** 424
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# DatadogLogsLoader\#

_class _langchain\_community.document\_loaders.datadog\_logs.DatadogLogsLoader\(

    _query : str_,     _api\_key : str_,     _app\_key : str_,     _from\_time : int | None = None_,     _to\_time : int | None = None_,     _limit : int = 100_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/datadog_logs.html#DatadogLogsLoader)\#     

Load Datadog logs.

Logs are written into the page\_content and into the metadata.

Initialize Datadog document loader.

Requirements:     

  * Must have datadog\_api\_client installed. Install with pip install datadog\_api\_client.

Parameters:     

  * **query** \(_str_\) – The query to run in Datadog.

  * **api\_key** \(_str_\) – The Datadog API key.

  * **app\_key** \(_str_\) – The Datadog APP key.

  * **from\_time** \(_int_ _|__None_\) – Optional. The start of the time range to query. Supports date math and regular timestamps \(milliseconds\) like ‘1688732708951’ Defaults to 20 minutes ago.

  * **to\_time** \(_int_ _|__None_\) – Optional. The end of the time range to query. Supports date math and regular timestamps \(milliseconds\) like ‘1688732708951’ Defaults to now.

  * **limit** \(_int_\) – The maximum number of logs to return. Defaults to 100.

Methods

`__init__`\(query, api\_key, app\_key\[, ...\]\) | Initialize Datadog document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Get logs from Datadog.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `parse_log`\(log\) | Create Document objects from Datadog log items.      \_\_init\_\_\(

    _query : str_,     _api\_key : str_,     _app\_key : str_,     _from\_time : int | None = None_,     _to\_time : int | None = None_,     _limit : int = 100_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/datadog_logs.html#DatadogLogsLoader.__init__)\#     

Initialize Datadog document loader.

Requirements:     

  * Must have datadog\_api\_client installed. Install with pip install datadog\_api\_client.

Parameters:     

  * **query** \(_str_\) – The query to run in Datadog.

  * **api\_key** \(_str_\) – The Datadog API key.

  * **app\_key** \(_str_\) – The Datadog APP key.

  * **from\_time** \(_int_ _|__None_\) – Optional. The start of the time range to query. Supports date math and regular timestamps \(milliseconds\) like ‘1688732708951’ Defaults to 20 minutes ago.

  * **to\_time** \(_int_ _|__None_\) – Optional. The end of the time range to query. Supports date math and regular timestamps \(milliseconds\) like ‘1688732708951’ Defaults to now.

  * **limit** \(_int_\) – The maximum number of logs to return. Defaults to 100.

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/datadog_logs.html#DatadogLogsLoader.load)\#     

Get logs from Datadog.

Returns:     

A list of Document objects.     

  * page\_content

  * metadata          * id

    * service

    * status

    * tags

    * timestamp

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

parse\_log\(

    _log : dict_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/datadog_logs.html#DatadogLogsLoader.parse_log)\#     

Create Document objects from Datadog log items.

Parameters:     

**log** \(_dict_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

Examples using DatadogLogsLoader

  * [Datadog Logs](https://python.langchain.com/docs/integrations/document_loaders/datadog_logs/)

__On this page