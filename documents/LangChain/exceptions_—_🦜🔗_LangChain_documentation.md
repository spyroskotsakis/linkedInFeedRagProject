# exceptions — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/exceptions.html
**Word Count:** 38
**Links Count:** 104
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# `exceptions`\#

Custom **exceptions** for LangChain.

**Classes**

[`exceptions.ErrorCode`](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.ErrorCode.html#langchain_core.exceptions.ErrorCode "langchain_core.exceptions.ErrorCode")\(value\) | Error codes.   ---|---   [`exceptions.LangChainException`](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.LangChainException.html#langchain_core.exceptions.LangChainException "langchain_core.exceptions.LangChainException") | General LangChain exception.   [`exceptions.OutputParserException`](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.OutputParserException.html#langchain_core.exceptions.OutputParserException "langchain_core.exceptions.OutputParserException")\(error\[, ...\]\) | Exception that output parsers should raise to signify a parsing error.   [`exceptions.TracerException`](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.TracerException.html#langchain_core.exceptions.TracerException "langchain_core.exceptions.TracerException") | Base class for exceptions in tracers module.      **Functions**

[`exceptions.create_message`](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.create_message.html#langchain_core.exceptions.create_message "langchain_core.exceptions.create_message")\(\*, message, error\_code\) | Create a message with a link to the LangChain troubleshooting guide.   ---|---