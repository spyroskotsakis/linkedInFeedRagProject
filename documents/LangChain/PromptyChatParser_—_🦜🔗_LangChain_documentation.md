# PromptyChatParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/parsers/langchain_prompty.parsers.PromptyChatParser.html
**Word Count:** 27
**Links Count:** 94
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# PromptyChatParser\#

_class _langchain\_prompty.parsers.PromptyChatParser\(_prompty : [Prompty](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/parsers.html#PromptyChatParser)\#     

Parse a chat prompt into a list of messages.

Methods

`__init__`\(prompty\) |    ---|---   `inline_image`\(image\_item\) |    `invoke`\(data\) |    `parse_content`\(content\) | for parsing inline images      Parameters:     

**prompty** \([_Prompty_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")\)

\_\_init\_\_\(

    _prompty : [Prompty](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/parsers.html#PromptyChatParser.__init__)\#     

Parameters:     

**prompty** \([_Prompty_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")\)

Return type:     

None

inline\_image\(_image\_item : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/parsers.html#PromptyChatParser.inline_image)\#     

Parameters:     

**image\_item** \(_str_\)

Return type:     

str

invoke\(

    _data : BaseModel_, \) → BaseModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/parsers.html#PromptyChatParser.invoke)\#     

Parameters:     

**data** \(_BaseModel_\)

Return type:     

_BaseModel_

parse\_content\(_content : str_\) → str | list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/parsers.html#PromptyChatParser.parse_content)\#     

for parsing inline images

Parameters:     

**content** \(_str_\)

Return type:     

str | list

__On this page