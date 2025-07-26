# ParseOracleDocMetadata — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleai.ParseOracleDocMetadata.html
**Word Count:** 127
**Links Count:** 479
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# ParseOracleDocMetadata\#

_class _langchain\_community.document\_loaders.oracleai.ParseOracleDocMetadata[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#ParseOracleDocMetadata)\#     

Parse Oracle doc metadata…

Initialize and reset this instance.

If convert\_charrefs is True \(the default\), all character references are automatically converted to the corresponding Unicode characters.

Attributes

`CDATA_CONTENT_ELEMENTS` |    ---|---      Methods

`__init__`\(\) | Initialize and reset this instance.   ---|---   `check_for_whole_start_tag`\(i\) |    `clear_cdata_mode`\(\) |    `close`\(\) | Handle any buffered data.   `feed`\(data\) | Feed data to the parser.   `get_metadata`\(\) |    `get_starttag_text`\(\) | Return full source of start tag: '<...>'.   `getpos`\(\) | Return current line number and offset.   `goahead`\(end\) |    `handle_charref`\(name\) |    `handle_comment`\(data\) |    `handle_data`\(data\) |    `handle_decl`\(decl\) |    `handle_endtag`\(tag\) |    `handle_entityref`\(name\) |    `handle_pi`\(data\) |    `handle_startendtag`\(tag, attrs\) |    `handle_starttag`\(tag, attrs\) |    `parse_bogus_comment`\(i\[, report\]\) |    `parse_comment`\(i\[, report\]\) |    `parse_declaration`\(i\) |    `parse_endtag`\(i\) |    `parse_html_declaration`\(i\) |    `parse_marked_section`\(i\[, report\]\) |    `parse_pi`\(i\) |    `parse_starttag`\(i\) |    `reset`\(\) | Reset this instance.   `set_cdata_mode`\(elem\) |    `unknown_decl`\(data\) |    `updatepos`\(i, j\) |       \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#ParseOracleDocMetadata.__init__)\#     

Initialize and reset this instance.

If convert\_charrefs is True \(the default\), all character references are automatically converted to the corresponding Unicode characters.

Return type:     

None

check\_for\_whole\_start\_tag\(_i_\)\#     

clear\_cdata\_mode\(\)\#     

close\(\)\#     

Handle any buffered data.

feed\(_data_\)\#     

Feed data to the parser.

Call this as often as you want, with as little or as much text as you want \(may include ‘n’\).

get\_metadata\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#ParseOracleDocMetadata.get_metadata)\#     

Return type:     

_Dict_\[str, _Any_\]

get\_starttag\_text\(\)\#     

Return full source of start tag: ‘<…>’.

getpos\(\)\#     

Return current line number and offset.

goahead\(_end_\)\#     

handle\_charref\(_name_\)\#     

handle\_comment\(_data_\)\#     

handle\_data\(_data : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#ParseOracleDocMetadata.handle_data)\#     

Parameters:     

**data** \(_str_\)

Return type:     

None

handle\_decl\(_decl_\)\#     

handle\_endtag\(_tag_\)\#     

handle\_entityref\(_name_\)\#     

handle\_pi\(_data_\)\#     

handle\_startendtag\(_tag_ , _attrs_\)\#     

handle\_starttag\(

    _tag : str_,     _attrs : List\[Tuple\[str, str | None\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#ParseOracleDocMetadata.handle_starttag)\#     

Parameters:     

  * **tag** \(_str_\)

  * **attrs** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _|__None_ _\]__\]_\)

Return type:     

None

parse\_bogus\_comment\(_i_ , _report =1_\)\#     

parse\_comment\(_i_ , _report =1_\)\#     

parse\_declaration\(_i_\)\#     

parse\_endtag\(_i_\)\#     

parse\_html\_declaration\(_i_\)\#     

parse\_marked\_section\(_i_ , _report =1_\)\#     

parse\_pi\(_i_\)\#     

parse\_starttag\(_i_\)\#     

reset\(\)\#     

Reset this instance. Loses all unprocessed data.

set\_cdata\_mode\(_elem_\)\#     

unknown\_decl\(_data_\)\#     

updatepos\(_i_ , _j_\)\#     

__On this page