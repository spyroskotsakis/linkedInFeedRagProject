# WeatherDataLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.weather.WeatherDataLoader.html
**Word Count:** 131
**Links Count:** 429
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# WeatherDataLoader\#

_class _langchain\_community.document\_loaders.weather.WeatherDataLoader\(

    _client : [OpenWeatherMapAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper.html#langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper "langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper")_,     _places : Sequence\[str\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/weather.html#WeatherDataLoader)\#     

Load weather data with Open Weather Map API.

Reads the forecast & current weather of any location using OpenWeatherMap’s free API. Checkout ‘<https://openweathermap.org/appid>’ for more on how to generate a free OpenWeatherMap API.

Initialize with parameters.

Methods

`__init__`\(client, places\) | Initialize with parameters.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `from_params`\(places, \*\[, openweathermap\_api\_key\]\) |    `lazy_load`\(\) | Lazily load weather data for the given locations.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **client** \([_OpenWeatherMapAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper.html#langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper "langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper")\)

  * **places** \(_Sequence_ _\[__str_ _\]_\)

\_\_init\_\_\(

    _client : [OpenWeatherMapAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper.html#langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper "langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper")_,     _places : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/weather.html#WeatherDataLoader.__init__)\#     

Initialize with parameters.

Parameters:     

  * **client** \([_OpenWeatherMapAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper.html#langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper "langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper")\)

  * **places** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_params\(

    _places : Sequence\[str\]_,     _\*_ ,     _openweathermap\_api\_key : str | None = None_, \) → WeatherDataLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/weather.html#WeatherDataLoader.from_params)\#     

Parameters:     

  * **places** \(_Sequence_ _\[__str_ _\]_\)

  * **openweathermap\_api\_key** \(_str_ _|__None_\)

Return type:     

_WeatherDataLoader_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/weather.html#WeatherDataLoader.lazy_load)\#     

Lazily load weather data for the given locations.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using WeatherDataLoader

  * [Weather](https://python.langchain.com/docs/integrations/document_loaders/weather/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)