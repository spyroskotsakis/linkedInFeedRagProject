# AstraDBLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/document_loaders/langchain_astradb.document_loaders.AstraDBLoader.html
**Word Count:** 693
**Links Count:** 109
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBLoader\#

_class _langchain\_astradb.document\_loaders.AstraDBLoader\(_collection\_name: str, \*, token: str | TokenProvider | None = None, api\_endpoint: str | None = None, environment: str | None = None, namespace: str | None = None, filter\_criteria: dict\[str, Any\] | None = None, projection: dict\[str, Any\] | None = <object object>, limit: int | None = None, nb\_prefetched: int = <object object>, page\_content\_mapper: Callable\[\[dict\], str\] = <function dumps>, metadata\_mapper: Callable\[\[dict\], dict\[str, Any\]\] | None = None, ext\_callers: list\[tuple\[str | None, str | None\] | str | None\] | None = None, api\_options: APIOptions | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/document_loaders.html#AstraDBLoader)\#     

Load DataStax Astra DB documents.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection resides. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **filter\_criteria** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Criteria to filter documents.

  * **projection** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Specifies the fields to return. If not provided, reads fall back to the Data API default projection.

  * **limit** \(_int_ _|__None_\) – a maximum number of documents to return in the read query.

  * **nb\_prefetched** \(_int_\) – Max number of documents to pre-fetch. _IGNORED starting from v. 0.3.5: astrapy v1.0+ does not support it._

  * **page\_content\_mapper** \(_Callable_ _\[__\[__dict_ _\]__,__str_ _\]_\) – Function applied to collection documents to create the page\_content of the LangChain Document. Defaults to json.dumps.

  * **metadata\_mapper** \(_Callable_ _\[__\[__dict_ _\]__,__dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – 

Function applied to collection documents to create the metadata of the LangChain Document. Defaults to returning the

> namespace, API endpoint and collection name.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Methods

`__init__`\(collection\_name, \*\[, token, ...\]\) | Load DataStax Astra DB documents.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(_collection\_name: str, \*, token: str | TokenProvider | None = None, api\_endpoint: str | None = None, environment: str | None = None, namespace: str | None = None, filter\_criteria: dict\[str, Any\] | None = None, projection: dict\[str, Any\] | None = <object object>, limit: int | None = None, nb\_prefetched: int = <object object>, page\_content\_mapper: Callable\[\[dict\], str\] = <function dumps>, metadata\_mapper: Callable\[\[dict\], dict\[str, Any\]\] | None = None, ext\_callers: list\[tuple\[str | None, str | None\] | str | None\] | None = None, api\_options: APIOptions | None = None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/document_loaders.html#AstraDBLoader.__init__)\#     

Load DataStax Astra DB documents.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection resides. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **filter\_criteria** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Criteria to filter documents.

  * **projection** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Specifies the fields to return. If not provided, reads fall back to the Data API default projection.

  * **limit** \(_int_ _|__None_\) – a maximum number of documents to return in the read query.

  * **nb\_prefetched** \(_int_\) – Max number of documents to pre-fetch. _IGNORED starting from v. 0.3.5: astrapy v1.0+ does not support it._

  * **page\_content\_mapper** \(_Callable_ _\[__\[__dict_ _\]__,__str_ _\]_\) – Function applied to collection documents to create the page\_content of the LangChain Document. Defaults to json.dumps.

  * **metadata\_mapper** \(_Callable_ _\[__\[__dict_ _\]__,__dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – 

Function applied to collection documents to create the metadata of the LangChain Document. Defaults to returning the

> namespace, API endpoint and collection name.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/document_loaders.html#AstraDBLoader.alazy_load)\#     

A lazy loader for Documents.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/document_loaders.html#AstraDBLoader.aload)\#     

Load data into Document objects.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/document_loaders.html#AstraDBLoader.lazy_load)\#     

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