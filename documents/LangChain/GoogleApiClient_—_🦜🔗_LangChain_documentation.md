# GoogleApiClient — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.GoogleApiClient.html
**Word Count:** 84
**Links Count:** 394
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# GoogleApiClient\#

_class _langchain\_community.document\_loaders.youtube.GoogleApiClient\(

    _credentials\_path : Path = PosixPath\('/home/runner/.credentials/credentials.json'\)_,     _service\_account\_path : Path = PosixPath\('/home/runner/.credentials/credentials.json'\)_,     _token\_path : Path = PosixPath\('/home/runner/.credentials/token.json'\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#GoogleApiClient)\#     

Generic Google API Client.

To use, you should have the `google_auth_oauthlib,youtube_transcript_api,google` python package installed. As the google api expects credentials you need to set up a google account and register your Service. “<https://developers.google.com/docs/api/quickstart/python>”

_Security Note_ : Note that parsing of the transcripts relies on the standard     

xml library but the input is viewed as trusted in this case.

Example               from langchain_community.document_loaders import GoogleApiClient     google_api_client = GoogleApiClient(         service_account_path=Path("path_to_your_sec_file.json")     )     

Attributes

`credentials_path` |    ---|---   `service_account_path` |    `token_path` |       Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `validate_channel_or_videoIds_is_set`\(values\) | Validate that either folder\_id or document\_ids is set, but not both.      Parameters:     

  * **credentials\_path** \(_Path_\)

  * **service\_account\_path** \(_Path_\)

  * **token\_path** \(_Path_\)

\_\_init\_\_\(_\* args: Any_, _\*\* kwargs: Any_\) → None\#     

Parameters:     

  * **\_\_dataclass\_self\_\_** \(_PydanticDataclass_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_classmethod _validate\_channel\_or\_videoIds\_is\_set\(

    _values : Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#GoogleApiClient.validate_channel_or_videoIds_is_set)\#     

Validate that either folder\_id or document\_ids is set, but not both.

Parameters:     

**values** \(_Any_\)

Return type:     

_Any_

Examples using GoogleApiClient

  * [YouTube transcripts](https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/)

__On this page