# create_neptune_opencypher_qa_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/chains/langchain_aws.chains.graph_qa.neptune_cypher.create_neptune_opencypher_qa_chain.html
**Word Count:** 108
**Links Count:** 99
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# create\_neptune\_opencypher\_qa\_chain\#

langchain\_aws.chains.graph\_qa.neptune\_cypher.create\_neptune\_opencypher\_qa\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _graph : [BaseNeptuneGraph](https://python.langchain.com/api_reference/aws/graphs/langchain_aws.graphs.neptune_graph.BaseNeptuneGraph.html#langchain_aws.graphs.neptune_graph.BaseNeptuneGraph "langchain_aws.graphs.neptune_graph.BaseNeptuneGraph")_,     _qa\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") = PromptTemplate\(input\_variables=\['context', 'question'\], input\_types=\{\}, partial\_variables=\{\}, template="You are an assistant that helps to form nice and human understandable answers.\nThe information part contains the provided information that you must use to construct an answer.\nThe provided information is authoritative, you must never doubt it or try to use your internal knowledge to correct it.\nMake the answer sound as a response to the question. Do not mention that you based the result on the given information.\nHere is an example:\n\nQuestion: Which managers own Neo4j stocks?\nContext:\[manager:CTL LLC, manager:JANE STREET GROUP LLC\]\nHelpful Answer: CTL LLC, JANE STREET GROUP LLC owns Neo4j stocks.\n\nFollow this example when generating answers.\nIf the provided information is empty, say that you don't know the answer.\nInformation:\n\{context\}\n\nQuestion: \{question\}\nHelpful Answer:"\)_,     _cypher\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _return\_intermediate\_steps : bool = False_,     _return\_direct : bool = False_,     _extra\_instructions : str | None = None_,     _allow\_dangerous\_requests : bool = False_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/chains/graph_qa/neptune_cypher.html#create_neptune_opencypher_qa_chain)\#     

Chain for question-answering against a Neptune graph by generating openCypher statements.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Example               

chain = create\_neptune\_opencypher\_qa\_chain\(     

llm=llm, graph=graph

\) response = chain.invoke\(\{“query”: “your\_query\_here”\}\)

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **graph** \([_BaseNeptuneGraph_](https://python.langchain.com/api_reference/aws/graphs/langchain_aws.graphs.neptune_graph.BaseNeptuneGraph.html#langchain_aws.graphs.neptune_graph.BaseNeptuneGraph "langchain_aws.graphs.neptune_graph.BaseNeptuneGraph")\)

  * **qa\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\)

  * **cypher\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\)

  * **return\_intermediate\_steps** \(_bool_\)

  * **return\_direct** \(_bool_\)

  * **extra\_instructions** \(_str_ _|__None_\)

  * **allow\_dangerous\_requests** \(_bool_\)

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

__On this page