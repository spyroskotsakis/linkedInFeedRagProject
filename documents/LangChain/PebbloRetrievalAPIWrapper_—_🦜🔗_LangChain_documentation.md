# PebbloRetrievalAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.utilities.PebbloRetrievalAPIWrapper.html
**Word Count:** 476
**Links Count:** 214
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# PebbloRetrievalAPIWrapper\#

_class _langchain\_community.chains.pebblo\_retrieval.utilities.PebbloRetrievalAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Pebblo Retrieval API.

Validate that api key in environment.

_param _api\_key _: str | None_ _\[Required\]_\#     

API key for Pebblo Cloud

_param _classifier\_location _: str_ _ = 'local'_\#     

Location of the classifier, local or cloud. Defaults to ‘local’

_param _classifier\_url _: str | None_ _\[Required\]_\#     

URL of the Pebblo Classifier

_param _cloud\_url _: str | None_ _\[Required\]_\#     

URL of the Pebblo Cloud

_async static _amake\_request\(

    _method : str_,     _url : str_,     _headers : dict_,     _payload : dict | None = None_,     _timeout : int = 20_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.amake_request)\#     

Make a async request to the Pebblo server/cloud API.

Parameters:     

  * **method** \(_str_\) – HTTP method \(GET, POST, PUT, DELETE, etc.\).

  * **url** \(_str_\) – URL for the request.

  * **headers** \(_dict_\) – Headers for the request.

  * **payload** \(_Optional_ _\[__dict_ _\]_\) – Payload for the request \(for POST, PUT, etc.\).

  * **timeout** \(_int_\) – Timeout for the request in seconds.

Returns:     

Response json if the request is successful.

Return type:     

Any

_static _make\_request\(

    _method : str_,     _url : str_,     _headers : dict_,     _payload : dict | None = None_,     _timeout : int = 20_, \) → Response | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.make_request)\#     

Make a request to the Pebblo server/cloud API.

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

_static _update\_cloud\_payload\(

    _payload : dict_,     _pebblo\_resp : dict | None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.update_cloud_payload)\#     

Update the payload with response, prompt and context from Pebblo response.

Parameters:     

  * **payload** \(_dict_\) – Payload to be updated.

  * **pebblo\_resp** \(_Optional_ _\[__dict_ _\]_\) – Response from Pebblo server.

Return type:     

None

_async _acheck\_prompt\_validity\(

    _question : str_, \) → Tuple\[bool, Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.acheck_prompt_validity)\#     

Check the validity of the given prompt using a remote classification service.

This method sends a prompt to a remote classifier service and return entities present in prompt or not.

Parameters:     

**question** \(_str_\) – The prompt question to be validated.

Returns:     

True if the prompt is valid \(does not contain deny list entities\), False otherwise. dict: The entities present in the prompt

Return type:     

bool

_async _asend\_prompt\(

    _app\_name : str_,     _retriever : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _question : str_,     _answer : str_,     _auth\_context : [AuthContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") | None_,     _docs : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _prompt\_entities : Dict\[str, Any\]_,     _prompt\_time : str_,     _prompt\_gov\_enabled : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.asend_prompt)\#     

Send prompt to Pebblo server for classification. Then send prompt to Daxa cloud\(If api\_key is present\).

Parameters:     

  * **app\_name** \(_str_\) – Name of the app.

  * **retriever** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\) – Retriever instance.

  * **question** \(_str_\) – Question asked in the prompt.

  * **answer** \(_str_\) – Answer generated by the model.

  * **auth\_context** \(_Optional_ _\[_[_AuthContext_](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") _\]_\) – Authentication context.

  * **docs** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of documents retrieved.

  * **prompt\_entities** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – Entities present in the prompt.

  * **prompt\_time** \(_str_\) – Time when the prompt was generated.

  * **prompt\_gov\_enabled** \(_bool_\) – Whether prompt governance is enabled.

Return type:     

None

build\_prompt\_qa\_payload\(

    _app\_name : str_,     _retriever : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _question : str_,     _answer : str_,     _auth\_context : [AuthContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") | None_,     _docs : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _prompt\_entities : Dict\[str, Any\]_,     _prompt\_time : str_,     _prompt\_gov\_enabled : bool = False_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.build_prompt_qa_payload)\#     

Build the QA payload for the prompt.

> Args: >      >  > app\_name \(str\): Name of the app. retriever \(VectorStoreRetriever\): Retriever instance. question \(str\): Question asked in the prompt. answer \(str\): Answer generated by the model. auth\_context \(Optional\[AuthContext\]\): Authentication context. docs \(List\[Document\]\): List of documents retrieved. prompt\_entities \(Dict\[str, Any\]\): Entities present in the prompt. prompt\_time \(str\): Time when the prompt was generated. prompt\_gov\_enabled \(bool\): Whether prompt governance is enabled.

Returns:     

The QA payload for the prompt.

Return type:     

dict

Parameters:     

  * **app\_name** \(_str_\)

  * **retriever** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\)

  * **question** \(_str_\)

  * **answer** \(_str_\)

  * **auth\_context** \([_AuthContext_](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") _|__None_\)

  * **docs** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **prompt\_entities** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **prompt\_time** \(_str_\)

  * **prompt\_gov\_enabled** \(_bool_\)

check\_prompt\_validity\(

    _question : str_, \) → Tuple\[bool, Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.check_prompt_validity)\#     

Check the validity of the given prompt using a remote classification service.

This method sends a prompt to a remote classifier service and return entities present in prompt or not.

Parameters:     

**question** \(_str_\) – The prompt question to be validated.

Returns:     

True if the prompt is valid \(does not contain deny list entities\), False otherwise. dict: The entities present in the prompt

Return type:     

bool

send\_app\_discover\(

    _app : [App](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.App.html#langchain_community.chains.pebblo_retrieval.models.App "langchain_community.chains.pebblo_retrieval.models.App")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.send_app_discover)\#     

Send app discovery request to Pebblo server & cloud.

Parameters:     

**app** \([_App_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html#langchain_community.utilities.pebblo.App "langchain_community.utilities.pebblo.App")\) – App instance to be discovered.

Return type:     

None

send\_prompt\(

    _app\_name : str_,     _retriever : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _question : str_,     _answer : str_,     _auth\_context : [AuthContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") | None_,     _docs : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _prompt\_entities : Dict\[str, Any\]_,     _prompt\_time : str_,     _prompt\_gov\_enabled : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/utilities.html#PebbloRetrievalAPIWrapper.send_prompt)\#     

Send prompt to Pebblo server for classification. Then send prompt to Daxa cloud\(If api\_key is present\).

Parameters:     

  * **app\_name** \(_str_\) – Name of the app.

  * **retriever** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\) – Retriever instance.

  * **question** \(_str_\) – Question asked in the prompt.

  * **answer** \(_str_\) – Answer generated by the model.

  * **auth\_context** \(_Optional_ _\[_[_AuthContext_](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") _\]_\) – Authentication context.

  * **docs** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of documents retrieved.

  * **prompt\_entities** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – Entities present in the prompt.

  * **prompt\_time** \(_str_\) – Time when the prompt was generated.

  * **prompt\_gov\_enabled** \(_bool_\) – Whether prompt governance is enabled.

Return type:     

None

__On this page