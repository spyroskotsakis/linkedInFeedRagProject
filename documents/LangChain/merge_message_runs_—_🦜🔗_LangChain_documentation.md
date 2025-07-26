# merge_message_runs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.merge_message_runs.html
**Word Count:** 160
**Links Count:** 156
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# merge\_message\_runs\#

langchain\_core.messages.utils.merge\_message\_runs\(

    _messages : Sequence\[MessageLikeRepresentation\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\] | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Sequence\[MessageLikeRepresentation\], list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/utils.html#merge_message_runs)\#     

Merge consecutive Messages of the same type.

**NOTE** : ToolMessages are not merged, as each has a distinct tool call id that can’t be merged.

Parameters:     

  * **messages** \(_Union_ _\[__Sequence_ _\[__MessageLikeRepresentation_ _\]__,__None_ _\]_\) – Sequence Message-like objects to merge.

  * **chunk\_separator** – Specify the string to be inserted between message chunks.

  * **"n".** \(_Default is_\)

  * **kwargs** \(_Any_\)

Returns:     

list of BaseMessages with consecutive runs of message types merged into single messages. By default, if two messages being merged both have string contents, the merged content is a concatenation of the two strings with a new-line separator. The separator inserted between message chunks can be controlled by specifying any string with `chunk_separator`. If at least one of the messages has a list of content blocks, the merged content is a list of content blocks.

Return type:     

Union\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\], [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Sequence\[MessageLikeRepresentation\], list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]\]

Example               from langchain_core.messages import (         merge_message_runs,         AIMessage,         HumanMessage,         SystemMessage,         ToolCall,     )          messages = [         SystemMessage("you're a good assistant."),         HumanMessage("what's your favorite color", id="foo",),         HumanMessage("wait your favorite food", id="bar",),         AIMessage(             "my favorite colo",             tool_calls=[ToolCall(name="blah_tool", args={"x": 2}, id="123", type="tool_call")],             id="baz",         ),         AIMessage(             [{"type": "text", "text": "my favorite dish is lasagna"}],             tool_calls=[ToolCall(name="blah_tool", args={"x": -10}, id="456", type="tool_call")],             id="blur",         ),     ]          merge_message_runs(messages)                    [         SystemMessage("you're a good assistant."),         HumanMessage("what's your favorite color\\nwait your favorite food", id="foo",),         AIMessage(             [                 "my favorite colo",                 {"type": "text", "text": "my favorite dish is lasagna"}             ],             tool_calls=[                 ToolCall({"name": "blah_tool", "args": {"x": 2}, "id": "123", "type": "tool_call"}),                 ToolCall({"name": "blah_tool", "args": {"x": -10}, "id": "456", "type": "tool_call"})             ]             id="baz"         ),     ]     

Examples using merge\_message\_runs

  * [How to merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)

__On this page