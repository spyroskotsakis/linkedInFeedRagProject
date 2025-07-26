# FileEncoding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.helpers.FileEncoding.html
**Word Count:** 57
**Links Count:** 391
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# FileEncoding\#

_class _langchain\_community.document\_loaders.helpers.FileEncoding\(

    _encoding : str | None_,     _confidence : float_,     _language : str | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/helpers.html#FileEncoding)\#     

File encoding as the NamedTuple.

Create new instance of FileEncoding\(encoding, confidence, language\)

Attributes

`confidence` | The confidence of the encoding.   ---|---   `encoding` | The encoding of the file.   `language` | The language of the file.      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      Parameters:     

  * **encoding** \(_str_ _|__None_\)

  * **confidence** \(_float_\)

  * **language** \(_str_ _|__None_\)

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)