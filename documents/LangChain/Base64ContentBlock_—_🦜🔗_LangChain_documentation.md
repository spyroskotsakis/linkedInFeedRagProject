# Base64ContentBlock — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.content_blocks.Base64ContentBlock.html
**Word Count:** 25
**Links Count:** 157
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# Base64ContentBlock\#

_class _langchain\_core.messages.content\_blocks.Base64ContentBlock[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/content_blocks.html#Base64ContentBlock)\#     

Content block for inline data from a base64 string.

mime\_type _: NotRequired\[str\]_\#     

type _: Literal\['image', 'audio', 'file'\]_\#     

Type of the content block.

source\_type _: Literal\['base64'\]_\#     

Source type \(base64\).

data _: str_\#     

Data as a base64 string.

__On this page