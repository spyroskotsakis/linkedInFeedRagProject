# OutputParserException — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.OutputParserException.html
**Word Count:** 159
**Links Count:** 104
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# OutputParserException\#

_class _langchain\_core.exceptions.OutputParserException\(

    _error : Any_,     _observation : str | None = None_,     _llm\_output : str | None = None_,     _send\_to\_llm : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/exceptions.html#OutputParserException)\#     

Exception that output parsers should raise to signify a parsing error.

This exists to differentiate parsing errors from other code or execution errors that also may arise inside the output parser. OutputParserExceptions will be available to catch and handle in ways to fix the parsing error, while other errors will be raised.

Create an OutputParserException.

Parameters:     

  * **error** \(_Any_\) – The error that’s being re-raised or an error message.

  * **observation** \(_str_ _|__None_\) – String explanation of error which can be passed to a model to try and remediate the issue. Defaults to None.

  * **llm\_output** \(_str_ _|__None_\) – String model output which is error-ing. Defaults to None.

  * **send\_to\_llm** \(_bool_\) – Whether to send the observation and llm\_output back to an Agent after an OutputParserException has been raised. This gives the underlying model driving the agent the context that the previous output was improperly structured, in the hopes that it will update the output to the correct format. Defaults to False.

Examples using OutputParserException

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

__On this page