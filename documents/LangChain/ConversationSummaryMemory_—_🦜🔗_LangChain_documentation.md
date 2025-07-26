# ConversationSummaryMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.ConversationSummaryMemory.html
**Word Count:** 105
**Links Count:** 165
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# ConversationSummaryMemory\#

_class _langchain.memory.summary.ConversationSummaryMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#ConversationSummaryMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory"), [`SummarizerMixin`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.SummarizerMixin.html#langchain.memory.summary.SummarizerMixin "langchain.memory.summary.SummarizerMixin")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Continually summarizes the conversation history.

The summary is updated after each conversation turn. The implementations returns a summary of the conversation history which can be used to provide context to the model.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _buffer _: str_ _ = ''_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['new\_lines', 'summary'\], input\_types=\{\}, partial\_variables=\{\}, template='Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.\n\nEXAMPLE\nCurrent summary:\nThe human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.\n\nNew lines of conversation:\nHuman: Why do you think artificial intelligence is a force for good?\nAI: Because artificial intelligence will help humans reach their full potential.\n\nNew summary:\nThe human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.\nEND OF EXAMPLE\n\nCurrent summary:\n\{summary\}\n\nNew lines of conversation:\n\{new\_lines\}\n\nNew summary:'\)_\#     

_param _return\_messages _: bool_ _ = False_\#     

_param _summary\_message\_cls _: type\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]__ = <class 'langchain\_core.messages.system.SystemMessage'>_\#     

_classmethod _from\_messages\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _chat\_memory : [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_,     _\*_ ,     _summarize\_step : int = 2_,     _\*\* kwargs: Any_, \) → ConversationSummaryMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#ConversationSummaryMemory.from_messages)\#     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **chat\_memory** \([_BaseChatMessageHistory_](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")\)

  * **summarize\_step** \(_int_\)

  * **kwargs** \(_Any_\)

Return type:     

_ConversationSummaryMemory_

_classmethod _validate\_prompt\_input\_variables\(

    _values : dict_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#ConversationSummaryMemory.validate_prompt_input_variables)\#     

Validate that prompt input variables are consistent.

Parameters:     

**values** \(_dict_\)

Return type:     

dict

_async _aclear\(\) → None\#     

Clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Async return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

dict\[str, _Any_\]

_async _apredict\_new\_summary\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _existing\_summary : str_, \) → str\#     

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **existing\_summary** \(_str_\)

Return type:     

str

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#ConversationSummaryMemory.clear)\#     

Clear memory contents.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#ConversationSummaryMemory.load_memory_variables)\#     

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

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#ConversationSummaryMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)