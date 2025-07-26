# langchain_core.tracers.langchain_v1 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/tracers/langchain_v1.html
**Word Count:** 59
**Links Count:** 14
**Scraped:** 2025-07-21 08:57:35
**Status:** completed

---

# Source code for langchain\_core.tracers.langchain\_v1               """This module is deprecated and will be removed in a future release.          Please use LangChainTracer instead.     """          from typing import Any                              [[docs]](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.langchain_v1.get_headers.html#langchain_core.tracers.langchain_v1.get_headers)     def get_headers(*args: Any, **kwargs: Any) -> Any:  # noqa: ARG001         """Throw an error because this has been replaced by get_headers."""         msg = (             "get_headers for LangChainTracerV1 is no longer supported. "             "Please use LangChainTracer instead."         )         raise RuntimeError(msg)                                             [[docs]](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.langchain_v1.LangChainTracerV1.html#langchain_core.tracers.langchain_v1.LangChainTracerV1)     def LangChainTracerV1(*args: Any, **kwargs: Any) -> Any:  # noqa: N802,ARG001         """Throw an error because this has been replaced by LangChainTracer."""         msg = (             "LangChainTracerV1 is no longer supported. Please use LangChainTracer instead."         )         raise RuntimeError(msg)