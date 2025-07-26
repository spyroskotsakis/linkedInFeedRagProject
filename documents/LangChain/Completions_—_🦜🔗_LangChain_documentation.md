# Completions — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.Completions.html
**Word Count:** 7
**Links Count:** 119
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# Completions\#

_class _langchain\_community.adapters.openai.Completions[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#Completions)\#     

Completions.

Methods

`acreate`\(\) |    ---|---   `create`\(\) |       _async static _acreate\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[False\] = False_,     _\*\* kwargs: Any_, \) → [ChatCompletions](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChatCompletions.html#langchain_community.adapters.openai.ChatCompletions "langchain_community.adapters.openai.ChatCompletions")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#Completions.acreate)\# _async static _acreate\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[True\]_,     _\*\* kwargs: Any_, \) → AsyncIterator     

_static _create\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[False\] = False_,     _\*\* kwargs: Any_, \) → [ChatCompletions](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChatCompletions.html#langchain_community.adapters.openai.ChatCompletions "langchain_community.adapters.openai.ChatCompletions")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#Completions.create)\# _static _create\(

    _messages : Sequence\[Dict\[str, Any\]\]_,     _\*_ ,     _provider : str = 'ChatOpenAI'_,     _stream : Literal\[True\]_,     _\*\* kwargs: Any_, \) → Iterable     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)