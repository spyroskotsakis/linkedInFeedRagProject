# GooglePlacesAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/places_api/langchain_google_community.places_api.GooglePlacesAPIWrapper.html
**Word Count:** 120
**Links Count:** 102
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# GooglePlacesAPIWrapper\#

_class _langchain\_google\_community.places\_api.GooglePlacesAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/places_api.html#GooglePlacesAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around Google Places API.

To use, you should have the `googlemaps` python package installed,     

**an API key for the google maps platform** , and the environment variable ‘’GPLACES\_API\_KEY’’ set with your API key , or pass ‘gplaces\_api\_key’ as a named parameter to the constructor.

By default, this will return the all the results on the input query.     

You can use the top\_k\_results argument to limit the number of results.

Example               from langchain_community.utilities import GooglePlacesAPIWrapper     gplaceapi = GooglePlacesAPIWrapper()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _gplaces\_api\_key _: str | None_ _ = None_\#     

_param _top\_k\_results _: int | None_ _ = None_\#     

fetch\_place\_details\(

    _place\_id : str_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/places_api.html#GooglePlacesAPIWrapper.fetch_place_details)\#     

Parameters:     

**place\_id** \(_str_\)

Return type:     

str | None

format\_place\_details\(

    _place\_details : Dict\[str, Any\]_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/places_api.html#GooglePlacesAPIWrapper.format_place_details)\#     

Parameters:     

**place\_details** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

str | None

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/places_api.html#GooglePlacesAPIWrapper.run)\#     

Run Places search and get k number of places that exists that match.

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page