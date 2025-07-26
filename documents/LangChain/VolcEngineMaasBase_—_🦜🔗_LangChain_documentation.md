# VolcEngineMaasBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.volcengine_maas.VolcEngineMaasBase.html
**Word Count:** 145
**Links Count:** 313
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# VolcEngineMaasBase\#

_class _langchain\_community.llms.volcengine\_maas.VolcEngineMaasBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/volcengine_maas.html#VolcEngineMaasBase)\#     

Bases: `BaseModel`

Base class for VolcEngineMaas models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

_param _connect\_timeout _: int | None_ _ = 60_\#     

Timeout for connect to volc engine maas endpoint. Default is 60 seconds.

_param _endpoint _: str | None_ _ = 'maas-api.ml-platform-cn-beijing.volces.com'_\#     

Endpoint of the VolcEngineMaas LLM.

_param _model _: str_ _ = 'skylark-lite-public'_\#     

Model name. you could check this model details here <https://www.volcengine.com/docs/82379/1133187> and you could choose other models by change this field

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

model special arguments, you could check detail on model page

_param _model\_version _: str | None_ _ = None_\#     

Model version. Only used in moonshot large language model. you could check details here <https://www.volcengine.com/docs/82379/1158281>

_param _read\_timeout _: int | None_ _ = 60_\#     

Timeout for read response from volc engine maas endpoint. Default is 60 seconds.

_param _region _: str | None_ _ = 'Region'_\#     

Region of the VolcEngineMaas LLM.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results.

_param _temperature _: float | None_ _ = 0.95_\#     

A non-negative float that tunes the degree of randomness in generation.

_param _top\_p _: float | None_ _ = 0.8_\#     

Total probability mass of tokens to consider at each step.

_param _volc\_engine\_maas\_ak _: SecretStr | None_ _ = None_\#     

access key for volc engine

_param _volc\_engine\_maas\_sk _: SecretStr | None_ _ = None_\#     

secret key for volc engine

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/volcengine_maas.html#VolcEngineMaasBase.validate_environment)\#     

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page