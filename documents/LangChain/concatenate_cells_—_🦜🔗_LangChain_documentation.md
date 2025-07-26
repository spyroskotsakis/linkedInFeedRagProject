# concatenate_cells — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notebook.concatenate_cells.html
**Word Count:** 53
**Links Count:** 385
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# concatenate\_cells\#

langchain\_community.document\_loaders.notebook.concatenate\_cells\(

    _cell : dict_,     _include\_outputs : bool_,     _max\_output\_length : int_,     _traceback : bool_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notebook.html#concatenate_cells)\#     

Combine cells information in a readable format ready to be used.

Parameters:     

  * **cell** \(_dict_\) – A dictionary

  * **include\_outputs** \(_bool_\) – Whether to include the outputs of the cell.

  * **max\_output\_length** \(_int_\) – Maximum length of the output to be displayed.

  * **traceback** \(_bool_\) – Whether to return a traceback of the error.

Returns:     

A string with the cell information.

Return type:     

str

__On this page