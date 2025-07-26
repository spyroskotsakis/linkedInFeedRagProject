# SummarizerMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.SummarizerMixin.html
**Word Count:** 61
**Links Count:** 127
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# SummarizerMixin\#

_class _langchain.memory.summary.SummarizerMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#SummarizerMixin)\#     

Bases: `BaseModel`

Deprecated since version 0.2.12: Refer here for how to incorporate summaries of conversation history: <https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/> It will not be removed until langchain==1.0.

Mixin for summarizer.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['new\_lines', 'summary'\], input\_types=\{\}, partial\_variables=\{\}, template='Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.\n\nEXAMPLE\nCurrent summary:\nThe human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.\n\nNew lines of conversation:\nHuman: Why do you think artificial intelligence is a force for good?\nAI: Because artificial intelligence will help humans reach their full potential.\n\nNew summary:\nThe human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.\nEND OF EXAMPLE\n\nCurrent summary:\n\{summary\}\n\nNew lines of conversation:\n\{new\_lines\}\n\nNew summary:'\)_\#     

_param _summary\_message\_cls _: type\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]__ = <class 'langchain\_core.messages.system.SystemMessage'>_\#     

_async _apredict\_new\_summary\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _existing\_summary : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#SummarizerMixin.apredict_new_summary)\#     

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **existing\_summary** \(_str_\)

Return type:     

str

predict\_new\_summary\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _existing\_summary : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/summary.html#SummarizerMixin.predict_new_summary)\#     

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **existing\_summary** \(_str_\)

Return type:     

str

__On this page