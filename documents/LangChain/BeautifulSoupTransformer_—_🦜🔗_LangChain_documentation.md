# BeautifulSoupTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.beautiful_soup_transformer.BeautifulSoupTransformer.html
**Word Count:** 331
**Links Count:** 148
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# BeautifulSoupTransformer\#

_class _langchain\_community.document\_transformers.beautiful\_soup\_transformer.BeautifulSoupTransformer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer)\#     

Transform HTML content by extracting specific tags and removing unwanted ones.

Example               from langchain_community.document_transformers import BeautifulSoupTransformer          bs4_transformer = BeautifulSoupTransformer()     docs_transformed = bs4_transformer.transform_documents(docs)     

Initialize the transformer.

This checks if the BeautifulSoup4 package is installed. If not, it raises an ImportError.

Methods

`__init__`\(\) | Initialize the transformer.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `extract_tags`\(html\_content, tags, \*\[, ...\]\) | Extract specific tags from a given HTML content.   `remove_unnecessary_lines`\(content\) | Clean up the content by removing unnecessary lines.   `remove_unwanted_classnames`\(html\_content, ...\) | Remove unwanted classname from a given HTML content.   `remove_unwanted_tags`\(html\_content, unwanted\_tags\) | Remove unwanted tags from a given HTML content.   `transform_documents`\(documents\[, ...\]\) | Transform a list of Document objects by cleaning their HTML content.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.__init__)\#     

Initialize the transformer.

This checks if the BeautifulSoup4 package is installed. If not, it raises an ImportError.

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_static _extract\_tags\(

    _html\_content : str_,     _tags : List\[str\] | Tuple\[str, ...\]_,     _\*_ ,     _remove\_comments : bool = False_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.extract_tags)\#     

Extract specific tags from a given HTML content.

Parameters:     

  * **html\_content** \(_str_\) – The original HTML content string.

  * **tags** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _,__...__\]_\) – A list of tags to be extracted from the HTML.

  * **remove\_comments** \(_bool_\) – If set to True, the comments will be removed.

Returns:     

A string combining the content of the extracted tags.

Return type:     

str

_static _remove\_unnecessary\_lines\(

    _content : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.remove_unnecessary_lines)\#     

Clean up the content by removing unnecessary lines.

Parameters:     

**content** \(_str_\) – A string, which may contain unnecessary lines or spaces.

Returns:     

A cleaned string with unnecessary lines removed.

Return type:     

str

_static _remove\_unwanted\_classnames\(

    _html\_content : str_,     _unwanted\_classnames : List\[str\] | Tuple\[str, ...\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.remove_unwanted_classnames)\#     

Remove unwanted classname from a given HTML content.

Parameters:     

  * **html\_content** \(_str_\) – The original HTML content string.

  * **unwanted\_classnames** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _,__...__\]_\) – A list of classnames to be removed from the HTML.

Returns:     

A cleaned HTML string with unwanted classnames removed.

Return type:     

str

_static _remove\_unwanted\_tags\(

    _html\_content : str_,     _unwanted\_tags : List\[str\] | Tuple\[str, ...\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.remove_unwanted_tags)\#     

Remove unwanted tags from a given HTML content.

Parameters:     

  * **html\_content** \(_str_\) – The original HTML content string.

  * **unwanted\_tags** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _,__...__\]_\) – A list of tags to be removed from the HTML.

Returns:     

A cleaned HTML string with unwanted tags removed.

Return type:     

str

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _unwanted\_tags : List\[str\] | Tuple\[str, ...\] = \('script', 'style'\)_,     _tags\_to\_extract : List\[str\] | Tuple\[str, ...\] = \('p', 'li', 'div', 'a'\)_,     _remove\_lines : bool = True_,     _\*_ ,     _unwanted\_classnames : Tuple\[str, ...\] | List\[str\] = \(\)_,     _remove\_comments : bool = False_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#BeautifulSoupTransformer.transform_documents)\#     

Transform a list of Document objects by cleaning their HTML content.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Document objects containing HTML content.

  * **unwanted\_tags** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _,__...__\]_\) – A list of tags to be removed from the HTML.

  * **tags\_to\_extract** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _,__...__\]_\) – A list of tags whose content will be extracted.

  * **remove\_lines** \(_bool_\) – If set to True, unnecessary lines will be removed.

  * **unwanted\_classnames** \(_Tuple_ _\[__str_ _,__...__\]__|__List_ _\[__str_ _\]_\) – A list of class names to be removed from the HTML

  * **remove\_comments** \(_bool_\) – If set to True, comments will be removed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of Document objects with transformed content.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using BeautifulSoupTransformer

  * [Beautiful Soup](https://python.langchain.com/docs/integrations/document_transformers/beautiful_soup/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)