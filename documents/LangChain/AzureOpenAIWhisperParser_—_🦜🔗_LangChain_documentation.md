# AzureOpenAIWhisperParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.AzureOpenAIWhisperParser.html
**Word Count:** 411
**Links Count:** 406
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# AzureOpenAIWhisperParser\#

_class _langchain\_community.document\_loaders.parsers.audio.AzureOpenAIWhisperParser\(

    _\*_ ,     _api\_key : str | None = None_,     _azure\_endpoint : str | None = None_,     _api\_version : str | None = None_,     _azure\_ad\_token\_provider : Callable\[\[\], str\] | None = None_,     _language : str | None = None_,     _prompt : str | None = None_,     _response\_format : Literal\['json', 'text', 'srt', 'verbose\_json', 'vtt'\] | None = None_,     _temperature : float | None = None_,     _deployment\_name : str_,     _max\_retries : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#AzureOpenAIWhisperParser)\#     

Transcribe and parse audio files using Azure OpenAI Whisper.

This parser integrates with the Azure OpenAI Whisper model to transcribe audio files. It differs from the standard OpenAI Whisper parser, requiring an Azure endpoint and credentials. The parser is limited to files under 25 MB.

**Note** : This parser uses the Azure OpenAI API, providing integration with the Azure

> ecosystem, and making it suitable for workflows involving other Azure services.

For files larger than 25 MB, consider using Azure AI Speech batch transcription: <https://learn.microsoft.com/azure/ai-services/speech-service/batch-transcription-create?pivots=rest-api#use-a-whisper-model>

Setup:     

  1. Follow the instructions here to deploy Azure Whisper: [https://learn.microsoft.com/azure/ai-services/openai/whisper-quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python](https://learn.microsoft.com/azure/ai-services/openai/whisper-quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python)

  2. Install `langchain` and set the following environment variables:

              pip install -U langchain langchain-community          export AZURE_OPENAI_API_KEY="your-api-key"     export AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"     export OPENAI_API_VERSION="your-api-version"     

Example Usage:                    from langchain.community import AzureOpenAIWhisperParser          whisper_parser = AzureOpenAIWhisperParser(         deployment_name="your-whisper-deployment",         api_version="2024-06-01",         api_key="your-api-key",         # other params...     )          audio_blob = Blob(path="your-audio-file-path")     response = whisper_parser.lazy_parse(audio_blob)          for document in response:         print(document.page_content)     

Integration with Other Loaders:     

The AzureOpenAIWhisperParser can be used with video/audio loaders and GenericLoader to automate retrieval and parsing.

YoutubeAudioLoader Example:                    from langchain_community.document_loaders.blob_loaders import (         YoutubeAudioLoader         )     from langchain_community.document_loaders.generic import GenericLoader          # Must be a list     youtube_url = ["https://your-youtube-url"]     save_dir = "directory-to-download-videos"          loader = GenericLoader(         YoutubeAudioLoader(youtube_url, save_dir),         AzureOpenAIWhisperParser(deployment_name="your-deployment-name")     )          docs = loader.load()     

Initialize the AzureOpenAIWhisperParser.

Parameters:     

  * **api\_key** \(_Optional_ _\[__str_ _\]_\) – Azure OpenAI API key. If not provided, defaults to the AZURE\_OPENAI\_API\_KEY environment variable.

  * **azure\_endpoint** \(_Optional_ _\[__str_ _\]_\) – Azure OpenAI service endpoint. Defaults to AZURE\_OPENAI\_ENDPOINT environment variable if not set.

  * **api\_version** \(_Optional_ _\[__str_ _\]_\) – API version to use, defaults to the OPENAI\_API\_VERSION environment variable.

  * **azure\_ad\_token\_provider** \(_Union_ _\[__Callable_ _\[__\[__\]__,__str_ _\]__,__None_ _\]_\) – Azure Active Directory token for authentication \(if applicable\).

  * **language** \(_Optional_ _\[__str_ _\]_\) – Language in which the request should be processed.

  * **prompt** \(_Optional_ _\[__str_ _\]_\) – Custom instructions or prompt for the Whisper model.

  * **response\_format** \(_Union_ _\[__str_ _,__None_ _\]_\) – The desired output format. Options: “json”, “text”, “srt”, “verbose\_json”, “vtt”.

  * **temperature** \(_Optional_ _\[__float_ _\]_\) – Controls the randomness of the model’s output.

  * **deployment\_name** \(_str_\) – The deployment name of the Whisper model.

  * **max\_retries** \(_int_\) – Maximum number of retries for failed API requests.

Raises:     

**ImportError** – If the required package openai is not installed.

Methods

`__init__`\(\*\[, api\_key, azure\_endpoint, ...\]\) | Initialize the AzureOpenAIWhisperParser.   ---|---   `lazy_parse`\(blob\) | Lazily parse the provided audio blob for transcription.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _\*_ ,     _api\_key : str | None = None_,     _azure\_endpoint : str | None = None_,     _api\_version : str | None = None_,     _azure\_ad\_token\_provider : Callable\[\[\], str\] | None = None_,     _language : str | None = None_,     _prompt : str | None = None_,     _response\_format : Literal\['json', 'text', 'srt', 'verbose\_json', 'vtt'\] | None = None_,     _temperature : float | None = None_,     _deployment\_name : str_,     _max\_retries : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#AzureOpenAIWhisperParser.__init__)\#     

Initialize the AzureOpenAIWhisperParser.

Parameters:     

  * **api\_key** \(_Optional_ _\[__str_ _\]_\) – Azure OpenAI API key. If not provided, defaults to the AZURE\_OPENAI\_API\_KEY environment variable.

  * **azure\_endpoint** \(_Optional_ _\[__str_ _\]_\) – Azure OpenAI service endpoint. Defaults to AZURE\_OPENAI\_ENDPOINT environment variable if not set.

  * **api\_version** \(_Optional_ _\[__str_ _\]_\) – API version to use, defaults to the OPENAI\_API\_VERSION environment variable.

  * **azure\_ad\_token\_provider** \(_Union_ _\[__Callable_ _\[__\[__\]__,__str_ _\]__,__None_ _\]_\) – Azure Active Directory token for authentication \(if applicable\).

  * **language** \(_Optional_ _\[__str_ _\]_\) – Language in which the request should be processed.

  * **prompt** \(_Optional_ _\[__str_ _\]_\) – Custom instructions or prompt for the Whisper model.

  * **response\_format** \(_Union_ _\[__str_ _,__None_ _\]_\) – The desired output format. Options: “json”, “text”, “srt”, “verbose\_json”, “vtt”.

  * **temperature** \(_Optional_ _\[__float_ _\]_\) – Controls the randomness of the model’s output.

  * **deployment\_name** \(_str_\) – The deployment name of the Whisper model.

  * **max\_retries** \(_int_\) – Maximum number of retries for failed API requests.

Raises:     

**ImportError** – If the required package openai is not installed.

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#AzureOpenAIWhisperParser.lazy_parse)\#     

Lazily parse the provided audio blob for transcription.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – The audio file in Blob format to be transcribed.

Yields:     

_Document_ – Parsed transcription from the audio file.

Raises:     

**Exception** – If an error occurs during transcription.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)