# chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.chain.html
**Word Count:** 92
**Links Count:** 203
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# chain\#

langchain\_core.runnables.base.chain\(

    _func : Callable\[\[Input\], Coroutine\[Any, Any, Output\]\]_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#chain)\# langchain\_core.runnables.base.chain\(

    _func : Callable\[\[Input\], Iterator\[Output\]\]_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] langchain\_core.runnables.base.chain\(

    _func : Callable\[\[Input\], AsyncIterator\[Output\]\]_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] langchain\_core.runnables.base.chain\(

    _func : Callable\[\[Input\], Output\]_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]     

Decorate a function to make it a Runnable.

Sets the name of the Runnable to the name of the function. Any runnables called by the function will be traced as dependencies.

Parameters:     

**func** – A callable.

Returns:     

A Runnable.

Example:               from langchain_core.runnables import chain     from langchain_core.prompts import PromptTemplate     from langchain_openai import OpenAI          @chain     def my_func(fields):         prompt = PromptTemplate("Hello, {name}!")         llm = OpenAI()         formatted = prompt.invoke(**fields)              for chunk in llm.stream(formatted):             yield chunk     

Examples using chain

  * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)

  * [How to create a dynamic \(self-constructing\) chain](https://python.langchain.com/docs/how_to/dynamic_chain/)

  * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)

  * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)

  * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)

  * [How to pass run time values to tools](https://python.langchain.com/docs/how_to/tool_runtime/)

  * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)

  * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)

  * [Tavily Search](https://python.langchain.com/docs/integrations/tools/tavily_search/)

__On this page