# BaseRateLimiter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/rate_limiters/langchain_core.rate_limiters.BaseRateLimiter.html
**Word Count:** 272
**Links Count:** 108
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# BaseRateLimiter\#

_class _langchain\_core.rate\_limiters.BaseRateLimiter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#BaseRateLimiter)\#     

Base class for rate limiters.

Usage of the base limiter is through the acquire and aacquire methods depending on whether running in a sync or async context.

Implementations are free to add a timeout parameter to their initialize method to allow users to specify a timeout for acquiring the necessary tokens when using a blocking call.

Current limitations:

  * Rate limiting information is not surfaced in tracing or callbacks. This means that the total time it takes to invoke a chat model will encompass both the time spent waiting for tokens and the time spent making the request.

Added in version 0.2.24.

Methods

`aacquire`\(\*\[, blocking\]\) | Attempt to acquire the necessary tokens for the rate limiter.   ---|---   `acquire`\(\*\[, blocking\]\) | Attempt to acquire the necessary tokens for the rate limiter.      _abstractmethod async _aacquire\(_\*_ , _blocking : bool = True_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#BaseRateLimiter.aacquire)\#     

Attempt to acquire the necessary tokens for the rate limiter.

This method blocks until the required tokens are available if blocking is set to True.

If blocking is set to False, the method will immediately return the result of the attempt to acquire the tokens.

Parameters:     

**blocking** \(_bool_\) – If True, the method will block until the tokens are available. If False, the method will return immediately with the result of the attempt. Defaults to True.

Returns:     

True if the tokens were successfully acquired, False otherwise.

Return type:     

bool

_abstractmethod _acquire\(_\*_ , _blocking : bool = True_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#BaseRateLimiter.acquire)\#     

Attempt to acquire the necessary tokens for the rate limiter.

This method blocks until the required tokens are available if blocking is set to True.

If blocking is set to False, the method will immediately return the result of the attempt to acquire the tokens.

Parameters:     

**blocking** \(_bool_\) – If True, the method will block until the tokens are available. If False, the method will return immediately with the result of the attempt. Defaults to True.

Returns:     

True if the tokens were successfully acquired, False otherwise.

Return type:     

bool

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)