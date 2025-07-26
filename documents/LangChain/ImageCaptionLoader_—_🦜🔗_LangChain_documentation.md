# ImageCaptionLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.image_captions.ImageCaptionLoader.html
**Word Count:** 211
**Links Count:** 419
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# ImageCaptionLoader\#

_class _langchain\_community.document\_loaders.image\_captions.ImageCaptionLoader\(

    _images : str | Path | bytes | List\[str | bytes | Path\]_,     _blip\_processor : str = 'Salesforce/blip-image-captioning-base'_,     _blip\_model : str = 'Salesforce/blip-image-captioning-base'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/image_captions.html#ImageCaptionLoader)\#     

Load image captions.

By default, the loader utilizes the pre-trained Salesforce BLIP image captioning model. <https://huggingface.co/Salesforce/blip-image-captioning-base>

Initialize with a list of image data \(bytes\) or file paths

Parameters:     

  * **images** \(_str_ _|__Path_ _|__bytes_ _|__List_ _\[__str_ _|__bytes_ _|__Path_ _\]_\) – Either a single image or a list of images. Accepts image data \(bytes\) or file paths to images.

  * **blip\_processor** \(_str_\) – The name of the pre-trained BLIP processor.

  * **blip\_model** \(_str_\) – The name of the pre-trained BLIP model.

Methods

`__init__`\(images\[, blip\_processor, blip\_model\]\) | Initialize with a list of image data \(bytes\) or file paths   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load from a list of image data or file paths   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _images : str | Path | bytes | List\[str | bytes | Path\]_,     _blip\_processor : str = 'Salesforce/blip-image-captioning-base'_,     _blip\_model : str = 'Salesforce/blip-image-captioning-base'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/image_captions.html#ImageCaptionLoader.__init__)\#     

Initialize with a list of image data \(bytes\) or file paths

Parameters:     

  * **images** \(_str_ _|__Path_ _|__bytes_ _|__List_ _\[__str_ _|__bytes_ _|__Path_ _\]_\) – Either a single image or a list of images. Accepts image data \(bytes\) or file paths to images.

  * **blip\_processor** \(_str_\) – The name of the pre-trained BLIP processor.

  * **blip\_model** \(_str_\) – The name of the pre-trained BLIP model.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/image_captions.html#ImageCaptionLoader.load)\#     

Load from a list of image data or file paths

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using ImageCaptionLoader

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

__On this page