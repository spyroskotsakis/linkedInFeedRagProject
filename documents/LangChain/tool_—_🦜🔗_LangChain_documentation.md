# tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html
**Word Count:** 444
**Links Count:** 156
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# tool\#

langchain\_core.tools.convert.tool\(

    _\*_ ,     _description : str | None = None_,     _return\_direct : bool = False_,     _args\_schema : type\[BaseModel\] | dict\[str, Any\] | None = None_,     _infer\_schema : bool = True_,     _response\_format : Literal\['content', 'content\_and\_artifact'\] = 'content'_,     _parse\_docstring : bool = False_,     _error\_on\_invalid\_docstring : bool = True_, \) → Callable\[\[Callable | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\], [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/convert.html#tool)\# langchain\_core.tools.convert.tool\(

    _name\_or\_callable : str_,     _runnable : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _\*_ ,     _description : str | None = None_,     _return\_direct : bool = False_,     _args\_schema : type\[BaseModel\] | dict\[str, Any\] | None = None_,     _infer\_schema : bool = True_,     _response\_format : Literal\['content', 'content\_and\_artifact'\] = 'content'_,     _parse\_docstring : bool = False_,     _error\_on\_invalid\_docstring : bool = True_, \) → [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") langchain\_core.tools.convert.tool\(

    _name\_or\_callable : Callable_,     _\*_ ,     _description : str | None = None_,     _return\_direct : bool = False_,     _args\_schema : type\[BaseModel\] | dict\[str, Any\] | None = None_,     _infer\_schema : bool = True_,     _response\_format : Literal\['content', 'content\_and\_artifact'\] = 'content'_,     _parse\_docstring : bool = False_,     _error\_on\_invalid\_docstring : bool = True_, \) → [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") langchain\_core.tools.convert.tool\(

    _name\_or\_callable : str_,     _\*_ ,     _description : str | None = None_,     _return\_direct : bool = False_,     _args\_schema : type\[BaseModel\] | dict\[str, Any\] | None = None_,     _infer\_schema : bool = True_,     _response\_format : Literal\['content', 'content\_and\_artifact'\] = 'content'_,     _parse\_docstring : bool = False_,     _error\_on\_invalid\_docstring : bool = True_, \) → Callable\[\[Callable | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\], [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]     

Make tools out of functions, can be used with or without arguments.

Parameters:     

  * **name\_or\_callable** – Optional name of the tool or the callable to be converted to a tool. Must be provided as a positional argument.

  * **runnable** – Optional runnable to convert to a tool. Must be provided as a positional argument.

  * **description** – 

Optional description for the tool. Precedence for the tool description value is as follows:

>     * description argument >      >  > \(used even if docstring and/or args\_schema are provided\) >  >     * tool function docstring >      >  > \(used even if args\_schema is provided\) >  >     * args\_schema description >      >  > \(used only if description / docstring are not provided\)

  * **\*args** – Extra positional arguments. Must be empty.

  * **return\_direct** – Whether to return directly from the tool rather than continuing the agent loop. Defaults to False.

  * **args\_schema** – optional argument schema for user to specify. Defaults to None.

  * **infer\_schema** – Whether to infer the schema of the arguments from the function’s signature. This also makes the resultant tool accept a dictionary input to its run\(\) function. Defaults to True.

  * **response\_format** – The tool response format. If “content” then the output of the tool is interpreted as the contents of a ToolMessage. If “content\_and\_artifact” then the output is expected to be a two-tuple corresponding to the \(content, artifact\) of a ToolMessage. Defaults to “content”.

  * **parse\_docstring** – if `infer_schema` and `parse_docstring`, will attempt to parse parameter descriptions from Google Style function docstrings. Defaults to False.

  * **error\_on\_invalid\_docstring** – if `parse_docstring` is provided, configure whether to raise ValueError on invalid Google Style docstrings. Defaults to True.

Returns:     

The tool.

Requires:     

  * Function must be of type \(str\) -> str

  * Function must have a docstring

Examples               @tool     def search_api(query: str) -> str:         # Searches the API for the query.         return          @tool("search", return_direct=True)     def search_api(query: str) -> str:         # Searches the API for the query.         return          @tool(response_format="content_and_artifact")     def search_api(query: str) -> tuple[str, dict]:         return "partial json of results", {"full": "object of results"}     

Added in version 0.2.14.

Parse Google-style docstrings:

>  >     @tool(parse_docstring=True) >     def foo(bar: str, baz: int) -> str: >         """The foo. >      >         Args: >             bar: The bar. >             baz: The baz. >         """ >         return bar >      >     foo.args_schema.model_json_schema() >      >      >      >     { >         "title": "foo", >         "description": "The foo.", >         "type": "object", >         "properties": { >             "bar": { >                 "title": "Bar", >                 "description": "The bar.", >                 "type": "string" >             }, >             "baz": { >                 "title": "Baz", >                 "description": "The baz.", >                 "type": "integer" >             } >         }, >         "required": [ >             "bar", >             "baz" >         ] >     } >      >  > Note that parsing by default will raise `ValueError` if the docstring is considered invalid. A docstring is considered invalid if it contains arguments not in the function signature, or is unable to be parsed into a summary and “Args:” blocks. Examples below: >      >      >     # No args section >     def invalid_docstring_1(bar: str, baz: int) -> str: >         """The foo.""" >         return bar >      >     # Improper whitespace between summary and args section >     def invalid_docstring_2(bar: str, baz: int) -> str: >         """The foo. >         Args: >             bar: The bar. >             baz: The baz. >         """ >         return bar >      >     # Documented args absent from function signature >     def invalid_docstring_3(bar: str, baz: int) -> str: >         """The foo. >      >         Args: >             banana: The bar. >             monkey: The baz. >         """ >         return bar >     

Examples using tool

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/llm_math_chain/)

  * [ChatNVIDIA](https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints/)

  * [ChatOllama](https://python.langchain.com/docs/integrations/chat/ollama/)

  * [ChatPremAI](https://python.langchain.com/docs/integrations/chat/premai/)

  * [ChatTongyi](https://python.langchain.com/docs/integrations/chat/tongyi/)

  * [Cohere](https://python.langchain.com/docs/integrations/providers/cohere/)

  * [DeepInfra](https://python.langchain.com/docs/integrations/chat/deepinfra/)

  * [Eden AI](https://python.langchain.com/docs/integrations/chat/edenai/)

  * [Exa Search](https://python.langchain.com/docs/integrations/tools/exa_search/)

  * [FinancialDatasets Toolkit](https://python.langchain.com/docs/integrations/tools/financial_datasets/)

  * [How to access the RunnableConfig from a tool](https://python.langchain.com/docs/how_to/tool_configure/)

  * [How to add a human-in-the-loop for tools](https://python.langchain.com/docs/how_to/tools_human/)

  * [How to add ad-hoc tool calling capability to LLMs and Chat Models](https://python.langchain.com/docs/how_to/tools_prompting/)

  * [How to create tools](https://python.langchain.com/docs/how_to/custom_tools/)

  * [How to disable parallel tool calling](https://python.langchain.com/docs/how_to/tool_calling_parallel/)

  * [How to do tool/function calling](https://python.langchain.com/docs/how_to/function_calling/)

  * [How to force models to call a tool](https://python.langchain.com/docs/how_to/tool_choice/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

  * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)

  * [How to pass multimodal data directly to models](https://python.langchain.com/docs/how_to/multimodal_inputs/)

  * [How to pass run time values to tools](https://python.langchain.com/docs/how_to/tool_runtime/)

  * [How to pass runtime secrets to runnables](https://python.langchain.com/docs/how_to/runnable_runtime_secrets/)

  * [How to pass tool outputs to chat models](https://python.langchain.com/docs/how_to/tool_results_pass_to_model/)

  * [How to return artifacts from a tool](https://python.langchain.com/docs/how_to/tool_artifacts/)

  * [How to stream events from a tool](https://python.langchain.com/docs/how_to/tool_stream_events/)

  * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)

  * [How to stream tool calls](https://python.langchain.com/docs/how_to/tool_streaming/)

  * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)

  * [How to use tools in a chain](https://python.langchain.com/docs/how_to/tools_chain/)

  * [JSONFormer](https://python.langchain.com/docs/integrations/llms/jsonformer_experimental/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [Llama.cpp](https://python.langchain.com/docs/integrations/chat/llamacpp/)

  * [Log, Trace, and Monitor](https://python.langchain.com/docs/integrations/providers/portkey/logging_tracing_portkey/)

  * [Portkey](https://python.langchain.com/docs/integrations/providers/portkey/index/)

  * [PremAI](https://python.langchain.com/docs/integrations/providers/premai/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)