# RedditSearchSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.reddit_search.tool.RedditSearchSchema.html
**Word Count:** 108
**Links Count:** 418
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# RedditSearchSchema\#

_class _langchain\_community.tools.reddit\_search.tool.RedditSearchSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/reddit_search/tool.html#RedditSearchSchema)\#     

Bases: `BaseModel`

Input for Reddit search.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _limit _: str_ _\[Required\]_\#     

a positive integer indicating the maximum number of results to return

_param _query _: str_ _\[Required\]_\#     

should be query string that post title should contain, or ‘\*’ if anything is allowed.

_param _sort _: str_ _\[Required\]_\#     

should be sort method, which is one of: “relevance” , “hot”, “top”, “new”, or “comments”.

_param _subreddit _: str_ _\[Required\]_\#     

should be name of subreddit, like “all” for r/all

_param _time\_filter _: str_ _\[Required\]_\#     

should be time period to filter by, which is one of “all”, “day”, “hour”, “month”, “week”, or “year”

Examples using RedditSearchSchema

  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)

__On this page