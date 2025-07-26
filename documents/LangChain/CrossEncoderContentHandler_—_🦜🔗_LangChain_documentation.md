# CrossEncoderContentHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler.html
**Word Count:** 13
**Links Count:** 108
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# CrossEncoderContentHandler\#

_class _langchain\_community.cross\_encoders.sagemaker\_endpoint.CrossEncoderContentHandler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/sagemaker_endpoint.html#CrossEncoderContentHandler)\#     

Content handler for CrossEncoder class.

Attributes

`accepts` |    ---|---   `content_type` |       Methods

`transform_input`\(text\_pairs\) |    ---|---   `transform_output`\(output\) |       transform\_input\(

    _text\_pairs : List\[Tuple\[str, str\]\]_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/sagemaker_endpoint.html#CrossEncoderContentHandler.transform_input)\#     

Parameters:     

**text\_pairs** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\)

Return type:     

bytes

transform\_output\(

    _output : Any_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/sagemaker_endpoint.html#CrossEncoderContentHandler.transform_output)\#     

Parameters:     

**output** \(_Any_\)

Return type:     

_List_\[float\]

__On this page