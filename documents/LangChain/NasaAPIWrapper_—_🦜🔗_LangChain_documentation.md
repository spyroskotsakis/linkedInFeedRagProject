# NasaAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nasa.NasaAPIWrapper.html
**Word Count:** 50
**Links Count:** 265
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# NasaAPIWrapper\#

_class _langchain\_community.utilities.nasa.NasaAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nasa.html#NasaAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for NASA API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

get\_media\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nasa.html#NasaAPIWrapper.get_media)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

get\_media\_metadata\_location\(

    _query : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nasa.html#NasaAPIWrapper.get_media_metadata_location)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

get\_media\_metadata\_manifest\(

    _query : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nasa.html#NasaAPIWrapper.get_media_metadata_manifest)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

get\_video\_captions\_location\(

    _query : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nasa.html#NasaAPIWrapper.get_video_captions_location)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

run\(_mode : str_, _query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nasa.html#NasaAPIWrapper.run)\#     

Parameters:     

  * **mode** \(_str_\)

  * **query** \(_str_\)

Return type:     

str

Examples using NasaAPIWrapper

  * [NASA Toolkit](https://python.langchain.com/docs/integrations/tools/nasa/)

__On this page