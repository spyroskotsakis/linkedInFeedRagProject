# OCIGenAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.oci_generative_ai.OCIGenAIEmbeddings.html
**Word Count:** 292
**Links Count:** 242
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# OCIGenAIEmbeddings\#

_class _langchain\_community.embeddings.oci\_generative\_ai.OCIGenAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oci_generative_ai.html#OCIGenAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

OCI embedding models.

To authenticate, the OCI client uses the methods described in <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm>

The authentifcation method is passed through auth\_type and should be one of: API\_KEY \(default\), SECURITY\_TOKEN, INSTANCE\_PRINCIPLE, RESOURCE\_PRINCIPLE

Make sure you have the required policies \(profile/roles\) to access the OCI Generative AI service. If a specific config profile is used, you must pass the name of the profile \(~/.oci/config\) through auth\_profile. If a specific config file location is used, you must pass the file location where profile name configs present through auth\_file\_location

To use, you must provide the compartment id along with the endpoint url, and model id as named parameters to the constructor.

Example               from langchain.embeddings import OCIGenAIEmbeddings          embeddings = OCIGenAIEmbeddings(         model_id="MY_EMBEDDING_MODEL",         service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",         compartment_id="MY_OCID"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _auth\_file\_location _: str | None_ _ = '~/.oci/config'_\#     

Path to the config file. If not specified, ~/.oci/config will be used

_param _auth\_profile _: str | None_ _ = 'DEFAULT'_\#     

The name of the profile in ~/.oci/config If not specified , DEFAULT will be used

_param _auth\_type _: str | None_ _ = 'API\_KEY'_\#     

Authentication type, could be

API\_KEY, SECURITY\_TOKEN, INSTANCE\_PRINCIPLE, RESOURCE\_PRINCIPLE

If not specified, API\_KEY will be used

_param _batch\_size _: int_ _ = 96_\#     

Batch size of OCI GenAI embedding requests. OCI GenAI may handle up to 96 texts per request

_param _compartment\_id _: str | None_ _ = None_\#     

OCID of compartment

_param _model\_id _: str | None_ _ = None_\#     

Id of the model to call, e.g., cohere.embed-english-light-v2.0

_param _model\_kwargs _: Dict | None_ _ = None_\#     

Keyword arguments to pass to the model

_param _service\_endpoint _: str | None_ _ = None_\#     

service endpoint url

_param _truncate _: str | None_ _ = 'END'_\#     

Truncate embeddings that are too long from start or end \(“NONE”|”START”|”END”\)

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oci_generative_ai.html#OCIGenAIEmbeddings.validate_environment)\#     

Validate that OCI config and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oci_generative_ai.html#OCIGenAIEmbeddings.embed_documents)\#     

Call out to OCIGenAI’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oci_generative_ai.html#OCIGenAIEmbeddings.embed_query)\#     

Call out to OCIGenAI’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using OCIGenAIEmbeddings

  * [Oracle Cloud Infrastructure \(OCI\)](https://python.langchain.com/docs/integrations/providers/oci/)

  * [Oracle Cloud Infrastructure Generative AI](https://python.langchain.com/docs/integrations/text_embedding/oci_generative_ai/)

__On this page