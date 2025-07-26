# LLMGraphTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.llm.LLMGraphTransformer.html
**Word Count:** 349
**Links Count:** 164
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# LLMGraphTransformer\#

_class _langchain\_experimental.graph\_transformers.llm.LLMGraphTransformer\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _allowed\_nodes : List\[str\] = \[\]_,     _allowed\_relationships : List\[str\] | List\[Tuple\[str, str, str\]\] = \[\]_,     _prompt : [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") | None = None_,     _strict\_mode : bool = True_,     _node\_properties : bool | List\[str\] = False_,     _relationship\_properties : bool | List\[str\] = False_,     _ignore\_tool\_usage : bool = False_,     _additional\_instructions : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#LLMGraphTransformer)\#     

Transform documents into graph-based documents using a LLM.

It allows specifying constraints on the types of nodes and relationships to include in the output graph. The class supports extracting properties for both nodes and relationships.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – An instance of a language model supporting structured output.

  * **allowed\_nodes** \(_List_ _\[__str_ _\]__,__optional_\) – Specifies which node types are allowed in the graph. Defaults to an empty list, allowing all node types.

  * **allowed\_relationships** \(_List_ _\[__str_ _\]__,__optional_\) – Specifies which relationship types are allowed in the graph. Defaults to an empty list, allowing all relationship types.

  * **prompt** \(_Optional_ _\[_[_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") _\]__,__optional_\) – The prompt to pass to the LLM with additional instructions.

  * **strict\_mode** \(_bool_ _,__optional_\) – Determines whether the transformer should apply filtering to strictly adhere to allowed\_nodes and allowed\_relationships. Defaults to True.

  * **node\_properties** \(_Union_ _\[__bool_ _,__List_ _\[__str_ _\]__\]_\) – If True, the LLM can extract any node properties from text. Alternatively, a list of valid properties can be provided for the LLM to extract, restricting extraction to those specified.

  * **relationship\_properties** \(_Union_ _\[__bool_ _,__List_ _\[__str_ _\]__\]_\) – If True, the LLM can extract any relationship properties from text. Alternatively, a list of valid properties can be provided for the LLM to extract, restricting extraction to those specified.

  * **ignore\_tool\_usage** \(_bool_\) – Indicates whether the transformer should bypass the use of structured output functionality of the language model. If set to True, the transformer will not use the language model’s native function calling capabilities to handle structured output. Defaults to False.

  * **additional\_instructions** \(_str_\) – Allows you to add additional instructions to the prompt without having to change the whole prompt.

Example

Methods

`__init__`\(llm\[, allowed\_nodes, ...\]\) |    ---|---   `aconvert_to_graph_documents`\(documents\[, config\]\) | Asynchronously convert a sequence of documents into graph documents.   `aprocess_response`\(document\[, config\]\) | Asynchronously processes a single document, transforming it into a graph document.   `convert_to_graph_documents`\(documents\[, config\]\) | Convert a sequence of documents into graph documents.   `process_response`\(document\[, config\]\) | Processes a single document, transforming it into a graph document using an LLM based on the model's schema and constraints.      \_\_init\_\_\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _allowed\_nodes : List\[str\] = \[\]_,     _allowed\_relationships : List\[str\] | List\[Tuple\[str, str, str\]\] = \[\]_,     _prompt : [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") | None = None_,     _strict\_mode : bool = True_,     _node\_properties : bool | List\[str\] = False_,     _relationship\_properties : bool | List\[str\] = False_,     _ignore\_tool\_usage : bool = False_,     _additional\_instructions : str = ''_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#LLMGraphTransformer.__init__)\#     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **allowed\_nodes** \(_List_ _\[__str_ _\]_\)

  * **allowed\_relationships** \(_List_ _\[__str_ _\]__|__List_ _\[__Tuple_ _\[__str_ _,__str_ _,__str_ _\]__\]_\)

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") _|__None_\)

  * **strict\_mode** \(_bool_\)

  * **node\_properties** \(_bool_ _|__List_ _\[__str_ _\]_\)

  * **relationship\_properties** \(_bool_ _|__List_ _\[__str_ _\]_\)

  * **ignore\_tool\_usage** \(_bool_\)

  * **additional\_instructions** \(_str_\)

Return type:     

None

_async _aconvert\_to\_graph\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#LLMGraphTransformer.aconvert_to_graph_documents)\#     

Asynchronously convert a sequence of documents into graph documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\)

Return type:     

_List_\[[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]

_async _aprocess\_response\(

    _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → [GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#LLMGraphTransformer.aprocess_response)\#     

Asynchronously processes a single document, transforming it into a graph document.

Parameters:     

  * **document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\)

Return type:     

[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")

convert\_to\_graph\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#LLMGraphTransformer.convert_to_graph_documents)\#     

Convert a sequence of documents into graph documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The original documents.

  * **kwargs** – Additional keyword arguments.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\)

Returns:     

The transformed documents as graphs.

Return type:     

Sequence\[[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")\]

process\_response\(

    _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → [GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#LLMGraphTransformer.process_response)\#     

Processes a single document, transforming it into a graph document using an LLM based on the model’s schema and constraints.

Parameters:     

  * **document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\)

Return type:     

[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")

Examples using LLMGraphTransformer

  * [How to construct knowledge graphs](https://python.langchain.com/docs/how_to/graph_constructing/)

__On this page