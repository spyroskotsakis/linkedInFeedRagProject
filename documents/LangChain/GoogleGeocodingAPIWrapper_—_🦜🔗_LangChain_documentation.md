# GoogleGeocodingAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/geocoding/langchain_google_community.geocoding.GoogleGeocodingAPIWrapper.html
**Word Count:** 406
**Links Count:** 122
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# GoogleGeocodingAPIWrapper\#

_class _langchain\_google\_community.geocoding.GoogleGeocodingAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodingAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Google Maps Geocoding API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _google\_api\_key _: SecretStr_ _\[Required\]_\#     

_param _include\_address\_components _: bool_ _ = True_\#     

_param _include\_bounds _: bool_ _ = True_\#     

_param _include\_metadata _: bool_ _ = True_\#     

_param _include\_navigation _: bool_ _ = True_\#     

_param _language _: str | None_ _ = 'en'_\#     

_param _max\_retries _: int_ _ = 2_\#     

_param _region _: str | None_ _ = 'us'_\#     

_param _timeout _: int_ _ = 30_\#     

batch\_geocode\(

    _locations : List\[str\]_,     _language : str | None = None_,     _region : str | None = None_,     _components : Dict\[str, str\] | None = None_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodingAPIWrapper.batch_geocode)\#     

Process multiple locations in a single structured request.

Efficiently handles multiple location queries, processing them as a batch while maintaining individual result integrity.

Parameters:     

  * **locations** \(_List_ _\[__str_ _\]_\) – List of location strings to geocode Examples: \[“Eiffel Tower”, “Times Square”, “東京スカイツリー”\]

  * **language** \(_str_ _|__None_\) – Optional language code for results

  * **region** \(_str_ _|__None_\) – Optional region bias

  * **components** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Optional filters \(e.g., \{“country”: “US”\}\)

Returns:     

status: Overall batch status total\_results: Number of successful geocoding results results: List of location data \(same structure as single results\) errors: List of any errors encountered:

> query: The location query that failed status: Error status code message: Detailed error message

query\_info: \{     

total\_queries: Total locations processed successful: Number of successful queries failed: Number of failed queries language: Language used region: Region bias used

\}

Return type:     

Dict containing

Example

batch\_geocode\(     

locations=\[“Eiffel Tower”, “Big Ben”\], language=”en”, components=\{“country”: “FR”\}

\)

clean\_results\(

    _results : List\[Dict\]_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodingAPIWrapper.clean_results)\#     

Clean and format results.

Parameters:     

**results** \(_List_ _\[__Dict_ _\]_\)

Return type:     

_List_\[_Dict_\]

_async _geocode\_async\(

    _query : str_,     _language : str | None = None_,     _region : str | None = None_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodingAPIWrapper.geocode_async)\#     

Run query through Google Maps Geocoding API asynchronously.

Parameters:     

  * **query** \(_str_\) – The location\(s\) to geocode

  * **language** \(_str_ _|__None_\) – Optional language code for results

  * **region** \(_str_ _|__None_\) – Optional region bias

Returns:     

status: Status of the request results: List of geocoding results query\_info: Metadata about the request

Return type:     

Dict containing

raw\_results\(

    _query : str_,     _language : str | None = None_,     _region : str | None = None_,     _components : Dict\[str, str\] | None = None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodingAPIWrapper.raw_results)\#     

Get raw results with improved error handling.

Parameters:     

  * **query** \(_str_\)

  * **language** \(_str_ _|__None_\)

  * **region** \(_str_ _|__None_\)

  * **components** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\)

Return type:     

_Dict_

results\(

    _query : str_,     _language : str | None = None_,     _region : str | None = None_,     _max\_results : int = 10_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodingAPIWrapper.results)\#     

Process geocoding request and return comprehensive results.

This method handles both single and batch geocoding requests, returning detailed location information with optional components.

Parameters:     

  * **query** \(_str_\) – 

Location\(s\) to geocode. .. rubric:: Examples

    * ”Eiffel Tower”

    * ”Times Square, Central Park”

  * **language** \(_str_ _|__None_\) – Optional language code for results \(e.g., “en”, “fr”, “ja”\)

  * **region** \(_str_ _|__None_\) – Optional region bias \(e.g., “us”, “fr”, “jp”\)

  * **max\_results** \(_int_\) – Maximum number of results to return \(default: 10\)

Returns:     

status: Status of the request \(“OK” or error status\) total\_results: Number of locations found results: List of dictionaries containing location data:

> address: \{ >      >  > full: Complete formatted address street\_number: Building number \(if available\) route: Street name locality: City/Town state: State/Province country: Country postal\_code: Postal/ZIP code >  > \} geometry: \{ >
>> location: \{lat, lng\} coordinates viewport: Recommended viewport bounds: Geographic bounds \(if available\) >  > \} metadata: \{ >
>> place\_id: Unique Google place identifier types: Categories \(e.g., \[“establishment”, “point\_of\_interest”\]\) location\_type:\(e.g., “ROOFTOP”, “GEOMETRIC\_CENTER”\) >  > \} navigation: List of navigation points with: >
>> location: \{latitude, longitude\} restrictions: Travel mode restrictions

query\_info: \{     

original\_query: Input query language: Language used region: Region bias used

\}

Return type:     

Dict containing

Example Response:     

\{     

“status”: “OK”, “total\_results”: 2, “results”: \[

> \{ >      >  > “address”: \{ >      >  > “full”: “Street, Country..”, “route”: “Avenue Gustave Eiffel”, “locality”: “Paris”, “country”: “France” >  > \}, “geometry”: \{ >
>> “location”: \{“lat”: 48.8584, “lng”: 2.2945\} >  > \}

\], “query\_info”: \{

> “original\_query”: “Eiffel Tower, Big Ben”, “language”: “en”, “region”: “us”

\}

\}

Raises:     

  * **ValueError** – If query is empty or invalid

  * **Exception** – For API errors or connection issues

Parameters:     

  * **query** \(_str_\)

  * **language** \(_str_ _|__None_\)

  * **region** \(_str_ _|__None_\)

  * **max\_results** \(_int_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page