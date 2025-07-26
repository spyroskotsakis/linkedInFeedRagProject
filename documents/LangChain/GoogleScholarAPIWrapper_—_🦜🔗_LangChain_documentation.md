# GoogleScholarAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_scholar.GoogleScholarAPIWrapper.html
**Word Count:** 193
**Links Count:** 274
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# GoogleScholarAPIWrapper\#

_class _langchain\_community.utilities.google\_scholar.GoogleScholarAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_scholar.html#GoogleScholarAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Google Scholar API

You can create serpapi key by signing up at: <https://serpapi.com/users/sign_up>.

The wrapper uses the serpapi python package: <https://serpapi.com/integrations/python#search-google-scholar>

To use, you should have the environment variable `SERP_API_KEY` set with your API key, or pass serp\_api\_key as a named parameter to the constructor.

top\_k\_results\#     

number of results to return from google-scholar query search. By default it returns top 10 results.

hl\#     

attribute defines the language to use for the Google Scholar search. It’s a two-letter language code. \(e.g., en for English, es for Spanish, or fr for French\). Head to the Google languages page for a full list of supported Google languages: <https://serpapi.com/google-languages>

lr\#     

> attribute defines one or multiple languages to limit the search to. It uses lang\_\{two-letter language code\} to specify languages and | as a delimiter. \(e.g., lang\_fr|lang\_de will only search French and German pages\). Head to the Google lr languages for a full list of supported languages: <https://serpapi.com/google-lr-languages>

Example:                    

from langchain\_community.utilities import GoogleScholarAPIWrapper google\_scholar = GoogleScholarAPIWrapper\(\) google\_scholar.run\(‘langchain’\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _google\_scholar\_engine _: Any_ _ = None_\#     

_param _hl _: str_ _ = 'en'_\#     

_param _lr _: str_ _ = 'lang\_en'_\#     

_param _serp\_api\_key _: str | None_ _ = None_\#     

_param _top\_k\_results _: int_ _ = 10_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_scholar.html#GoogleScholarAPIWrapper.run)\#     

Run query through GoogleSearchScholar and parse result

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using GoogleScholarAPIWrapper

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [Google Scholar](https://python.langchain.com/docs/integrations/tools/google_scholar/)

__On this page