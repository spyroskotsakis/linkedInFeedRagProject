# GoogleSpeechToTextLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.google_speech_to_text.GoogleSpeechToTextLoader.html
**Word Count:** 303
**Links Count:** 422
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# GoogleSpeechToTextLoader\#

_class _langchain\_community.document\_loaders.google\_speech\_to\_text.GoogleSpeechToTextLoader\(

    _project\_id : str_,     _file\_path : str_,     _location : str = 'us-central1'_,     _recognizer\_id : str = '\_'_,     _config : RecognitionConfig | None = None_,     _config\_mask : FieldMask | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/google_speech_to_text.html#GoogleSpeechToTextLoader)\#     

Deprecated since version 0.0.32: Use `:class:`~langchain_google_community.SpeechToTextLoader`` instead. It will not be removed until langchain-community==1.0.

Loader for Google Cloud Speech-to-Text audio transcripts.

It uses the Google Cloud Speech-to-Text API to transcribe audio files and loads the transcribed text into one or more Documents, depending on the specified format.

To use, you should have the `google-cloud-speech` python package installed.

Audio files can be specified via a Google Cloud Storage uri or a local file path.

For a detailed explanation of Google Cloud Speech-to-Text, refer to the product documentation. <https://cloud.google.com/speech-to-text>

Initializes the GoogleSpeechToTextLoader.

Parameters:     

  * **project\_id** \(_str_\) – Google Cloud Project ID.

  * **file\_path** \(_str_\) – A Google Cloud Storage URI or a local file path.

  * **location** \(_str_\) – Speech-to-Text recognizer location.

  * **recognizer\_id** \(_str_\) – Speech-to-Text recognizer id.

  * **config** \(_Optional_ _\[__RecognitionConfig_ _\]_\) – Recognition options and features. For more information: <https://cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionConfig>

  * **config\_mask** \(_Optional_ _\[__FieldMask_ _\]_\) – The list of fields in config that override the values in the `default_recognition_config` of the recognizer during this recognition request. For more information: <https://cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognizeRequest>

Methods

`__init__`\(project\_id, file\_path\[, location, ...\]\) | Initializes the GoogleSpeechToTextLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Transcribes the audio file and loads the transcript into documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _project\_id : str_,     _file\_path : str_,     _location : str = 'us-central1'_,     _recognizer\_id : str = '\_'_,     _config : RecognitionConfig | None = None_,     _config\_mask : FieldMask | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/google_speech_to_text.html#GoogleSpeechToTextLoader.__init__)\#     

Initializes the GoogleSpeechToTextLoader.

Parameters:     

  * **project\_id** \(_str_\) – Google Cloud Project ID.

  * **file\_path** \(_str_\) – A Google Cloud Storage URI or a local file path.

  * **location** \(_str_\) – Speech-to-Text recognizer location.

  * **recognizer\_id** \(_str_\) – Speech-to-Text recognizer id.

  * **config** \(_Optional_ _\[__RecognitionConfig_ _\]_\) – Recognition options and features. For more information: <https://cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionConfig>

  * **config\_mask** \(_Optional_ _\[__FieldMask_ _\]_\) – The list of fields in config that override the values in the `default_recognition_config` of the recognizer during this recognition request. For more information: <https://cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognizeRequest>

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/google_speech_to_text.html#GoogleSpeechToTextLoader.load)\#     

Transcribes the audio file and loads the transcript into documents.

It uses the Google Cloud Speech-to-Text API to transcribe the audio file and blocks until the transcription is finished.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

__On this page