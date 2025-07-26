# extract_from_images_with_rapidocr — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.extract_from_images_with_rapidocr.html
**Word Count:** 26
**Links Count:** 385
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# extract\_from\_images\_with\_rapidocr\#

langchain\_community.document\_loaders.parsers.pdf.extract\_from\_images\_with\_rapidocr\(

    _images : Sequence\[Iterable\[ndarray\] | bytes\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#extract_from_images_with_rapidocr)\#     

Extract text from images with RapidOCR.

Parameters:     

**images** \(_Sequence_ _\[__Iterable_ _\[__ndarray_ _\]__|__bytes_ _\]_\) – Images to extract text from.

Returns:     

Text extracted from images.

Raises:     

**ImportError** – If rapidocr-onnxruntime package is not installed.

Return type:     

str

__On this page