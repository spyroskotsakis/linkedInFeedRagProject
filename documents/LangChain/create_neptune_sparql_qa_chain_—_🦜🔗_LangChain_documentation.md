# create_neptune_sparql_qa_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/chains/langchain_aws.chains.graph_qa.neptune_sparql.create_neptune_sparql_qa_chain.html
**Word Count:** 109
**Links Count:** 99
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# create\_neptune\_sparql\_qa\_chain\#

langchain\_aws.chains.graph\_qa.neptune\_sparql.create\_neptune\_sparql\_qa\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _graph : [NeptuneRdfGraph](https://python.langchain.com/api_reference/aws/graphs/langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph.html#langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph "langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph")_,     _qa\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") = PromptTemplate\(input\_variables=\['context', 'prompt'\], input\_types=\{\}, partial\_variables=\{\}, template="Task: Generate a natural language response from the results of a SPARQL query.\nYou are an assistant that creates well-written and human understandable answers.\nThe information part contains the information provided, which you can use to construct an answer.\nThe information provided is authoritative, you must never doubt it or try to use your internal knowledge to correct it.\nMake your response sound like the information is coming from an AI assistant, but don't add any information.\nInformation:\n\{context\}\n\nQuestion: \{prompt\}\nHelpful Answer:"\)_,     _sparql\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _return\_intermediate\_steps : bool = False_,     _return\_direct : bool = False_,     _extra\_instructions : str | None = None_,     _allow\_dangerous\_requests : bool = False_,     _examples : str | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Any, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/chains/graph_qa/neptune_sparql.html#create_neptune_sparql_qa_chain)\#     

Chain for question-answering against a Neptune graph by generating SPARQL statements.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Example               

chain = create\_neptune\_sparql\_qa\_chain\(     

llm=llm, graph=graph

\) response = chain.invoke\(\{“query”: “your\_query\_here”\}\)

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **graph** \([_NeptuneRdfGraph_](https://python.langchain.com/api_reference/aws/graphs/langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph.html#langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph "langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph")\)

  * **qa\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\)

  * **sparql\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\)

  * **return\_intermediate\_steps** \(_bool_\)

  * **return\_direct** \(_bool_\)

  * **extra\_instructions** \(_str_ _|__None_\)

  * **allow\_dangerous\_requests** \(_bool_\)

  * **examples** \(_str_ _|__None_\)

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Any_ , dict\]

__On this page