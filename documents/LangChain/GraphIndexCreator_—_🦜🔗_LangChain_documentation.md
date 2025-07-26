# GraphIndexCreator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.index_creator.GraphIndexCreator.html
**Word Count:** 56
**Links Count:** 150
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# GraphIndexCreator\#

_class _langchain\_community.graphs.index\_creator.GraphIndexCreator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/index_creator.html#GraphIndexCreator)\#     

Bases: `BaseModel`

Functionality to create graph index.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _graph\_type _: Type\[[NetworkxEntityGraph](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html#langchain_community.graphs.networkx_graph.NetworkxEntityGraph "langchain_community.graphs.networkx_graph.NetworkxEntityGraph")\]__ = <class 'langchain\_community.graphs.networkx\_graph.NetworkxEntityGraph'>_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_async _afrom\_text\(

    _text : str_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") = PromptTemplate\(input\_variables=\['text'\], input\_types=\{\}, partial\_variables=\{\}, template="You are a networked intelligence helping a human track knowledge triples about all relevant people, things, concepts, etc. and integrating them with your knowledge stored within your weights as well as that stored in a knowledge graph. Extract all of the knowledge triples from the text. A knowledge triple is a clause that contains a subject, a predicate, and an object. The subject is the entity being described, the predicate is the property of the subject that is being described, and the object is the value of the property.\n\nEXAMPLE\nIt's a state in the US. It's also the number 1 producer of gold in the US.\n\nOutput: \(Nevada, is a, state\)<|>\(Nevada, is in, US\)<|>\(Nevada, is the number 1 producer of, gold\)\nEND OF EXAMPLE\n\nEXAMPLE\nI'm going to the store.\n\nOutput: NONE\nEND OF EXAMPLE\n\nEXAMPLE\nOh huh. I know Descartes likes to drive antique scooters and play the mandolin.\nOutput: \(Descartes, likes to drive, antique scooters\)<|>\(Descartes, plays, mandolin\)\nEND OF EXAMPLE\n\nEXAMPLE\n\{text\}Output:"\)_, \) → [NetworkxEntityGraph](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html#langchain_community.graphs.networkx_graph.NetworkxEntityGraph "langchain_community.graphs.networkx_graph.NetworkxEntityGraph")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/index_creator.html#GraphIndexCreator.afrom_text)\#     

Create graph index from text asynchronously.

Parameters:     

  * **text** \(_str_\)

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\)

Return type:     

[_NetworkxEntityGraph_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html#langchain_community.graphs.networkx_graph.NetworkxEntityGraph "langchain_community.graphs.networkx_graph.NetworkxEntityGraph")

from\_text\(

    _text : str_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") = PromptTemplate\(input\_variables=\['text'\], input\_types=\{\}, partial\_variables=\{\}, template="You are a networked intelligence helping a human track knowledge triples about all relevant people, things, concepts, etc. and integrating them with your knowledge stored within your weights as well as that stored in a knowledge graph. Extract all of the knowledge triples from the text. A knowledge triple is a clause that contains a subject, a predicate, and an object. The subject is the entity being described, the predicate is the property of the subject that is being described, and the object is the value of the property.\n\nEXAMPLE\nIt's a state in the US. It's also the number 1 producer of gold in the US.\n\nOutput: \(Nevada, is a, state\)<|>\(Nevada, is in, US\)<|>\(Nevada, is the number 1 producer of, gold\)\nEND OF EXAMPLE\n\nEXAMPLE\nI'm going to the store.\n\nOutput: NONE\nEND OF EXAMPLE\n\nEXAMPLE\nOh huh. I know Descartes likes to drive antique scooters and play the mandolin.\nOutput: \(Descartes, likes to drive, antique scooters\)<|>\(Descartes, plays, mandolin\)\nEND OF EXAMPLE\n\nEXAMPLE\n\{text\}Output:"\)_, \) → [NetworkxEntityGraph](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html#langchain_community.graphs.networkx_graph.NetworkxEntityGraph "langchain_community.graphs.networkx_graph.NetworkxEntityGraph")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/index_creator.html#GraphIndexCreator.from_text)\#     

Create graph index from text.

Parameters:     

  * **text** \(_str_\)

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\)

Return type:     

[_NetworkxEntityGraph_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html#langchain_community.graphs.networkx_graph.NetworkxEntityGraph "langchain_community.graphs.networkx_graph.NetworkxEntityGraph")

Examples using GraphIndexCreator

  * [NetworkX](https://python.langchain.com/docs/integrations/graphs/networkx/)

__On this page