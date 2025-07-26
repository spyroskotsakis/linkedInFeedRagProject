# InMemoryRateLimiter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/rate_limiters/langchain_core.rate_limiters.InMemoryRateLimiter.html
**Word Count:** 706
**Links Count:** 113
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# InMemoryRateLimiter\#

_class _langchain\_core.rate\_limiters.InMemoryRateLimiter\(

    _\*_ ,     _requests\_per\_second : float = 1_,     _check\_every\_n\_seconds : float = 0.1_,     _max\_bucket\_size : float = 1_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#InMemoryRateLimiter)\#     

An in memory rate limiter based on a token bucket algorithm.

This is an in memory rate limiter, so it cannot rate limit across different processes.

The rate limiter only allows time-based rate limiting and does not take into account any information about the input or the output, so it cannot be used to rate limit based on the size of the request.

It is thread safe and can be used in either a sync or async context.

The in memory rate limiter is based on a token bucket. The bucket is filled with tokens at a given rate. Each request consumes a token. If there are not enough tokens in the bucket, the request is blocked until there are enough tokens.

These _tokens_ have NOTHING to do with LLM tokens. They are just a way to keep track of how many requests can be made at a given time.

Current limitations:

  * The rate limiter is not designed to work across different processes. It is an in-memory rate limiter, but it is thread safe.

  * The rate limiter only supports time-based rate limiting. It does not take into account the size of the request or any other factors.

Example               import time          from langchain_core.rate_limiters import InMemoryRateLimiter          rate_limiter = InMemoryRateLimiter(         requests_per_second=0.1,  # <-- Can only make a request once every 10 seconds!!         check_every_n_seconds=0.1,  # Wake up every 100 ms to check whether allowed to make a request,         max_bucket_size=10,  # Controls the maximum burst size.     )          from langchain_anthropic import ChatAnthropic     model = ChatAnthropic(         model_name="claude-3-opus-20240229",         rate_limiter=rate_limiter     )          for _ in range(5):         tic = time.time()         model.invoke("hello")         toc = time.time()         print(toc - tic)     

Added in version 0.2.24.

A rate limiter based on a token bucket.

These _tokens_ have NOTHING to do with LLM tokens. They are just a way to keep track of how many requests can be made at a given time.

This rate limiter is designed to work in a threaded environment.

It works by filling up a bucket with tokens at a given rate. Each request consumes a given number of tokens. If there are not enough tokens in the bucket, the request is blocked until there are enough tokens.

Parameters:     

  * **requests\_per\_second** \(_float_\) – The number of tokens to add per second to the bucket. Must be at least 1. The tokens represent “credit” that can be used to make requests.

  * **check\_every\_n\_seconds** \(_float_\) – check whether the tokens are available every this many seconds. Can be a float to represent fractions of a second.

  * **max\_bucket\_size** \(_float_\) – The maximum number of tokens that can be in the bucket. This is used to prevent bursts of requests.

Methods

`__init__`\(\*\[, requests\_per\_second, ...\]\) | A rate limiter based on a token bucket.   ---|---   `aacquire`\(\*\[, blocking\]\) | Attempt to acquire a token from the rate limiter.   `acquire`\(\*\[, blocking\]\) | Attempt to acquire a token from the rate limiter.      \_\_init\_\_\(

    _\*_ ,     _requests\_per\_second : float = 1_,     _check\_every\_n\_seconds : float = 0.1_,     _max\_bucket\_size : float = 1_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#InMemoryRateLimiter.__init__)\#     

A rate limiter based on a token bucket.

These _tokens_ have NOTHING to do with LLM tokens. They are just a way to keep track of how many requests can be made at a given time.

This rate limiter is designed to work in a threaded environment.

It works by filling up a bucket with tokens at a given rate. Each request consumes a given number of tokens. If there are not enough tokens in the bucket, the request is blocked until there are enough tokens.

Parameters:     

  * **requests\_per\_second** \(_float_\) – The number of tokens to add per second to the bucket. Must be at least 1. The tokens represent “credit” that can be used to make requests.

  * **check\_every\_n\_seconds** \(_float_\) – check whether the tokens are available every this many seconds. Can be a float to represent fractions of a second.

  * **max\_bucket\_size** \(_float_\) – The maximum number of tokens that can be in the bucket. This is used to prevent bursts of requests.

Return type:     

None

_async _aacquire\(

    _\*_ ,     _blocking : bool = True_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#InMemoryRateLimiter.aacquire)\#     

Attempt to acquire a token from the rate limiter. Async version.

This method blocks until the required tokens are available if blocking is set to True.

If blocking is set to False, the method will immediately return the result of the attempt to acquire the tokens.

Parameters:     

**blocking** \(_bool_\) – If True, the method will block until the tokens are available. If False, the method will return immediately with the result of the attempt. Defaults to True.

Returns:     

True if the tokens were successfully acquired, False otherwise.

Return type:     

bool

acquire\(

    _\*_ ,     _blocking : bool = True_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/rate_limiters.html#InMemoryRateLimiter.acquire)\#     

Attempt to acquire a token from the rate limiter.

This method blocks until the required tokens are available if blocking is set to True.

If blocking is set to False, the method will immediately return the result of the attempt to acquire the tokens.

Parameters:     

**blocking** \(_bool_\) – If True, the method will block until the tokens are available. If False, the method will return immediately with the result of the attempt. Defaults to True.

Returns:     

True if the tokens were successfully acquired, False otherwise.

Return type:     

bool

Examples using InMemoryRateLimiter

  * [How to handle rate limits](https://python.langchain.com/docs/how_to/chat_model_rate_limiting/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)