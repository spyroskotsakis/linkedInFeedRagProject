# OpenAIMetadataTagger — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger.html
**Word Count:** 136
**Links Count:** 128
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# OpenAIMetadataTagger\#

_class _langchain\_community.document\_transformers.openai\_functions.OpenAIMetadataTagger[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/openai_functions.html#OpenAIMetadataTagger)\#     

Bases: [`BaseDocumentTransformer`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.transformers.BaseDocumentTransformer.html#langchain_core.documents.transformers.BaseDocumentTransformer "langchain_core.documents.transformers.BaseDocumentTransformer"), `BaseModel`

Extract metadata tags from document contents using OpenAI functions.

> Example: >      >      >      >     from langchain_community.chat_models import ChatOpenAI >     from langchain_community.document_transformers import OpenAIMetadataTagger >     from langchain_core.documents import Document >      >     schema = { >         "properties": { >             "movie_title": { "type": "string" }, >             "critic": { "type": "string" }, >             "tone": { >                 "type": "string", >                 "enum": ["positive", "negative"] >             }, >             "rating": { >                 "type": "integer", >                 "description": "The number of stars the critic rated the movie" >             } >         }, >         "required": ["movie_title", "critic", "tone"] >     } >      >     # Must be an OpenAI model that supports functions >     llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613") >     tagging_chain = create_tagging_chain(schema, llm) >     document_transformer = OpenAIMetadataTagger(tagging_chain=tagging_chain) >     original_documents = [ >         Document(page_content="Review of The Bee Movie >     

By Roger Ebert

This is the greatest movie ever made. 4 out of 5 stars.”\),     

Document\(page\_content=”Review of The Godfather

By Anonymous

This movie was super boring. 1 out of 5 stars.”, metadata=\{“reliable”: False\}\),     

\]

enhanced\_documents = document\_transformer.transform\_documents\(original\_documents\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tagging\_chain _: Any_ _\[Required\]_\#     

The chain used to extract metadata from each document.

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/openai_functions.html#OpenAIMetadataTagger.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/openai_functions.html#OpenAIMetadataTagger.transform_documents)\#     

Automatically extract and populate metadata for each document according to the provided schema.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page