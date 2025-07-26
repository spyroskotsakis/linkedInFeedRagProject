# Task — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.Task.html
**Word Count:** 15
**Links Count:** 258
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# Task\#

_class _langchain\_community.utilities.clickup.Task\(

    _id : int_,     _name : str_,     _text\_content : str_,     _description : str_,     _status : str_,     _creator\_id : int_,     _creator\_username : str_,     _creator\_email : str_,     _assignees : List\[Dict\[str, Any\]\]_,     _watchers : List\[Dict\[str, Any\]\]_,     _priority : str | None_,     _due\_date : str | None_,     _start\_date : str | None_,     _points : int_,     _team\_id : int_,     _project\_id : int_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#Task)\#     

Class for a task.

Attributes

Methods

`__init__`\(id, name, text\_content, ...\) |    ---|---   `from_data`\(data\) |       Parameters:     

  * **id** \(_int_\)

  * **name** \(_str_\)

  * **text\_content** \(_str_\)

  * **description** \(_str_\)

  * **status** \(_str_\)

  * **creator\_id** \(_int_\)

  * **creator\_username** \(_str_\)

  * **creator\_email** \(_str_\)

  * **assignees** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **watchers** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **priority** \(_str_ _|__None_\)

  * **due\_date** \(_str_ _|__None_\)

  * **start\_date** \(_str_ _|__None_\)

  * **points** \(_int_\)

  * **team\_id** \(_int_\)

  * **project\_id** \(_int_\)

\_\_init\_\_\(

    _id : int_,     _name : str_,     _text\_content : str_,     _description : str_,     _status : str_,     _creator\_id : int_,     _creator\_username : str_,     _creator\_email : str_,     _assignees : List\[Dict\[str, Any\]\]_,     _watchers : List\[Dict\[str, Any\]\]_,     _priority : str | None_,     _due\_date : str | None_,     _start\_date : str | None_,     _points : int_,     _team\_id : int_,     _project\_id : int_, \) → None\#     

Parameters:     

  * **id** \(_int_\)

  * **name** \(_str_\)

  * **text\_content** \(_str_\)

  * **description** \(_str_\)

  * **status** \(_str_\)

  * **creator\_id** \(_int_\)

  * **creator\_username** \(_str_\)

  * **creator\_email** \(_str_\)

  * **assignees** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **watchers** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **priority** \(_str_ _|__None_\)

  * **due\_date** \(_str_ _|__None_\)

  * **start\_date** \(_str_ _|__None_\)

  * **points** \(_int_\)

  * **team\_id** \(_int_\)

  * **project\_id** \(_int_\)

Return type:     

None

_classmethod _from\_data\(

    _data : Dict\[str, Any\]_, \) → Task[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#Task.from_data)\#     

Parameters:     

**data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

_Task_

__On this page