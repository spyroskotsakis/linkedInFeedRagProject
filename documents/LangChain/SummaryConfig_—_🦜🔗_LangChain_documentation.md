# SummaryConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.SummaryConfig.html
**Word Count:** 45
**Links Count:** 322
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# SummaryConfig\#

_class _langchain\_community.vectorstores.vectara.SummaryConfig\(

    _is\_enabled : bool = False_,     _max\_results : int = 7_,     _response\_lang : str = 'eng'_,     _prompt\_name : str = 'vectara-summary-ext-24-05-med-omni'_,     _stream : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#SummaryConfig)\#     

Configuration for summary generation.

is\_enabled: True if summary is enabled, False otherwise max\_results: maximum number of results to summarize response\_lang: requested language for the summary prompt\_name: name of the prompt to use for summarization

> \(see <https://docs.vectara.com/docs/learn/grounded-generation/select-a-summarizer>\)

Attributes

`is_enabled` |    ---|---   `max_results` |    `prompt_name` |    `response_lang` |    `stream` |       Methods

`__init__`\(\[is\_enabled, max\_results, ...\]\) |    ---|---      Parameters:     

  * **is\_enabled** \(_bool_\)

  * **max\_results** \(_int_\)

  * **response\_lang** \(_str_\)

  * **prompt\_name** \(_str_\)

  * **stream** \(_bool_\)

\_\_init\_\_\(

    _is\_enabled : bool = False_,     _max\_results : int = 7_,     _response\_lang : str = 'eng'_,     _prompt\_name : str = 'vectara-summary-ext-24-05-med-omni'_,     _stream : bool = False_, \) → None\#     

Parameters:     

  * **is\_enabled** \(_bool_\)

  * **max\_results** \(_int_\)

  * **response\_lang** \(_str_\)

  * **prompt\_name** \(_str_\)

  * **stream** \(_bool_\)

Return type:     

None

Examples using SummaryConfig

  * [Vectara](https://python.langchain.com/docs/integrations/vectorstores/vectara/)

  * [Vectara Chat](https://python.langchain.com/docs/integrations/providers/vectara/vectara_chat/)

__On this page