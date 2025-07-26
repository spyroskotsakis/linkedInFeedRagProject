# GoogleSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/search/langchain_google_community.search.GoogleSearchAPIWrapper.html
**Word Count:** 301
**Links Count:** 108
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# GoogleSearchAPIWrapper\#

_class _langchain\_google\_community.search.GoogleSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/search.html#GoogleSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Google Search API.

Adapted from: Instructions adapted from <https://stackoverflow.com/questions/> 37083058/ programmatically-searching-google-in-python-using-custom-search

TODO: DOCS for using it 1\. Install google-api-python-client \- If you don’t already have a Google account, sign up. \- If you have never created a Google APIs Console project, read the Managing Projects page and create a project in the Google API Console. \- Install the library using pip install google-api-python-client

2\. Enable the Custom Search API \- Navigate to the APIs & Services→Dashboard panel in Cloud Console. \- Click Enable APIs and Services. \- Search for Custom Search API and click on it. \- Click Enable. URL for it: <https://console.cloud.google.com/apis/library/customsearch.googleapis> .com

3\. To create an API key: \- Navigate to the APIs & Services → Credentials panel in Cloud Console. \- Select Create credentials, then select API key from the drop-down menu. \- The API key created dialog box displays your newly created key. \- You now have an API\_KEY

Alternatively, you can just generate an API key here: <https://developers.google.com/custom-search/docs/paid_element#api_key>

4\. Setup Custom Search Engine so you can search the entire web \- Create a custom search engine here: <https://programmablesearchengine.google.com/>. \- In What to search to search, pick the Search the entire Web option. After search engine is created, you can click on it and find Search engine ID

> on the Overview page.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _google\_api\_key _: str | None_ _ = None_\#     

_param _google\_cse\_id _: str | None_ _ = None_\#     

_param _k _: int_ _ = 10_\#     

_param _siterestrict _: bool_ _ = False_\#     

results\(

    _query : str_,     _num\_results : int_,     _search\_params : Dict\[str, str\] | None = None_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/search.html#GoogleSearchAPIWrapper.results)\#     

Run query through GoogleSearch and return metadata.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **num\_results** \(_int_\) – The number of results to return.

  * **search\_params** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Parameters to be passed on search

Returns:     

snippet - The description of the result. title - The title of the result. link - The link to the result.

Return type:     

A list of dictionaries with the following keys

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/search.html#GoogleSearchAPIWrapper.run)\#     

Run query through GoogleSearch and parse result.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using GoogleSearchAPIWrapper

  * [Bittensor](https://python.langchain.com/docs/integrations/llms/bittensor/)

__On this page