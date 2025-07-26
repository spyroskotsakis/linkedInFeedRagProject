# CustomPersister — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomPersister.html
**Word Count:** 41
**Links Count:** 84
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# CustomPersister\#

_class _langchain\_tests.conftest.CustomPersister[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/conftest.html#CustomPersister)\#     

A custom persister for VCR that uses the CustomSerializer.

Methods

`load_cassette`\(cassette\_path, serializer\) | Load a cassette from a file.   ---|---   `save_cassette`\(cassette\_path, cassette\_dict, ...\) | Save a cassette to a file.      _classmethod _load\_cassette\(

    _cassette\_path : str | PathLike\[str\]_,     _serializer : [CustomSerializer](https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomSerializer.html#langchain_tests.conftest.CustomSerializer "langchain_tests.conftest.CustomSerializer")_, \) → tuple\[dict, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/conftest.html#CustomPersister.load_cassette)\#     

Load a cassette from a file.

Parameters:     

  * **cassette\_path** \(_str_ _|__PathLike_ _\[__str_ _\]_\)

  * **serializer** \([_CustomSerializer_](https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomSerializer.html#langchain_tests.conftest.CustomSerializer "langchain_tests.conftest.CustomSerializer")\)

Return type:     

tuple\[dict, dict\]

_static _save\_cassette\(

    _cassette\_path : str | PathLike\[str\]_,     _cassette\_dict : dict_,     _serializer : [CustomSerializer](https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomSerializer.html#langchain_tests.conftest.CustomSerializer "langchain_tests.conftest.CustomSerializer")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/conftest.html#CustomPersister.save_cassette)\#     

Save a cassette to a file.

Parameters:     

  * **cassette\_path** \(_str_ _|__PathLike_ _\[__str_ _\]_\)

  * **cassette\_dict** \(_dict_\)

  * **serializer** \([_CustomSerializer_](https://python.langchain.com/api_reference/standard_tests/conftest/langchain_tests.conftest.CustomSerializer.html#langchain_tests.conftest.CustomSerializer "langchain_tests.conftest.CustomSerializer")\)

Return type:     

None

__On this page