# AudioStream — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.AudioStream.html
**Word Count:** 123
**Links Count:** 278
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# AudioStream\#

_class _langchain\_community.utilities.nvidia\_riva.AudioStream\(_maxsize : int = 0_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream)\#     

A message containing streaming audio.

Initialize the queue.

Attributes

`complete` | Indicate if the audio stream has hungup and been processed.   ---|---   `empty` | Indicate in the input stream buffer is empty.   `hungup` | Indicate if the audio stream has hungup.   `running` | Indicate if the ASR stream is running.      Methods

`__init__`\(\[maxsize\]\) | Initialize the queue.   ---|---   `aclose`\(\[timeout\]\) | Async send the hangup signal.   `aput`\(item\[, timeout\]\) | Async put a new item into the queue.   `close`\(\[timeout\]\) | Send the hangup signal.   `put`\(item\[, timeout\]\) | Put a new item into the queue.   `register`\(responses\) | Drain the responses from the provided iterator and put them into a queue.      Parameters:     

**maxsize** \(_int_\)

\_\_init\_\_\(_maxsize : int = 0_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream.__init__)\#     

Initialize the queue.

Parameters:     

**maxsize** \(_int_\)

Return type:     

None

_async _aclose\(_timeout : int | None = None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream.aclose)\#     

Async send the hangup signal.

Parameters:     

**timeout** \(_int_ _|__None_\)

Return type:     

None

_async _aput\(

    _item : bytes | [SentinelT](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.SentinelT.html#langchain_community.utilities.nvidia_riva.SentinelT "langchain_community.utilities.nvidia_riva.SentinelT")_,     _timeout : int | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream.aput)\#     

Async put a new item into the queue.

Parameters:     

  * **item** \(_bytes_ _|_[_SentinelT_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.SentinelT.html#langchain_community.utilities.nvidia_riva.SentinelT "langchain_community.utilities.nvidia_riva.SentinelT")\)

  * **timeout** \(_int_ _|__None_\)

Return type:     

None

close\(_timeout : int | None = None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream.close)\#     

Send the hangup signal.

Parameters:     

**timeout** \(_int_ _|__None_\)

Return type:     

None

put\(

    _item : bytes | [SentinelT](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.SentinelT.html#langchain_community.utilities.nvidia_riva.SentinelT "langchain_community.utilities.nvidia_riva.SentinelT")_,     _timeout : int | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream.put)\#     

Put a new item into the queue.

Parameters:     

  * **item** \(_bytes_ _|_[_SentinelT_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.SentinelT.html#langchain_community.utilities.nvidia_riva.SentinelT "langchain_community.utilities.nvidia_riva.SentinelT")\)

  * **timeout** \(_int_ _|__None_\)

Return type:     

None

register\(

    _responses : Iterator\[rasr.StreamingRecognizeResponse\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#AudioStream.register)\#     

Drain the responses from the provided iterator and put them into a queue.

Parameters:     

**responses** \(_Iterator_ _\[__rasr.StreamingRecognizeResponse_ _\]_\)

Return type:     

None

Examples using AudioStream

  * [NVIDIA Riva: ASR and TTS](https://python.langchain.com/docs/integrations/tools/nvidia_riva/)

__On this page