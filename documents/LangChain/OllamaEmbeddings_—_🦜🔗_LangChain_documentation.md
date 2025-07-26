# OllamaEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.ollama.OllamaEmbeddings.html
**Word Count:** 497
**Links Count:** 261
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# OllamaEmbeddings\#

_class _langchain\_community.embeddings.ollama.OllamaEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ollama.html#OllamaEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.3.1: Use `:class:`~langchain_ollama.OllamaEmbeddings`` instead. It will not be removed until langchain-community==1.0.0.

Ollama locally runs large language models.

To use, follow the instructions at <https://ollama.ai/>.

Example               from langchain_community.embeddings import OllamaEmbeddings     ollama_emb = OllamaEmbeddings(         model="llama:7b",     )     r1 = ollama_emb.embed_documents(         [             "Alpha is the first letter of Greek alphabet",             "Beta is the second letter of Greek alphabet",         ]     )     r2 = ollama_emb.embed_query(         "What is the second letter of Greek alphabet"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _base\_url _: str_ _ = 'http://localhost:11434'_\#     

Base url the model is hosted under.

_param _embed\_instruction _: str_ _ = 'passage: '_\#     

Instruction used to embed documents.

_param _headers _: dict | None_ _ = None_\#     

Additional headers to pass to endpoint \(e.g. Authorization, Referer\). This is useful when Ollama is hosted on cloud services that require tokens for authentication.

_param _mirostat _: int | None_ _ = None_\#     

Enable Mirostat sampling for controlling perplexity. \(default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0\)

_param _mirostat\_eta _: float | None_ _ = None_\#     

Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive. \(Default: 0.1\)

_param _mirostat\_tau _: float | None_ _ = None_\#     

Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text. \(Default: 5.0\)

_param _model _: str_ _ = 'llama2'_\#     

Model name to use.

_param _model\_kwargs _: dict | None_ _ = None_\#     

Other model keyword args

_param _num\_ctx _: int | None_ _ = None_\#     

Sets the size of the context window used to generate the next token. \(Default: 2048\)

_param _num\_gpu _: int | None_ _ = None_\#     

The number of GPUs to use. On macOS it defaults to 1 to enable metal support, 0 to disable.

_param _num\_thread _: int | None_ _ = None_\#     

Sets the number of threads to use during computation. By default, Ollama will detect this for optimal performance. It is recommended to set this value to the number of physical CPU cores your system has \(as opposed to the logical number of cores\).

_param _query\_instruction _: str_ _ = 'query: '_\#     

Instruction used to embed the query.

_param _repeat\_last\_n _: int | None_ _ = None_\#     

Sets how far back for the model to look back to prevent repetition. \(Default: 64, 0 = disabled, -1 = num\_ctx\)

_param _repeat\_penalty _: float | None_ _ = None_\#     

Sets how strongly to penalize repetitions. A higher value \(e.g., 1.5\) will penalize repetitions more strongly, while a lower value \(e.g., 0.9\) will be more lenient. \(Default: 1.1\)

_param _show\_progress _: bool_ _ = False_\#     

Whether to show a tqdm progress bar. Must have tqdm installed.

_param _stop _: List\[str\] | None_ _ = None_\#     

Sets the stop tokens to use.

_param _temperature _: float | None_ _ = None_\#     

The temperature of the model. Increasing the temperature will make the model answer more creatively. \(Default: 0.8\)

_param _tfs\_z _: float | None_ _ = None_\#     

Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value \(e.g., 2.0\) will reduce the impact more, while a value of 1.0 disables this setting. \(default: 1\)

_param _top\_k _: int | None_ _ = None_\#     

Reduces the probability of generating nonsense. A higher value \(e.g. 100\) will give more diverse answers, while a lower value \(e.g. 10\) will be more conservative. \(Default: 40\)

_param _top\_p _: float | None_ _ = None_\#     

Works together with top-k. A higher value \(e.g., 0.95\) will lead to more diverse text, while a lower value \(e.g., 0.5\) will generate more focused and conservative text. \(Default: 0.9\)

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ollama.html#OllamaEmbeddings.embed_documents)\#     

Embed documents using an Ollama deployed embedding model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ollama.html#OllamaEmbeddings.embed_query)\#     

Embed a query using a Ollama deployed embedding model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using OllamaEmbeddings

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [Ollama](https://python.langchain.com/docs/integrations/providers/ollama/)

__On this page