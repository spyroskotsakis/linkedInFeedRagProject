# ChatVertexAI — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/chat_models/langchain_google_vertexai.chat_models.ChatVertexAI.html
**Word Count:** 4359
**Links Count:** 349
**Scraped:** 2025-07-21 08:27:19
**Status:** completed

---

# ChatVertexAI\#

_class _langchain\_google\_vertexai.chat\_models.ChatVertexAI[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/chat_models.html#ChatVertexAI)\#     

Bases: `_VertexAICommon`, [`BaseChatModel`](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")

Google Cloud Vertex AI chat model integration.

Setup:     

You must either:     

  * Have credentials configured for your environment \(gcloud, workload identity, etc…\)

  * Store the path to a service account JSON file as the `GOOGLE_APPLICATION_CREDENTIALS` environment variable

This codebase uses the `google.auth` library which first looks for the application credentials variable mentioned above, and then looks for system-level auth.

**More information:**

  * [Credential types](https://cloud.google.com/docs/authentication/application-default-credentials#GAC)

  * `google.auth` [API reference](https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth)

Key init args — completion params:     

model: str     

Name of ChatVertexAI model to use. e.g. `'gemini-2.0-flash-001'`, `'gemini-2.5-pro'`, etc.

temperature: Optional\[float\]     

Sampling temperature.

seed: Optional\[int\]     

Sampling integer to use.

max\_tokens: Optional\[int\]     

Max number of tokens to generate.

stop: Optional\[List\[str\]\]     

Default stop sequences.

safety\_settings: Optional\[Dict\[vertexai.generative\_models.HarmCategory, vertexai.generative\_models.HarmBlockThreshold\]\]     

The default safety settings to use for all generations.

Key init args — client params:     

max\_retries: int     

Max number of retries.

wait\_exponential\_kwargs: Optional\[dict\[str, float\]\]     

Optional dictionary with parameters for wait\_exponential: \- multiplier: Initial wait time multiplier \(default: `1.0`\) \- min: Minimum wait time in seconds \(default: `4.0`\) \- max: Maximum wait time in seconds \(default: `10.0`\) \- exp\_base: Exponent base to use \(default: `2.0`\)

credentials: Optional\[google.auth.credentials.Credentials\]     

The default custom credentials to use when making API calls. If not provided, credentials will be ascertained from the environment.

project: Optional\[str\]     

The default GCP project to use when making Vertex API calls.

location: str = “us-central1”     

The default location to use when making API calls.

request\_parallelism: int = 5     

The amount of parallelism allowed for requests issued to VertexAI models. \(default: `5`\)

base\_url: Optional\[str\]     

Base URL for API requests.

See full list of supported init args and their descriptions in the params section.

Instantiate:                    from langchain_google_vertexai import ChatVertexAI          llm = ChatVertexAI(         model="gemini-1.5-flash-001",         temperature=0,         max_tokens=None,         max_retries=6,         stop=None,         # other params...     )     

Invoke:                    messages = [         ("system", "You are a helpful translator. Translate the user sentence to French."),         ("human", "I love programming."),     ]     llm.invoke(messages)                    AIMessage(content="J'adore programmer. ", response_metadata={'is_blocked': False, 'safety_ratings': [{'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}], 'citation_metadata': None, 'usage_metadata': {'prompt_token_count': 17, 'candidates_token_count': 7, 'total_token_count': 24}}, id='run-925ce305-2268-44c4-875f-dde9128520ad-0')     

Stream:                    for chunk in llm.stream(messages):         print(chunk)                    AIMessageChunk(content='J', response_metadata={'is_blocked': False, 'safety_ratings': [], 'citation_metadata': None}, id='run-9df01d73-84d9-42db-9d6b-b1466a019e89')     AIMessageChunk(content="'adore programmer. ", response_metadata={'is_blocked': False, 'safety_ratings': [{'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}], 'citation_metadata': None}, id='run-9df01d73-84d9-42db-9d6b-b1466a019e89')     AIMessageChunk(content='', response_metadata={'is_blocked': False, 'safety_ratings': [], 'citation_metadata': None, 'usage_metadata': {'prompt_token_count': 17, 'candidates_token_count': 7, 'total_token_count': 24}}, id='run-9df01d73-84d9-42db-9d6b-b1466a019e89')                    stream = llm.stream(messages)     full = next(stream)     for chunk in stream:         full += chunk     full                    AIMessageChunk(content="J'adore programmer. ", response_metadata={'is_blocked': False, 'safety_ratings': [{'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}], 'citation_metadata': None, 'usage_metadata': {'prompt_token_count': 17, 'candidates_token_count': 7, 'total_token_count': 24}}, id='run-b7f7492c-4cb5-42d0-8fc3-dce9b293b0fb')     

Async:                    await llm.ainvoke(messages)          # stream:     # async for chunk in (await llm.astream(messages))          # batch:     # await llm.abatch([messages])                    AIMessage(content="J'adore programmer. ", response_metadata={'is_blocked': False, 'safety_ratings': [{'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability_label': 'NEGLIGIBLE', 'probability_score': 0.1, 'blocked': False, 'severity': 'HARM_SEVERITY_NEGLIGIBLE', 'severity_score': 0.1}], 'citation_metadata': None, 'usage_metadata': {'prompt_token_count': 17, 'candidates_token_count': 7, 'total_token_count': 24}}, id='run-925ce305-2268-44c4-875f-dde9128520ad-0')     

Context Caching:     

Context caching allows you to store and reuse content \(e.g., PDFs, images\) for faster processing. The `cached_content` parameter accepts a cache name created via the Google Generative AI API with Vertex AI. Below is an example of caching content from GCS and querying it.

Example: This caches content from GCS and queries it.               from google import genai     from google.genai.types import Content, CreateCachedContentConfig, HttpOptions, Part     from langchain_google_vertexai import ChatVertexAI     from langchain_core.messages import HumanMessage          client = genai.Client(http_options=HttpOptions(api_version="v1beta1"))          contents = [         Content(             role="user",             parts=[                 Part.from_uri(                     file_uri="gs://your-bucket/file1",                     mime_type="application/pdf",                 ),                 Part.from_uri(                     file_uri="gs://your-bucket/file2",                     mime_type="image/jpeg",                 ),             ],         )     ]          cache = client.caches.create(         model="gemini-1.5-flash-001",         config=CreateCachedContentConfig(             contents=contents,             system_instruction="You are an expert content analyzer.",             display_name="content-cache",             ttl="300s",         ),     )          llm = ChatVertexAI(         model_name="gemini-1.5-flash-001",         cached_content=cache.name,     )     message = HumanMessage(content="Provide a summary of the key information across the content.")     llm.invoke([message])     

Tool calling:                    from pydantic import BaseModel, Field          class GetWeather(BaseModel):         '''Get the current weather in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          class GetPopulation(BaseModel):         '''Get the current population in a given location'''              location: str = Field(..., description="The city and state, e.g. San Francisco, CA")          llm_with_tools = llm.bind_tools([GetWeather, GetPopulation])     ai_msg = llm_with_tools.invoke("Which city is hotter today and which is bigger: LA or NY?")     ai_msg.tool_calls                    [{'name': 'GetWeather',       'args': {'location': 'Los Angeles, CA'},       'id': '2a2401fa-40db-470d-83ce-4e52de910d9e'},      {'name': 'GetWeather',       'args': {'location': 'New York City, NY'},       'id': '96761deb-ab7f-4ef9-b4b4-6d44562fc46e'},      {'name': 'GetPopulation',       'args': {'location': 'Los Angeles, CA'},       'id': '9147d532-abee-43a2-adb5-12f164300484'},      {'name': 'GetPopulation',       'args': {'location': 'New York City, NY'},       'id': 'c43374ea-bde5-49ca-8487-5b83ebeea1e6'}]     

See `ChatVertexAI.bind_tools()` method for more.

Built-in search:                    from google.cloud.aiplatform_v1beta1.types import Tool as VertexTool     from langchain_google_vertexai import ChatVertexAI          llm = ChatVertexAI(model="gemini-2.0-flash-exp")     resp = llm.invoke(         "When is the next total solar eclipse in US?",         tools=[VertexTool(google_search={})],     )     

Built-in code execution:                    from google.cloud.aiplatform_v1beta1.types import Tool as VertexTool     from langchain_google_vertexai import ChatVertexAI          llm = ChatVertexAI(model="gemini-2.0-flash-exp")     resp = llm.invoke(         "What is 3^3?",         tools=[VertexTool(code_execution={})],     )     

Structured output:                    from typing import Optional          from pydantic import BaseModel, Field          class Joke(BaseModel):         '''Joke to tell user.'''              setup: str = Field(description="The setup of the joke")         punchline: str = Field(description="The punchline to the joke")         rating: Optional[int] = Field(default=None, description="How funny the joke is, from 1 to 10")          structured_llm = llm.with_structured_output(Joke)     structured_llm.invoke("Tell me a joke about cats")                    Joke(setup='What do you call a cat that loves to bowl?', punchline='An alley cat!', rating=None)     

See `ChatVertexAI.with_structured_output()` for more.

Image input:                    import base64     import httpx     from langchain_core.messages import HumanMessage          image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"     image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")     message = HumanMessage(         content=[             {"type": "text", "text": "describe the weather in this image"},             {                 "type": "image_url",                 "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},             },         ],     )     ai_msg = llm.invoke([message])     ai_msg.content                    'The weather in this image appears to be sunny and pleasant. The sky is a bright blue with scattered white clouds, suggesting a clear and mild day. The lush green grass indicates recent rainfall or sufficient moisture. The absence of strong shadows suggests that the sun is high in the sky, possibly late afternoon. Overall, the image conveys a sense of tranquility and warmth, characteristic of a beautiful summer day.'     

You can also point to GCS files which is faster / more efficient because bytes are transferred back and forth.               llm.invoke(         [             HumanMessage(                 [                     "What's in the image?",                     {                         "type": "media",                         "file_uri": "gs://cloud-samples-data/generative-ai/image/scones.jpg",                         "mime_type": "image/jpeg",                     },                 ]             )         ]     ).content                    'The image is of five blueberry scones arranged on a piece of baking paper. Here is a list of what is in the picture:* **Five blueberry scones:** They are scattered across the parchment paper, dusted with powdered sugar.  * **Two cups of coffee:**  Two white cups with saucers. One appears full, the other partially drunk. * **A bowl of blueberries:** A brown bowl is filled with fresh blueberries, placed near the scones.* **A spoon:**  A silver spoon with the words "Let's Jam" rests on the paper.* **Pink peonies:** Several pink peonies lie beside the scones, adding a touch of color.* **Baking paper:** The scones, cups, bowl, and spoon are arranged on a piece of white baking paper, splattered with purple.  The paper is crinkled and sits on a dark surface. The image has a rustic and delicious feel, suggesting a cozy and enjoyable breakfast or brunch setting.' # codespell:ignore brunch     

Video input:

> Note >  > Currently only supported for `gemini-...-vision` models. >      >      >     llm = ChatVertexAI(model="gemini-1.0-pro-vision") >      >     llm.invoke( >         [ >             HumanMessage( >                 [ >                     "What's in the video?", >                     { >                         "type": "media", >                         "file_uri": "gs://cloud-samples-data/video/animals.mp4", >                         "mime_type": "video/mp4", >                     }, >                 ] >             ) >         ] >     ).content >      >      >      >     'The video is about a new feature in Google Photos called "Zoomable Selfies". The feature allows users to take selfies with animals at the zoo. The video shows several examples of people taking selfies with animals, including a tiger, an elephant, and a sea otter. The video also shows how the feature works. Users simply need to open the Google Photos app and select the "Zoomable Selfies" option. Then, they need to choose an animal from the list of available animals. The app will then guide the user through the process of taking the selfie.' >     

Audio input:                    from langchain_core.messages import HumanMessage          llm = ChatVertexAI(model="gemini-1.5-flash-001")          llm.invoke(         [             HumanMessage(                 [                     "What's this audio about?",                     {                         "type": "media",                         "file_uri": "gs://cloud-samples-data/generative-ai/audio/pixel.mp3",                         "mime_type": "audio/mpeg",                     },                 ]             )         ]     ).content                    "This audio is an interview with two product managers from Google who work on Pixel feature drops. They discuss how feature drops are important for showcasing how Google devices are constantly improving and getting better. They also discuss some of the highlights of the January feature drop and the new features coming in the March drop for Pixel phones and Pixel watches. The interview concludes with discussion of how user feedback is extremely important to them in deciding which features to include in the feature drops. "     

Token usage:                    ai_msg = llm.invoke(messages)     ai_msg.usage_metadata                    {'input_tokens': 17, 'output_tokens': 7, 'total_tokens': 24}     

Logprobs:                    llm = ChatVertexAI(model="gemini-1.5-flash-001", logprobs=True)     ai_msg = llm.invoke(messages)     ai_msg.response_metadata["logprobs_result"]                    [         {'token': 'J', 'logprob': -1.549651415189146e-06, 'top_logprobs': []},         {'token': "'", 'logprob': -1.549651415189146e-06, 'top_logprobs': []},         {'token': 'adore', 'logprob': 0.0, 'top_logprobs': []},         {'token': ' programmer', 'logprob': -1.1922384146600962e-07, 'top_logprobs': []},         {'token': '.', 'logprob': -4.827636439586058e-05, 'top_logprobs': []},         {'token': ' ', 'logprob': -0.018011733889579773, 'top_logprobs': []},         {'token': '\n', 'logprob': -0.0008687592926435173, 'top_logprobs': []}     ]     

Response metadata                    ai_msg = llm.invoke(messages)     ai_msg.response_metadata                    {'is_blocked': False,      'safety_ratings': [{'category': 'HARM_CATEGORY_HATE_SPEECH',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1},       {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1},       {'category': 'HARM_CATEGORY_HARASSMENT',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1},       {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1}],      'usage_metadata': {'prompt_token_count': 17,       'candidates_token_count': 7,       'total_token_count': 24}}     

Safety settings                    from langchain_google_vertexai import HarmBlockThreshold, HarmCategory          llm = ChatVertexAI(         model="gemini-1.5-pro",         safety_settings={             HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,             HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,             HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,             HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,         },     )          llm.invoke(messages).response_metadata                    {'is_blocked': False,      'safety_ratings': [{'category': 'HARM_CATEGORY_HATE_SPEECH',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1},       {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1},       {'category': 'HARM_CATEGORY_HARASSMENT',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1},       {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',        'probability_label': 'NEGLIGIBLE',        'probability_score': 0.1,        'blocked': False,        'severity': 'HARM_SEVERITY_NEGLIGIBLE',        'severity_score': 0.1}],      'usage_metadata': {'prompt_token_count': 17,       'candidates_token_count': 7,       'total_token_count': 24}}     

Needed for mypy typing to recognize model\_name as a valid arg and for arg validation.

Note

ChatVertexAI implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

_param _additional\_headers _: Dict\[str, str\] | None_ _ = None_\#     

A key-value dictionary representing additional headers for the model call

_param _api\_endpoint _: str | None_ _ = None_ _\(alias 'base\_url'\)_\#     

Desired API endpoint, e.g., us-central1-aiplatform.googleapis.com

_param _api\_transport _: str | None_ _ = None_\#     

The desired API transport method, can be either ‘grpc’ or ‘rest’. Uses the default parameter in vertexai.init if defined.

_param _audio\_timestamp _: bool | None_ _ = None_\#     

Enable timestamp understanding of audio-only files

_param _cache _: [BaseCache](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") | bool | None_ _ = None_\#     

Whether to cache the response.

  * If true, will use the global cache.

  * If false, will not use a cache

  * If None, will use the global cache if it’s set, otherwise no cache.

  * If instance of BaseCache, will use the provided cache.

Caching is not currently supported for streaming methods of models.

_param _cached\_content _: str | None_ _ = None_\#     

Optional. Use the model in cache mode. Only supported in Gemini 1.5 and later models. Must be a string containing the cache name \(A sequence of numbers\)

_param _callback\_manager _: [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None_ _ = None_\#     

Deprecated since version 0.1.7: Use `callbacks()` instead. It will be removed in pydantic==1.0.

Callback manager to add to the run trace.

_param _callbacks _: Callbacks_ _ = None_\#     

Callbacks to add to the run trace.

_param _client\_cert\_source _: Callable\[\[\], Tuple\[bytes, bytes\]\] | None_ _ = None_\#     

A callback which returns client certificate bytes and private key bytes both

_param _credentials _: Any_ _ = None_\#     

The default custom credentials \(google.auth.credentials.Credentials\) to use

_param _custom\_get\_token\_ids _: Callable\[\[str\], list\[int\]\] | None_ _ = None_\#     

Optional encoder to use for counting tokens.

_param _disable\_streaming _: bool | Literal\['tool\_calling'\]__ = False_\#     

Whether to disable streaming for this model.

If streaming is bypassed, then `stream()`/`astream()`/`astream_events()` will defer to `invoke()`/`ainvoke()`.

  * If True, will always bypass streaming case.

  * If `'tool_calling'`, will bypass streaming case only when the model is called with a `tools` keyword argument. In other words, LangChain will automatically switch to non-streaming behavior \(`invoke()`\) only when the tools argument is provided. This offers the best of both worlds.

  * If False \(default\), will always use streaming case if available.

The main reason for this flag is that code might be written using `.stream()` and a user may want to swap out a given model for another model whose the implementation does not properly support streaming.

_param _endpoint\_version _: Literal\['v1', 'v1beta1'\]__ = 'v1beta1'_\#     

Whether to use v1 or v1beta1 endpoint.

v1 is more performant, but v1beta1 might have some new features.

_param _examples _: List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\] | None_ _ = None_\#     

_param _frequency\_penalty _: float | None_ _ = None_\#     

Positive values penalize tokens that repeatedly appear in the generated text,

_param _full\_model\_name _: str | None_ _ = None_\#     

The full name of the model’s endpoint.

_param _include\_thoughts _: bool | None_ _ = None_\#     

Indicates whether to include thoughts in the response.

_param _labels _: Dict\[str, str\] | None_ _ = None_\#     

Optional tag llm calls with metadata to help in tracebility and biling.

_param _location _: str_ _ = 'us-central1'_\#     

The default location to use when making API calls.

_param _logprobs _: bool | int_ _ = False_\#     

Whether to return logprobs as part of AIMessage.response\_metadata.

If False, don’t return logprobs. If True, return logprobs for top candidate. If int, return logprobs for top `logprobs` candidates.

Note

As of 2024-10-28 this is only supported for gemini-1.5-flash models.

_param _max\_output\_tokens _: int | None_ _ = None_ _\(alias 'max\_tokens'\)_\#     

Token limit determines the maximum amount of text output from one prompt.

_param _max\_retries _: int_ _ = 6_\#     

The maximum number of retries to make when generating.

_param _metadata _: dict\[str, Any\] | None_ _ = None_\#     

Metadata to add to the run trace.

_param _model\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Holds any unexpected initialization parameters.

_param _model\_name _: str_ _\[Required\]__\(alias 'model'\)_\#     

Underlying model name.

_param _n _: int_ _ = 1_\#     

How many completions to generate for each prompt.

_param _perform\_literal\_eval\_on\_string\_raw\_content _: bool_ _ = True_\#     

Whether to perform literal eval on string raw content.

_param _presence\_penalty _: float | None_ _ = None_\#     

Positive values penalize tokens that already appear in the generated text,

_param _project _: str | None_ _ = None_\#     

The default GCP project to use when making Vertex API calls.

_param _rate\_limiter _: [BaseRateLimiter](https://python.langchain.com/api_reference/core/rate_limiters/langchain_core.rate_limiters.BaseRateLimiter.html#langchain_core.rate_limiters.BaseRateLimiter "langchain_core.rate_limiters.BaseRateLimiter") | None_ _ = None_\#     

An optional rate limiter to use for limiting the number of requests.

_param _request\_parallelism _: int_ _ = 5_\#     

The amount of parallelism allowed for requests issued to VertexAI models.

_param _response\_mime\_type _: str | None_ _ = None_\#     

Optional. Output response mimetype of the generated candidate text. Only     

supported in Gemini 1.5 and later models. Supported mimetype:     

  * `'text/plain'`: \(default\) Text output.

  * `'application/json'`: JSON response in the candidates.

  * `'text/x.enum'`: Enum in plain text.

The model also needs to be prompted to output the appropriate response type, otherwise the behavior is undefined. This is a preview feature.

_param _response\_schema _: Dict\[str, Any\] | None_ _ = None_\#     

Optional. Enforce an schema to the output. The format of the dictionary should follow Open API schema.

_param _safety\_settings _: 'SafetySettingsType' | None_ _ = None_\#     

The default safety settings to use for all generations.

For example:

> from langchain\_google\_vertexai import HarmBlockThreshold, HarmCategory >  > safety\_settings = \{ >      >  > HarmCategory.HARM\_CATEGORY\_UNSPECIFIED: HarmBlockThreshold.BLOCK\_NONE, HarmCategory.HARM\_CATEGORY\_DANGEROUS\_CONTENT: HarmBlockThreshold.BLOCK\_MEDIUM\_AND\_ABOVE, HarmCategory.HARM\_CATEGORY\_HATE\_SPEECH: HarmBlockThreshold.BLOCK\_ONLY\_HIGH, HarmCategory.HARM\_CATEGORY\_HARASSMENT: HarmBlockThreshold.BLOCK\_LOW\_AND\_ABOVE, HarmCategory.HARM\_CATEGORY\_SEXUALLY\_EXPLICIT: HarmBlockThreshold.BLOCK\_NONE, >  > \}

_param _seed _: int | None_ _ = None_\#     

Random seed for the generation.

_param _stop _: List\[str\] | None_ _ = None_ _\(alias 'stop\_sequences'\)_\#     

Optional list of stop words to use when generating.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results or not.

_param _tags _: list\[str\] | None_ _ = None_\#     

Tags to add to the run trace.

_param _temperature _: float | None_ _ = None_\#     

Sampling temperature, it controls the degree of randomness in token selection.

_param _thinking\_budget _: int | None_ _ = None_\#     

Indicates the thinking budget in tokens.

_param _top\_k _: int | None_ _ = None_\#     

How the model selects tokens for output, the next token is selected from

_param _top\_p _: float | None_ _ = None_\#     

Tokens are selected from most probable to least until the sum of their

_param _tuned\_model\_name _: str | None_ _ = None_\#     

The name of a tuned model.

_param _verbose _: bool_ _\[Optional\]_\#     

Whether to print out response text.

_param _wait\_exponential\_kwargs _: dict\[str, float\] | None_ _ = None_\#     

Optional dictionary with parameters for wait\_exponential: \- multiplier: Initial wait time multiplier \(default: `1.0`\) \- min: Minimum wait time in seconds \(default: `4.0`\) \- max: Maximum wait time in seconds \(default: `10.0`\) \- exp\_base: Exponent base to use \(default: `2.0`\)

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

    _tools : Sequence\[Tool | Tool | \_ToolDictLike | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") | Type\[BaseModel\] | [FunctionDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription") | Callable | FunctionDeclaration | Dict\[str, Any\]\]_,     _tool\_config : \_ToolConfigDict | None = None_,     _\*_ ,     _tool\_choice : dict | List\[str\] | str | Literal\['auto', 'none', 'any'\] | Literal\[True\] | bool | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/chat_models.html#ChatVertexAI.bind_tools)\#     

Bind tool-like objects to this chat model.

Assumes model is compatible with Vertex tool-calling API.

Parameters:     

  * **tools** \(_Sequence_ _\[__Tool_ _|__Tool_ _|__\_ToolDictLike_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _|__Type_ _\[__BaseModel_ _\]__|_[_FunctionDescription_](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription") _|__Callable_ _|__FunctionDeclaration_ _|__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – A list of tool definitions to bind to this chat model. Can be a pydantic model, callable, or BaseTool. Pydantic models, callables, and BaseTools will be automatically converted to their schema dictionary representation. Tools with Union types in their arguments are now supported and converted to anyOf schemas.

  * **\*\*kwargs** \(_Any_\) – Any additional parameters to pass to the `Runnable` constructor.

  * **tool\_config** \(_\_ToolConfigDict_ _|__None_\)

  * **tool\_choice** \(_dict_ _|__List_ _\[__str_ _\]__|__str_ _|__Literal_ _\[__'auto'__,__'none'__,__'any'__\]__|__~typing.Literal_ _\[__True_ _\]__|__bool_ _|__None_\)

  * **\*\*kwargs**

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

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

get\_num\_tokens\(_text : str_\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/chat_models.html#ChatVertexAI.get_num_tokens)\#     

Get the number of tokens present in the text.

[More info](https://cloud.google.com/vertex-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#counttokensrequest)

Parameters:     

**text** \(_str_\)

Return type:     

int

get\_num\_tokens\_from\_messages\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _tools : Sequence | None = None_, \) → int\#     

Get the number of tokens in the messages.

Useful for checking if an input fits in a model’s context window.

**Note** : the base implementation of get\_num\_tokens\_from\_messages ignores tool schemas.

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – The message inputs to tokenize.

  * **tools** \(_Sequence_ _|__None_\) – If provided, sequence of dict, BaseModel, function, or BaseTools to be converted to tool schemas.

Returns:     

The sum of the number of tokens across the messages.

Return type:     

int

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

    _schema : Dict | Type\[BaseModel\] | Type_,     _\*_ ,     _include\_raw : bool = False_,     _method : Literal\['json\_mode'\] | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], Dict | BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/chat_models.html#ChatVertexAI.with_structured_output)\#     

Model wrapper that returns outputs formatted to match the given schema.

Changed in version 1.1.0: Return type corrected in version 1.1.0. Previously if a dict schema was provided then the output had the form `[{"args": {}, "name": "schema_name"}]` where the output was a list with a single dict and the “args” of the one dict corresponded to the schema. As of `1.1.0` this has been fixed so that the schema \(the value corresponding to the old “args” key\) is returned directly.

Parameters:     

  * **schema** \(_Dict_ _|__Type_ _\[__BaseModel_ _\]__|__Type_\) – The output schema as a dict or a Pydantic class. If a Pydantic class then the model output will be an object of that class. If a dict then the model output will be a dict. With a Pydantic class the returned attributes will be validated, whereas with a dict they will not be. If `method` is `'function_calling'` and `schema` is a dict, then the dict must match the OpenAI function-calling spec.

  * **include\_raw** \(_bool_\) – If False then only the parsed structured output is returned. If an error occurs during model output parsing it will be raised. If True then both the raw model response \(a BaseMessage\) and the parsed model response will be returned. If an error occurs during output parsing it will be caught and returned as well. The final output is always a dict with keys `'raw'`, `'parsed'`, and `'parsing_error'`.

  * **method** \(_Literal_ _\[__'json\_mode'__\]__|__None_\) – If set to `'json_schema'` it will use controlled genetration to generate the response rather than function calling. Does not work with schemas with references or Pydantic models with self-references.

  * **kwargs** \(_Any_\)

Returns:     

A Runnable that takes any ChatModel input. If `'include_raw'` is True then a dict with keys — raw: BaseMessage, parsed: Optional\[\_DictOrPydantic\], parsing\_error: Optional\[BaseException\]. If `'include_raw'` is False then just `_DictOrPydantic` is returned, where `_DictOrPydantic` depends on the schema. If schema is a Pydantic class then `_DictOrPydantic` is the Pydantic class. If schema is a dict then `_DictOrPydantic` is a dict.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], _Dict_ | _BaseModel_\]

Example: Pydantic schema, exclude raw:                    from pydantic import BaseModel     from langchain_google_vertexai import ChatVertexAI          class AnswerWithJustification(BaseModel):         '''An answer to the user question along with justification for the answer.'''         answer: str         justification: str          llm = ChatVertexAI(model_name="gemini-2.0-flash-001", temperature=0)     structured_llm = llm.with_structured_output(AnswerWithJustification)          structured_llm.invoke("What weighs more a pound of bricks or a pound of feathers")     # -> AnswerWithJustification(     #     answer='They weigh the same.', justification='A pound is a pound.'     # )     

Example: Pydantic schema, include raw:                    from pydantic import BaseModel     from langchain_google_vertexai import ChatVertexAI          class AnswerWithJustification(BaseModel):         '''An answer to the user question along with justification for the answer.'''         answer: str         justification: str          llm = ChatVertexAI(model_name="gemini-2.0-flash-001", temperature=0)     structured_llm = llm.with_structured_output(AnswerWithJustification, include_raw=True)          structured_llm.invoke("What weighs more a pound of bricks or a pound of feathers")     # -> {     #     'raw': AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_Ao02pnFYXD6GN1yzc0uXPsvF', 'function': {'arguments': '{"answer":"They weigh the same.","justification":"Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ."}', 'name': 'AnswerWithJustification'}, 'type': 'function'}]}),     #     'parsed': AnswerWithJustification(answer='They weigh the same.', justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'),     #     'parsing_error': None     # }     

Example: Dict schema, exclude raw:                    from pydantic import BaseModel     from langchain_core.utils.function_calling import convert_to_openai_function     from langchain_google_vertexai import ChatVertexAI          class AnswerWithJustification(BaseModel):         '''An answer to the user question along with justification for the answer.'''         answer: str         justification: str          dict_schema = convert_to_openai_function(AnswerWithJustification)     llm = ChatVertexAI(model_name="gemini-2.0-flash-001", temperature=0)     structured_llm = llm.with_structured_output(dict_schema)          structured_llm.invoke("What weighs more a pound of bricks or a pound of feathers")     # -> {     #     'answer': 'They weigh the same',     #     'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.'     # }     

Example: Pydantic schema, streaming:                    from pydantic import BaseModel, Field     from langchain_google_vertexai import ChatVertexAI          class Explanation(BaseModel):         '''A topic explanation with examples.'''         description: str = Field(description="A brief description of the topic.")         examples: str = Field(description="Two examples related to the topic.")          llm = ChatVertexAI(model_name="gemini-2.0-flash", temperature=0)     structured_llm = llm.with_structured_output(Explanation, method="json_mode")          for chunk in structured_llm.stream("Tell me about transformer models"):         print(chunk)         print('-------------------------')     # -> description='Transformer models are a type of neural network architecture that have revolutionized the field of natural language processing (NLP) and are also increasingly used in computer vision and other domains. They rely on the self-attention mechanism to weigh the importance of different parts of the input data, allowing them to effectively capture long-range dependencies. Unlike recurrent neural networks (RNNs), transformers can process the entire input sequence in parallel, leading to significantly faster training times. Key components of transformer models include: the self-attention mechanism (calculates attention weights between different parts of the input), multi-head attention (performs self-attention multiple times with different learned parameters), positional encoding (adds information about the position of tokens in the input sequence), feedforward networks (applies a non-linear transformation to each position), and encoder-decoder structure (used for sequence-to-sequence tasks).' examples='1. BERT (Bidirectional Encoder Representations from Transformers): A pre-trained transformer'     #    -------------------------     #    description='Transformer models are a type of neural network architecture that have revolutionized the field of natural language processing (NLP) and are also increasingly used in computer vision and other domains. They rely on the self-attention mechanism to weigh the importance of different parts of the input data, allowing them to effectively capture long-range dependencies. Unlike recurrent neural networks (RNNs), transformers can process the entire input sequence in parallel, leading to significantly faster training times. Key components of transformer models include: the self-attention mechanism (calculates attention weights between different parts of the input), multi-head attention (performs self-attention multiple times with different learned parameters), positional encoding (adds information about the position of tokens in the input sequence), feedforward networks (applies a non-linear transformation to each position), and encoder-decoder structure (used for sequence-to-sequence tasks).' examples='1. BERT (Bidirectional Encoder Representations from Transformers): A pre-trained transformer model that can be fine-tuned for various NLP tasks like text classification, question answering, and named entity recognition. 2. GPT (Generative Pre-trained Transformer): A language model that uses transformers to generate coherent and contextually relevant text. GPT models are used in chatbots, content creation, and code generation.'     #    -------------------------     

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

_property _async\_prediction\_client _: PredictionServiceAsyncClient | PredictionServiceAsyncClient_\#     

Returns PredictionServiceClient.

_property _max\_tokens _: int | None_\#     

_property _prediction\_client _: PredictionServiceClient | PredictionServiceClient_\#     

Returns PredictionServiceClient.

task\_executor _: ClassVar\[Executor | None\]__ = FieldInfo\(annotation=NoneType, required=False, default=None, exclude=True\)_\#     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)