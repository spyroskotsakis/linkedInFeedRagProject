# ConversationKGMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/memory/langchain_community.memory.kg.ConversationKGMemory.html
**Word Count:** 79
**Links Count:** 154
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# ConversationKGMemory\#

_class _langchain\_community.memory.kg.ConversationKGMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/kg.html#ConversationKGMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")

Knowledge graph conversation memory.

Integrates with external knowledge graph to store and retrieve information about knowledge triples in the conversation.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _entity\_extraction\_prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['history', 'input'\], input\_types=\{\}, partial\_variables=\{\}, template='You are an AI assistant reading the transcript of a conversation between an AI and a human. Extract all of the proper nouns from the last line of conversation. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.\n\nThe conversation history is provided just in case of a coreference \(e.g. "What do you know about him" where "him" is defined in a previous line\) \-- ignore items mentioned there that are not in the last line.\n\nReturn the output as a single comma-separated list, or NONE if there is nothing of note to return \(e.g. the user is just issuing a greeting or having a simple conversation\).\n\nEXAMPLE\nConversation history:\nPerson \#1: how\'s it going today?\nAI: "It\'s going great\! How about you?"\nPerson \#1: good\! busy working on Langchain. lots to do.\nAI: "That sounds like a lot of work\! What kind of things are you doing to make Langchain better?"\nLast line:\nPerson \#1: i\'m trying to improve Langchain\'s interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.\nOutput: Langchain\nEND OF EXAMPLE\n\nEXAMPLE\nConversation history:\nPerson \#1: how\'s it going today?\nAI: "It\'s going great\! How about you?"\nPerson \#1: good\! busy working on Langchain. lots to do.\nAI: "That sounds like a lot of work\! What kind of things are you doing to make Langchain better?"\nLast line:\nPerson \#1: i\'m trying to improve Langchain\'s interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I\'m working with Person \#2.\nOutput: Langchain, Person \#2\nEND OF EXAMPLE\n\nConversation history \(for reference only\):\n\{history\}\nLast line of conversation \(for extraction\):\nHuman: \{input\}\n\nOutput:'\)_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _k _: int_ _ = 2_\#     

_param _kg _: [NetworkxEntityGraph](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html#langchain_community.graphs.networkx_graph.NetworkxEntityGraph "langchain_community.graphs.networkx_graph.NetworkxEntityGraph")_ _\[Optional\]_\#     

_param _knowledge\_extraction\_prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _ = PromptTemplate\(input\_variables=\['history', 'input'\], input\_types=\{\}, partial\_variables=\{\}, template="You are a networked intelligence helping a human track knowledge triples about all relevant people, things, concepts, etc. and integrating them with your knowledge stored within your weights as well as that stored in a knowledge graph. Extract all of the knowledge triples from the last line of conversation. A knowledge triple is a clause that contains a subject, a predicate, and an object. The subject is the entity being described, the predicate is the property of the subject that is being described, and the object is the value of the property.\n\nEXAMPLE\nConversation history:\nPerson \#1: Did you hear aliens landed in Area 51?\nAI: No, I didn't hear that. What do you know about Area 51?\nPerson \#1: It's a secret military base in Nevada.\nAI: What do you know about Nevada?\nLast line of conversation:\nPerson \#1: It's a state in the US. It's also the number 1 producer of gold in the US.\n\nOutput: \(Nevada, is a, state\)<|>\(Nevada, is in, US\)<|>\(Nevada, is the number 1 producer of, gold\)\nEND OF EXAMPLE\n\nEXAMPLE\nConversation history:\nPerson \#1: Hello.\nAI: Hi\! How are you?\nPerson \#1: I'm good. How are you?\nAI: I'm good too.\nLast line of conversation:\nPerson \#1: I'm going to the store.\n\nOutput: NONE\nEND OF EXAMPLE\n\nEXAMPLE\nConversation history:\nPerson \#1: What do you know about Descartes?\nAI: Descartes was a French philosopher, mathematician, and scientist who lived in the 17th century.\nPerson \#1: The Descartes I'm referring to is a standup comedian and interior designer from Montreal.\nAI: Oh yes, He is a comedian and an interior designer. He has been in the industry for 30 years. His favorite food is baked bean pie.\nLast line of conversation:\nPerson \#1: Oh huh. I know Descartes likes to drive antique scooters and play the mandolin.\nOutput: \(Descartes, likes to drive, antique scooters\)<|>\(Descartes, plays, mandolin\)\nEND OF EXAMPLE\n\nConversation history \(for reference only\):\n\{history\}\nLast line of conversation \(for extraction\):\nHuman: \{input\}\n\nOutput:"\)_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _return\_messages _: bool_ _ = False_\#     

_param _summary\_message\_cls _: Type\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]__ = <class 'langchain\_core.messages.system.SystemMessage'>_\#     

Number of previous utterances to include in the context.

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/kg.html#ConversationKGMemory.clear)\#     

Clear memory contents.

Return type:     

None

get\_current\_entities\(

    _input\_string : str_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/kg.html#ConversationKGMemory.get_current_entities)\#     

Parameters:     

**input\_string** \(_str_\)

Return type:     

_List_\[str\]

get\_knowledge\_triplets\(

    _input\_string : str_, \) → List\[[KnowledgeTriple](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html#langchain_community.graphs.networkx_graph.KnowledgeTriple "langchain_community.graphs.networkx_graph.KnowledgeTriple")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/kg.html#ConversationKGMemory.get_knowledge_triplets)\#     

Parameters:     

**input\_string** \(_str_\)

Return type:     

_List_\[[_KnowledgeTriple_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html#langchain_community.graphs.networkx_graph.KnowledgeTriple "langchain_community.graphs.networkx_graph.KnowledgeTriple")\]

load\_memory\_variables\(

    _inputs : Dict\[str, Any\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/kg.html#ConversationKGMemory.load_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

_Dict_\[str, _Any_\]

save\_context\(

    _inputs : Dict\[str, Any\]_,     _outputs : Dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/memory/kg.html#ConversationKGMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

__On this page