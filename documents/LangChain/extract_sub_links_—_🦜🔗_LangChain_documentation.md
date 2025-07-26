# extract_sub_links — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.html.extract_sub_links.html
**Word Count:** 91
**Links Count:** 166
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# extract\_sub\_links\#

langchain\_core.utils.html.extract\_sub\_links\(

    _raw\_html : str_,     _url : str_,     _\*_ ,     _base\_url : str | None = None_,     _pattern : str | Pattern | None = None_,     _prevent\_outside : bool = True_,     _exclude\_prefixes : Sequence\[str\] = \(\)_,     _continue\_on\_failure : bool = False_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/html.html#extract_sub_links)\#     

Extract all links from a raw HTML string and convert into absolute paths.

Parameters:     

  * **raw\_html** \(_str_\) – original HTML.

  * **url** \(_str_\) – the url of the HTML.

  * **base\_url** \(_str_ _|__None_\) – the base URL to check for outside links against.

  * **pattern** \(_str_ _|__Pattern_ _|__None_\) – Regex to use for extracting links from raw HTML.

  * **prevent\_outside** \(_bool_\) – If True, ignore external links which are not children of the base URL.

  * **exclude\_prefixes** \(_Sequence_ _\[__str_ _\]_\) – Exclude any URLs that start with one of these prefixes.

  * **continue\_on\_failure** \(_bool_\) – If True, continue if parsing a specific link raises an exception. Otherwise, raise the exception.

Returns:     

sub links.

Return type:     

list\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)