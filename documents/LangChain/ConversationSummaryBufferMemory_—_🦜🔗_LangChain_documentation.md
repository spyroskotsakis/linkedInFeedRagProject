# ConversationSummaryBufferMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary_buffer.ConversationSummaryBufferMemory.html
**Word Count:** 130
**Links Count:** 177
**Scraped:** 2025-07-21 07:49:33
**Status:** completed

---

# ConversationSummaryBufferMemory\#

_class _langchain.memory.summary\_buffer.ConversationSummaryBufferMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory"), [`SummarizerMixin`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.SummarizerMixin.html#langchain.memory.summary.SummarizerMixin "langchain.memory.summary.SummarizerMixin")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Buffer with summarizer for storing conversation memory.

Provides a running summary of the conversation together with the most recent messages in the conversation under the constraint that the total number of tokens in the conversation does not exceed a certain limit.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _max\_token\_limit _: int_ _ = 2000_\#     

_param _memory\_key _: str_ _ = 'history'_\#     

_param _moving\_summary\_buffer _: str_ _ = ''_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['new\_lines', 'summary'\], input\_types=\{\}, partial\_variables=\{\}, template='Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.\n\nEXAMPLE\nCurrent summary:\nThe human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.\n\nNew lines of conversation:\nHuman: Why do you think artificial intelligence is a force for good?\nAI: Because artificial intelligence will help humans reach their full potential.\n\nNew summary:\nThe human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.\nEND OF EXAMPLE\n\nCurrent summary:\n\{summary\}\n\nNew lines of conversation:\n\{new\_lines\}\n\nNew summary:'\)_\#     

_param _return\_messages _: bool_ _ = False_\#     

_param _summary\_message\_cls _: type\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]__ = <class 'langchain\_core.messages.system.SystemMessage'>_\#     

_classmethod _validate\_prompt\_input\_variables\(

    _values : dict_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.validate_prompt_input_variables)\#     

Validate that prompt input variables are consistent.

Parameters:     

**values** \(_dict_\)

Return type:     

dict

_async _abuffer\(\) → str | list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.abuffer)\#     

Async memory buffer.

Return type:     

str | list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.aclear)\#     

Asynchronously clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.aload_memory_variables)\#     

Asynchronously return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

_async _apredict\_new\_summary\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _existing\_summary : str_, \) → str\#     

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **existing\_summary** \(_str_\)

Return type:     

str

_async _aprune\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.aprune)\#     

Asynchronously prune buffer if it exceeds max token limit

Return type:     

None

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.asave_context)\#     

Asynchronously save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.clear)\#     

Clear memory contents.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.load_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

predict\_new\_summary\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _existing\_summary : str_, \) → str\#     

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **existing\_summary** \(_str_\)

Return type:     

str

prune\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.prune)\#     

Prune buffer if it exceeds max token limit

Return type:     

None

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary_buffer.html#ConversationSummaryBufferMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _buffer _: str | list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

String buffer of memory.

__On this page