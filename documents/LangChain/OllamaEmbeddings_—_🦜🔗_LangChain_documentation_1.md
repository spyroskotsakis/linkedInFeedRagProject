# OllamaEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ollama/embeddings/langchain_ollama.embeddings.OllamaEmbeddings.html
**Word Count:** 635
**Links Count:** 130
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# OllamaEmbeddings\#

_class _langchain\_ollama.embeddings.OllamaEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ollama/embeddings.html#OllamaEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Ollama embedding model integration.

Set up a local Ollama instance:     

Install the Ollama package and set up a local Ollama instance using the instructions here: [ollama/ollama](https://github.com/ollama/ollama) .

You will need to choose a model to serve.

You can view a list of available models via the model library \(<https://ollama.com/library>\).

To fetch a model from the Ollama model library use `ollama pull <name-of-model>`.

For example, to pull the llama3 model:               ollama pull llama3     

This will download the default tagged version of the model. Typically, the default points to the latest, smallest sized-parameter model.

  * On Mac, the models will be downloaded to ~/.ollama/models

  * On Linux \(or WSL\), the models will be stored at /usr/share/ollama/.ollama/models

You can specify the exact version of the model of interest as such `ollama pull vicuna:13b-v1.5-16k-q4_0`.

To view pulled models:               ollama list     

To start serving:               ollama serve     

View the Ollama documentation for more commands.               ollama help     

Install the langchain-ollama integration package:                    pip install -U langchain_ollama     

Key init args — completion params:     

model: str     

Name of Ollama model to use.

base\_url: Optional\[str\]     

Base url the model is hosted under.

See full list of supported init args and their descriptions in the params section.

Instantiate:                    from langchain_ollama import OllamaEmbeddings          embed = OllamaEmbeddings(         model="llama3"     )     

Embed single text:                    input_text = "The meaning of life is 42"     vector = embed.embed_query(input_text)     print(vector[:3])                    [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Embed multiple texts:                    input_texts = ["Document 1...", "Document 2..."]     vectors = embed.embed_documents(input_texts)     print(len(vectors))     # The first 3 coordinates for the first vector     print(vectors[0][:3])                    2     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Async:                    vector = await embed.aembed_query(input_text)     print(vector[:3])          # multiple:     # await embed.aembed_documents(input_texts)                    [-0.009100092574954033, 0.005071679595857859, -0.0029193938244134188]     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _async\_client\_kwargs _: dict | None_ _ = \{\}_\#     

Additional kwargs to merge with client\_kwargs before passing to the httpx AsyncClient.

For a full list of the params, see the [HTTPX documentation](https://www.python-httpx.org/api/#asyncclient).

_param _base\_url _: str | None_ _ = None_\#     

Base url the model is hosted under.

_param _client\_kwargs _: dict | None_ _ = \{\}_\#     

Additional kwargs to pass to the httpx clients. These arguments are passed to both synchronous and async clients. Use sync\_client\_kwargs and async\_client\_kwargs to pass different arguments to synchronous and asynchronous clients.

_param _keep\_alive _: int | None_ _ = None_\#     

controls how long the model will stay loaded into memory following the request \(default: 5m\)

_param _mirostat _: int | None_ _ = None_\#     

Enable Mirostat sampling for controlling perplexity. \(default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0\)

_param _mirostat\_eta _: float | None_ _ = None_\#     

Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive. \(Default: 0.1\)

_param _mirostat\_tau _: float | None_ _ = None_\#     

Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text. \(Default: 5.0\)

_param _model _: str_ _\[Required\]_\#     

Model name to use.

_param _num\_ctx _: int | None_ _ = None_\#     

Sets the size of the context window used to generate the next token. \(Default: 2048\)

_param _num\_gpu _: int | None_ _ = None_\#     

The number of GPUs to use. On macOS it defaults to 1 to enable metal support, 0 to disable.

_param _num\_thread _: int | None_ _ = None_\#     

Sets the number of threads to use during computation. By default, Ollama will detect this for optimal performance. It is recommended to set this value to the number of physical CPU cores your system has \(as opposed to the logical number of cores\).

_param _repeat\_last\_n _: int | None_ _ = None_\#     

Sets how far back for the model to look back to prevent repetition. \(Default: 64, 0 = disabled, -1 = num\_ctx\)

_param _repeat\_penalty _: float | None_ _ = None_\#     

Sets how strongly to penalize repetitions. A higher value \(e.g., 1.5\) will penalize repetitions more strongly, while a lower value \(e.g., 0.9\) will be more lenient. \(Default: 1.1\)

_param _stop _: list\[str\] | None_ _ = None_\#     

Sets the stop tokens to use.

_param _sync\_client\_kwargs _: dict | None_ _ = \{\}_\#     

Additional kwargs to merge with client\_kwargs before passing to the HTTPX Client.

For a full list of the params, see the [HTTPX documentation](https://www.python-httpx.org/api/#client).

_param _temperature _: float | None_ _ = None_\#     

The temperature of the model. Increasing the temperature will make the model answer more creatively. \(Default: 0.8\)

_param _tfs\_z _: float | None_ _ = None_\#     

Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value \(e.g., 2.0\) will reduce the impact more, while a value of 1.0 disables this setting. \(default: 1\)

_param _top\_k _: int | None_ _ = None_\#     

Reduces the probability of generating nonsense. A higher value \(e.g. 100\) will give more diverse answers, while a lower value \(e.g. 10\) will be more conservative. \(Default: 40\)

_param _top\_p _: float | None_ _ = None_\#     

Works together with top-k. A higher value \(e.g., 0.95\) will lead to more diverse text, while a lower value \(e.g., 0.5\) will generate more focused and conservative text. \(Default: 0.9\)

_param _validate\_model\_on\_init _: bool_ _ = False_\#     

Whether to validate the model exists in ollama locally on initialization.

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ollama/embeddings.html#OllamaEmbeddings.aembed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ollama/embeddings.html#OllamaEmbeddings.aembed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ollama/embeddings.html#OllamaEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ollama/embeddings.html#OllamaEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

list\[float\]

Examples using OllamaEmbeddings

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [Ollama](https://python.langchain.com/docs/integrations/providers/ollama/)

__On this page