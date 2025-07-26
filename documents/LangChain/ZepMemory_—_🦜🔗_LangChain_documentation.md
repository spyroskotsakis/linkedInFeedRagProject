# ZepMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/memory/langchain_community.memory.zep_memory.ZepMemory.html
**Word Count:** 403
**Links Count:** 149
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# ZepMemory\#

_class _langchain\_community.memory.zep\_memory.ZepMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/zep_memory.html#ZepMemory)\#     

Bases: [`ConversationBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory "langchain.memory.buffer.ConversationBufferMemory")

Persist your chain history to the Zep MemoryStore.

The number of messages returned by Zep and when the Zep server summarizes chat histories is configurable. See the Zep documentation for more details.

Documentation: <https://docs.getzep.com>

Example               

memory = ZepMemory\(     

> session\_id=session\_id, \# Identifies your user or a user’s session url=ZEP\_API\_URL, \# Your Zep server’s URL api\_key=<your\_api\_key>, \# Optional memory\_key=”history”, \# Ensure this matches the key used in >
>> \# chain’s prompt template >  > return\_messages=True, \# Does your prompt template expect a string >      >  > \# or a list of Messages?

\)

chain = LLMChain\(memory=memory,…\) \# Configure your chain to use the ZepMemory     

instance

Note

To persist metadata alongside your chat history, your will need to create a

custom Chain class that overrides the prep\_outputs method to include the metadata in the call to self.memory.save\_context.

## Zep - Fast, scalable building blocks for LLM Apps\#

Zep is an open source platform for productionizing LLM apps. Go from a prototype built in LangChain or LlamaIndex, or a custom app, to production in minutes without rewriting code.

For server installation instructions and more, see: <https://docs.getzep.com/deployment/quickstart/>

For more information on the zep-python package, see: [getzep/zep-python](https://github.com/getzep/zep-python)

Initialize ZepMemory.

param session\_id:     

Identifies your user or a user’s session

type session\_id:     

str

param url:     

Your Zep server’s URL. Defaults to “<http://localhost:8000>”.

type url:     

str, optional

param api\_key:     

Your Zep API key. Defaults to None.

type api\_key:     

Optional\[str\], optional

param output\_key:     

The key to use for the output message. Defaults to None.

type output\_key:     

Optional\[str\], optional

param input\_key:     

The key to use for the input message. Defaults to None.

type input\_key:     

Optional\[str\], optional

param return\_messages:     

Does your prompt template expect a string or a list of Messages? Defaults to False i.e. return a string.

type return\_messages:     

bool, optional

param human\_prefix:     

The prefix to use for human messages. Defaults to “Human”.

type human\_prefix:     

str, optional

param ai\_prefix:     

The prefix to use for AI messages. Defaults to “AI”.

type ai\_prefix:     

str, optional

param memory\_key:     

The key to use for the memory. Defaults to “history”. Ensure that this matches the key used in chain’s prompt template.

type memory\_key:     

str, optional

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _chat\_memory _: [ZepChatMessageHistory](https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.zep.ZepChatMessageHistory.html#langchain_community.chat_message_histories.zep.ZepChatMessageHistory "langchain_community.chat_message_histories.zep.ZepChatMessageHistory")_ _\[Required\]_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _return\_messages _: bool_ _ = False_\#     

_async _abuffer\(\) → Any\#     

String buffer of memory.

Return type:     

_Any_

_async _abuffer\_as\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Exposes the buffer as a list of messages in case return\_messages is False.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_async _abuffer\_as\_str\(\) → str\#     

Exposes the buffer as a string in case return\_messages is True.

Return type:     

str

_async _aclear\(\) → None\#     

Clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None\#     

Clear memory contents.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

save\_context\(

    _inputs : Dict\[str, Any\]_,     _outputs : Dict\[str, str\]_,     _metadata : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/zep_memory.html#ZepMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

  * **outputs** \(_Dict_ _\[__str_ _,__str_ _\]_\) – The outputs from the chain.

  * **metadata** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – Any metadata to save with the context. Defaults to None

Returns:     

None

Return type:     

None

_property _buffer _: Any_\#     

String buffer of memory.

_property _buffer\_as\_messages _: list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Exposes the buffer as a list of messages in case return\_messages is False.

_property _buffer\_as\_str _: str_\#     

Exposes the buffer as a string in case return\_messages is True.

Examples using ZepMemory

  * [Zep Open Source](https://python.langchain.com/docs/integrations/retrievers/zep_memorystore/)

  * [Zep Open Source Memory](https://python.langchain.com/docs/integrations/memory/zep_memory/)

__On this page