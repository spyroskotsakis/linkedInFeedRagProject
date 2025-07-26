# tracing_v2_enabled — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.context.tracing_v2_enabled.html
**Word Count:** 80
**Links Count:** 138
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# tracing\_v2\_enabled\#

langchain\_core.tracers.context.tracing\_v2\_enabled\(

    _project\_name : str | None = None_,     _\*_ ,     _example\_id : str | UUID | None = None_,     _tags : list\[str\] | None = None_,     _client : LangSmithClient | None = None_, \) → Generator\[[LangChainTracer](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.langchain.LangChainTracer.html#langchain_core.tracers.langchain.LangChainTracer "langchain_core.tracers.langchain.LangChainTracer"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/context.html#tracing_v2_enabled)\#     

Instruct LangChain to log all runs in context to LangSmith.

Parameters:     

  * **project\_name** \(_str_ _,__optional_\) – The name of the project. Defaults to “default”.

  * **example\_id** \(_str_ _or_ _UUID_ _,__optional_\) – The ID of the example. Defaults to None.

  * **tags** \(_list_ _\[__str_ _\]__,__optional_\) – The tags to add to the run. Defaults to None.

  * **client** \(_LangSmithClient_ _,__optional_\) – The client of the langsmith. Defaults to None.

Yields:     

_LangChainTracer_ – The LangChain tracer.

Return type:     

Generator\[[LangChainTracer](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.langchain.LangChainTracer.html#langchain_core.tracers.langchain.LangChainTracer "langchain_core.tracers.langchain.LangChainTracer"), None, None\]

Example               >>> with tracing_v2_enabled():     ...     # LangChain code will automatically be traced     

You can use this to fetch the LangSmith run URL:               >>> with tracing_v2_enabled() as cb:     ...     chain.invoke("foo")     ...     run_url = cb.get_run_url()     

Examples using tracing\_v2\_enabled

  * [Chat Bot Feedback Template](https://python.langchain.com/docs/templates/chat-bot-feedback/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)