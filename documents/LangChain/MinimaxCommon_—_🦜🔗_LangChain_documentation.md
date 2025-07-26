# MinimaxCommon — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.minimax.MinimaxCommon.html
**Word Count:** 93
**Links Count:** 301
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# MinimaxCommon\#

_class _langchain\_community.llms.minimax.MinimaxCommon[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/minimax.html#MinimaxCommon)\#     

Bases: `BaseModel`

Common parameters for Minimax large language models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _max\_tokens _: int_ _ = 256_\#     

Denotes the number of tokens to predict per generation.

_param _minimax\_api\_host _: str | None_ _ = None_\#     

_param _minimax\_api\_key _: SecretStr | None_ _ = None_\#     

_param _minimax\_group\_id _: str | None_ _ = None_\#     

_param _model _: str_ _ = 'abab5.5-chat'_\#     

Model name to use.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _temperature _: float_ _ = 0.7_\#     

A non-negative float that tunes the degree of randomness in generation.

_param _top\_p _: float_ _ = 0.95_\#     

Total probability mass of tokens to consider at each step.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/minimax.html#MinimaxCommon.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page