# Policy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Policy.html
**Word Count:** 16
**Links Count:** 144
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# Policy\#

_class _langchain\_experimental.rl\_chain.base.Policy\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#Policy)\#     

Abstract class to represent a policy.

Methods

`__init__`\(\*\*kwargs\) |    ---|---   `learn`\(event\) |    `log`\(event\) |    `predict`\(event\) |    `save`\(\) |       Parameters:     

**kwargs** \(_Any_\)

\_\_init\_\_\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#Policy.__init__)\#     

Parameters:     

**kwargs** \(_Any_\)

_abstractmethod _learn\(

    _event : TEvent_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#Policy.learn)\#     

Parameters:     

**event** \(_TEvent_\)

Return type:     

None

_abstractmethod _log\(

    _event : TEvent_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#Policy.log)\#     

Parameters:     

**event** \(_TEvent_\)

Return type:     

None

_abstractmethod _predict\(

    _event : TEvent_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#Policy.predict)\#     

Parameters:     

**event** \(_TEvent_\)

Return type:     

_Any_

save\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#Policy.save)\#     

Return type:     

None

__On this page