# ChatCompletion — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChatCompletion.html
**Word Count:** 8
**Links Count:** 117
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# ChatCompletion\#

_class _langchain\_community.adapters.openai.ChatCompletion[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#ChatCompletion)\#     

Chat completion.

Methods

`acreate`\(\) |    ---|---   `create`\(\) |       _async static _acreate\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[False\] = False_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#ChatCompletion.acreate)\# _async static _acreate\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[True\]_,     _\*\* kwargs: Any_, \) → AsyncIterator     

_static _create\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[False\] = False_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#ChatCompletion.create)\# _static _create\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[True\]_,     _\*\* kwargs: Any_, \) → Iterable     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)