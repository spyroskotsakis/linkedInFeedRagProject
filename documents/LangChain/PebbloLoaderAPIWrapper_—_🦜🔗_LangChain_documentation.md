# PebbloLoaderAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.PebbloLoaderAPIWrapper.html
**Word Count:** 255
**Links Count:** 290
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# PebbloLoaderAPIWrapper\#

_class _langchain\_community.utilities.pebblo.PebbloLoaderAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Pebblo Loader API.

Validate that api key in environment.

_param _anonymize\_snippets _: bool_ _ = False_\#     

Whether to anonymize snippets going into VectorDB and the generated reports

_param _api\_key _: str | None_ _\[Required\]_\#     

API key for Pebblo Cloud

_param _classifier\_location _: str_ _ = 'local'_\#     

Location of the classifier, local or cloud. Defaults to ‘local’

_param _classifier\_url _: str | None_ _\[Required\]_\#     

URL of the Pebblo Classifier

_param _cloud\_url _: str | None_ _\[Required\]_\#     

URL of the Pebblo Cloud

_static _make\_request\(

    _method : str_,     _url : str_,     _headers : dict_,     _payload : dict | None = None_,     _timeout : int = 20_, \) → Response | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.make_request)\#     

Make a request to the Pebblo API

Parameters:     

  * **method** \(_str_\) – HTTP method \(GET, POST, PUT, DELETE, etc.\).

  * **url** \(_str_\) – URL for the request.

  * **headers** \(_dict_\) – Headers for the request.

  * **payload** \(_Optional_ _\[__dict_ _\]_\) – Payload for the request \(for POST, PUT, etc.\).

  * **timeout** \(_int_\) – Timeout for the request in seconds.

Returns:     

Response object if the request is successful.

Return type:     

Optional\[Response\]

_static _prepare\_docs\_for\_classification\(

    _docs\_with\_id : List\[[IndexedDocument](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.IndexedDocument.html#langchain_community.utilities.pebblo.IndexedDocument "langchain_community.utilities.pebblo.IndexedDocument")\]_,     _source\_path : str_,     _loader\_details : dict_, \) → Tuple\[List\[dict\], int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.prepare_docs_for_classification)\#     

Prepare documents for classification.

Parameters:     

  * **docs\_with\_id** \(_List_ _\[_[_IndexedDocument_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.IndexedDocument.html#langchain_community.utilities.pebblo.IndexedDocument "langchain_community.utilities.pebblo.IndexedDocument") _\]_\) – List of documents to be classified.

  * **source\_path** \(_str_\) – Source path of the documents.

  * **loader\_details** \(_dict_\) – Contains loader info.

Returns:     

Documents and the aggregate size of the source.

Return type:     

Tuple\[List\[dict\], int\]

_static _update\_doc\_data\(

    _docs : List\[dict\]_,     _classified\_docs : dict_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.update_doc_data)\#     

Update the document data with classified information.

Parameters:     

  * **docs** \(_List_ _\[__dict_ _\]_\) – List of document data to be updated.

  * **classified\_docs** \(_dict_\) – The dictionary containing classified documents.

Return type:     

None

build\_classification\_payload\(

    _app : [App](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")_,     _docs : List\[dict\]_,     _loader\_details : dict_,     _source\_owner : str_,     _source\_aggregate\_size : int_,     _loading\_end : bool_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.build_classification_payload)\#     

Build the payload for document classification.

Parameters:     

  * **app** \([_App_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")\) – App instance.

  * **docs** \(_List_ _\[__dict_ _\]_\) – List of documents to be classified.

  * **loader\_details** \(_dict_\) – Loader details.

  * **source\_owner** \(_str_\) – Owner of the source.

  * **source\_aggregate\_size** \(_int_\) – Aggregate size of the source.

  * **loading\_end** \(_bool_\) – Boolean indicating the halt of data loading by loader.

Returns:     

Payload for document classification.

Return type:     

dict

classify\_documents\(

    _docs\_with\_id : List\[[IndexedDocument](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.IndexedDocument.html#langchain_community.utilities.pebblo.IndexedDocument "langchain_community.utilities.pebblo.IndexedDocument")\]_,     _app : [App](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")_,     _loader\_details : dict_,     _loading\_end : bool = False_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.classify_documents)\#     

Send documents to Pebblo server for classification. Then send classified documents to Daxa cloud\(If api\_key is present\).

Parameters:     

  * **docs\_with\_id** \(_List_ _\[_[_IndexedDocument_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.IndexedDocument.html#langchain_community.utilities.pebblo.IndexedDocument "langchain_community.utilities.pebblo.IndexedDocument") _\]_\) – List of documents to be classified.

  * **app** \([_App_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")\) – App instance.

  * **loader\_details** \(_dict_\) – Loader details.

  * **loading\_end** \(_bool_\) – Boolean, indicating the halt of data loading by loader.

Return type:     

dict

send\_docs\_to\_pebblo\_cloud\(

    _payload : dict_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.send_docs_to_pebblo_cloud)\#     

Send documents to Pebblo cloud.

Parameters:     

**payload** \(_dict_\) – The payload containing documents to be sent.

Return type:     

None

send\_loader\_discover\(

    _app : [App](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#PebbloLoaderAPIWrapper.send_loader_discover)\#     

Send app discovery request to Pebblo server & cloud.

Parameters:     

**app** \([_App_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")\) – App instance to be discovered.

Return type:     

None

__On this page