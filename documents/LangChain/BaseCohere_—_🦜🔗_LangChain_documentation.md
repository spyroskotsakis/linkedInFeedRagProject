# BaseCohere — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.cohere.BaseCohere.html
**Word Count:** 66
**Links Count:** 298
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# BaseCohere\#

_class _langchain\_community.llms.cohere.BaseCohere[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/cohere.html#BaseCohere)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Deprecated since version 0.0.30: Use `:class:`~langchain_cohere.BaseCohere`` instead. It will not be removed until langchain-community==1.0.

Base class for Cohere models.

_param _cohere\_api\_key _: SecretStr | None_ _ = None_\#     

Cohere API key. If not provided, will be read from the environment variable.

_param _model _: str | None_ _ = None_\#     

Model name to use.

_param _stop _: List\[str\] | None_ _ = None_\#     

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results.

_param _temperature _: float_ _ = 0.75_\#     

A non-negative float that tunes the degree of randomness in generation.

_param _user\_agent _: str_ _ = 'langchain'_\#     

Identifier for the application making the request.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/cohere.html#BaseCohere.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page