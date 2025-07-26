# BaseMetadataCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.utils.BaseMetadataCallbackHandler.html
**Word Count:** 238
**Links Count:** 245
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# BaseMetadataCallbackHandler\#

_class _langchain\_community.callbacks.utils.BaseMetadataCallbackHandler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/utils.html#BaseMetadataCallbackHandler)\#     

Handle the metadata and associated function states for callbacks.

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

on\_llm\_start\_records\#     

A list of records of the on\_llm\_start method.

Type:     

list

on\_llm\_token\_records\#     

A list of records of the on\_llm\_token method.

Type:     

list

on\_llm\_end\_records\#     

A list of records of the on\_llm\_end method.

Type:     

list

on\_chain\_start\_records\#     

A list of records of the on\_chain\_start method.

Type:     

list

on\_chain\_end\_records\#     

A list of records of the on\_chain\_end method.

Type:     

list

on\_tool\_start\_records\#     

A list of records of the on\_tool\_start method.

Type:     

list

on\_tool\_end\_records\#     

A list of records of the on\_tool\_end method.

Type:     

list

on\_agent\_finish\_records\#     

A list of records of the on\_agent\_end method.

Type:     

list

Attributes

`always_verbose` | Whether to call verbose callbacks even if verbose is False.   ---|---   `ignore_agent` | Whether to ignore agent callbacks.   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_llm` | Whether to ignore LLM callbacks.      Methods

`__init__`\(\) |    ---|---   `get_custom_callback_meta`\(\) |    `reset_callback_meta`\(\) | Reset the callback metadata.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/utils.html#BaseMetadataCallbackHandler.__init__)\#     

Return type:     

None

get\_custom\_callback\_meta\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/utils.html#BaseMetadataCallbackHandler.get_custom_callback_meta)\#     

Return type:     

_Dict_\[str, _Any_\]

reset\_callback\_meta\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/utils.html#BaseMetadataCallbackHandler.reset_callback_meta)\#     

Reset the callback metadata.

Return type:     

None

__On this page