# BaseFriendli — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.friendli.BaseFriendli.html
**Word Count:** 19
**Links Count:** 310
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# BaseFriendli\#

_class _langchain\_community.llms.friendli.BaseFriendli[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/friendli.html#BaseFriendli)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Base class of Friendli.

_param _async\_client _: Any_ _ = None_\#     

_param _client _: Any_ _ = None_\#     

_param _frequency\_penalty _: float | None_ _ = None_\#     

_param _friendli\_team _: str | None_ _ = None_\#     

_param _friendli\_token _: SecretStr | None_ _ = None_\#     

_param _max\_tokens _: int | None_ _ = None_\#     

_param _model _: str_ _ = 'meta-llama-3.1-8b-instruct'_\#     

_param _presence\_penalty _: float | None_ _ = None_\#     

_param _stop _: List\[str\] | None_ _ = None_\#     

_param _streaming _: bool_ _ = False_\#     

_param _temperature _: float | None_ _ = None_\#     

_param _top\_p _: float | None_ _ = None_\#     

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/friendli.html#BaseFriendli.validate_environment)\#     

Validate if personal access token is provided in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page