# TagParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/llms/langchain_experimental.llms.anthropic_functions.TagParser.html
**Word Count:** 281
**Links Count:** 199
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# TagParser\#

_class _langchain\_experimental.llms.anthropic\_functions.TagParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llms/anthropic_functions.html#TagParser)\#     

Parser for the tool tags.

A heavy-handed solution, but it’s fast for prototyping.

Might be re-implemented later to restrict scope to the limited grammar, and more efficiency.

Uses an HTML parser to parse a limited grammar that allows for syntax of the form:

> INPUT -> JUNK? VALUE\* JUNK -> JUNK\_CHARACTER+ JUNK\_CHARACTER -> whitespace | , VALUE -> <IDENTIFIER>DATA</IDENTIFIER> | OBJECT OBJECT -> <IDENTIFIER>VALUE+</IDENTIFIER> IDENTIFIER -> \[a-Z\]\[a-Z0-9\_\]\* DATA -> .\*

Interprets the data to allow repetition of tags and recursion to support representation of complex types.

^ Just another approximately wrong grammar specification.

Attributes

`CDATA_CONTENT_ELEMENTS` |    ---|---      Methods

`__init__`\(\) | A heavy-handed solution, but it's fast for prototyping.   ---|---   `check_for_whole_start_tag`\(i\) |    `clear_cdata_mode`\(\) |    `close`\(\) | Handle any buffered data.   `feed`\(data\) | Feed data to the parser.   `get_starttag_text`\(\) | Return full source of start tag: '<...>'.   `getpos`\(\) | Return current line number and offset.   `goahead`\(end\) |    `handle_charref`\(name\) |    `handle_comment`\(data\) |    `handle_data`\(data\) | Hook when handling data.   `handle_decl`\(decl\) |    `handle_endtag`\(tag\) | Hook when a tag is closed.   `handle_entityref`\(name\) |    `handle_pi`\(data\) |    `handle_startendtag`\(tag, attrs\) |    `handle_starttag`\(tag, attrs\) | Hook when a new tag is encountered.   `parse_bogus_comment`\(i\[, report\]\) |    `parse_comment`\(i\[, report\]\) |    `parse_declaration`\(i\) |    `parse_endtag`\(i\) |    `parse_html_declaration`\(i\) |    `parse_marked_section`\(i\[, report\]\) |    `parse_pi`\(i\) |    `parse_starttag`\(i\) |    `reset`\(\) | Reset this instance.   `set_cdata_mode`\(elem\) |    `unknown_decl`\(data\) |    `updatepos`\(i, j\) |       \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llms/anthropic_functions.html#TagParser.__init__)\#     

A heavy-handed solution, but it’s fast for prototyping.

Might be re-implemented later to restrict scope to the limited grammar, and more efficiency.

Uses an HTML parser to parse a limited grammar that allows for syntax of the form:

> INPUT -> JUNK? VALUE\* JUNK -> JUNK\_CHARACTER+ JUNK\_CHARACTER -> whitespace | , VALUE -> <IDENTIFIER>DATA</IDENTIFIER> | OBJECT OBJECT -> <IDENTIFIER>VALUE+</IDENTIFIER> IDENTIFIER -> \[a-Z\]\[a-Z0-9\_\]\* DATA -> .\*

Interprets the data to allow repetition of tags and recursion to support representation of complex types.

^ Just another approximately wrong grammar specification.

Return type:     

None

check\_for\_whole\_start\_tag\(_i_\)\#     

clear\_cdata\_mode\(\)\#     

close\(\)\#     

Handle any buffered data.

feed\(_data_\)\#     

Feed data to the parser.

Call this as often as you want, with as little or as much text as you want \(may include ‘n’\).

get\_starttag\_text\(\)\#     

Return full source of start tag: ‘<…>’.

getpos\(\)\#     

Return current line number and offset.

goahead\(_end_\)\#     

handle\_charref\(_name_\)\#     

handle\_comment\(_data_\)\#     

handle\_data\(_data : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llms/anthropic_functions.html#TagParser.handle_data)\#     

Hook when handling data.

Parameters:     

**data** \(_str_\)

Return type:     

None

handle\_decl\(_decl_\)\#     

handle\_endtag\(_tag : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llms/anthropic_functions.html#TagParser.handle_endtag)\#     

Hook when a tag is closed.

Parameters:     

**tag** \(_str_\)

Return type:     

None

handle\_entityref\(_name_\)\#     

handle\_pi\(_data_\)\#     

handle\_startendtag\(_tag_ , _attrs_\)\#     

handle\_starttag\(

    _tag : str_,     _attrs : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llms/anthropic_functions.html#TagParser.handle_starttag)\#     

Hook when a new tag is encountered.

Parameters:     

  * **tag** \(_str_\)

  * **attrs** \(_Any_\)

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