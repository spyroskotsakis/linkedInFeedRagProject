# convert_to_openai_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_openai_messages.html
**Word Count:** 216
**Links Count:** 153
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# convert\_to\_openai\_messages\#

langchain\_core.messages.utils.convert\_to\_openai\_messages\(

    _messages : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\] | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\]_,     _\*_ ,     _text\_format : Literal\['string', 'block'\] = 'string'_, \) → dict | list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/utils.html#convert_to_openai_messages)\#     

Convert LangChain messages into OpenAI message dicts.

Parameters:     

  * **messages** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__|__Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__\]_\) – Message-like object or iterable of objects whose contents are in OpenAI, Anthropic, Bedrock Converse, or VertexAI formats.

  * **text\_format** \(_Literal_ _\[__'string'__,__'block'__\]_\) – 

How to format string or text block contents:

    * ”string”:     

If a message has a string content, this is left as a string. If a message has content blocks that are all of type ‘text’, these are joined with a newline to make a single string. If a message has content blocks and at least one isn’t of type ‘text’, then all blocks are left as dicts.

    * ”block”:     

If a message has a string content, this is turned into a list with a single content block of type ‘text’. If a message has content blocks these are left as is.

Returns:     

  * dict:     

If a single message-like object is passed in, a single OpenAI message dict is returned.

  * list\[dict\]:     

If a sequence of message-like objects are passed in, a list of OpenAI message dicts is returned.

Return type:     

The return type depends on the input type

Example               from langchain_core.messages import (         convert_to_openai_messages,         AIMessage,         SystemMessage,         ToolMessage,     )          messages = [         SystemMessage([{"type": "text", "text": "foo"}]),         {"role": "user", "content": [{"type": "text", "text": "whats in this"}, {"type": "image_url", "image_url": {"url": "data:image/png;base64,'/9j/4AAQSk'"}}]},         AIMessage("", tool_calls=[{"name": "analyze", "args": {"baz": "buz"}, "id": "1", "type": "tool_call"}]),         ToolMessage("foobar", tool_call_id="1", name="bar"),         {"role": "assistant", "content": "thats nice"},     ]     oai_messages = convert_to_openai_messages(messages)     # -> [     #   {'role': 'system', 'content': 'foo'},     #   {'role': 'user', 'content': [{'type': 'text', 'text': 'whats in this'}, {'type': 'image_url', 'image_url': {'url': "data:image/png;base64,'/9j/4AAQSk'"}}]},     #   {'role': 'assistant', 'tool_calls': [{'type': 'function', 'id': '1','function': {'name': 'analyze', 'arguments': '{"baz": "buz"}'}}], 'content': ''},     #   {'role': 'tool', 'name': 'bar', 'content': 'foobar'},     #   {'role': 'assistant', 'content': 'thats nice'}     # ]     

Added in version 0.3.11.

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)