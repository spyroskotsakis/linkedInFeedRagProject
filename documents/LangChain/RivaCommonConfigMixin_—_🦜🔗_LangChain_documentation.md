# RivaCommonConfigMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaCommonConfigMixin.html
**Word Count:** 62
**Links Count:** 257
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# RivaCommonConfigMixin\#

_class _langchain\_community.utilities.nvidia\_riva.RivaCommonConfigMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#RivaCommonConfigMixin)\#     

Bases: `BaseModel`

A collection of common Riva settings.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _encoding _: [RivaAudioEncoding](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaAudioEncoding.html#langchain_community.utilities.nvidia_riva.RivaAudioEncoding "langchain_community.utilities.nvidia_riva.RivaAudioEncoding")_ _ = RivaAudioEncoding.LINEAR\_PCM_\#     

The encoding on the audio stream.

_param _language\_code _: str_ _ = 'en-US'_\#     

The \[BCP-47 language code\]\(<https://www.rfc-editor.org/rfc/bcp/bcp47.txt>\) for the target language.

_param _sample\_rate\_hertz _: int_ _ = 8000_\#     

The sample rate frequency of audio stream.

__On this page