# UpstashRatelimitError — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.upstash_ratelimit_callback.UpstashRatelimitError.html
**Word Count:** 63
**Links Count:** 182
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# UpstashRatelimitError\#

_class _langchain\_community.callbacks.upstash\_ratelimit\_callback.UpstashRatelimitError\(

    _message : str_,     _type : Literal\['token', 'request'\]_,     _limit : int | None = None_,     _reset : float | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitError)\#     

Upstash Ratelimit Error

Raised when the rate limit is reached in UpstashRatelimitHandler

Parameters:     

  * **message** \(_str_\) – error message

  * **type** \(_str_\) – The kind of the limit which was reached. One of “token” or “request”

  * **limit** \(_Optional_ _\[__int_ _\]_\) – The limit which was reached. Passed when type is request

  * **reset** \(_Optional_ _\[__int_ _\]_\) – unix timestamp in milliseconds when the limits are reset. Passed when type is request

Examples using UpstashRatelimitError

  * [Upstash Ratelimit Callback](https://python.langchain.com/docs/integrations/callbacks/upstash_ratelimit/)

__On this page