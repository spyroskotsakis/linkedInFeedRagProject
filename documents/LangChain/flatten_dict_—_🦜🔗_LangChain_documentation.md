# flatten_dict — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.utils.flatten_dict.html
**Word Count:** 51
**Links Count:** 181
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# flatten\_dict\#

langchain\_community.callbacks.utils.flatten\_dict\(

    _nested\_dict : Dict\[str, Any\]_,     _parent\_key : str = ''_,     _sep : str = '\_'_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/utils.html#flatten_dict)\#     

Flatten a nested dictionary into a flat dictionary.

Parameters:     

  * **nested\_dict** \(_dict_\) – The nested dictionary to flatten.

  * **parent\_key** \(_str_\) – The prefix to prepend to the keys of the flattened dict.

  * **sep** \(_str_\) – The separator to use between the parent key and the key of the flattened dictionary.

Returns:     

A flat dictionary.

Return type:     

\(dict\)

__On this page