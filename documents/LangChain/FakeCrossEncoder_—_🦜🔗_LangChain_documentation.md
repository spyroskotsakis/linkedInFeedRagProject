# FakeCrossEncoder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.fake.FakeCrossEncoder.html
**Word Count:** 53
**Links Count:** 104
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# FakeCrossEncoder\#

_class _langchain\_community.cross\_encoders.fake.FakeCrossEncoder[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/fake.html#FakeCrossEncoder)\#     

Bases: [`BaseCrossEncoder`](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.html#langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder "langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder"), `BaseModel`

Fake cross encoder model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

score\(

    _text\_pairs : List\[Tuple\[str, str\]\]_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/fake.html#FakeCrossEncoder.score)\#     

Score pairs’ similarity.

Parameters:     

**text\_pairs** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\) – List of pairs of texts.

Returns:     

List of scores.

Return type:     

_List_\[float\]

__On this page