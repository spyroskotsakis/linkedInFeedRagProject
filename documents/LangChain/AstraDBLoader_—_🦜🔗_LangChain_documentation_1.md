# AstraDBLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.astradb.AstraDBLoader.html
**Word Count:** 311
**Links Count:** 422
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# AstraDBLoader\#

_class _langchain\_community.document\_loaders.astradb.AstraDBLoader\(_collection\_name: str, \*, token: Optional\[str\] = None, api\_endpoint: Optional\[str\] = None, astra\_db\_client: Optional\[AstraDB\] = None, async\_astra\_db\_client: Optional\[AsyncAstraDB\] = None, namespace: Optional\[str\] = None, filter\_criteria: Optional\[Dict\[str, Any\]\] = None, projection: Optional\[Dict\[str, Any\]\] = None, find\_options: Optional\[Dict\[str, Any\]\] = None, nb\_prefetched: int = 1000, extraction\_function: Callable\[\[Dict\], str\] = <function dumps>_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/astradb.html#AstraDBLoader)\#     

Deprecated since version 0.0.29: Use `:class:`~langchain_astradb.AstraDBLoader`` instead. It will not be removed until langchain-community==1.0.

Load DataStax Astra DB documents.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is. Defaults to the database’s “default namespace”.

  * **filter\_criteria** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Criteria to filter documents.

  * **projection** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Specifies the fields to return.

  * **find\_options** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Additional options for the query.

  * **nb\_prefetched** \(_int_\) – Max number of documents to pre-fetch. Defaults to 1000.

  * **extraction\_function** \(_Callable_ _\[__\[__Dict_ _\]__,__str_ _\]_\) – Function applied to collection documents to create the page\_content of the LangChain Document. Defaults to json.dumps.

Methods

`__init__`\(collection\_name, \*\[, token, ...\]\) | Load DataStax Astra DB documents.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(_collection\_name: str, \*, token: Optional\[str\] = None, api\_endpoint: Optional\[str\] = None, astra\_db\_client: Optional\[AstraDB\] = None, async\_astra\_db\_client: Optional\[AsyncAstraDB\] = None, namespace: Optional\[str\] = None, filter\_criteria: Optional\[Dict\[str, Any\]\] = None, projection: Optional\[Dict\[str, Any\]\] = None, find\_options: Optional\[Dict\[str, Any\]\] = None, nb\_prefetched: int = 1000, extraction\_function: Callable\[\[Dict\], str\] = <function dumps>_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/astradb.html#AstraDBLoader.__init__)\#     

Load DataStax Astra DB documents.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is. Defaults to the database’s “default namespace”.

  * **filter\_criteria** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Criteria to filter documents.

  * **projection** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Specifies the fields to return.

  * **find\_options** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Additional options for the query.

  * **nb\_prefetched** \(_int_\) – Max number of documents to pre-fetch. Defaults to 1000.

  * **extraction\_function** \(_Callable_ _\[__\[__Dict_ _\]__,__str_ _\]_\) – Function applied to collection documents to create the page\_content of the LangChain Document. Defaults to json.dumps.

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/astradb.html#AstraDBLoader.alazy_load)\#     

A lazy loader for Documents.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/astradb.html#AstraDBLoader.aload)\#     

Load data into Document objects.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/astradb.html#AstraDBLoader.lazy_load)\#     

A lazy loader for Documents.

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

Examples using AstraDBLoader

  * [AstraDB](https://python.langchain.com/docs/integrations/document_loaders/astradb/)

__On this page