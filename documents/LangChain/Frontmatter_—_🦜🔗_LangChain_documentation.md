# Frontmatter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Frontmatter.html
**Word Count:** 80
**Links Count:** 90
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# Frontmatter\#

_class _langchain\_prompty.core.Frontmatter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Frontmatter)\#     

Class for reading frontmatter from a string or file.

Methods

`read`\(string\) | Returns dict with separated frontmatter from string.   ---|---   `read_file`\(path\) | Reads file at path and returns dict with separated frontmatter.      _classmethod _read\(_string : str_\) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Frontmatter.read)\#     

Returns dict with separated frontmatter from string.

Returned dict keys: \- attributes: extracted YAML attributes in dict form. \- body: string contents below the YAML separators \- frontmatter: string representation of YAML

Parameters:     

**string** \(_str_\)

Return type:     

dict\[str, _Any_\]

_classmethod _read\_file\(_path : str_\) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Frontmatter.read_file)\#     

Reads file at path and returns dict with separated frontmatter. See read\(\) for more info on dict return value.

Parameters:     

**path** \(_str_\)

Return type:     

dict\[str, _Any_\]

__On this page