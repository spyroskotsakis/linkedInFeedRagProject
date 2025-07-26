# validate_file_path — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/document_parse/langchain_upstage.document_parse.validate_file_path.html
**Word Count:** 38
**Links Count:** 75
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# validate\_file\_path\#

langchain\_upstage.document\_parse.validate\_file\_path\(

    _file\_path : str | Path | List\[str\] | List\[Path\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse.html#validate_file_path)\#     

Validates if a file exists at the given file path.

Parameters:     

**file\_path** \(_Union_ _\[__str_ _,__Path_ _,__List_ _\[__str_ _\]__,__List_ _\[__Path_ _\]_\) – The file path\(s\) to be validated.

Raises:     

**FileNotFoundError** – If the file or any of the files in the list do not exist.

Return type:     

None

__On this page