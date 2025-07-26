# init_chat_model — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html
**Word Count:** 629
**Links Count:** 87
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# init\_chat\_model\#

langchain.chat\_models.base.init\_chat\_model\(

    _model : str_,     _\*_ ,     _model\_provider : str | None = None_,     _configurable\_fields : Literal\[None\] = None_,     _config\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chat_models/base.html#init_chat_model)\# langchain.chat\_models.base.init\_chat\_model\(

    _model : Literal\[None\] = None_,     _\*_ ,     _model\_provider : str | None = None_,     _configurable\_fields : Literal\[None\] = None_,     _config\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → \_ConfigurableModel langchain.chat\_models.base.init\_chat\_model\(

    _model : str | None = None_,     _\*_ ,     _model\_provider : str | None = None_,     _configurable\_fields : Literal\['any'\] | list\[str\] | tuple\[str, ...\] = None_,     _config\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → \_ConfigurableModel     

Initialize a ChatModel from the model name and provider.

**Note:** Must have the integration package corresponding to the model provider installed.

Parameters:     

  * **model** – The name of the model, e.g. “o3-mini”, “claude-3-5-sonnet-latest”. You can also specify model and model provider in a single argument using ‘\{model\_provider\}:\{model\}’ format, e.g. “openai:o1”.

  * **model\_provider** – 

The model provider if not specified as part of model arg \(see above\). Supported model\_provider values and the corresponding integration package are:

    * ’openai’ -> langchain-openai

    * ’anthropic’ -> langchain-anthropic

    * ’azure\_openai’ -> langchain-openai

    * ’azure\_ai’ -> langchain-azure-ai

    * ’google\_vertexai’ -> langchain-google-vertexai

    * ’google\_genai’ -> langchain-google-genai

    * ’bedrock’ -> langchain-aws

    * ’bedrock\_converse’ -> langchain-aws

    * ’cohere’ -> langchain-cohere

    * ’fireworks’ -> langchain-fireworks

    * ’together’ -> langchain-together

    * ’mistralai’ -> langchain-mistralai

    * ’huggingface’ -> langchain-huggingface

    * ’groq’ -> langchain-groq

    * ’ollama’ -> langchain-ollama

    * ’google\_anthropic\_vertex’ -> langchain-google-vertexai

    * ’deepseek’ -> langchain-deepseek

    * ’ibm’ -> langchain-ibm

    * ’nvidia’ -> langchain-nvidia-ai-endpoints

    * ’xai’ -> langchain-xai

    * ’perplexity’ -> langchain-perplexity

Will attempt to infer model\_provider from model if not specified. The following providers will be inferred based on these model prefixes:

    * ’gpt-3…’ | ‘gpt-4…’ | ‘o1…’ -> ‘openai’

    * ’claude…’ -> ‘anthropic’

    * ’amazon….’ -> ‘bedrock’

    * ’gemini…’ -> ‘google\_vertexai’

    * ’command…’ -> ‘cohere’

    * ’accounts/fireworks…’ -> ‘fireworks’

    * ’mistral…’ -> ‘mistralai’

    * ’deepseek…’ -> ‘deepseek’

    * ’grok…’ -> ‘xai’

    * ’sonar…’ -> ‘perplexity’

  * **configurable\_fields** – 

Which model parameters are configurable:

    * None: No configurable fields.

    * ”any”: All fields are configurable. _See Security Note below._

    * Union\[List\[str\], Tuple\[str, …\]\]: Specified fields are configurable.

Fields are assumed to have config\_prefix stripped if there is a config\_prefix. If model is specified, then defaults to None. If model is not specified, then defaults to `("model", "model_provider")`.

**\*Security Note\*** : Setting `configurable_fields="any"` means fields like api\_key, base\_url, etc. can be altered at runtime, potentially redirecting model requests to a different service/user. Make sure that if you’re accepting untrusted configurations that you enumerate the `configurable_fields=(...)` explicitly.

  * **config\_prefix** – If config\_prefix is a non-empty string then model will be configurable at runtime via the `config["configurable"]["{config_prefix}_{param}"]` keys. If config\_prefix is an empty string then model will be configurable via `config["configurable"]["{param}"]`.

  * **temperature** – Model temperature.

  * **max\_tokens** – Max output tokens.

  * **timeout** – The maximum time \(in seconds\) to wait for a response from the model before canceling the request.

  * **max\_retries** – The maximum number of attempts the system will make to resend a request if it fails due to issues like network timeouts or rate limits.

  * **base\_url** – The URL of the API endpoint where requests are sent.

  * **rate\_limiter** – A `BaseRateLimiter` to space out requests to avoid exceeding rate limits.

  * **kwargs** – Additional model-specific keyword args to pass to `<<selected ChatModel>>.__init__(model=model_name, **kwargs)`.

Returns:     

A BaseChatModel corresponding to the model\_name and model\_provider specified if configurability is inferred to be False. If configurable, a chat model emulator that initializes the underlying model at runtime once a config is passed in.

Raises:     

  * **ValueError** – If model\_provider cannot be inferred or isn’t supported.

  * **ImportError** – If the model provider integration package is not installed.

Init non-configurable model               # pip install langchain langchain-openai langchain-anthropic langchain-google-vertexai     from langchain.chat_models import init_chat_model          o3_mini = init_chat_model("openai:o3-mini", temperature=0)     claude_sonnet = init_chat_model("anthropic:claude-3-5-sonnet-latest", temperature=0)     gemini_2_flash = init_chat_model("google_vertexai:gemini-2.0-flash", temperature=0)          o3_mini.invoke("what's your name")     claude_sonnet.invoke("what's your name")     gemini_2_flash.invoke("what's your name")     

Partially configurable model with no default               # pip install langchain langchain-openai langchain-anthropic     from langchain.chat_models import init_chat_model          # We don't need to specify configurable=True if a model isn't specified.     configurable_model = init_chat_model(temperature=0)          configurable_model.invoke(         "what's your name",         config={"configurable": {"model": "gpt-4o"}}     )     # GPT-4o response          configurable_model.invoke(         "what's your name",         config={"configurable": {"model": "claude-3-5-sonnet-latest"}}     )     # claude-3.5 sonnet response     

Fully configurable model with a default               # pip install langchain langchain-openai langchain-anthropic     from langchain.chat_models import init_chat_model          configurable_model_with_default = init_chat_model(         "openai:gpt-4o",         configurable_fields="any",  # this allows us to configure other params like temperature, max_tokens, etc at runtime.         config_prefix="foo",         temperature=0     )          configurable_model_with_default.invoke("what's your name")     # GPT-4o response with temperature 0          configurable_model_with_default.invoke(         "what's your name",         config={             "configurable": {                 "foo_model": "anthropic:claude-3-5-sonnet-20240620",                 "foo_temperature": 0.6             }         }     )     # Claude-3.5 sonnet response with temperature 0.6     

Bind tools to a configurable model

You can call any ChatModel declarative methods on a configurable model in the same way that you would with a normal model.               # pip install langchain langchain-openai langchain-anthropic     from langchain.chat_models import init_chat_model     from pydantic import BaseModel, Field          class GetWeather(BaseModel):         '''Get the current weather in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          class GetPopulation(BaseModel):         '''Get the current population in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          configurable_model = init_chat_model(         "gpt-4o",         configurable_fields=("model", "model_provider"),         temperature=0     )          configurable_model_with_tools = configurable_model.bind_tools([GetWeather, GetPopulation])     configurable_model_with_tools.invoke(         "Which city is hotter today and which is bigger: LA or NY?"     )     # GPT-4o response with tool calls          configurable_model_with_tools.invoke(         "Which city is hotter today and which is bigger: LA or NY?",         config={"configurable": {"model": "claude-3-5-sonnet-20240620"}}     )     # Claude-3.5 sonnet response with tools     

Added in version 0.2.7.

Changed in version 0.2.8: Support for `configurable_fields` and `config_prefix` added.

Changed in version 0.2.12: Support for Ollama via langchain-ollama package added \(langchain\_ollama.ChatOllama\). Previously, the now-deprecated langchain-community version of Ollama was imported \(langchain\_community.chat\_models.ChatOllama\).

Support for AWS Bedrock models via the Converse API added \(model\_provider=”bedrock\_converse”\).

Changed in version 0.3.5: Out of beta.

Changed in version 0.3.19: Support for Deepseek, IBM, Nvidia, and xAI models added.

Examples using init\_chat\_model

  * [How to init any model in one line](https://python.langchain.com/docs/how_to/chat_models_universal_init/)

  * [How to select examples from a LangSmith dataset](https://python.langchain.com/docs/how_to/example_selectors_langsmith/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)