# RivaAudioEncoding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaAudioEncoding.html
**Word Count:** 46
**Links Count:** 264
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# RivaAudioEncoding\#

_class _langchain\_community.utilities.nvidia\_riva.RivaAudioEncoding\(_value_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#RivaAudioEncoding)\#     

An enum of the possible choices for Riva audio encoding.

The list of types exposed by the Riva GRPC Protobuf files can be found with the following commands: ``python import riva.client print(riva.client.AudioEncoding.keys()) # noqa: T201 ``

riva\_pb2\#     

Returns the Riva API object for the encoding.

ALAW _ = 'ALAW'_\#     

ENCODING\_UNSPECIFIED _ = 'ENCODING\_UNSPECIFIED'_\#     

FLAC _ = 'FLAC'_\#     

LINEAR\_PCM _ = 'LINEAR\_PCM'_\#     

MULAW _ = 'MULAW'_\#     

OGGOPUS _ = 'OGGOPUS'_\#     

Examples using RivaAudioEncoding

  * [NVIDIA Riva: ASR and TTS](https://python.langchain.com/docs/integrations/tools/nvidia_riva/)

__On this page