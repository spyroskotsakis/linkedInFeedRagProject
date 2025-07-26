# ExponentialJitterParams — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.ExponentialJitterParams.html
**Word Count:** 19
**Links Count:** 198
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# ExponentialJitterParams\#

_class _langchain\_core.runnables.retry.ExponentialJitterParams[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/retry.html#ExponentialJitterParams)\#     

Parameters for `tenacity.wait_exponential_jitter`.

initial _: float_\#     

Initial wait.

max _: float_\#     

Maximum wait.

exp\_base _: float_\#     

Base for exponential backoff.

jitter _: float_\#     

Random additional wait sampled from random.uniform\(0, jitter\).

__On this page