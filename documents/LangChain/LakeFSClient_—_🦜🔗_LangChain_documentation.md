# LakeFSClient — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.lakefs.LakeFSClient.html
**Word Count:** 15
**Links Count:** 397
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# LakeFSClient\#

_class _langchain\_community.document\_loaders.lakefs.LakeFSClient\(

    _lakefs\_access\_key : str_,     _lakefs\_secret\_key : str_,     _lakefs\_endpoint : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSClient)\#     

Client for lakeFS.

Methods

`__init__`\(lakefs\_access\_key, ...\) |    ---|---   `is_presign_supported`\(\) |    `ls_objects`\(repo, ref, path, presign\) |       Parameters:     

  * **lakefs\_access\_key** \(_str_\)

  * **lakefs\_secret\_key** \(_str_\)

  * **lakefs\_endpoint** \(_str_\)

\_\_init\_\_\(

    _lakefs\_access\_key : str_,     _lakefs\_secret\_key : str_,     _lakefs\_endpoint : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSClient.__init__)\#     

Parameters:     

  * **lakefs\_access\_key** \(_str_\)

  * **lakefs\_secret\_key** \(_str_\)

  * **lakefs\_endpoint** \(_str_\)

is\_presign\_supported\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSClient.is_presign_supported)\#     

Return type:     

bool

ls\_objects\(

    _repo : str_,     _ref : str_,     _path : str_,     _presign : bool | None_, \) → List[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#LakeFSClient.ls_objects)\#     

Parameters:     

  * **repo** \(_str_\)

  * **ref** \(_str_\)

  * **path** \(_str_\)

  * **presign** \(_bool_ _|__None_\)

Return type:     

_List_

__On this page