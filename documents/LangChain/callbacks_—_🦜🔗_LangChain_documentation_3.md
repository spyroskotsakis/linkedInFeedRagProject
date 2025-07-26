# callbacks — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/callbacks.html
**Word Count:** 37
**Links Count:** 87
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# `callbacks`\#

**Callback handlers** allow listening to events in LangChain.

**Class hierarchy:**               BaseCallbackHandler --> <name>CallbackHandler  # Example: AimCallbackHandler     

**Classes**

[`callbacks.streaming_aiter.AsyncIteratorCallbackHandler`](https://python.langchain.com/api_reference/langchain/callbacks/langchain.callbacks.streaming_aiter.AsyncIteratorCallbackHandler.html#langchain.callbacks.streaming_aiter.AsyncIteratorCallbackHandler "langchain.callbacks.streaming_aiter.AsyncIteratorCallbackHandler")\(\) | Callback handler that returns an async iterator.   ---|---   [`callbacks.streaming_aiter_final_only.AsyncFinalIteratorCallbackHandler`](https://python.langchain.com/api_reference/langchain/callbacks/langchain.callbacks.streaming_aiter_final_only.AsyncFinalIteratorCallbackHandler.html#langchain.callbacks.streaming_aiter_final_only.AsyncFinalIteratorCallbackHandler "langchain.callbacks.streaming_aiter_final_only.AsyncFinalIteratorCallbackHandler")\(\*\) | Callback handler that returns an async iterator.   [`callbacks.streaming_stdout_final_only.FinalStreamingStdOutCallbackHandler`](https://python.langchain.com/api_reference/langchain/callbacks/langchain.callbacks.streaming_stdout_final_only.FinalStreamingStdOutCallbackHandler.html#langchain.callbacks.streaming_stdout_final_only.FinalStreamingStdOutCallbackHandler "langchain.callbacks.streaming_stdout_final_only.FinalStreamingStdOutCallbackHandler")\(\*\) | Callback handler for streaming in agents.   [`callbacks.tracers.logging.LoggingCallbackHandler`](https://python.langchain.com/api_reference/langchain/callbacks/langchain.callbacks.tracers.logging.LoggingCallbackHandler.html#langchain.callbacks.tracers.logging.LoggingCallbackHandler "langchain.callbacks.tracers.logging.LoggingCallbackHandler")\(logger\) | Tracer that logs via the input Logger.