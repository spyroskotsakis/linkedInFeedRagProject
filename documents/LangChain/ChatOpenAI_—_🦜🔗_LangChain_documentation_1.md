# ChatOpenAI — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html
**Word Count:** 5362
**Links Count:** 543
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# ChatOpenAI\#

_class _langchain\_openai.chat\_models.base.ChatOpenAI[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#ChatOpenAI)\#     

Bases: [`BaseChatOpenAI`](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.BaseChatOpenAI.html#langchain_openai.chat_models.base.BaseChatOpenAI "langchain_openai.chat_models.base.BaseChatOpenAI")

OpenAI chat model integration.

Setup

Install `langchain-openai` and set environment variable `OPENAI_API_KEY`.               pip install -U langchain-openai     export OPENAI_API_KEY="your-api-key"     

Key init args — completion params

model: str     

Name of OpenAI model to use.

temperature: float     

Sampling temperature.

max\_tokens: Optional\[int\]     

Max number of tokens to generate.

logprobs: Optional\[bool\]     

Whether to return logprobs.

stream\_options: Dict     

Configure streaming outputs, like whether to return token usage when streaming \(`{"include_usage": True}`\).

use\_responses\_api: Optional\[bool\]     

Whether to use the responses API.

See full list of supported init args and their descriptions in the params section.

Key init args — client params

timeout: Union\[float, Tuple\[float, float\], Any, None\]     

Timeout for requests.

max\_retries: Optional\[int\]     

Max number of retries.

api\_key: Optional\[str\]     

OpenAI API key. If not passed in will be read from env var `OPENAI_API_KEY`.

base\_url: Optional\[str\]     

Base URL for API requests. Only specify if using a proxy or service emulator.

organization: Optional\[str\]     

OpenAI organization ID. If not passed in will be read from env var `OPENAI_ORG_ID`.

See full list of supported init args and their descriptions in the params section.

Instantiate               from langchain_openai import ChatOpenAI          llm = ChatOpenAI(         model="gpt-4o",         temperature=0,         max_tokens=None,         timeout=None,         max_retries=2,         # api_key="...",         # base_url="...",         # organization="...",         # other params...     )     

**NOTE** : Any param which is not explicitly supported will be passed directly to the `openai.OpenAI.chat.completions.create(...)` API every time to the model is invoked. For example:               from langchain_openai import ChatOpenAI     import openai          ChatOpenAI(..., frequency_penalty=0.2).invoke(...)          # results in underlying API call of:          openai.OpenAI(..).chat.completions.create(..., frequency_penalty=0.2)          # which is also equivalent to:          ChatOpenAI(...).invoke(..., frequency_penalty=0.2)     

Invoke               messages = [         (             "system",             "You are a helpful translator. Translate the user sentence to French.",         ),         ("human", "I love programming."),     ]     llm.invoke(messages)                    AIMessage(         content="J'adore la programmation.",         response_metadata={             "token_usage": {                 "completion_tokens": 5,                 "prompt_tokens": 31,                 "total_tokens": 36,             },             "model_name": "gpt-4o",             "system_fingerprint": "fp_43dfabdef1",             "finish_reason": "stop",             "logprobs": None,         },         id="run-012cffe2-5d3d-424d-83b5-51c6d4a593d1-0",         usage_metadata={"input_tokens": 31, "output_tokens": 5, "total_tokens": 36},     )     

Stream               for chunk in llm.stream(messages):         print(chunk.text(), end="")                    AIMessageChunk(content="", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")     AIMessageChunk(content="J", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")     AIMessageChunk(         content="'adore", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0"     )     AIMessageChunk(content=" la", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")     AIMessageChunk(         content=" programmation", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0"     )     AIMessageChunk(content=".", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")     AIMessageChunk(         content="",         response_metadata={"finish_reason": "stop"},         id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0",     )                    stream = llm.stream(messages)     full = next(stream)     for chunk in stream:         full += chunk     full                    AIMessageChunk(         content="J'adore la programmation.",         response_metadata={"finish_reason": "stop"},         id="run-bf917526-7f58-4683-84f7-36a6b671d140",     )     

Async               await llm.ainvoke(messages)          # stream:     # async for chunk in (await llm.astream(messages))          # batch:     # await llm.abatch([messages])                    AIMessage(         content="J'adore la programmation.",         response_metadata={             "token_usage": {                 "completion_tokens": 5,                 "prompt_tokens": 31,                 "total_tokens": 36,             },             "model_name": "gpt-4o",             "system_fingerprint": "fp_43dfabdef1",             "finish_reason": "stop",             "logprobs": None,         },         id="run-012cffe2-5d3d-424d-83b5-51c6d4a593d1-0",         usage_metadata={             "input_tokens": 31,             "output_tokens": 5,             "total_tokens": 36,         },     )     

Tool calling               from pydantic import BaseModel, Field               class GetWeather(BaseModel):         '''Get the current weather in a given location'''              location: str = Field(             ..., description="The city and state, e.g. San Francisco, CA"         )               class GetPopulation(BaseModel):         '''Get the current population in a given location'''              location: str = Field(             ..., description="The city and state, e.g. San Francisco, CA"         )               llm_with_tools = llm.bind_tools(         [GetWeather, GetPopulation]         # strict = True  # enforce tool args schema is respected     )     ai_msg = llm_with_tools.invoke(         "Which city is hotter today and which is bigger: LA or NY?"     )     ai_msg.tool_calls                    [         {             "name": "GetWeather",             "args": {"location": "Los Angeles, CA"},             "id": "call_6XswGD5Pqk8Tt5atYr7tfenU",         },         {             "name": "GetWeather",             "args": {"location": "New York, NY"},             "id": "call_ZVL15vA8Y7kXqOy3dtmQgeCi",         },         {             "name": "GetPopulation",             "args": {"location": "Los Angeles, CA"},             "id": "call_49CFW8zqC9W7mh7hbMLSIrXw",         },         {             "name": "GetPopulation",             "args": {"location": "New York, NY"},             "id": "call_6ghfKxV264jEfe1mRIkS3PE7",         },     ]     

Note that `openai >= 1.32` supports a `parallel_tool_calls` parameter that defaults to `True`. This parameter can be set to `False` to disable parallel tool calls:               ai_msg = llm_with_tools.invoke(         "What is the weather in LA and NY?", parallel_tool_calls=False     )     ai_msg.tool_calls                    [         {             "name": "GetWeather",             "args": {"location": "Los Angeles, CA"},             "id": "call_4OoY0ZR99iEvC7fevsH8Uhtz",         }     ]     

Like other runtime parameters, `parallel_tool_calls` can be bound to a model using `llm.bind(parallel_tool_calls=False)` or during instantiation by setting `model_kwargs`.

See `ChatOpenAI.bind_tools()` method for more.

Built-in tools

Added in version 0.3.9.

You can access [built-in tools](https://platform.openai.com/docs/guides/tools?api-mode=responses) supported by the OpenAI Responses API. See LangChain [docs](https://python.langchain.com/docs/integrations/chat/openai/) for more detail.

Note

`langchain-openai >= 0.3.26` allows users to opt-in to an updated AIMessage format when using the Responses API. Setting               llm = ChatOpenAI(model="...", output_version="responses/v1")     

will format output from reasoning summaries, built-in tool invocations, and other response items into the message’s `content` field, rather than `additional_kwargs`. We recommend this format for new applications.               from langchain_openai import ChatOpenAI          llm = ChatOpenAI(model="gpt-4.1-mini", output_version="responses/v1")          tool = {"type": "web_search_preview"}     llm_with_tools = llm.bind_tools([tool])          response = llm_with_tools.invoke(         "What was a positive news story from today?"     )     response.content                    [         {             "type": "text",             "text": "Today, a heartwarming story emerged from ...",             "annotations": [                 {                     "end_index": 778,                     "start_index": 682,                     "title": "Title of story",                     "type": "url_citation",                     "url": "<url of story>",                 }             ],         }     ]     

Managing conversation state

Added in version 0.3.9.

OpenAI’s Responses API supports management of [conversation state](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses). Passing in response IDs from previous messages will continue a conversational thread. See LangChain [docs](https://python.langchain.com/docs/integrations/chat/openai/) for more detail.               from langchain_openai import ChatOpenAI          llm = ChatOpenAI(model="gpt-4.1-mini", use_responses_api=True)     response = llm.invoke("Hi, I'm Bob.")     response.text()                    "Hi Bob! How can I assist you today?"                    second_response = llm.invoke(         "What is my name?",         previous_response_id=response.response_metadata["id"],     )     second_response.text()                    "Your name is Bob. How can I help you today, Bob?"     

Added in version 0.3.26.

You can also initialize ChatOpenAI with `use_previous_response_id`. Input messages up to the most recent response will then be dropped from request payloads, and `previous_response_id` will be set using the ID of the most recent response.               llm = ChatOpenAI(model="gpt-4.1-mini", use_previous_response_id=True)     

Reasoning output

OpenAI’s Responses API supports [reasoning models](https://platform.openai.com/docs/guides/reasoning?api-mode=responses) that expose a summary of internal reasoning processes.

Note

`langchain-openai >= 0.3.26` allows users to opt-in to an updated AIMessage format when using the Responses API. Setting               llm = ChatOpenAI(model="...", output_version="responses/v1")     

will format output from reasoning summaries, built-in tool invocations, and other response items into the message’s `content` field, rather than `additional_kwargs`. We recommend this format for new applications.               from langchain_openai import ChatOpenAI          reasoning = {         "effort": "medium",  # 'low', 'medium', or 'high'         "summary": "auto",  # 'detailed', 'auto', or None     }          llm = ChatOpenAI(         model="o4-mini", reasoning=reasoning, output_version="responses/v1"     )     response = llm.invoke("What is 3^3?")          # Response text     print(f"Output: {response.text()}")          # Reasoning summaries     for block in response.content:         if block["type"] == "reasoning":             for summary in block["summary"]:                 print(summary["text"])                    Output: 3³ = 27     Reasoning: The user wants to know...     

Structured output               from typing import Optional          from pydantic import BaseModel, Field               class Joke(BaseModel):         '''Joke to tell user.'''              setup: str = Field(description="The setup of the joke")         punchline: str = Field(description="The punchline to the joke")         rating: Optional[int] = Field(             description="How funny the joke is, from 1 to 10"         )               structured_llm = llm.with_structured_output(Joke)     structured_llm.invoke("Tell me a joke about cats")                    Joke(         setup="Why was the cat sitting on the computer?",         punchline="To keep an eye on the mouse!",         rating=None,     )     

See `ChatOpenAI.with_structured_output()` for more.

JSON mode               json_llm = llm.bind(response_format={"type": "json_object"})     ai_msg = json_llm.invoke(         "Return a JSON object with key 'random_ints' and a value of 10 random ints in [0-99]"     )     ai_msg.content                    '\n{\n  "random_ints": [23, 87, 45, 12, 78, 34, 56, 90, 11, 67]\n}'     

Image input               import base64     import httpx     from langchain_core.messages import HumanMessage          image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"     image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")     message = HumanMessage(         content=[             {"type": "text", "text": "describe the weather in this image"},             {                 "type": "image_url",                 "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},             },         ]     )     ai_msg = llm.invoke([message])     ai_msg.content                    "The weather in the image appears to be clear and pleasant. The sky is mostly blue with scattered, light clouds, suggesting a sunny day with minimal cloud cover. There is no indication of rain or strong winds, and the overall scene looks bright and calm. The lush green grass and clear visibility further indicate good weather conditions."     

Token usage               ai_msg = llm.invoke(messages)     ai_msg.usage_metadata                    {"input_tokens": 28, "output_tokens": 5, "total_tokens": 33}     

When streaming, set the `stream_usage` kwarg:               stream = llm.stream(messages, stream_usage=True)     full = next(stream)     for chunk in stream:         full += chunk     full.usage_metadata                    {"input_tokens": 28, "output_tokens": 5, "total_tokens": 33}     

Alternatively, setting `stream_usage` when instantiating the model can be useful when incorporating `ChatOpenAI` into LCEL chains– or when using methods like `.with_structured_output`, which generate chains under the hood.               llm = ChatOpenAI(model="gpt-4o", stream_usage=True)     structured_llm = llm.with_structured_output(...)     

Logprobs               logprobs_llm = llm.bind(logprobs=True)     ai_msg = logprobs_llm.invoke(messages)     ai_msg.response_metadata["logprobs"]                    {         "content": [             {                 "token": "J",                 "bytes": [74],                 "logprob": -4.9617593e-06,                 "top_logprobs": [],             },             {                 "token": "'adore",                 "bytes": [39, 97, 100, 111, 114, 101],                 "logprob": -0.25202933,                 "top_logprobs": [],             },             {                 "token": " la",                 "bytes": [32, 108, 97],                 "logprob": -0.20141791,                 "top_logprobs": [],             },             {                 "token": " programmation",                 "bytes": [                     32,                     112,                     114,                     111,                     103,                     114,                     97,                     109,                     109,                     97,                     116,                     105,                     111,                     110,                 ],                 "logprob": -1.9361265e-07,                 "top_logprobs": [],             },             {                 "token": ".",                 "bytes": [46],                 "logprob": -1.2233183e-05,                 "top_logprobs": [],             },         ]     }     

Response metadata               ai_msg = llm.invoke(messages)     ai_msg.response_metadata                    {         "token_usage": {             "completion_tokens": 5,             "prompt_tokens": 28,             "total_tokens": 33,         },         "model_name": "gpt-4o",         "system_fingerprint": "fp_319be4768e",         "finish_reason": "stop",         "logprobs": None,     }     

Flex processing

OpenAI offers a variety of [service tiers](https://platform.openai.com/docs/guides/flex-processing). The “flex” tier offers cheaper pricing for requests, with the trade-off that responses may take longer and resources might not always be available. This approach is best suited for non-critical tasks, including model testing, data enhancement, or jobs that can be run asynchronously.

To use it, initialize the model with `service_tier="flex"`:               from langchain_openai import ChatOpenAI          llm = ChatOpenAI(model="o4-mini", service_tier="flex")     

Note that this is a beta feature that is only available for a subset of models. See OpenAI [docs](https://platform.openai.com/docs/guides/flex-processing) for more detail.

Note

ChatOpenAI implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

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

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _disable\_streaming _: bool | Literal\['tool\_calling'\]__ = False_\#     

Whether to disable streaming for this model.

If streaming is bypassed, then `stream()`/`astream()`/`astream_events()` will defer to `invoke()`/`ainvoke()`.

  * If True, will always bypass streaming case.

  * If `'tool_calling'`, will bypass streaming case only when the model is called with a `tools` keyword argument. In other words, LangChain will automatically switch to non-streaming behavior \(`invoke()`\) only when the tools argument is provided. This offers the best of both worlds.

  * If False \(default\), will always use streaming case if available.

The main reason for this flag is that code might be written using `.stream()` and a user may want to swap out a given model for another model whose the implementation does not properly support streaming.

_param _disabled\_params _: dict\[str, Any\] | None_ _ = None_\#     

Parameters of the OpenAI client or chat.completions endpoint that should be disabled for the given model.

Should be specified as `{"param": None | ['val1', 'val2']}` where the key is the parameter and the value is either None, meaning that parameter should never be used, or it’s a list of disabled values for the parameter.

For example, older models may not support the ‘parallel\_tool\_calls’ parameter at all, in which case `disabled_params={"parallel_tool_calls": None}` can be passed in.

If a parameter is disabled then it will not be used by default in any methods, e.g. in `with_structured_output()`. However this does not prevent a user from directly passed in the parameter during invocation.

_param _extra\_body _: Mapping\[str, Any\] | None_ _ = None_\#     

Optional additional JSON properties to include in the request parameters when making requests to OpenAI compatible APIs, such as vLLM.

_param _frequency\_penalty _: float | None_ _ = None_\#     

Penalizes repeated tokens according to frequency.

_param _http\_async\_client _: Any | None_ _ = None_\#     

Optional httpx.AsyncClient. Only used for async invocations. Must specify `http_client` as well if you’d like a custom client for sync invocations.

_param _http\_client _: Any | None_ _ = None_\#     

Optional `httpx.Client`. Only used for sync invocations. Must specify `http_async_client` as well if you’d like a custom client for async invocations.

_param _include _: list\[str\] | None_ _ = None_\#     

Additional fields to include in generations from Responses API.

Supported values:

  * `"file_search_call.results"`

  * `"message.input_image.image_url"`

  * `"computer_call_output.output.image_url"`

  * `"reasoning.encrypted_content"`

  * `"code_interpreter_call.outputs"`

Added in version 0.3.24.

_param _include\_response\_headers _: bool_ _ = False_\#     

Whether to include response headers in the output message response\_metadata.

_param _logit\_bias _: dict\[int, int\] | None_ _ = None_\#     

Modify the likelihood of specified tokens appearing in the completion.

_param _logprobs _: bool | None_ _ = None_\#     

Whether to return logprobs.

_param _max\_retries _: int | None_ _ = None_\#     

Maximum number of retries to make when generating.

_param _max\_tokens _: int | None_ _ = None_ _\(alias 'max\_completion\_tokens'\)_\#     

Maximum number of tokens to generate.

_param _metadata _: dict\[str, Any\] | None_ _ = None_\#     

Metadata to add to the run trace.

_param _model\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _model\_name _: str_ _ = 'gpt-3.5-turbo'__\(alias 'model'\)_\#     

Model name to use.

_param _n _: int | None_ _ = None_\#     

Number of chat completions to generate for each prompt.

_param _openai\_api\_base _: str | None_ _ = None_ _\(alias 'base\_url'\)_\#     

Base URL path for API requests, leave blank if not using a proxy or service emulator.

_param _openai\_api\_key _: SecretStr | None_ _\[Optional\]__\(alias 'api\_key'\)_\#     

_param _openai\_organization _: str | None_ _ = None_ _\(alias 'organization'\)_\#     

Automatically inferred from env var OPENAI\_ORG\_ID if not provided.

_param _openai\_proxy _: str | None_ _\[Optional\]_\#     

_param _output\_version _: Literal\['v0', 'responses/v1'\]__ = 'v0'_\#     

Version of AIMessage output format to use.

This field is used to roll-out new output formats for chat model AIMessages in a backwards-compatible way.

Supported values:

  * `"v0"`: AIMessage format as of langchain-openai 0.3.x.

  * `"responses/v1"`: Formats Responses API output items into AIMessage content blocks.

Currently only impacts the Responses API. `output_version="responses/v1"` is recommended.

Added in version 0.3.25.

_param _presence\_penalty _: float | None_ _ = None_\#     

Penalizes repeated tokens.

_param _rate\_limiter _: [BaseRateLimiter](https://python.langchain.com/api_reference/core/rate_limiters/langchain_core.rate_limiters.BaseRateLimiter.html#langchain_core.rate_limiters.BaseRateLimiter "langchain_core.rate_limiters.BaseRateLimiter") | None_ _ = None_\#     

An optional rate limiter to use for limiting the number of requests.

_param _reasoning _: dict\[str, Any\] | None_ _ = None_\#     

Reasoning parameters for reasoning models, i.e., OpenAI o-series models \(o1, o3, o4-mini, etc.\). For use with the Responses API.

Example:               reasoning={         "effort": "medium",  # can be "low", "medium", or "high"         "summary": "auto",  # can be "auto", "concise", or "detailed"     }     

Added in version 0.3.24.

_param _reasoning\_effort _: str | None_ _ = None_\#     

Constrains effort on reasoning for reasoning models. For use with the Chat Completions API.

Reasoning models only, like OpenAI o1, o3, and o4-mini.

Currently supported values are low, medium, and high. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.

Added in version 0.2.14.

_param _request\_timeout _: float | tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to OpenAI completion API. Can be float, httpx.Timeout or None.

_param _seed _: int | None_ _ = None_\#     

Seed for generation

_param _service\_tier _: str | None_ _ = None_\#     

Latency tier for request. Options are `'auto'`, `'default'`, or `'flex'`. Relevant for users of OpenAI’s scale tier service.

_param _stop _: list\[str\] | str | None_ _ = None_ _\(alias 'stop\_sequences'\)_\#     

Default stop sequences.

_param _store _: bool | None_ _ = None_\#     

If True, OpenAI may store response data for future use. Defaults to True for the Responses API and False for the Chat Completions API.

Added in version 0.3.24.

_param _stream\_usage _: bool_ _ = False_\#     

Whether to include usage metadata in streaming output. If True, an additional message chunk will be generated during the stream including usage metadata.

Added in version 0.3.9.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results or not.

_param _tags _: list\[str\] | None_ _ = None_\#     

Tags to add to the run trace.

_param _temperature _: float | None_ _ = None_\#     

What sampling temperature to use.

_param _tiktoken\_model\_name _: str | None_ _ = None_\#     

The model name to pass to tiktoken when using this class. Tiktoken is used to count the number of tokens in documents to constrain them to be under a certain limit. By default, when set to None, this will be the same as the embedding model name. However, there are some cases where you may want to use this Embedding class with a model name not supported by tiktoken. This can include when using Azure embeddings or when using one of the many model providers that expose an OpenAI-like API but with different models. In those cases, in order to avoid erroring when tiktoken is called, you can specify a model name to use here.

_param _top\_logprobs _: int | None_ _ = None_\#     

Number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.

_param _top\_p _: float | None_ _ = None_\#     

Total probability mass of tokens to consider at each step.

_param _truncation _: str | None_ _ = None_\#     

Truncation strategy \(Responses API\). Can be `'auto'` or `'disabled'` \(default\). If `'auto'`, model may drop input items from the middle of the message sequence to fit the context window.

Added in version 0.3.24.

_param _use\_previous\_response\_id _: bool_ _ = False_\#     

If True, always pass `previous_response_id` using the ID of the most recent response. Responses API only.

Input messages up to the most recent response will be dropped from request payloads.

For example, the following two are equivalent:               llm = ChatOpenAI(         model="o4-mini",         use_previous_response_id=True,     )     llm.invoke(         [             HumanMessage("Hello"),             AIMessage("Hi there!", response_metadata={"id": "resp_123"}),             HumanMessage("How are you?"),         ]     )                    llm = ChatOpenAI(         model="o4-mini",         use_responses_api=True,     )     llm.invoke([HumanMessage("How are you?")], previous_response_id="resp_123")     

Added in version 0.3.26.

_param _use\_responses\_api _: bool | None_ _ = None_\#     

Whether to use the Responses API instead of the Chat API.

If not specified then will be inferred based on invocation params.

Added in version 0.3.9.

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

bind\_functions\(

    _functions : Sequence\[dict\[str, Any\] | type\[BaseModel\] | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _function\_call : \_FunctionCall | str | Literal\['auto', 'none'\] | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Deprecated since version 0.2.1: Use `bind_tools()` instead. It will not be removed until langchain-openai==1.0.0.

Bind functions \(and other objects\) to this chat model.

Assumes model is compatible with OpenAI function-calling API.

NOTE: Using bind\_tools is recommended instead, as the functions and     

function\_call request parameters are officially marked as deprecated by OpenAI.

Parameters:     

  * **functions** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__BaseModel_ _\]__|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of function definitions to bind to this chat model. Can be a dictionary, pydantic model, or callable. Pydantic models and callables will be automatically converted to their schema dictionary representation.

  * **function\_call** \(_\_FunctionCall_ _|__str_ _|__Literal_ _\[__'auto'__,__'none'__\]__|__None_\) – Which function to require the model to call. Must be the name of the single provided function or “auto” to automatically determine which function to call \(if any\).

  * **\*\*kwargs** \(_Any_\) – Any additional parameters to pass to the `Runnable` constructor.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

bind\_tools\(

    _tools : Sequence\[dict\[str, Any\] | type | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _\*_ ,     _tool\_choice : dict | str | Literal\['auto', 'none', 'any', 'required'\] | bool | None = None_,     _strict : bool | None = None_,     _parallel\_tool\_calls : bool | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Bind tool-like objects to this chat model.

Assumes model is compatible with OpenAI tool-calling API.

Parameters:     

  * **tools** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of tool definitions to bind to this chat model. Supports any tool definition handled by [`langchain_core.utils.function_calling.convert_to_openai_tool()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html#langchain_core.utils.function_calling.convert_to_openai_tool "langchain_core.utils.function_calling.convert_to_openai_tool").

  * **tool\_choice** \(_dict_ _|__str_ _|__Literal_ _\[__'auto'__,__'none'__,__'any'__,__'required'__\]__|__bool_ _|__None_\) – 

Which tool to require the model to call. Options are:

    * str of the form `"<<tool_name>>"`: calls <<tool\_name>> tool.

    * `"auto"`: automatically selects a tool \(including no tool\).

    * `"none"`: does not call a tool.

    * `"any"` or `"required"` or `True`: force at least one tool to be called.

    * dict of the form `{"type": "function", "function": {"name": <<tool_name>>}}`: calls <<tool\_name>> tool.

    * `False` or `None`: no effect, default OpenAI behavior.

  * **strict** \(_bool_ _|__None_\) – If True, model output is guaranteed to exactly match the JSON Schema provided in the tool definition. If True, the input schema will be validated according to <https://platform.openai.com/docs/guides/structured-outputs/supported-schemas>. If False, input schema will not be validated and model output will not be validated. If None, `strict` argument will not be passed to the model.

  * **parallel\_tool\_calls** \(_bool_ _|__None_\) – Set to `False` to disable parallel tool use. Defaults to `None` \(no specification, which allows parallel tool use\).

  * **kwargs** \(_Any_\) – Any additional parameters are passed directly to `bind()`.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Changed in version 0.1.21: Support for `strict` argument added.

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

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _tools : Sequence\[dict\[str, Any\] | type | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\] | None = None_, \) → int\#     

Calculate num tokens for `gpt-3.5-turbo` and `gpt-4` with `tiktoken` package.

**Requirements** : You must have the `pillow` installed if you want to count image tokens if you are specifying the image as a base64 string, and you must have both `pillow` and `httpx` installed if you are specifying the image as a URL. If these aren’t installed image inputs will be ignored in token counting.

[OpenAI reference](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – The message inputs to tokenize.

  * **tools** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]__|__None_\) – If provided, sequence of dict, BaseModel, function, or BaseTools to be converted to tool schemas.

Return type:     

int

get\_token\_ids\(_text : str_\) → list\[int\]\#     

Get the tokens present in the text with tiktoken package.

Parameters:     

**text** \(_str_\)

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

    _schema : dict\[str, Any\] | type\[\_BM\] | type | None = None_,     _\*_ ,     _method : Literal\['function\_calling', 'json\_mode', 'json\_schema'\] = 'json\_schema'_,     _include\_raw : bool = False_,     _strict : bool | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], dict | \_BM\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#ChatOpenAI.with_structured_output)\#     

Model wrapper that returns outputs formatted to match the given schema.

Parameters:     

  * **schema** \(_dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__\_BM_ _\]__|__type_ _|__None_\) – 

The output schema. Can be passed in as:

    * a JSON Schema,

    * a TypedDict class,

    * or a Pydantic class,

    * an OpenAI function/tool schema.

If `schema` is a Pydantic class then the model output will be a Pydantic instance of that class, and the model-generated fields will be validated by the Pydantic class. Otherwise the model output will be a dict and will not be validated. See [`langchain_core.utils.function_calling.convert_to_openai_tool()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html#langchain_core.utils.function_calling.convert_to_openai_tool "langchain_core.utils.function_calling.convert_to_openai_tool") for more on how to properly specify types and descriptions of schema fields when specifying a Pydantic or TypedDict class.

  * **method** \(_Literal_ _\[__'function\_calling'__,__'json\_mode'__,__'json\_schema'__\]_\) – 

The method for steering model generation, one of:

    * ”json\_schema”:     

Uses OpenAI’s Structured Output API: <https://platform.openai.com/docs/guides/structured-outputs> Supported for “gpt-4o-mini”, “gpt-4o-2024-08-06”, “o1”, and later models.

    * ”function\_calling”:     

Uses OpenAI’s tool-calling \(formerly called function calling\) API: <https://platform.openai.com/docs/guides/function-calling>

    * ”json\_mode”:     

Uses OpenAI’s JSON mode. Note that if using JSON mode then you must include instructions for formatting the output into the desired schema into the model call: <https://platform.openai.com/docs/guides/structured-outputs/json-mode>

Learn more about the differences between the methods and which models support which methods here:

    * <https://platform.openai.com/docs/guides/structured-outputs/structured-outputs-vs-json-mode>

    * <https://platform.openai.com/docs/guides/structured-outputs/function-calling-vs-response-format>

  * **include\_raw** \(_bool_\) – If False then only the parsed structured output is returned. If an error occurs during model output parsing it will be raised. If True then both the raw model response \(a BaseMessage\) and the parsed model response will be returned. If an error occurs during output parsing it will be caught and returned as well. The final output is always a dict with keys “raw”, “parsed”, and “parsing\_error”.

  * **strict** \(_bool_ _|__None_\) –      * True:     

Model output is guaranteed to exactly match the schema. The input schema will also be validated according to <https://platform.openai.com/docs/guides/structured-outputs/supported-schemas>

    * False:     

Input schema will not be validated and model output will not be validated.

    * None:     

`strict` argument will not be passed to the model.

If schema is specified via TypedDict or JSON schema, `strict` is not enabled by default. Pass `strict=True` to enable it.

Note: `strict` can only be non-null if `method` is `"json_schema"` or `"function_calling"`.

  * **tools** – 

A list of tool-like objects to bind to the chat model. Requires that:

    * `method` is `"json_schema"` \(default\).

    * `strict=True`

    * `include_raw=True`

If a model elects to call a tool, the resulting `AIMessage` in `"raw"` will include tool calls.

Example          from langchain.chat_models import init_chat_model     from pydantic import BaseModel               class ResponseSchema(BaseModel):         response: str               def get_weather(location: str) -> str:         """Get weather at a location."""         pass          llm = init_chat_model("openai:gpt-4o-mini")          structured_llm = llm.with_structured_output(         ResponseSchema,         tools=[get_weather],         strict=True,         include_raw=True,     )          structured_llm.invoke("What's the weather in Boston?")               {         "raw": AIMessage(content="", tool_calls=[...], ...),         "parsing_error": None,         "parsed": None,     }     

  * **kwargs** \(_Any_\) – Additional keyword args are passed through to the model.

Returns:     

A Runnable that takes same inputs as a `langchain_core.language_models.chat.BaseChatModel`.

If `include_raw` is False and `schema` is a Pydantic class, Runnable outputs an instance of `schema` \(i.e., a Pydantic object\). Otherwise, if `include_raw` is False then Runnable outputs a dict.

If `include_raw` is True, then Runnable outputs a dict with keys:

  * ”raw”: BaseMessage

  * ”parsed”: None if there was a parsing error, otherwise the type depends on the `schema` as described above.

  * ”parsing\_error”: Optional\[BaseException\]

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], dict | _\_BM_\]

Changed in version 0.1.20: Added support for TypedDict class `schema`.

Changed in version 0.1.21: Support for `strict` argument added. Support for `method="json_schema"` added.

Changed in version 0.3.0: `method` default changed from “function\_calling” to “json\_schema”.

Changed in version 0.3.12: Support for `tools` added.

Changed in version 0.3.21: Pass `kwargs` through to the model.

Example: schema=Pydantic class, method=”json\_schema”, include\_raw=False, strict=True

Note, OpenAI has a number of restrictions on what types of schemas can be provided if `strict` = True. When using Pydantic, our model cannot specify any Field metadata \(like min/max constraints\) and fields cannot have default values.

See all constraints here: <https://platform.openai.com/docs/guides/structured-outputs/supported-schemas>               from typing import Optional          from langchain_openai import ChatOpenAI     from pydantic import BaseModel, Field               class AnswerWithJustification(BaseModel):         '''An answer to the user question along with justification for the answer.'''              answer: str         justification: Optional[str] = Field(             default=..., description="A justification for the answer."         )               llm = ChatOpenAI(model="gpt-4o", temperature=0)     structured_llm = llm.with_structured_output(AnswerWithJustification)          structured_llm.invoke(         "What weighs more a pound of bricks or a pound of feathers"     )          # -> AnswerWithJustification(     #     answer='They weigh the same',     #     justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'     # )     

Example: schema=Pydantic class, method=”function\_calling”, include\_raw=False, strict=False               from typing import Optional          from langchain_openai import ChatOpenAI     from pydantic import BaseModel, Field               class AnswerWithJustification(BaseModel):         '''An answer to the user question along with justification for the answer.'''              answer: str         justification: Optional[str] = Field(             default=..., description="A justification for the answer."         )               llm = ChatOpenAI(model="gpt-4o", temperature=0)     structured_llm = llm.with_structured_output(         AnswerWithJustification, method="function_calling"     )          structured_llm.invoke(         "What weighs more a pound of bricks or a pound of feathers"     )          # -> AnswerWithJustification(     #     answer='They weigh the same',     #     justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'     # )     

Example: schema=Pydantic class, method=”json\_schema”, include\_raw=True               from langchain_openai import ChatOpenAI     from pydantic import BaseModel               class AnswerWithJustification(BaseModel):         '''An answer to the user question along with justification for the answer.'''              answer: str         justification: str               llm = ChatOpenAI(model="gpt-4o", temperature=0)     structured_llm = llm.with_structured_output(         AnswerWithJustification, include_raw=True     )          structured_llm.invoke(         "What weighs more a pound of bricks or a pound of feathers"     )     # -> {     #     'raw': AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_Ao02pnFYXD6GN1yzc0uXPsvF', 'function': {'arguments': '{"answer":"They weigh the same.","justification":"Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ."}', 'name': 'AnswerWithJustification'}, 'type': 'function'}]}),     #     'parsed': AnswerWithJustification(answer='They weigh the same.', justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'),     #     'parsing_error': None     # }     

Example: schema=TypedDict class, method=”json\_schema”, include\_raw=False, strict=False               # IMPORTANT: If you are using Python <=3.8, you need to import Annotated     # from typing_extensions, not from typing.     from typing_extensions import Annotated, TypedDict          from langchain_openai import ChatOpenAI               class AnswerWithJustification(TypedDict):         '''An answer to the user question along with justification for the answer.'''              answer: str         justification: Annotated[             Optional[str], None, "A justification for the answer."         ]               llm = ChatOpenAI(model="gpt-4o", temperature=0)     structured_llm = llm.with_structured_output(AnswerWithJustification)          structured_llm.invoke(         "What weighs more a pound of bricks or a pound of feathers"     )     # -> {     #     'answer': 'They weigh the same',     #     'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.'     # }     

Example: schema=OpenAI function schema, method=”json\_schema”, include\_raw=False                from langchain_openai import ChatOpenAI           oai_schema = {          'name': 'AnswerWithJustification',          'description': 'An answer to the user question along with justification for the answer.',          'parameters': {              'type': 'object',              'properties': {                  'answer': {'type': 'string'},                  'justification': {'description': 'A justification for the answer.', 'type': 'string'}              },             'required': ['answer']         }     }           llm = ChatOpenAI(model="gpt-4o", temperature=0)      structured_llm = llm.with_structured_output(oai_schema)           structured_llm.invoke(          "What weighs more a pound of bricks or a pound of feathers"      )      # -> {      #     'answer': 'They weigh the same',      #     'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.'      # }     

Example: schema=Pydantic class, method=”json\_mode”, include\_raw=True               from langchain_openai import ChatOpenAI     from pydantic import BaseModel          class AnswerWithJustification(BaseModel):         answer: str         justification: str          llm = ChatOpenAI(model="gpt-4o", temperature=0)     structured_llm = llm.with_structured_output(         AnswerWithJustification,         method="json_mode",         include_raw=True     )          structured_llm.invoke(         "Answer the following question. "         "Make sure to return a JSON blob with keys 'answer' and 'justification'.\n\n"         "What's heavier a pound of bricks or a pound of feathers?"     )     # -> {     #     'raw': AIMessage(content='{\n    "answer": "They are both the same weight.",\n    "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight." \n}'),     #     'parsed': AnswerWithJustification(answer='They are both the same weight.', justification='Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight.'),     #     'parsing_error': None     # }     

Example: schema=None, method=”json\_mode”, include\_raw=True               structured_llm = llm.with_structured_output(method="json_mode", include_raw=True)          structured_llm.invoke(         "Answer the following question. "         "Make sure to return a JSON blob with keys 'answer' and 'justification'.\n\n"         "What's heavier a pound of bricks or a pound of feathers?"     )     # -> {     #     'raw': AIMessage(content='{\n    "answer": "They are both the same weight.",\n    "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight." \n}'),     #     'parsed': {     #         'answer': 'They are both the same weight.',     #         'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight.'     #     },     #     'parsing_error': None     # }     

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

Examples using ChatOpenAI

  * [\# Example](https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain/)

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/llm_router_chain/)

  * [AINetwork Toolkit](https://python.langchain.com/docs/integrations/tools/ainetwork/)

  * [AWS DynamoDB](https://python.langchain.com/docs/integrations/memory/aws_dynamodb/)

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Amadeus Toolkit](https://python.langchain.com/docs/integrations/tools/amadeus/)

  * [Amazon Neptune with Cypher](https://python.langchain.com/docs/integrations/graphs/amazon_neptune_open_cypher/)

  * [Apache AGE](https://python.langchain.com/docs/integrations/graphs/apache_age/)

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [ArXiv](https://python.langchain.com/docs/integrations/tools/arxiv/)

  * [ArangoDB](https://python.langchain.com/docs/integrations/graphs/arangodb/)

  * [Arthur](https://python.langchain.com/docs/integrations/providers/arthur_tracking/)

  * [AskNews](https://python.langchain.com/docs/integrations/tools/asknews/)

  * [Azure Container Apps dynamic sessions](https://python.langchain.com/docs/integrations/tools/azure_dynamic_sessions/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [Bearly Code Interpreter](https://python.langchain.com/docs/integrations/tools/bearly/)

  * [Browserbase](https://python.langchain.com/docs/integrations/document_loaders/browserbase/)

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [Build a Question Answering application over a Graph Database](https://python.langchain.com/docs/tutorials/graph/)

  * [Build a Simple LLM Application with LCEL](https://python.langchain.com/docs/tutorials/llm_chain/)

  * [Cassandra Database Toolkit](https://python.langchain.com/docs/integrations/tools/cassandra_database/)

  * [ChatGPT Plugins](https://python.langchain.com/docs/integrations/tools/chatgpt_plugins/)

  * [ChatOpenAI](https://python.langchain.com/docs/integrations/chat/openai/)

  * [Classify Text into Labels](https://python.langchain.com/docs/tutorials/classification/)

  * [CnosDB](https://python.langchain.com/docs/integrations/providers/cnosdb/)

  * [Cogniswitch Toolkit](https://python.langchain.com/docs/integrations/tools/cogniswitch/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [Connery Toolkit](https://python.langchain.com/docs/integrations/tools/connery_toolkit/)

  * [Connery Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/connery/)

  * [Context](https://python.langchain.com/docs/integrations/callbacks/context/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Couchbase](https://python.langchain.com/docs/integrations/memory/couchbase_chat_message_history/)

  * [Dataherald](https://python.langchain.com/docs/integrations/providers/dataherald/)

  * [Diffbot](https://python.langchain.com/docs/integrations/graphs/diffbot/)

  * [Discord](https://python.langchain.com/docs/integrations/chat_loaders/discord/)

  * [E2B Data Analysis](https://python.langchain.com/docs/integrations/tools/e2b_data_analysis/)

  * [ElasticsearchRetriever](https://python.langchain.com/docs/integrations/retrievers/elasticsearch_retriever/)

  * [Exa Search](https://python.langchain.com/docs/integrations/tools/exa_search/)

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

  * [FalkorDB](https://python.langchain.com/docs/integrations/graphs/falkordb/)

  * [Figma](https://python.langchain.com/docs/integrations/document_loaders/figma/)

  * [FinancialDatasets Toolkit](https://python.langchain.com/docs/integrations/tools/financial_datasets/)

  * [FlashRank reranker](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/)

  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)

  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)

  * [Generate Synthetic Data](https://python.langchain.com/docs/tutorials/data_generation/)

  * [Hippo](https://python.langchain.com/docs/integrations/vectorstores/hippo/)

  * [How deal with high cardinality categoricals when doing query analysis](https://python.langchain.com/docs/how_to/query_high_cardinality/)

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add default invocation args to a Runnable](https://python.langchain.com/docs/how_to/binding/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to add fallbacks to a runnable](https://python.langchain.com/docs/how_to/fallbacks/)

  * [How to add memory to chatbots](https://python.langchain.com/docs/how_to/chatbots_memory/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)

  * [How to add tools to chatbots](https://python.langchain.com/docs/how_to/chatbots_tools/)

  * [How to add values to a chain’s state](https://python.langchain.com/docs/how_to/assign/)

  * [How to best prompt for Graph-RAG](https://python.langchain.com/docs/how_to/graph_prompting/)

  * [How to bind model-specific tools](https://python.langchain.com/docs/how_to/tools_model_specific/)

  * [How to configure runtime chain internals](https://python.langchain.com/docs/how_to/configure/)

  * [How to construct knowledge graphs](https://python.langchain.com/docs/how_to/graph_constructing/)

  * [How to convert tools to OpenAI Functions](https://python.langchain.com/docs/how_to/tools_as_openai_functions/)

  * [How to disable parallel tool calling](https://python.langchain.com/docs/how_to/tool_calling_parallel/)

  * [How to do “self-querying” retrieval](https://python.langchain.com/docs/how_to/self_query/)

  * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)

  * [How to get log probabilities](https://python.langchain.com/docs/how_to/logprobs/)

  * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)

  * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)

  * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)

  * [How to inspect runnables](https://python.langchain.com/docs/how_to/inspect/)

  * [How to invoke runnables in parallel](https://python.langchain.com/docs/how_to/parallel/)

  * [How to map values to a graph database](https://python.langchain.com/docs/how_to/graph_mapping/)

  * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)

  * [How to parse JSON output](https://python.langchain.com/docs/how_to/output_parser_json/)

  * [How to parse YAML output](https://python.langchain.com/docs/how_to/output_parser_yaml/)

  * [How to pass multimodal data directly to models](https://python.langchain.com/docs/how_to/multimodal_inputs/)

  * [How to pass through arguments from one step to the next](https://python.langchain.com/docs/how_to/passthrough/)

  * [How to retry when a parsing error occurs](https://python.langchain.com/docs/how_to/output_parser_retry/)

  * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)

  * [How to save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)

  * [How to stream tool calls](https://python.langchain.com/docs/how_to/tool_streaming/)

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

  * [How to use LangChain with different Pydantic versions](https://python.langchain.com/docs/how_to/pydantic_compatibility/)

  * [How to use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)

  * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)

  * [How to use multimodal prompts](https://python.langchain.com/docs/how_to/multimodal_prompts/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

  * [How to use the output-fixing parser](https://python.langchain.com/docs/how_to/output_parser_fixing/)

  * [HugeGraph](https://python.langchain.com/docs/integrations/graphs/hugegraph/)

  * [Human as a tool](https://python.langchain.com/docs/integrations/tools/human_tools/)

  * [Hybrid Search](https://python.langchain.com/docs/how_to/hybrid/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [Infino](https://python.langchain.com/docs/integrations/callbacks/infino/)

  * [Infobip](https://python.langchain.com/docs/integrations/tools/infobip/)

  * [Jaguar Vector Database](https://python.langchain.com/docs/integrations/vectorstores/jaguar/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

  * [KDB.AI](https://python.langchain.com/docs/integrations/vectorstores/kdbai/)

  * [Kay.ai](https://python.langchain.com/docs/integrations/retrievers/kay/)

  * [Kuzu](https://python.langchain.com/docs/integrations/graphs/kuzu_db/)

  * [LLMLingua Document Compressor](https://python.langchain.com/docs/integrations/retrievers/llmlingua/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [Label Studio](https://python.langchain.com/docs/integrations/callbacks/labelstudio/)

  * [LangSmith Chat Datasets](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_dataset/)

  * [LangSmith LLM Runs](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_llm_runs/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [Log, Trace, and Monitor](https://python.langchain.com/docs/integrations/providers/portkey/logging_tracing_portkey/)

  * [Log10](https://python.langchain.com/docs/integrations/providers/log10/)

  * [MLflow](https://python.langchain.com/docs/integrations/providers/mlflow_tracking/)

  * [Memgraph](https://python.langchain.com/docs/integrations/graphs/memgraph/)

  * [Milvus Hybrid Search Retriever](https://python.langchain.com/docs/integrations/retrievers/milvus_hybrid_search/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Momento Vector Index \(MVI\)](https://python.langchain.com/docs/integrations/vectorstores/momento_vector_index/)

  * [MongoDB](https://python.langchain.com/docs/integrations/memory/mongodb_chat_message_history/)

  * [MultiOn Toolkit](https://python.langchain.com/docs/integrations/tools/multion/)

  * [MyScale](https://python.langchain.com/docs/integrations/retrievers/self_query/myscale_self_query/)

  * [NebulaGraph](https://python.langchain.com/docs/integrations/graphs/nebula_graph/)

  * [Neo4j](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)

  * [Neo4j Vector Index](https://python.langchain.com/docs/integrations/vectorstores/neo4jvector/)

  * [Ontotext GraphDB](https://python.langchain.com/docs/integrations/graphs/ontotext/)

  * [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/)

  * [OpenAI metadata tagger](https://python.langchain.com/docs/integrations/document_transformers/openai_metadata_tagger/)

  * [OpenAPI Toolkit](https://python.langchain.com/docs/integrations/tools/openapi/)

  * [Outline](https://python.langchain.com/docs/integrations/retrievers/outline/)

  * [Pandas Dataframe](https://python.langchain.com/docs/integrations/tools/pandas/)

  * [Passio NutritionAI](https://python.langchain.com/docs/integrations/tools/passio_nutrition_ai/)

  * [Polygon IO Toolkit](https://python.langchain.com/docs/integrations/tools/polygon_toolkit/)

  * [Polygon IO Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/polygon/)

  * [Portkey](https://python.langchain.com/docs/integrations/providers/portkey/index/)

  * [PowerBI Toolkit](https://python.langchain.com/docs/integrations/tools/powerbi/)

  * [PromptLayer](https://python.langchain.com/docs/integrations/callbacks/promptlayer/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/retrievers/ragatouille/)

  * [RDFLib](https://python.langchain.com/docs/integrations/graphs/rdflib_sparql/)

  * [RankLLM Reranker](https://python.langchain.com/docs/integrations/document_transformers/rankllm-reranker/)

  * [RePhraseQuery](https://python.langchain.com/docs/integrations/retrievers/re_phrase/)

  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)

  * [Redis](https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/)

  * [Rememberizer](https://python.langchain.com/docs/integrations/retrievers/rememberizer/)

  * [Remembrall](https://python.langchain.com/docs/integrations/memory/remembrall/)

  * [Requests Toolkit](https://python.langchain.com/docs/integrations/tools/requests/)

  * [Response metadata](https://python.langchain.com/docs/how_to/response_metadata/)

  * [Robocorp Toolkit](https://python.langchain.com/docs/integrations/tools/robocorp/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SEC filing](https://python.langchain.com/docs/integrations/retrievers/sec_filings/)

  * [SQL \(SQLAlchemy\)](https://python.langchain.com/docs/integrations/memory/sql_chat_message_history/)

  * [SQLite](https://python.langchain.com/docs/integrations/memory/sqlite/)

  * [Semantic Scholar API Tool](https://python.langchain.com/docs/integrations/tools/semanticscholar/)

  * [Shell \(bash\)](https://python.langchain.com/docs/integrations/tools/bash/)

  * [Slack](https://python.langchain.com/docs/integrations/chat_loaders/slack/)

  * [Slack Toolkit](https://python.langchain.com/docs/integrations/tools/slack/)

  * [Spark SQL Toolkit](https://python.langchain.com/docs/integrations/tools/spark_sql/)

  * [Streamlit](https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history/)

  * [TavilySearchAPIRetriever](https://python.langchain.com/docs/integrations/retrievers/tavily/)

  * [Telegram](https://python.langchain.com/docs/integrations/chat_loaders/telegram/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/retrievers/self_query/tencentvectordb/)

  * [TiDB](https://python.langchain.com/docs/integrations/memory/tidb_chat_message_history/)

  * [Timescale Vector \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/timescalevector/)

  * [Trubrics](https://python.langchain.com/docs/integrations/callbacks/trubrics/)

  * [UpTrain](https://python.langchain.com/docs/integrations/callbacks/uptrain/)

  * [Upstash Ratelimit Callback](https://python.langchain.com/docs/integrations/callbacks/upstash_ratelimit/)

  * [Vectara](https://python.langchain.com/docs/integrations/vectorstores/vectara/)

  * [Vectara self-querying ](https://python.langchain.com/docs/integrations/retrievers/self_query/vectara_self_query/)

  * [WeChat](https://python.langchain.com/docs/integrations/chat_loaders/wechat/)

  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)

  * [WhatsApp](https://python.langchain.com/docs/integrations/chat_loaders/whatsapp/)

  * [Xata](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history/)

  * [Yahoo Finance News](https://python.langchain.com/docs/integrations/tools/yahoo_finance_news/)

  * [Yellowbrick](https://python.langchain.com/docs/integrations/vectorstores/yellowbrick/)

  * [You.com](https://python.langchain.com/docs/integrations/retrievers/you-retriever/)

  * [You.com Search](https://python.langchain.com/docs/integrations/tools/you/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

  * [vLLM Chat](https://python.langchain.com/docs/integrations/chat/vllm/)

  * [🦜️🏓 LangServe](https://python.langchain.com/docs/langserve/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)