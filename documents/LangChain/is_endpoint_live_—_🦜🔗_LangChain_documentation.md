# is_endpoint_live — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.nemo.is_endpoint_live.html
**Word Count:** 57
**Links Count:** 207
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# is\_endpoint\_live\#

langchain\_community.embeddings.nemo.is\_endpoint\_live\(

    _url : str_,     _headers : dict | None_,     _payload : Any_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#is_endpoint_live)\#     

Check if an endpoint is live by sending a GET request to the specified URL.

Parameters:     

  * **url** \(_str_\) – The URL of the endpoint to check.

  * **headers** \(_dict_ _|__None_\)

  * **payload** \(_Any_\)

Returns:     

True if the endpoint is live \(status code 200\), False otherwise.

Return type:     

bool

Raises:     

**Exception** – If the endpoint returns a non-successful status code or if there is an error querying the endpoint.

__On this page