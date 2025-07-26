# parse_output — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/document_parse_parsers/langchain_upstage.document_parse_parsers.parse_output.html
**Word Count:** 41
**Links Count:** 75
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# parse\_output\#

langchain\_upstage.document\_parse\_parsers.parse\_output\(

    _data : dict_,     _output\_format : Literal\['text', 'html', 'markdown'\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse_parsers.html#parse_output)\#     

Parse the output data based on the specified output type.

Parameters:     

  * **data** \(_dict_\) – The data to be parsed.

  * **output\_format** \(_OutputFormat_\) – The output format to parse the element data into.

Returns:     

The parsed output.

Return type:     

str

Raises:     

**ValueError** – If the output type is invalid.

__On this page