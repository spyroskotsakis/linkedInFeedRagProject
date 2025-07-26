# CUList — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.CUList.html
**Word Count:** 16
**Links Count:** 258
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# CUList\#

_class _langchain\_community.utilities.clickup.CUList\(

    _folder\_id : float_,     _name : str_,     _content : str | None = None_,     _due\_date : int | None = None_,     _due\_date\_time : bool | None = None_,     _priority : int | None = None_,     _assignee : int | None = None_,     _status : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#CUList)\#     

Component class for a list.

Attributes

`assignee` |    ---|---   `content` |    `due_date` |    `due_date_time` |    `priority` |    `status` |       Methods

`__init__`\(folder\_id, name\[, content, ...\]\) |    ---|---   `from_data`\(data\) |       Parameters:     

  * **folder\_id** \(_float_\)

  * **name** \(_str_\)

  * **content** \(_str_ _|__None_\)

  * **due\_date** \(_int_ _|__None_\)

  * **due\_date\_time** \(_bool_ _|__None_\)

  * **priority** \(_int_ _|__None_\)

  * **assignee** \(_int_ _|__None_\)

  * **status** \(_str_ _|__None_\)

\_\_init\_\_\(

    _folder\_id : float_,     _name : str_,     _content : str | None = None_,     _due\_date : int | None = None_,     _due\_date\_time : bool | None = None_,     _priority : int | None = None_,     _assignee : int | None = None_,     _status : str | None = None_, \) → None\#     

Parameters:     

  * **folder\_id** \(_float_\)

  * **name** \(_str_\)

  * **content** \(_str_ _|__None_\)

  * **due\_date** \(_int_ _|__None_\)

  * **due\_date\_time** \(_bool_ _|__None_\)

  * **priority** \(_int_ _|__None_\)

  * **assignee** \(_int_ _|__None_\)

  * **status** \(_str_ _|__None_\)

Return type:     

None

_classmethod _from\_data\(

    _data : dict_, \) → CUList[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#CUList.from_data)\#     

Parameters:     

**data** \(_dict_\)

Return type:     

_CUList_

__On this page