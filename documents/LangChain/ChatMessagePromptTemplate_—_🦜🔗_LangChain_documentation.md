# ChatMessagePromptTemplate — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatMessagePromptTemplate.html
**Word Count:** 197
**Links Count:** 164
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# ChatMessagePromptTemplate\#

_class _langchain\_core.prompts.chat.ChatMessagePromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatMessagePromptTemplate)\#     

Bases: [`BaseStringMessagePromptTemplate`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.BaseStringMessagePromptTemplate.html#langchain_core.prompts.chat.BaseStringMessagePromptTemplate "langchain_core.prompts.chat.BaseStringMessagePromptTemplate")

Chat message prompt template.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Additional keyword arguments to pass to the prompt template.

_param _prompt _: [StringPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.StringPromptTemplate.html#langchain_core.prompts.string.StringPromptTemplate "langchain_core.prompts.string.StringPromptTemplate")_ _\[Required\]_\#     

String prompt template.

_param _role _: str_ _\[Required\]_\#     

Role of the message.

_classmethod _from\_template\(

    _template : str_,     _template\_format : Literal\['f-string', 'mustache', 'jinja2'\] = 'f-string'_,     _partial\_variables : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Self\#     

Create a class from a string template.

Parameters:     

  * **template** \(_str_\) – a template.

  * **template\_format** \(_Literal_ _\[__'f-string'__,__'mustache'__,__'jinja2'__\]_\) – format of the template. Defaults to “f-string”.

  * **partial\_variables** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – 

A dictionary of variables that can be used to partially     

fill in the template. For example, if the template is

”\{variable1\} \{variable2\}”, and partial\_variables is \{“variable1”: “foo”\}, then the final prompt will be “foo \{variable2\}”. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – keyword arguments to pass to the constructor.

Returns:     

A new instance of this class.

Return type:     

_Self_

_classmethod _from\_template\_file\(

    _template\_file : str | Path_,     _input\_variables : list\[str\]_,     _\*\* kwargs: Any_, \) → Self\#     

Create a class from a template file.

Parameters:     

  * **template\_file** \(_str_ _|__Path_\) – path to a template file. String or Path.

  * **input\_variables** \(_list_ _\[__str_ _\]_\) – list of input variables.

  * **\*\*kwargs** \(_Any_\) – keyword arguments to pass to the constructor.

Returns:     

A new instance of this class.

Return type:     

_Self_

_async _aformat\(

    _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatMessagePromptTemplate.aformat)\#     

Async format the prompt template.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

Formatted message.

Return type:     

[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

_async _aformat\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Async format messages from kwargs.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

List of BaseMessages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

format\(

    _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatMessagePromptTemplate.format)\#     

Format the prompt template.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

Formatted message.

Return type:     

[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

format\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Format messages from kwargs.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

List of BaseMessages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

pretty\_print\(\) → None\#     

Print a human-readable representation.

Return type:     

None

pretty\_repr\(

    _html : bool = False_, \) → str\#     

Human-readable representation.

Parameters:     

**html** \(_bool_\) – Whether to format as HTML. Defaults to False.

Returns:     

Human-readable representation.

Return type:     

str

_property _input\_variables _: list\[str\]_\#     

Input variables for this prompt template.

Returns:     

List of input variable names.

__On this page