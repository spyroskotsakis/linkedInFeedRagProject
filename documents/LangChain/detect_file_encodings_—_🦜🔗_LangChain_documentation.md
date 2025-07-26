# detect_file_encodings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.helpers.detect_file_encodings.html
**Word Count:** 43
**Links Count:** 387
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# detect\_file\_encodings\#

langchain\_community.document\_loaders.helpers.detect\_file\_encodings\(

    _file\_path : str | Path_,     _timeout : int = 5_, \) → List\[[FileEncoding](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.helpers.FileEncoding.html#langchain_community.document_loaders.helpers.FileEncoding "langchain_community.document_loaders.helpers.FileEncoding")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/helpers.html#detect_file_encodings)\#     

Try to detect the file encoding.

Returns a list of FileEncoding tuples with the detected encodings ordered by confidence.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the file to detect the encoding for.

  * **timeout** \(_int_\) – The timeout in seconds for the encoding detection.

Return type:     

_List_\[[_FileEncoding_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.helpers.FileEncoding.html#langchain_community.document_loaders.helpers.FileEncoding "langchain_community.document_loaders.helpers.FileEncoding")\]

__On this page