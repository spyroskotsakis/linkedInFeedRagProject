# ChainConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.mrkl.base.ChainConfig.html
**Word Count:** 76
**Links Count:** 165
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# ChainConfig\#

_class _langchain.agents.mrkl.base.ChainConfig\(

    _action\_name : str_,     _action : Callable_,     _action\_description : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/mrkl/base.html#ChainConfig)\#     

Configuration for a chain to use in MRKL system.

Parameters:     

  * **action\_name** \(_str_\) – Name of the action.

  * **action** \(_Callable_\) – Action function to call.

  * **action\_description** \(_str_\) – Description of the action.

Create new instance of ChainConfig\(action\_name, action, action\_description\)

Attributes

`action` | Alias for field number 1   ---|---   `action_description` | Alias for field number 2   `action_name` | Alias for field number 0      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)