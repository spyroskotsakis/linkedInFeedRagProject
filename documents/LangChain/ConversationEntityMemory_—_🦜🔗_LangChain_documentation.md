# ConversationEntityMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.ConversationEntityMemory.html
**Word Count:** 180
**Links Count:** 154
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# ConversationEntityMemory\#

_class _langchain.memory.entity.ConversationEntityMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#ConversationEntityMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Entity extractor & summarizer memory.

Extracts named entities from the recent chat history and generates summaries. With a swappable entity store, persisting entities across conversations. Defaults to an in-memory entity store, and can be swapped out for a Redis, SQLite, or other entity store.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _chat\_history\_key _: str_ _ = 'history'_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _entity\_cache _: list\[str\]__ = \[\]_\#     

_param _entity\_extraction\_prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['history', 'input'\], input\_types=\{\}, partial\_variables=\{\}, template='You are an AI assistant reading the transcript of a conversation between an AI and a human. Extract all of the proper nouns from the last line of conversation. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.\n\nThe conversation history is provided just in case of a coreference \(e.g. "What do you know about him" where "him" is defined in a previous line\) \-- ignore items mentioned there that are not in the last line.\n\nReturn the output as a single comma-separated list, or NONE if there is nothing of note to return \(e.g. the user is just issuing a greeting or having a simple conversation\).\n\nEXAMPLE\nConversation history:\nPerson \#1: how\'s it going today?\nAI: "It\'s going great\! How about you?"\nPerson \#1: good\! busy working on Langchain. lots to do.\nAI: "That sounds like a lot of work\! What kind of things are you doing to make Langchain better?"\nLast line:\nPerson \#1: i\'m trying to improve Langchain\'s interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.\nOutput: Langchain\nEND OF EXAMPLE\n\nEXAMPLE\nConversation history:\nPerson \#1: how\'s it going today?\nAI: "It\'s going great\! How about you?"\nPerson \#1: good\! busy working on Langchain. lots to do.\nAI: "That sounds like a lot of work\! What kind of things are you doing to make Langchain better?"\nLast line:\nPerson \#1: i\'m trying to improve Langchain\'s interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I\'m working with Person \#2.\nOutput: Langchain, Person \#2\nEND OF EXAMPLE\n\nConversation history \(for reference only\):\n\{history\}\nLast line of conversation \(for extraction\):\nHuman: \{input\}\n\nOutput:'\)_\#     

_param _entity\_store _: [BaseEntityStore](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html#langchain.memory.entity.BaseEntityStore "langchain.memory.entity.BaseEntityStore")_ _\[Optional\]_\#     

_param _entity\_summarization\_prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['entity', 'history', 'input', 'summary'\], input\_types=\{\}, partial\_variables=\{\}, template='You are an AI assistant helping a human keep track of facts about relevant people, places, and concepts in their life. Update the summary of the provided entity in the "Entity" section based on the last line of your conversation with the human. If you are writing the summary for the first time, return a single sentence.\nThe update should only include facts that are relayed in the last line of conversation about the provided entity, and should only contain facts about the provided entity.\n\nIf there is no new information about the provided entity or the information is not worth noting \(not an important or relevant fact to remember long-term\), return the existing summary unchanged.\n\nFull conversation history \(for context\):\n\{history\}\n\nEntity to summarize:\n\{entity\}\n\nExisting summary of \{entity\}:\n\{summary\}\n\nLast line of conversation:\nHuman: \{input\}\nUpdated summary:'\)_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _k _: int_ _ = 3_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _return\_messages _: bool_ _ = False_\#     

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

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#ConversationEntityMemory.clear)\#     

Clear memory contents.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#ConversationEntityMemory.load_memory_variables)\#     

Returns chat history and all generated entities with summaries if available, and updates or clears the recent entity cache.

New entity name can be found when calling this method, before the entity summaries are generated, so the entity cache values may be empty if no entity descriptions are generated yet.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#ConversationEntityMemory.save_context)\#     

Save context from this conversation history to the entity store.

Generates a summary for each entity in the entity cache by prompting the model, and saves these summaries to the entity store.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _buffer _: list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Access chat memory messages.

__On this page