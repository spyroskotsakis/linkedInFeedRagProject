# OCIGenAIBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.oci_generative_ai.OCIGenAIBase.html
**Word Count:** 132
**Links Count:** 303
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# OCIGenAIBase\#

_class _langchain\_community.llms.oci\_generative\_ai.OCIGenAIBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/oci_generative_ai.html#OCIGenAIBase)\#     

Bases: `BaseModel`, `ABC`

Base class for OCI GenAI models

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _auth\_file\_location _: str | None_ _ = '~/.oci/config'_\#     

Path to the config file. If not specified, ~/.oci/config will be used

_param _auth\_profile _: str | None_ _ = 'DEFAULT'_\#     

The name of the profile in ~/.oci/config If not specified , DEFAULT will be used

_param _auth\_type _: str | None_ _ = 'API\_KEY'_\#     

Authentication type, could be

API\_KEY, SECURITY\_TOKEN, INSTANCE\_PRINCIPAL, RESOURCE\_PRINCIPAL

If not specified, API\_KEY will be used

_param _compartment\_id _: str | None_ _ = None_\#     

OCID of compartment

_param _is\_stream _: bool_ _ = False_\#     

Whether to stream back partial progress

_param _model\_id _: str | None_ _ = None_\#     

Id of the model to call, e.g., cohere.command

_param _model\_kwargs _: Dict | None_ _ = None_\#     

Keyword arguments to pass to the model

_param _provider _: str | None_ _ = None_\#     

Provider name of the model. Default to None, will try to be derived from the model\_id otherwise, requires user input

_param _service\_endpoint _: str | None_ _ = None_\#     

service endpoint url

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/oci_generative_ai.html#OCIGenAIBase.validate_environment)\#     

Validate that OCI config and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page