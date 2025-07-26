# check_package_version — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.check_package_version.html
**Word Count:** 78
**Links Count:** 166
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# check\_package\_version\#

langchain\_core.utils.utils.check\_package\_version\(

    _package : str_,     _lt\_version : str | None = None_,     _lte\_version : str | None = None_,     _gt\_version : str | None = None_,     _gte\_version : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#check_package_version)\#     

Check the version of a package.

Parameters:     

  * **package** \(_str_\) – The name of the package.

  * **lt\_version** \(_str_ _,__optional_\) – The version must be less than this. Defaults to None.

  * **lte\_version** \(_str_ _,__optional_\) – The version must be less than or equal to this. Defaults to None.

  * **gt\_version** \(_str_ _,__optional_\) – The version must be greater than this. Defaults to None.

  * **gte\_version** \(_str_ _,__optional_\) – The version must be greater than or equal to this. Defaults to None.

Raises:     

**ValueError** – If the package version does not meet the requirements.

Return type:     

None

__On this page