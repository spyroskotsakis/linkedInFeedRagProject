# filter_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.filter_messages.html
**Word Count:** 229
**Links Count:** 156
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# filter\_messages\#

langchain\_core.messages.utils.filter\_messages\(

    _messages : Sequence\[MessageLikeRepresentation\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\] | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Sequence\[MessageLikeRepresentation\], list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/utils.html#filter_messages)\#     

Filter messages based on name, type or id.

Parameters:     

  * **messages** \(_Union_ _\[__Sequence_ _\[__MessageLikeRepresentation_ _\]__,__None_ _\]_\) – Sequence Message-like objects to filter.

  * **include\_names** – Message names to include. Default is None.

  * **exclude\_names** – Messages names to exclude. Default is None.

  * **include\_types** – Message types to include. Can be specified as string names \(e.g. “system”, “human”, “ai”, …\) or as BaseMessage classes \(e.g. SystemMessage, HumanMessage, AIMessage, …\). Default is None.

  * **exclude\_types** – Message types to exclude. Can be specified as string names \(e.g. “system”, “human”, “ai”, …\) or as BaseMessage classes \(e.g. SystemMessage, HumanMessage, AIMessage, …\). Default is None.

  * **include\_ids** – Message IDs to include. Default is None.

  * **exclude\_ids** – Message IDs to exclude. Default is None.

  * **exclude\_tool\_calls** – 

Tool call IDs to exclude. Default is None. Can be one of the following: \- True: all AIMessages with tool calls and all ToolMessages will be excluded. \- a sequence of tool call IDs to exclude:

>     * ToolMessages with the corresponding tool call ID will be excluded. >  >     * The tool\_calls in the AIMessage will be updated to exclude matching tool calls. If all tool\_calls are filtered from an AIMessage, the whole message is excluded.

  * **kwargs** \(_Any_\)

Returns:     

A list of Messages that meets at least one of the incl\_\* conditions and none of the excl\_\* conditions. If not incl\_\* conditions are specified then anything that is not explicitly excluded will be included.

Raises:     

**ValueError if two incompatible arguments are provided.** – 

Return type:     

Union\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\], [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Sequence\[MessageLikeRepresentation\], list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]\]

Example               from langchain_core.messages import filter_messages, AIMessage, HumanMessage, SystemMessage          messages = [         SystemMessage("you're a good assistant."),         HumanMessage("what's your name", id="foo", name="example_user"),         AIMessage("steve-o", id="bar", name="example_assistant"),         HumanMessage("what's your favorite color", id="baz",),         AIMessage("silicon blue", id="blah",),     ]          filter_messages(         messages,         incl_names=("example_user", "example_assistant"),         incl_types=("system",),         excl_ids=("bar",),     )                    [         SystemMessage("you're a good assistant."),         HumanMessage("what's your name", id="foo", name="example_user"),     ]     

Examples using filter\_messages

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)

__On this page