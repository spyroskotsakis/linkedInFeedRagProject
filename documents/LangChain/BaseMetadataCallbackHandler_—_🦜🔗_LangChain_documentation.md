# BaseMetadataCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.aim_callback.BaseMetadataCallbackHandler.html
**Word Count:** 188
**Links Count:** 229
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# BaseMetadataCallbackHandler\#

_class _langchain\_community.callbacks.aim\_callback.BaseMetadataCallbackHandler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#BaseMetadataCallbackHandler)\#     

Callback handler for the metadata and associated function states for callbacks.

step\#     

The current step.

Type:     

int

starts\#     

The number of times the start method has been called.

Type:     

int

ends\#     

The number of times the end method has been called.

Type:     

int

errors\#     

The number of times the error method has been called.

Type:     

int

text\_ctr\#     

The number of times the text method has been called.

Type:     

int

ignore\_llm\_\#     

Whether to ignore llm callbacks.

Type:     

bool

ignore\_chain\_\#     

Whether to ignore chain callbacks.

Type:     

bool

ignore\_agent\_\#     

Whether to ignore agent callbacks.

Type:     

bool

ignore\_retriever\_\#     

Whether to ignore retriever callbacks.

Type:     

bool

always\_verbose\_\#     

Whether to always be verbose.

Type:     

bool

chain\_starts\#     

The number of times the chain start method has been called.

Type:     

int

chain\_ends\#     

The number of times the chain end method has been called.

Type:     

int

llm\_starts\#     

The number of times the llm start method has been called.

Type:     

int

llm\_ends\#     

The number of times the llm end method has been called.

Type:     

int

llm\_streams\#     

The number of times the text method has been called.

Type:     

int

tool\_starts\#     

The number of times the tool start method has been called.

Type:     

int

tool\_ends\#     

The number of times the tool end method has been called.

Type:     

int

agent\_ends\#     

The number of times the agent end method has been called.

Type:     

int

Attributes

`always_verbose` | Whether to call verbose callbacks even if verbose is False.   ---|---   `ignore_agent` | Whether to ignore agent callbacks.   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.      Methods

`__init__`\(\) |    ---|---   `get_custom_callback_meta`\(\) |    `reset_callback_meta`\(\) | Reset the callback metadata.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#BaseMetadataCallbackHandler.__init__)\#     

Return type:     

None

get\_custom\_callback\_meta\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#BaseMetadataCallbackHandler.get_custom_callback_meta)\#     

Return type:     

_Dict_\[str, _Any_\]

reset\_callback\_meta\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#BaseMetadataCallbackHandler.reset_callback_meta)\#     

Reset the callback metadata.

Return type:     

None

__On this page