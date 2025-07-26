# CustomSerializer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomSerializer.html
**Word Count:** 92
**Links Count:** 80
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# CustomSerializer\#

_class _langchain\_tests.conftest.CustomSerializer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/conftest.html#CustomSerializer)\#     

Custom serializer for VCR cassettes using YAML and gzip.

We’re using a custom serializer to avoid the default yaml serializer used by VCR, which is not designed to be safe for untrusted input.

This step is an extra precaution necessary because the cassette files are in compressed YAML format, which makes it more difficult to inspect their contents during development or debugging.

Methods

`deserialize`\(data\) | Decompress data and convert it from YAML.   ---|---   `serialize`\(cassette\_dict\) | Convert cassette to YAML and compress it.      _static _deserialize\(_data : bytes_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/conftest.html#CustomSerializer.deserialize)\#     

Decompress data and convert it from YAML.

Parameters:     

**data** \(_bytes_\)

Return type:     

dict

_static _serialize\(_cassette\_dict : dict_\) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/conftest.html#CustomSerializer.serialize)\#     

Convert cassette to YAML and compress it.

Parameters:     

**cassette\_dict** \(_dict_\)

Return type:     

bytes

__On this page