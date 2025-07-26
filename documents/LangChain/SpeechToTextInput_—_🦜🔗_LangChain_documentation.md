# SpeechToTextInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.edenai.audio_speech_to_text.SpeechToTextInput.html
**Word Count:** 44
**Links Count:** 409
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# SpeechToTextInput\#

_class _langchain\_community.tools.edenai.audio\_speech\_to\_text.SpeechToTextInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/edenai/audio_speech_to_text.html#SpeechToTextInput)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: HttpUrl_ _\[Required\]_\#     

url of the audio to analyze

__On this page