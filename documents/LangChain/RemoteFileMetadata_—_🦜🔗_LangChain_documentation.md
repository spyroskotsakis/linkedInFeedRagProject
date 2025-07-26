# RemoteFileMetadata — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_dynamic_sessions/tools/langchain_azure_dynamic_sessions.tools.sessions.RemoteFileMetadata.html
**Word Count:** 34
**Links Count:** 79
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# RemoteFileMetadata\#

_class _langchain\_azure\_dynamic\_sessions.tools.sessions.RemoteFileMetadata\(_filename : str_, _size\_in\_bytes : int_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_dynamic_sessions/tools/sessions.html#RemoteFileMetadata)\#     

Metadata for a file in the session.

Attributes

`full_path` | Get the full path of the file.   ---|---      Methods

`__init__`\(filename, size\_in\_bytes\) |    ---|---   `from_dict`\(data\) | Create a RemoteFileMetadata object from a dictionary.      Parameters:     

  * **filename** \(_str_\)

  * **size\_in\_bytes** \(_int_\)

\_\_init\_\_\(

    _filename : str_,     _size\_in\_bytes : int_, \) → None\#     

Parameters:     

  * **filename** \(_str_\)

  * **size\_in\_bytes** \(_int_\)

Return type:     

None

_static _from\_dict\(

    _data : dict_, \) → RemoteFileMetadata[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_dynamic_sessions/tools/sessions.html#RemoteFileMetadata.from_dict)\#     

Create a RemoteFileMetadata object from a dictionary.

Parameters:     

**data** \(_dict_\)

Return type:     

_RemoteFileMetadata_

__On this page