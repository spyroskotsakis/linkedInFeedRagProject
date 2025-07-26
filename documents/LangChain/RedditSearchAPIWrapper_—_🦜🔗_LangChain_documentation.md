# RedditSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.reddit_search.RedditSearchAPIWrapper.html
**Word Count:** 103
**Links Count:** 264
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# RedditSearchAPIWrapper\#

_class _langchain\_community.utilities.reddit\_search.RedditSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/reddit_search.html#RedditSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Reddit API

To use, set the environment variables `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT` to set the client ID, client secret, and user agent, respectively, as given by Reddit’s API. Alternatively, all three can be supplied as named parameters in the constructor: `reddit_client_id`, `reddit_client_secret`, and `reddit_user_agent`, respectively.

Example               from langchain_community.utilities import RedditSearchAPIWrapper     reddit_search = RedditSearchAPIWrapper()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _reddit\_client _: Any_ _\[Required\]_\#     

_param _reddit\_client\_id _: str | None_ _\[Required\]_\#     

_param _reddit\_client\_secret _: str | None_ _\[Required\]_\#     

_param _reddit\_user\_agent _: str | None_ _\[Required\]_\#     

results\(

    _query : str_,     _sort : str_,     _time\_filter : str_,     _subreddit : str_,     _limit : int_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/reddit_search.html#RedditSearchAPIWrapper.results)\#     

Use praw to search Reddit and return a list of dictionaries, one for each post.

Parameters:     

  * **query** \(_str_\)

  * **sort** \(_str_\)

  * **time\_filter** \(_str_\)

  * **subreddit** \(_str_\)

  * **limit** \(_int_\)

Return type:     

_List_\[_Dict_\]

run\(

    _query : str_,     _sort : str_,     _time\_filter : str_,     _subreddit : str_,     _limit : int_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/reddit_search.html#RedditSearchAPIWrapper.run)\#     

Search Reddit and return posts as a single string.

Parameters:     

  * **query** \(_str_\)

  * **sort** \(_str_\)

  * **time\_filter** \(_str_\)

  * **subreddit** \(_str_\)

  * **limit** \(_int_\)

Return type:     

str

Examples using RedditSearchAPIWrapper

  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)

__On this page