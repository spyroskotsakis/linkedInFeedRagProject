# ChatAnthropic — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html
**Word Count:** 4046
**Links Count:** 336
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# ChatAnthropic\#

_class _langchain\_anthropic.chat\_models.ChatAnthropic[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_anthropic/chat_models.html#ChatAnthropic)\#     

Bases: [`BaseChatModel`](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")

Anthropic chat models.

See [Anthropic’s docs](https://docs.anthropic.com/en/docs/models-overview) for a list of the latest models.

Setup:     

Install `langchain-anthropic` and set environment variable `ANTHROPIC_API_KEY`.               pip install -U langchain-anthropic     export ANTHROPIC_API_KEY="your-api-key"     

Key init args — completion params:     

model: str     

Name of Anthropic model to use. e.g. `'claude-3-sonnet-20240229'`.

temperature: float     

Sampling temperature. Ranges from `0.0` to `1.0`.

max\_tokens: int     

Max number of tokens to generate.

Key init args — client params:     

timeout: Optional\[float\]     

Timeout for requests.

max\_retries: int     

Max number of retries if a request fails.

api\_key: Optional\[str\]     

Anthropic API key. If not passed in will be read from env var `ANTHROPIC_API_KEY`.

base\_url: Optional\[str\]     

Base URL for API requests. Only specify if using a proxy or service emulator.

See full list of supported init args and their descriptions in the params section.

Instantiate:                    from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(         model="claude-3-sonnet-20240229",         temperature=0,         max_tokens=1024,         timeout=None,         max_retries=2,         # api_key="...",         # base_url="...",         # other params...     )     

**NOTE** : Any param which is not explicitly supported will be passed directly to the `anthropic.Anthropic.messages.create(...)` API every time to the model is invoked. For example:               from langchain_anthropic import ChatAnthropic     import anthropic          ChatAnthropic(..., extra_headers={}).invoke(...)          # results in underlying API call of:          anthropic.Anthropic(..).messages.create(..., extra_headers={})          # which is also equivalent to:          ChatAnthropic(...).invoke(..., extra_headers={})     

Invoke:                    messages = [         ("system", "You are a helpful translator. Translate the user sentence to French."),         ("human", "I love programming."),     ]     llm.invoke(messages)                    AIMessage(content="J'aime la programmation.", response_metadata={'id': 'msg_01Trik66aiQ9Z1higrD5XFx3', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 25, 'output_tokens': 11}}, id='run-5886ac5f-3c2e-49f5-8a44-b1e92808c929-0', usage_metadata={'input_tokens': 25, 'output_tokens': 11, 'total_tokens': 36})     

Stream:                    for chunk in llm.stream(messages):         print(chunk.text(), end="")                    AIMessageChunk(content='J', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content="'", id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content='a', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content='ime', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content=' la', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content=' programm', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content='ation', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')     AIMessageChunk(content='.', id='run-272ff5f9-8485-402c-b90d-eac8babc5b25')                    stream = llm.stream(messages)     full = next(stream)     for chunk in stream:         full += chunk     full                    AIMessageChunk(content="J'aime la programmation.", id='run-b34faef0-882f-4869-a19c-ed2b856e6361')     

Async:                    await llm.ainvoke(messages)          # stream:     # async for chunk in (await llm.astream(messages))          # batch:     # await llm.abatch([messages])                    AIMessage(content="J'aime la programmation.", response_metadata={'id': 'msg_01Trik66aiQ9Z1higrD5XFx3', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 25, 'output_tokens': 11}}, id='run-5886ac5f-3c2e-49f5-8a44-b1e92808c929-0', usage_metadata={'input_tokens': 25, 'output_tokens': 11, 'total_tokens': 36})     

Tool calling:                    from pydantic import BaseModel, Field          class GetWeather(BaseModel):         '''Get the current weather in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          class GetPopulation(BaseModel):         '''Get the current population in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          llm_with_tools = llm.bind_tools([GetWeather, GetPopulation])     ai_msg = llm_with_tools.invoke("Which city is hotter today and which is bigger: LA or NY?")     ai_msg.tool_calls                    [{'name': 'GetWeather',         'args': {'location': 'Los Angeles, CA'},         'id': 'toolu_01KzpPEAgzura7hpBqwHbWdo'},      {'name': 'GetWeather',          'args': {'location': 'New York, NY'},          'id': 'toolu_01JtgbVGVJbiSwtZk3Uycezx'},      {'name': 'GetPopulation',         'args': {'location': 'Los Angeles, CA'},         'id': 'toolu_01429aygngesudV9nTbCKGuw'},      {'name': 'GetPopulation',         'args': {'location': 'New York, NY'},         'id': 'toolu_01JPktyd44tVMeBcPPnFSEJG'}]     

See `ChatAnthropic.bind_tools()` method for more.

Structured output:                    from typing import Optional          from pydantic import BaseModel, Field          class Joke(BaseModel):         '''Joke to tell user.'''              setup: str = Field(description="The setup of the joke")         punchline: str = Field(description="The punchline to the joke")         rating: Optional[int] = Field(description="How funny the joke is, from 1 to 10")          structured_llm = llm.with_structured_output(Joke)     structured_llm.invoke("Tell me a joke about cats")                    Joke(setup='Why was the cat sitting on the computer?', punchline='To keep an eye on the mouse!', rating=None)     

See `ChatAnthropic.with_structured_output()` for more.

Image input:     

See [multimodal guides](https://python.langchain.com/docs/how_to/multimodal_inputs/) for more detail.               import base64          import httpx     from langchain_anthropic import ChatAnthropic     from langchain_core.messages import HumanMessage          image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"     image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")          llm = ChatAnthropic(model="claude-3-5-sonnet-latest")     message = HumanMessage(         content=[             {                 "type": "text",                 "text": "Can you highlight the differences between these two images?",             },             {                 "type": "image",                 "source_type": "base64",                 "data": image_data,                 "mime_type": "image/jpeg",             },             {                 "type": "image",                 "source_type": "url",                 "url": image_url,             },         ],     )     ai_msg = llm.invoke([message])     ai_msg.content                    "After examining both images carefully, I can see that they are actually identical."     

Files API

You can also pass in files that are managed through Anthropic’s [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files):               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(         model="claude-sonnet-4-20250514",         betas=["files-api-2025-04-14"],     )     input_message = {         "role": "user",         "content": [             {                 "type": "text",                 "text": "Describe this document.",             },             {                 "type": "image",                 "source_type": "id",                 "id": "file_abc123...",             },         ],     }     llm.invoke([input_message])     

PDF input:     

See [multimodal guides](https://python.langchain.com/docs/how_to/multimodal_inputs/) for more detail.               from base64 import b64encode     from langchain_anthropic import ChatAnthropic     from langchain_core.messages import HumanMessage     import requests          url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"     data = b64encode(requests.get(url).content).decode()          llm = ChatAnthropic(model="claude-3-5-sonnet-latest")     ai_msg = llm.invoke(         [             HumanMessage(                 [                     "Summarize this document.",                     {                         "type": "file",                         "source_type": "base64",                         "mime_type": "application/pdf",                         "data": data,                     },                 ]             )         ]     )     ai_msg.content                    "This appears to be a simple document..."     

Files API

You can also pass in files that are managed through Anthropic’s [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files):               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(         model="claude-sonnet-4-20250514",         betas=["files-api-2025-04-14"],     )     input_message = {         "role": "user",         "content": [             {                 "type": "text",                 "text": "Describe this document.",             },             {                 "type": "file",                 "source_type": "id",                 "id": "file_abc123...",             },         ],     }     llm.invoke([input_message])     

Extended thinking:     

Claude 3.7 Sonnet supports an [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) feature, which will output the step-by-step reasoning process that led to its final answer.

To use it, specify the thinking parameter when initializing ChatAnthropic. It can also be passed in as a kwarg during invocation.

You will need to specify a token budget to use this feature. See usage example:               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(         model="claude-3-7-sonnet-latest",         max_tokens=5000,         thinking={"type": "enabled", "budget_tokens": 2000},     )          response = llm.invoke("What is the cube root of 50.653?")     response.content                    [{'signature': '...', 'thinking': "To find the cube root of 50.653...", 'type': 'thinking'}, {'text': 'The cube root of 50.653 is ...', 'type': 'text'}]     

Citations:     

Anthropic supports a [citations](https://docs.anthropic.com/en/docs/build-with-claude/citations) feature that lets Claude attach context to its answers based on source documents supplied by the user. When [document content blocks](https://docs.anthropic.com/en/docs/build-with-claude/citations#document-types) with `"citations": {"enabled": True}` are included in a query, Claude may generate citations in its response.               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(model="claude-3-5-haiku-latest")          messages = [         {             "role": "user",             "content": [                 {                     "type": "document",                     "source": {                         "type": "text",                         "media_type": "text/plain",                         "data": "The grass is green. The sky is blue.",                     },                     "title": "My Document",                     "context": "This is a trustworthy document.",                     "citations": {"enabled": True},                 },                 {"type": "text", "text": "What color is the grass and sky?"},             ],         }     ]     response = llm.invoke(messages)     response.content                    [{'text': 'Based on the document, ', 'type': 'text'},     {'text': 'the grass is green',     'type': 'text',     'citations': [{'type': 'char_location',         'cited_text': 'The grass is green. ',         'document_index': 0,         'document_title': 'My Document',         'start_char_index': 0,         'end_char_index': 20}]},     {'text': ', and ', 'type': 'text'},     {'text': 'the sky is blue',     'type': 'text',     'citations': [{'type': 'char_location',         'cited_text': 'The sky is blue.',         'document_index': 0,         'document_title': 'My Document',         'start_char_index': 20,         'end_char_index': 36}]},     {'text': '.', 'type': 'text'}]     

Token usage:                    ai_msg = llm.invoke(messages)     ai_msg.usage_metadata                    {'input_tokens': 25, 'output_tokens': 11, 'total_tokens': 36}     

Message chunks containing token usage will be included during streaming by default:               stream = llm.stream(messages)     full = next(stream)     for chunk in stream:         full += chunk     full.usage_metadata                    {'input_tokens': 25, 'output_tokens': 11, 'total_tokens': 36}     

These can be disabled by setting `stream_usage=False` in the stream method, or by setting `stream_usage=False` when initializing ChatAnthropic.

Prompt caching:     

See LangChain [docs](https://python.langchain.com/docs/integrations/chat/anthropic/#built-in-tools) for more detail.               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(model="claude-3-7-sonnet-20250219")          messages = [         {             "role": "system",             "content": [                 {                     "type": "text",                     "text": "Below is some long context:",                 },                 {                     "type": "text",                     "text": f"{long_text}",                     "cache_control": {"type": "ephemeral"},                 },             ],         },         {             "role": "user",             "content": "What's that about?",         },     ]          response = llm.invoke(messages)     response.usage_metadata["input_token_details"]                    {'cache_read': 0, 'cache_creation': 1458}     

Extended caching

Added in version 0.3.15.

The cache lifetime is 5 minutes by default. If this is too short, you can apply one hour caching by enabling the `"extended-cache-ttl-2025-04-11"` beta header:               llm = ChatAnthropic(         model="claude-3-7-sonnet-20250219",         betas=["extended-cache-ttl-2025-04-11"],     )     

and specifying `"cache_control": {"type": "ephemeral", "ttl": "1h"}`.

Details of cached token counts will be included on the `InputTokenDetails` of response’s `usage_metadata`:               response = llm.invoke(messages)     response.usage_metadata                    {         "input_tokens": 1500,         "output_tokens": 200,         "total_tokens": 1700,         "input_token_details": {             "cache_read": 0,             "cache_creation": 1000,             "ephemeral_1h_input_tokens": 750,             "ephemeral_5m_input_tokens": 250,         }     }     

See [Claude documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration-beta) for detail.

Token-efficient tool use \(beta\):     

See LangChain [docs](https://python.langchain.com/docs/integrations/chat/anthropic/) for more detail.               from langchain_anthropic import ChatAnthropic     from langchain_core.tools import tool          llm = ChatAnthropic(         model="claude-3-7-sonnet-20250219",         temperature=0,         model_kwargs={             "extra_headers": {                 "anthropic-beta": "token-efficient-tools-2025-02-19"             }         }     )          @tool     def get_weather(location: str) -> str:         """Get the weather at a location."""         return "It's sunny."          llm_with_tools = llm.bind_tools([get_weather])     response = llm_with_tools.invoke(         "What's the weather in San Francisco?"     )     print(response.tool_calls)     print(f'Total tokens: {response.usage_metadata["total_tokens"]}')                    [{'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'toolu_01HLjQMSb1nWmgevQUtEyz17', 'type': 'tool_call'}]          Total tokens: 408     

Built-in tools:     

See LangChain [docs](https://python.langchain.com/docs/integrations/chat/anthropic/) for more detail.

Web search               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(model="claude-3-5-sonnet-latest")          tool = {"type": "web_search_20250305", "name": "web_search", "max_uses": 3}     llm_with_tools = llm.bind_tools([tool])          response = llm_with_tools.invoke(         "How do I update a web app to TypeScript 5.5?"     )     

Code execution               llm = ChatAnthropic(         model="claude-sonnet-4-20250514",         betas=["code-execution-2025-05-22"],     )          tool = {"type": "code_execution_20250522", "name": "code_execution"}     llm_with_tools = llm.bind_tools([tool])          response = llm_with_tools.invoke(         "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"     )     

Remote MCP               from langchain_anthropic import ChatAnthropic          mcp_servers = [         {             "type": "url",             "url": "https://mcp.deepwiki.com/mcp",             "name": "deepwiki",             "tool_configuration": {  # optional configuration                 "enabled": True,                 "allowed_tools": ["ask_question"],             },             "authorization_token": "PLACEHOLDER",  # optional authorization         }     ]          llm = ChatAnthropic(         model="claude-sonnet-4-20250514",         betas=["mcp-client-2025-04-04"],         mcp_servers=mcp_servers,     )          response = llm.invoke(         "What transport protocols does the 2025-03-26 version of the MCP "         "spec (modelcontextprotocol/modelcontextprotocol) support?"     )     

Text editor               from langchain_anthropic import ChatAnthropic          llm = ChatAnthropic(model="claude-3-7-sonnet-20250219")          tool = {"type": "text_editor_20250124", "name": "str_replace_editor"}     llm_with_tools = llm.bind_tools([tool])          response = llm_with_tools.invoke(         "There's a syntax error in my primes.py file. Can you help me fix it?"     )     print(response.text())     response.tool_calls                    I'd be happy to help you fix the syntax error in your primes.py file. First, let's look at the current content of the file to identify the error.          [{'name': 'str_replace_editor',     'args': {'command': 'view', 'path': '/repo/primes.py'},     'id': 'toolu_01VdNgt1YV7kGfj9LFLm6HyQ',     'type': 'tool_call'}]     

Response metadata                    ai_msg = llm.invoke(messages)     ai_msg.response_metadata                    {'id': 'msg_013xU6FHEGEq76aP4RgFerVT',      'model': 'claude-3-sonnet-20240229',      'stop_reason': 'end_turn',      'stop_sequence': None,      'usage': {'input_tokens': 25, 'output_tokens': 11}}     

Note

ChatAnthropic implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

_param _anthropic\_api\_key _: SecretStr_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically read from env var `ANTHROPIC_API_KEY` if not provided.

_param _anthropic\_api\_url _: str | None_ _\[Optional\]__\(alias 'base\_url'\)_\#     

Base URL for API requests. Only specify if using a proxy or service emulator.

If a value isn’t passed in, will attempt to read the value first from `ANTHROPIC_API_URL` and if that is not set, `ANTHROPIC_BASE_URL`. If neither are set, the default value of `https://api.anthropic.com` will be used.

_param _betas _: list\[str\] | None_ _ = None_\#     

List of beta features to enable. If specified, invocations will be routed through client.beta.messages.create.

Example: `betas=["mcp-client-2025-04-04"]`

_param _cache _: [BaseCache](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") | bool | None_ _ = None_\#     

Whether to cache the response.

  * If true, will use the global cache.

  * If false, will not use a cache

  * If None, will use the global cache if it’s set, otherwise no cache.

  * If instance of BaseCache, will use the provided cache.

Caching is not currently supported for streaming methods of models.

_param _callback\_manager _: [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None_ _ = None_\#     

Deprecated since version 0.1.7: Use `callbacks()` instead. It will be removed in pydantic==1.0.

Callback manager to add to the run trace.

_param _callbacks _: Callbacks_ _ = None_\#     

Callbacks to add to the run trace.

_param _custom\_get\_token\_ids _: Callable\[\[str\], list\[int\]\] | None_ _ = None_\#     

Optional encoder to use for counting tokens.

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

Headers to pass to the Anthropic clients, will be used for every API call.

_param _default\_request\_timeout _: float | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to Anthropic Completion API.

_param _disable\_streaming _: bool | Literal\['tool\_calling'\]__ = False_\#     

Whether to disable streaming for this model.

If streaming is bypassed, then `stream()`/`astream()`/`astream_events()` will defer to `invoke()`/`ainvoke()`.

  * If True, will always bypass streaming case.

  * If `'tool_calling'`, will bypass streaming case only when the model is called with a `tools` keyword argument. In other words, LangChain will automatically switch to non-streaming behavior \(`invoke()`\) only when the tools argument is provided. This offers the best of both worlds.

  * If False \(default\), will always use streaming case if available.

The main reason for this flag is that code might be written using `.stream()` and a user may want to swap out a given model for another model whose the implementation does not properly support streaming.

_param _max\_retries _: int_ _ = 2_\#     

Number of retries allowed for requests sent to the Anthropic Completion API.

_param _max\_tokens _: int_ _ = 1024_ _\(alias 'max\_tokens\_to\_sample'\)_\#     

Denotes the number of tokens to predict per generation.

_param _mcp\_servers _: list\[dict\[str, Any\]\] | None_ _ = None_\#     

List of MCP servers to use for the request.

Example: `mcp_servers=[{"type": "url", "url": "https://mcp.example.com/mcp", "name": "example-mcp"}]`

_param _metadata _: dict\[str, Any\] | None_ _ = None_\#     

Metadata to add to the run trace.

_param _model _: str_ _\[Required\]__\(alias 'model\_name'\)_\#     

Model name to use.

_param _model\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

_param _rate\_limiter _: [BaseRateLimiter](https://python.langchain.com/api_reference/core/rate_limiters/langchain_core.rate_limiters.BaseRateLimiter.html#langchain_core.rate_limiters.BaseRateLimiter "langchain_core.rate_limiters.BaseRateLimiter") | None_ _ = None_\#     

An optional rate limiter to use for limiting the number of requests.

_param _stop\_sequences _: list\[str\] | None_ _ = None_ _\(alias 'stop'\)_\#     

Default stop sequences.

_param _stream\_usage _: bool_ _ = True_\#     

Whether to include usage metadata in streaming output. If `True`, additional message chunks will be generated during the stream including usage metadata.

_param _streaming _: bool_ _ = False_\#     

Whether to use streaming or not.

_param _tags _: list\[str\] | None_ _ = None_\#     

Tags to add to the run trace.

_param _temperature _: float | None_ _ = None_\#     

A non-negative float that tunes the degree of randomness in generation.

_param _thinking _: dict\[str, Any\] | None_ _ = None_\#     

Parameters for Claude reasoning, e.g., `{"type": "enabled", "budget_tokens": 10_000}`

_param _top\_k _: int | None_ _ = None_\#     

Number of most likely tokens to consider at each step.

_param _top\_p _: float | None_ _ = None_\#     

Total probability mass of tokens to consider at each step.

_param _verbose _: bool_ _\[Optional\]_\#     

Whether to print out response text.

\_\_call\_\_\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _stop : list\[str\] | None = None_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\#     

Deprecated since version 0.1.7: Use `invoke()` instead. It will not be removed until langchain-core==1.0.

Call the model.

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – List of messages.

  * **stop** \(_list_ _\[__str_ _\]__|__None_\) – Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation.

  * **\*\*kwargs** \(_Any_\) – Arbitrary additional keyword arguments. These are usually passed to the model provider API call.

Returns:     

The model output message.

Return type:     

[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

_async _abatch\(

    _inputs : list\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → list\[Output\]\#     

Default implementation runs ainvoke in parallel using asyncio.gather.

The default implementation of batch works well for IO bound runnables.

Subclasses should override this method if they can batch more efficiently; e.g., if the underlying Runnable uses an API which supports a batch mode.

Parameters:     

  * **inputs** \(_list_ _\[__Input_ _\]_\) – A list of inputs to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__list_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None.

  * **return\_exceptions** \(_bool_\) – Whether to return exceptions instead of raising them. Defaults to False.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Returns:     

A list of outputs from the Runnable.

Return type:     

list\[_Output_\]

_async _abatch\_as\_completed\(

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[tuple\[int, Output | Exception\]\]\#     

Run ainvoke in parallel on a list of inputs.

Yields results as they complete.

Parameters:     

  * **inputs** \(_Sequence_ _\[__Input_ _\]_\) – A list of inputs to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__Sequence_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None. Defaults to None.

  * **return\_exceptions** \(_bool_\) – Whether to return exceptions instead of raising them. Defaults to False.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Yields:     

A tuple of the index of the input and the output from the Runnable.

Return type:     

_AsyncIterator_\[tuple\[int, _Output_ | Exception\]\]

_async _ainvoke\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\#     

Default implementation of ainvoke, calls invoke from a thread.

The default implementation allows usage of async code even if the Runnable did not implement a native async version of invoke.

Subclasses should override this method if they can run asynchronously.

Parameters:     

  * **input** \(_LanguageModelInput_\)

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\)

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Return type:     

[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

_async _astream\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]\#     

Default implementation of astream, which calls ainvoke.

Subclasses should override this method if they support streaming output.

Parameters:     

  * **input** \(_LanguageModelInput_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

Yields:     

The output of the Runnable.

Return type:     

AsyncIterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]

_async _astream\_events\(

    _input : Any_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _version : Literal\['v1', 'v2'\] = 'v2'_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[StreamEvent\]\#     

Generate a stream of events.

Use to create an iterator over StreamEvents that provide real-time information about the progress of the Runnable, including StreamEvents from intermediate results.

A StreamEvent is a dictionary with the following schema:

  * `event`: **str** \- Event names are of the format: on\_\[runnable\_type\]\_\(start|stream|end\).

  * `name`: **str** \- The name of the Runnable that generated the event.

  * `run_id`: **str** \- randomly generated ID associated with the given execution of the Runnable that emitted the event. A child Runnable that gets invoked as part of the execution of a parent Runnable is assigned its own unique ID.

  * `parent_ids`: **list\[str\]** \- The IDs of the parent runnables that generated the event. The root Runnable will have an empty list. The order of the parent IDs is from the root to the immediate parent. Only available for v2 version of the API. The v1 version of the API will return an empty list.

  * `tags`: **Optional\[list\[str\]\]** \- The tags of the Runnable that generated the event.

  * `metadata`: **Optional\[dict\[str, Any\]\]** \- The metadata of the Runnable that generated the event.

  * `data`: **dict\[str, Any\]**

Below is a table that illustrates some events that might be emitted by various chains. Metadata fields have been omitted from the table for brevity. Chain definitions have been included after the table.

Note

This reference table is for the V2 version of the schema.

event | name | chunk | input | output   ---|---|---|---|---   on\_chat\_model\_start | \[model name\] |  | \{“messages”: \[\[SystemMessage, HumanMessage\]\]\} |    on\_chat\_model\_stream | \[model name\] | AIMessageChunk\(content=”hello”\) |  |    on\_chat\_model\_end | \[model name\] |  | \{“messages”: \[\[SystemMessage, HumanMessage\]\]\} | AIMessageChunk\(content=”hello world”\)   on\_llm\_start | \[model name\] |  | \{‘input’: ‘hello’\} |    on\_llm\_stream | \[model name\] | ‘Hello’ |  |    on\_llm\_end | \[model name\] |  | ‘Hello human\!’ |    on\_chain\_start | format\_docs |  |  |    on\_chain\_stream | format\_docs | “hello world\!, goodbye world\!” |  |    on\_chain\_end | format\_docs |  | \[Document\(…\)\] | “hello world\!, goodbye world\!”   on\_tool\_start | some\_tool |  | \{“x”: 1, “y”: “2”\} |    on\_tool\_end | some\_tool |  |  | \{“x”: 1, “y”: “2”\}   on\_retriever\_start | \[retriever name\] |  | \{“query”: “hello”\} |    on\_retriever\_end | \[retriever name\] |  | \{“query”: “hello”\} | \[Document\(…\), ..\]   on\_prompt\_start | \[template\_name\] |  | \{“question”: “hello”\} |    on\_prompt\_end | \[template\_name\] |  | \{“question”: “hello”\} | ChatPromptValue\(messages: \[SystemMessage, …\]\)      In addition to the standard events, users can also dispatch custom events \(see example below\).

Custom events will be only be surfaced with in the v2 version of the API\!

A custom event has following format:

Attribute | Type | Description   ---|---|---   name | str | A user defined name for the event.   data | Any | The data associated with the event. This can be anything, though we suggest making it JSON serializable.      Here are declarations associated with the standard events shown above:

format\_docs:               def format_docs(docs: list[Document]) -> str:         '''Format the docs.'''         return ", ".join([doc.page_content for doc in docs])          format_docs = RunnableLambda(format_docs)     

some\_tool:               @tool     def some_tool(x: int, y: str) -> dict:         '''Some_tool.'''         return {"x": x, "y": y}     

prompt:               template = ChatPromptTemplate.from_messages(         [("system", "You are Cat Agent 007"), ("human", "{question}")]     ).with_config({"run_name": "my_template", "tags": ["my_template"]})     

Example:               from langchain_core.runnables import RunnableLambda          async def reverse(s: str) -> str:         return s[::-1]          chain = RunnableLambda(func=reverse)          events = [         event async for event in chain.astream_events("hello", version="v2")     ]          # will produce the following events (run_id, and parent_ids     # has been omitted for brevity):     [         {             "data": {"input": "hello"},             "event": "on_chain_start",             "metadata": {},             "name": "reverse",             "tags": [],         },         {             "data": {"chunk": "olleh"},             "event": "on_chain_stream",             "metadata": {},             "name": "reverse",             "tags": [],         },         {             "data": {"output": "olleh"},             "event": "on_chain_end",             "metadata": {},             "name": "reverse",             "tags": [],         },     ]     

Example: Dispatch Custom Event               from langchain_core.callbacks.manager import (         adispatch_custom_event,     )     from langchain_core.runnables import RunnableLambda, RunnableConfig     import asyncio               async def slow_thing(some_input: str, config: RunnableConfig) -> str:         """Do something that takes a long time."""         await asyncio.sleep(1) # Placeholder for some slow operation         await adispatch_custom_event(             "progress_event",             {"message": "Finished step 1 of 3"},             config=config # Must be included for python < 3.10         )         await asyncio.sleep(1) # Placeholder for some slow operation         await adispatch_custom_event(             "progress_event",             {"message": "Finished step 2 of 3"},             config=config # Must be included for python < 3.10         )         await asyncio.sleep(1) # Placeholder for some slow operation         return "Done"          slow_thing = RunnableLambda(slow_thing)          async for event in slow_thing.astream_events("some_input", version="v2"):         print(event)     

Parameters:     

  * **input** \(_Any_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to use for the Runnable.

  * **version** \(_Literal_ _\[__'v1'__,__'v2'__\]_\) – The version of the schema to use either v2 or v1. Users should use v2. v1 is for backwards compatibility and will be deprecated in 0.4.0. No default will be assigned until the API is stabilized. custom events will only be surfaced in v2.

  * **include\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include events from runnables with matching names.

  * **include\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include events from runnables with matching types.

  * **include\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include events from runnables with matching tags.

  * **exclude\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude events from runnables with matching names.

  * **exclude\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude events from runnables with matching types.

  * **exclude\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude events from runnables with matching tags.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable. These will be passed to astream\_log as this implementation of astream\_events is built on top of astream\_log.

Yields:     

An async stream of StreamEvents.

Raises:     

**NotImplementedError** – If the version is not v1 or v2.

Return type:     

AsyncIterator\[StreamEvent\]

batch\(

    _inputs : list\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → list\[Output\]\#     

Default implementation runs invoke in parallel using a thread pool executor.

The default implementation of batch works well for IO bound runnables.

Subclasses should override this method if they can batch more efficiently; e.g., if the underlying Runnable uses an API which supports a batch mode.

Parameters:     

  * **inputs** \(_list_ _\[__Input_ _\]_\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__list_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\)

  * **return\_exceptions** \(_bool_\)

  * **kwargs** \(_Any_ _|__None_\)

Return type:     

list\[_Output_\]

batch\_as\_completed\(

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → Iterator\[tuple\[int, Output | Exception\]\]\#     

Run invoke in parallel on a list of inputs.

Yields results as they complete.

Parameters:     

  * **inputs** \(_Sequence_ _\[__Input_ _\]_\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__Sequence_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\)

  * **return\_exceptions** \(_bool_\)

  * **kwargs** \(_Any_ _|__None_\)

Return type:     

_Iterator_\[tuple\[int, _Output_ | Exception\]\]

bind\(

    _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind arguments to a Runnable, returning a new Runnable.

Useful when a Runnable in a chain requires an argument that is not in the output of the previous Runnable or included in the user input.

Parameters:     

**kwargs** \(_Any_\) – The arguments to bind to the Runnable.

Returns:     

A new Runnable with the arguments bound.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

Example:               from langchain_ollama import ChatOllama     from langchain_core.output_parsers import StrOutputParser          llm = ChatOllama(model='llama2')          # Without bind.     chain = (         llm         | StrOutputParser()     )          chain.invoke("Repeat quoted words exactly: 'One two three four five.'")     # Output is 'One two three four five.'          # With bind.     chain = (         llm.bind(stop=["three"])         | StrOutputParser()     )          chain.invoke("Repeat quoted words exactly: 'One two three four five.'")     # Output is 'One two'     

bind\_tools\(

    _tools : Sequence\[dict\[str, Any\] | type | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _\*_ ,     _tool\_choice : dict\[str, str\] | Literal\['any', 'auto'\] | str | None = None_,     _parallel\_tool\_calls : bool | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_anthropic/chat_models.html#ChatAnthropic.bind_tools)\#     

Bind tool-like objects to this chat model.

Parameters:     

  * **tools** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of tool definitions to bind to this chat model. Supports Anthropic format tool schemas and any tool definition handled by [`convert_to_openai_tool()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html#langchain_core.utils.function_calling.convert_to_openai_tool "langchain_core.utils.function_calling.convert_to_openai_tool").

  * **tool\_choice** \(_dict_ _\[__str_ _,__str_ _\]__|__Literal_ _\[__'any'__,__'auto'__\]__|__str_ _|__None_\) – 

Which tool to require the model to call. Options are:

    * name of the tool as a string or as dict `{"type": "tool", "name": "<<tool_name>>"}`: calls corresponding tool;

    * `"auto"`, `{"type: "auto"}`, or `None`: automatically selects a tool \(including no tool\);

    * `"any"` or `{"type: "any"}`: force at least one tool to be called;

  * **parallel\_tool\_calls** \(_bool_ _|__None_\) – 

Set to `False` to disable parallel tool use. Defaults to `None` \(no specification, which allows parallel tool use\).

Added in version 0.3.2.

  * **kwargs** \(_Any_\) – Any additional parameters are passed directly to `bind()`.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Example               from langchain_anthropic import ChatAnthropic     from pydantic import BaseModel, Field          class GetWeather(BaseModel):         '''Get the current weather in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          class GetPrice(BaseModel):         '''Get the price of a specific product.'''              product: str = Field(..., description="The product to look up.")               llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)     llm_with_tools = llm.bind_tools([GetWeather, GetPrice])     llm_with_tools.invoke("what is the weather like in San Francisco",)     # -> AIMessage(     #     content=[     #         {'text': '<thinking>\nBased on the user\'s question, the relevant function to call is GetWeather, which requires the "location" parameter.\n\nThe user has directly specified the location as "San Francisco". Since San Francisco is a well known city, I can reasonably infer they mean San Francisco, CA without needing the state specified.\n\nAll the required parameters are provided, so I can proceed with the API call.\n</thinking>', 'type': 'text'},     #         {'text': None, 'type': 'tool_use', 'id': 'toolu_01SCgExKzQ7eqSkMHfygvYuu', 'name': 'GetWeather', 'input': {'location': 'San Francisco, CA'}}     #     ],     #     response_metadata={'id': 'msg_01GM3zQtoFv8jGQMW7abLnhi', 'model': 'claude-3-5-sonnet-20240620', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 487, 'output_tokens': 145}},     #     id='run-87b1331e-9251-4a68-acef-f0a018b639cc-0'     # )     

Example — force tool call with tool\_choice `'any'`:

>  >     from langchain_anthropic import ChatAnthropic >     from pydantic import BaseModel, Field >      >     class GetWeather(BaseModel): >         '''Get the current weather in a given location''' >      >         location: str = Field(..., description="The city and state, e.g. San Francisco, CA") >      >     class GetPrice(BaseModel): >         '''Get the price of a specific product.''' >      >         product: str = Field(..., description="The product to look up.") >      >      >     llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0) >     llm_with_tools = llm.bind_tools([GetWeather, GetPrice], tool_choice="any") >     llm_with_tools.invoke("what is the weather like in San Francisco",) >     

Example — force specific tool call with tool\_choice `'<name_of_tool>'`:

>  >     from langchain_anthropic import ChatAnthropic >     from pydantic import BaseModel, Field >      >     class GetWeather(BaseModel): >         '''Get the current weather in a given location''' >      >         location: str = Field(..., description="The city and state, e.g. San Francisco, CA") >      >     class GetPrice(BaseModel): >         '''Get the price of a specific product.''' >      >         product: str = Field(..., description="The product to look up.") >      >      >     llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0) >     llm_with_tools = llm.bind_tools([GetWeather, GetPrice], tool_choice="GetWeather") >     llm_with_tools.invoke("what is the weather like in San Francisco",) >     

Example — cache specific tools:

>  >     from langchain_anthropic import ChatAnthropic, convert_to_anthropic_tool >     from pydantic import BaseModel, Field >      >     class GetWeather(BaseModel): >         '''Get the current weather in a given location''' >      >         location: str = Field(..., description="The city and state, e.g. San Francisco, CA") >      >     class GetPrice(BaseModel): >         '''Get the price of a specific product.''' >      >         product: str = Field(..., description="The product to look up.") >      >     # We'll convert our pydantic class to the anthropic tool format >     # before passing to bind_tools so that we can set the 'cache_control' >     # field on our tool. >     cached_price_tool = convert_to_anthropic_tool(GetPrice) >     # Currently the only supported "cache_control" value is >     # {"type": "ephemeral"}. >     cached_price_tool["cache_control"] = {"type": "ephemeral"} >      >     # We need to pass in extra headers to enable use of the beta cache >     # control API. >     llm = ChatAnthropic( >         model="claude-3-5-sonnet-20240620", >         temperature=0, >     ) >     llm_with_tools = llm.bind_tools([GetWeather, cached_price_tool]) >     llm_with_tools.invoke("what is the weather like in San Francisco",) >      >  > This outputs: >      >      >     AIMessage(content=[{'text': "Certainly! I can help you find out the current weather in San Francisco. To get this information, I'll use the GetWeather function. Let me fetch that data for you right away.", 'type': 'text'}, {'id': 'toolu_01TS5h8LNo7p5imcG7yRiaUM', 'input': {'location': 'San Francisco, CA'}, 'name': 'GetWeather', 'type': 'tool_use'}], response_metadata={'id': 'msg_01Xg7Wr5inFWgBxE5jH9rpRo', 'model': 'claude-3-5-sonnet-20240620', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 171, 'output_tokens': 96, 'cache_creation_input_tokens': 1470, 'cache_read_input_tokens': 0}}, id='run-b36a5b54-5d69-470e-a1b0-b932d00b089e-0', tool_calls=[{'name': 'GetWeather', 'args': {'location': 'San Francisco, CA'}, 'id': 'toolu_01TS5h8LNo7p5imcG7yRiaUM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 171, 'output_tokens': 96, 'total_tokens': 267}) >      >  > If we invoke the tool again, we can see that the “usage” information in the AIMessage.response\_metadata shows that we had a cache hit: >      >      >     AIMessage(content=[{'text': 'To get the current weather in San Francisco, I can use the GetWeather function. Let me check that for you.', 'type': 'text'}, {'id': 'toolu_01HtVtY1qhMFdPprx42qU2eA', 'input': {'location': 'San Francisco, CA'}, 'name': 'GetWeather', 'type': 'tool_use'}], response_metadata={'id': 'msg_016RfWHrRvW6DAGCdwB6Ac64', 'model': 'claude-3-5-sonnet-20240620', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 171, 'output_tokens': 82, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 1470}}, id='run-88b1f825-dcb7-4277-ac27-53df55d22001-0', tool_calls=[{'name': 'GetWeather', 'args': {'location': 'San Francisco, CA'}, 'id': 'toolu_01HtVtY1qhMFdPprx42qU2eA', 'type': 'tool_call'}], usage_metadata={'input_tokens': 171, 'output_tokens': 82, 'total_tokens': 253}) >     

configurable\_alternatives\(

    _which : [ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")_,     _\*_ ,     _default\_key : str = 'default'_,     _prefix\_keys : bool = False_,     _\*\* kwargs: [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[\], [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\]_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\#     

Configure alternatives for Runnables that can be set at runtime.

Parameters:     

  * **which** \([_ConfigurableField_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")\) – The ConfigurableField instance that will be used to select the alternative.

  * **default\_key** \(_str_\) – The default key to use if no alternative is selected. Defaults to “default”.

  * **prefix\_keys** \(_bool_\) – Whether to prefix the keys with the ConfigurableField id. Defaults to False.

  * **\*\*kwargs** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__\]__,_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]_\) – A dictionary of keys to Runnable instances or callables that return Runnable instances.

Returns:     

A new Runnable with the alternatives configured.

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")               from langchain_anthropic import ChatAnthropic     from langchain_core.runnables.utils import ConfigurableField     from langchain_openai import ChatOpenAI          model = ChatAnthropic(         model_name="claude-3-sonnet-20240229"     ).configurable_alternatives(         ConfigurableField(id="llm"),         default_key="anthropic",         openai=ChatOpenAI()     )          # uses the default model ChatAnthropic     print(model.invoke("which organization created you?").content)          # uses ChatOpenAI     print(         model.with_config(             configurable={"llm": "openai"}         ).invoke("which organization created you?").content     )     

configurable\_fields\(

    _\*\* kwargs: [ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField") | [ConfigurableFieldSingleOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") | [ConfigurableFieldMultiOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\#     

Configure particular Runnable fields at runtime.

Parameters:     

**\*\*kwargs** \([_ConfigurableField_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField") _|_[_ConfigurableFieldSingleOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") _|_[_ConfigurableFieldMultiOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")\) – A dictionary of ConfigurableField instances to configure.

Returns:     

A new Runnable with the fields configured.

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")               from langchain_core.runnables import ConfigurableField     from langchain_openai import ChatOpenAI          model = ChatOpenAI(max_tokens=20).configurable_fields(         max_tokens=ConfigurableField(             id="output_token_number",             name="Max tokens in the output",             description="The maximum number of tokens in the output",         )     )          # max_tokens = 20     print(         "max_tokens_20: ",         model.invoke("tell me something about chess").content     )          # max_tokens = 200     print("max_tokens_200: ", model.with_config(         configurable={"output_token_number": 200}         ).invoke("tell me something about chess").content     )     

get\_num\_tokens\(_text : str_\) → int\#     

Get the number of tokens present in the text.

Useful for checking if an input fits in a model’s context window.

Parameters:     

**text** \(_str_\) – The string input to tokenize.

Returns:     

The integer number of tokens in the text.

Return type:     

int

get\_num\_tokens\_from\_messages\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _tools : Sequence\[dict\[str, Any\] | type | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\] | None = None_,     _\*\* kwargs: Any_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_anthropic/chat_models.html#ChatAnthropic.get_num_tokens_from_messages)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Count tokens in a sequence of input messages.

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – The message inputs to tokenize.

  * **tools** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]__|__None_\) – If provided, sequence of dict, BaseModel, function, or BaseTools to be converted to tool schemas.

  * **kwargs** \(_Any_\) – Additional keyword arguments are passed to the `bind()` method.

Return type:     

int

Basic usage:

>  >     from langchain_anthropic import ChatAnthropic >     from langchain_core.messages import HumanMessage, SystemMessage >      >     llm = ChatAnthropic(model="claude-3-5-sonnet-20241022") >      >     messages = [ >         SystemMessage(content="You are a scientist"), >         HumanMessage(content="Hello, Claude"), >     ] >     llm.get_num_tokens_from_messages(messages) >      >      >      >     14 >     

Pass tool schemas:

>  >     from langchain_anthropic import ChatAnthropic >     from langchain_core.messages import HumanMessage >     from langchain_core.tools import tool >      >     llm = ChatAnthropic(model="claude-3-5-sonnet-20241022") >      >     @tool(parse_docstring=True) >     def get_weather(location: str) -> str: >         """Get the current weather in a given location >      >         Args: >             location: The city and state, e.g. San Francisco, CA >         """ >         return "Sunny" >      >     messages = [ >         HumanMessage(content="What's the weather like in San Francisco?"), >     ] >     llm.get_num_tokens_from_messages(messages, tools=[get_weather]) >      >      >      >     403 >     

Changed in version 0.3.0: Uses Anthropic’s [token counting API](https://docs.anthropic.com/en/docs/build-with-claude/token-counting) to count tokens in messages.

get\_token\_ids\(_text : str_\) → list\[int\]\#     

Return the ordered ids of the tokens in a text.

Parameters:     

**text** \(_str_\) – The string input to tokenize.

Returns:     

A list of ids corresponding to the tokens in the text, in order they occur     

in the text.

Return type:     

list\[int\]

invoke\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\#     

Transform a single input into an output.

Parameters:     

  * **input** \(_LanguageModelInput_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details.

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Returns:     

The output of the Runnable.

Return type:     

[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

stream\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → Iterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]\#     

Default implementation of stream, which calls invoke.

Subclasses should override this method if they support streaming output.

Parameters:     

  * **input** \(_LanguageModelInput_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

Yields:     

The output of the Runnable.

Return type:     

Iterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]

with\_alisteners\(

    _\*_ ,     _on\_start : AsyncListener | None = None_,     _on\_end : AsyncListener | None = None_,     _on\_error : AsyncListener | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind async lifecycle listeners to a Runnable, returning a new Runnable.

on\_start: Asynchronously called before the Runnable starts running. on\_end: Asynchronously called after the Runnable finishes running. on\_error: Asynchronously called if the Runnable throws an error.

The Run object contains information about the run, including its id, type, input, output, error, start\_time, end\_time, and any tags or metadata added to the run.

Parameters:     

  * **on\_start** \(_Optional_ _\[__AsyncListener_ _\]_\) – Asynchronously called before the Runnable starts running. Defaults to None.

  * **on\_end** \(_Optional_ _\[__AsyncListener_ _\]_\) – Asynchronously called after the Runnable finishes running. Defaults to None.

  * **on\_error** \(_Optional_ _\[__AsyncListener_ _\]_\) – Asynchronously called if the Runnable throws an error. Defaults to None.

Returns:     

A new Runnable with the listeners bound.

Return type:     

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda, Runnable     from datetime import datetime, timezone     import time     import asyncio          def format_t(timestamp: float) -> str:         return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()          async def test_runnable(time_to_sleep : int):         print(f"Runnable[{time_to_sleep}s]: starts at {format_t(time.time())}")         await asyncio.sleep(time_to_sleep)         print(f"Runnable[{time_to_sleep}s]: ends at {format_t(time.time())}")          async def fn_start(run_obj : Runnable):         print(f"on start callback starts at {format_t(time.time())}")         await asyncio.sleep(3)         print(f"on start callback ends at {format_t(time.time())}")          async def fn_end(run_obj : Runnable):         print(f"on end callback starts at {format_t(time.time())}")         await asyncio.sleep(2)         print(f"on end callback ends at {format_t(time.time())}")          runnable = RunnableLambda(test_runnable).with_alisteners(         on_start=fn_start,         on_end=fn_end     )     async def concurrent_runs():         await asyncio.gather(runnable.ainvoke(2), runnable.ainvoke(3))          asyncio.run(concurrent_runs())     Result:     on start callback starts at 2025-03-01T07:05:22.875378+00:00     on start callback starts at 2025-03-01T07:05:22.875495+00:00     on start callback ends at 2025-03-01T07:05:25.878862+00:00     on start callback ends at 2025-03-01T07:05:25.878947+00:00     Runnable[2s]: starts at 2025-03-01T07:05:25.879392+00:00     Runnable[3s]: starts at 2025-03-01T07:05:25.879804+00:00     Runnable[2s]: ends at 2025-03-01T07:05:27.881998+00:00     on end callback starts at 2025-03-01T07:05:27.882360+00:00     Runnable[3s]: ends at 2025-03-01T07:05:28.881737+00:00     on end callback starts at 2025-03-01T07:05:28.882428+00:00     on end callback ends at 2025-03-01T07:05:29.883893+00:00     on end callback ends at 2025-03-01T07:05:30.884831+00:00     

with\_config\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind config to a Runnable, returning a new Runnable.

Parameters:     

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to bind to the Runnable.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

Returns:     

A new Runnable with the config bound.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

with\_fallbacks\(_fallbacks: Sequence\[Runnable\[Input, Output\]\], \*, exceptions\_to\_handle: tuple\[type\[BaseException\], ...\] = \(<class 'Exception'>,\), exception\_key: Optional\[str\] = None_\) → RunnableWithFallbacksT\[Input, Output\]\#     

Add fallbacks to a Runnable, returning a new Runnable.

The new Runnable will try the original Runnable, and then each fallback in order, upon failures.

Parameters:     

  * **fallbacks** \(_Sequence_ _\[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]_\) – A sequence of runnables to try if the original Runnable fails.

  * **exceptions\_to\_handle** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to handle. Defaults to \(Exception,\).

  * **exception\_key** \(_Optional_ _\[__str_ _\]_\) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input. Defaults to None.

Returns:     

A new Runnable that will try the original Runnable, and then each fallback in order, upon failures.

Return type:     

RunnableWithFallbacksT\[Input, Output\]

Example               from typing import Iterator          from langchain_core.runnables import RunnableGenerator               def _generate_immediate_error(input: Iterator) -> Iterator[str]:         raise ValueError()         yield ""               def _generate(input: Iterator) -> Iterator[str]:         yield from "foo bar"               runnable = RunnableGenerator(_generate_immediate_error).with_fallbacks(         [RunnableGenerator(_generate)]         )     print(''.join(runnable.stream({}))) #foo bar     

Parameters:     

  * **fallbacks** \(_Sequence_ _\[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]_\) – A sequence of runnables to try if the original Runnable fails.

  * **exceptions\_to\_handle** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to handle.

  * **exception\_key** \(_Optional_ _\[__str_ _\]_\) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input.

Returns:     

A new Runnable that will try the original Runnable, and then each fallback in order, upon failures.

Return type:     

RunnableWithFallbacksT\[Input, Output\]

with\_listeners\(

    _\*_ ,     _on\_start : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_,     _on\_end : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_,     _on\_error : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind lifecycle listeners to a Runnable, returning a new Runnable.

on\_start: Called before the Runnable starts running, with the Run object. on\_end: Called after the Runnable finishes running, with the Run object. on\_error: Called if the Runnable throws an error, with the Run object.

The Run object contains information about the run, including its id, type, input, output, error, start\_time, end\_time, and any tags or metadata added to the run.

Parameters:     

  * **on\_start** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Run_ _\]__,__None_ _\]__,__Callable_ _\[__\[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__None_ _\]__\]__\]_\) – Called before the Runnable starts running. Defaults to None.

  * **on\_end** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Run_ _\]__,__None_ _\]__,__Callable_ _\[__\[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__None_ _\]__\]__\]_\) – Called after the Runnable finishes running. Defaults to None.

  * **on\_error** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Run_ _\]__,__None_ _\]__,__Callable_ _\[__\[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__None_ _\]__\]__\]_\) – Called if the Runnable throws an error. Defaults to None.

Returns:     

A new Runnable with the listeners bound.

Return type:     

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda     from langchain_core.tracers.schemas import Run          import time          def test_runnable(time_to_sleep : int):         time.sleep(time_to_sleep)          def fn_start(run_obj: Run):         print("start_time:", run_obj.start_time)          def fn_end(run_obj: Run):         print("end_time:", run_obj.end_time)          chain = RunnableLambda(test_runnable).with_listeners(         on_start=fn_start,         on_end=fn_end     )     chain.invoke(2)     

with\_retry\(_\*, retry\_if\_exception\_type: tuple\[type\[BaseException\], ...\] = \(<class 'Exception'>,\), wait\_exponential\_jitter: bool = True, exponential\_jitter\_params: Optional\[ExponentialJitterParams\] = None, stop\_after\_attempt: int = 3_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Create a new Runnable that retries the original Runnable on exceptions.

Parameters:     

  * **retry\_if\_exception\_type** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to retry on. Defaults to \(Exception,\).

  * **wait\_exponential\_jitter** \(_bool_\) – Whether to add jitter to the wait time between retries. Defaults to True.

  * **stop\_after\_attempt** \(_int_\) – The maximum number of attempts to make before giving up. Defaults to 3.

  * **exponential\_jitter\_params** \(_Optional_ _\[_[_ExponentialJitterParams_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.ExponentialJitterParams.html#langchain_core.runnables.retry.ExponentialJitterParams "langchain_core.runnables.retry.ExponentialJitterParams") _\]_\) – Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` \(all float values\).

Returns:     

A new Runnable that retries the original Runnable on exceptions.

Return type:     

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda          count = 0               def _lambda(x: int) -> None:         global count         count = count + 1         if x == 1:             raise ValueError("x is 1")         else:              pass               runnable = RunnableLambda(_lambda)     try:         runnable.with_retry(             stop_after_attempt=2,             retry_if_exception_type=(ValueError,),         ).invoke(1)     except ValueError:         pass          assert (count == 2)     

with\_structured\_output\(

    _schema : dict | type_,     _\*_ ,     _include\_raw : bool = False_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], dict | BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_anthropic/chat_models.html#ChatAnthropic.with_structured_output)\#     

Model wrapper that returns outputs formatted to match the given schema.

Parameters:     

  * **schema** \(_dict_ _|__type_\) – 

The output schema. Can be passed in as:

    * an Anthropic tool schema,

    * an OpenAI function/tool schema,

    * a JSON Schema,

    * a TypedDict class,

    * or a Pydantic class.

If `schema` is a Pydantic class then the model output will be a Pydantic instance of that class, and the model-generated fields will be validated by the Pydantic class. Otherwise the model output will be a dict and will not be validated. See [`convert_to_openai_tool()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html#langchain_core.utils.function_calling.convert_to_openai_tool "langchain_core.utils.function_calling.convert_to_openai_tool") for more on how to properly specify types and descriptions of schema fields when specifying a Pydantic or TypedDict class.

  * **include\_raw** \(_bool_\) – If `False` then only the parsed structured output is returned. If an error occurs during model output parsing it will be raised. If `True` then both the raw model response \(a BaseMessage\) and the parsed model response will be returned. If an error occurs during output parsing it will be caught and returned as well. The final output is always a dict with keys `raw`, `parsed`, and `parsing_error`.

  * **kwargs** \(_Any_\) – Additional keyword arguments are ignored.

Returns:     

A Runnable that takes same inputs as a `BaseChatModel`.

If `include_raw` is `False` and `schema` is a Pydantic class, Runnable outputs an instance of `schema` \(i.e., a Pydantic object\).

Otherwise, if `include_raw` is `False` then Runnable outputs a dict.

If `include_raw` is True, then Runnable outputs a dict with keys:     

  * `raw`: BaseMessage

  * `parsed`: None if there was a parsing error, otherwise the type depends on the `schema` as described above.

  * `parsing_error`: Optional\[BaseException\]

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], dict | _BaseModel_\]

Example: Pydantic schema \(include\_raw=False\):

>  >     from langchain_anthropic import ChatAnthropic >     from pydantic import BaseModel >      >     class AnswerWithJustification(BaseModel): >         '''An answer to the user question along with justification for the answer.''' >         answer: str >         justification: str >      >     llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0) >     structured_llm = llm.with_structured_output(AnswerWithJustification) >      >     structured_llm.invoke("What weighs more a pound of bricks or a pound of feathers") >      >     # -> AnswerWithJustification( >     #     answer='They weigh the same', >     #     justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.' >     # ) >     

Example: Pydantic schema \(include\_raw=True\):

>  >     from langchain_anthropic import ChatAnthropic >     from pydantic import BaseModel >      >     class AnswerWithJustification(BaseModel): >         '''An answer to the user question along with justification for the answer.''' >         answer: str >         justification: str >      >     llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0) >     structured_llm = llm.with_structured_output(AnswerWithJustification, include_raw=True) >      >     structured_llm.invoke("What weighs more a pound of bricks or a pound of feathers") >     # -> { >     #     'raw': AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_Ao02pnFYXD6GN1yzc0uXPsvF', 'function': {'arguments': '{"answer":"They weigh the same.","justification":"Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ."}', 'name': 'AnswerWithJustification'}, 'type': 'function'}]}), >     #     'parsed': AnswerWithJustification(answer='They weigh the same.', justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'), >     #     'parsing_error': None >     # } >     

Example: Dict schema \(include\_raw=False\):

>  >     from langchain_anthropic import ChatAnthropic >      >     schema = { >         "name": "AnswerWithJustification", >         "description": "An answer to the user question along with justification for the answer.", >         "input_schema": { >             "type": "object", >             "properties": { >                 "answer": {"type": "string"}, >                 "justification": {"type": "string"}, >             }, >             "required": ["answer", "justification"] >         } >     } >     llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0) >     structured_llm = llm.with_structured_output(schema) >      >     structured_llm.invoke("What weighs more a pound of bricks or a pound of feathers") >     # -> { >     #     'answer': 'They weigh the same', >     #     'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.' >     # } >     

Changed in version 0.1.22: Added support for TypedDict class as schema.

with\_types\(

    _\*_ ,     _input\_type : type\[Input\] | None = None_,     _output\_type : type\[Output\] | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind input and output types to a Runnable, returning a new Runnable.

Parameters:     

  * **input\_type** \(_type_ _\[__Input_ _\]__|__None_\) – The input type to bind to the Runnable. Defaults to None.

  * **output\_type** \(_type_ _\[__Output_ _\]__|__None_\) – The output type to bind to the Runnable. Defaults to None.

Returns:     

A new Runnable with the types bound.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

Examples using ChatAnthropic

  * [Anthropic](https://python.langchain.com/docs/integrations/providers/anthropic/)

  * [Build an Agent](https://python.langchain.com/docs/tutorials/agents/)

  * [ChatAnthropic](https://python.langchain.com/docs/integrations/chat/anthropic/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [How to add fallbacks to a runnable](https://python.langchain.com/docs/how_to/fallbacks/)

  * [How to attach callbacks to a runnable](https://python.langchain.com/docs/how_to/callbacks_attach/)

  * [How to configure runtime chain internals](https://python.langchain.com/docs/how_to/configure/)

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

  * [How to create a dynamic \(self-constructing\) chain](https://python.langchain.com/docs/how_to/dynamic_chain/)

  * [How to create custom callback handlers](https://python.langchain.com/docs/how_to/custom_callbacks/)

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)

  * [How to handle rate limits](https://python.langchain.com/docs/how_to/chat_model_rate_limiting/)

  * [How to merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)

  * [How to parse XML output](https://python.langchain.com/docs/how_to/output_parser_xml/)

  * [How to pass callbacks in at runtime](https://python.langchain.com/docs/how_to/callbacks_runtime/)

  * [How to propagate callbacks constructor](https://python.langchain.com/docs/how_to/callbacks_constructor/)

  * [How to route between sub-chains](https://python.langchain.com/docs/how_to/routing/)

  * [How to stream chat model responses](https://python.langchain.com/docs/how_to/chat_streaming/)

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

  * [How to use callbacks in async environments](https://python.langchain.com/docs/how_to/callbacks_async/)

  * [How to use prompting alone \(no tool calling\) to do extraction](https://python.langchain.com/docs/how_to/extraction_parse/)

  * [Log10](https://python.langchain.com/docs/integrations/providers/log10/)

  * [PlayWright Browser Toolkit](https://python.langchain.com/docs/integrations/tools/playwright/)

  * [Response metadata](https://python.langchain.com/docs/how_to/response_metadata/)

  * [Riza Code Interpreter](https://python.langchain.com/docs/integrations/tools/riza/)

  * [🦜️🏓 LangServe](https://python.langchain.com/docs/langserve/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)