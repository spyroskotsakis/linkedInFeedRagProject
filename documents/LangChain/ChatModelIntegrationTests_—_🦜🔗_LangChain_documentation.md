# ChatModelIntegrationTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.chat_models.ChatModelIntegrationTests.html
**Word Count:** 4196
**Links Count:** 326
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# ChatModelIntegrationTests\#

_class _langchain\_tests.integration\_tests.chat\_models.ChatModelIntegrationTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests)\#     

Base class for chat model integration tests.

Test subclasses must implement the `chat_model_class` and `chat_model_params` properties to specify what model to test and its initialization parameters.

Example:               from typing import Type          from langchain_tests.integration_tests import ChatModelIntegrationTests     from my_package.chat_models import MyChatModel               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def chat_model_class(self) -> Type[MyChatModel]:             # Return the chat model class to test here             return MyChatModel              @property         def chat_model_params(self) -> dict:             # Return initialization parameters for the model.             return {"model": "model-001", "temperature": 0}     

Note

API references for individual test methods include troubleshooting tips.

Test subclasses must implement the following two properties:

chat\_model\_class     

The chat model class to test, e.g., `ChatParrotLink`.

Example:               @property     def chat_model_class(self) -> Type[ChatParrotLink]:         return ChatParrotLink     

chat\_model\_params     

Initialization parameters for the chat model.

Example:               @property     def chat_model_params(self) -> dict:         return {"model": "bird-brain-001", "temperature": 0}     

In addition, test subclasses can control what features are tested \(such as tool calling or multi-modality\) by selectively overriding the following properties. Expand to see details:

has\_tool\_calling

Boolean property indicating whether the chat model supports tool calling.

By default, this is determined by whether the chat model’s bind\_tools method is overridden. It typically does not need to be overridden on the test class.

Example override:               @property     def has_tool_calling(self) -> bool:         return True     

tool\_choice\_value

Value to use for tool choice when used in tests.

Warning

Deprecated since version 0.3.15: This property will be removed in version 0.3.20. If a model supports `tool_choice`, it should accept `tool_choice="any"` and `tool_choice=<string name of tool>`. If a model does not support forcing tool calling, override the `has_tool_choice` property to return `False`.

Example:               @property     def tool_choice_value(self) -> Optional[str]:         return "any"     

has\_tool\_choice

Boolean property indicating whether the chat model supports forcing tool calling via a `tool_choice` parameter.

By default, this is determined by whether the parameter is included in the signature for the corresponding `bind_tools` method.

If `True`, the minimum requirement for this feature is that `tool_choice="any"` will force a tool call, and `tool_choice=<tool name>` will force a call to a specific tool.

Example override:               @property     def has_tool_choice(self) -> bool:         return False     

has\_structured\_output

Boolean property indicating whether the chat model supports structured output.

By default, this is determined by whether the chat model’s `with_structured_output` method is overridden. If the base implementation is intended to be used, this method should be overridden.

See: <https://python.langchain.com/docs/concepts/structured_outputs/>

Example:               @property     def has_structured_output(self) -> bool:         return True     

structured\_output\_kwargs

Dict property that can be used to specify additional kwargs for `with_structured_output`. Useful for testing different models.

Example:               @property     def structured_output_kwargs(self) -> dict:         return {"method": "function_calling"}     

supports\_json\_mode

Boolean property indicating whether the chat model supports JSON mode in `with_structured_output`.

See: <https://python.langchain.com/docs/concepts/structured_outputs/#json-mode>

Example:               @property     def supports_json_mode(self) -> bool:         return True     

supports\_image\_inputs

Boolean property indicating whether the chat model supports image inputs. Defaults to `False`.

If set to `True`, the chat model will be tested using content blocks of the form               {         "type": "image",         "source_type": "base64",         "data": "<base64 image data>",         "mime_type": "image/jpeg",  # or appropriate mime-type     }     

In addition to OpenAI-style content blocks:               {         "type": "image_url",         "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},     }     

See <https://python.langchain.com/docs/concepts/multimodality/>

Example:               @property     def supports_image_inputs(self) -> bool:         return True     

supports\_image\_urls

Boolean property indicating whether the chat model supports image inputs from URLs. Defaults to `False`.

If set to `True`, the chat model will be tested using content blocks of the form               {         "type": "image",         "source_type": "url",         "url": "https://...",     }     

See <https://python.langchain.com/docs/concepts/multimodality/>

Example:               @property     def supports_image_urls(self) -> bool:         return True     

supports\_pdf\_inputs

Boolean property indicating whether the chat model supports PDF inputs. Defaults to `False`.

If set to `True`, the chat model will be tested using content blocks of the form               {         "type": "file",         "source_type": "base64",         "data": "<base64 file data>",         "mime_type": "application/pdf",     }     

See <https://python.langchain.com/docs/concepts/multimodality/>

Example:               @property     def supports_pdf_inputs(self) -> bool:         return True     

supports\_audio\_inputs

Boolean property indicating whether the chat model supports audio inputs. Defaults to `False`.

If set to `True`, the chat model will be tested using content blocks of the form               {         "type": "audio",         "source_type": "base64",         "data": "<base64 audio data>",         "mime_type": "audio/wav",  # or appropriate mime-type     }     

See <https://python.langchain.com/docs/concepts/multimodality/>

Example:               @property     def supports_audio_inputs(self) -> bool:         return True     

supports\_video\_inputs

Boolean property indicating whether the chat model supports image inputs. Defaults to `False`. No current tests are written for this feature.

returns\_usage\_metadata

Boolean property indicating whether the chat model returns usage metadata on invoke and streaming responses.

`usage_metadata` is an optional dict attribute on AIMessages that track input and output tokens: <https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html>

Example:               @property     def returns_usage_metadata(self) -> bool:         return False     

Models supporting `usage_metadata` should also return the name of the underlying model in the `response_metadata` of the AIMessage.

supports\_anthropic\_inputs

Boolean property indicating whether the chat model supports Anthropic-style inputs.

These inputs might feature “tool use” and “tool result” content blocks, e.g.,               [         {"type": "text", "text": "Hmm let me think about that"},         {             "type": "tool_use",             "input": {"fav_color": "green"},             "id": "foo",             "name": "color_picker",         },     ]     

If set to `True`, the chat model will be tested using content blocks of this form.

Example:               @property     def supports_anthropic_inputs(self) -> bool:         return False     

supports\_image\_tool\_message

Boolean property indicating whether the chat model supports ToolMessages that include image content, e.g.,               ToolMessage(         content=[             {                 "type": "image_url",                 "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},             },         ],         tool_call_id="1",         name="random_image",     )     

\(OpenAI Chat Completions format\), as well as               ToolMessage(         content=[             {                 "type": "image",                 "source_type": "base64",                 "data": image_data,                 "mime_type": "image/jpeg",             },         ],         tool_call_id="1",         name="random_image",     )     

\(standard format\).

If set to `True`, the chat model will be tested with message sequences that include ToolMessages of this form.

Example:               @property     def supports_image_tool_message(self) -> bool:         return False     

supported\_usage\_metadata\_details

Property controlling what usage metadata details are emitted in both invoke and stream.

`usage_metadata` is an optional dict attribute on AIMessages that track input and output tokens: <https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html>

It includes optional keys `input_token_details` and `output_token_details` that can track usage details associated with special types of tokens, such as cached, audio, or reasoning.

Only needs to be overridden if these details are supplied.

enable\_vcr\_tests

Property controlling whether to enable select tests that rely on [VCR](https://vcrpy.readthedocs.io/en/latest/) caching of HTTP calls, such as benchmarking tests.

To enable these tests, follow these steps:

  1. Override the `enable_vcr_tests` property to return `True`:

> @property >          def enable_vcr_tests(self) -> bool: >              return True >          

  2. Configure VCR to exclude sensitive headers and other information from cassettes.

> Important >  > VCR will by default record authentication headers and other sensitive information in cassettes. Read below for how to configure what information is recorded in cassettes. >  > To add configuration to VCR, add a `conftest.py` file to the `tests/` directory and implement the `vcr_config` fixture there. >  > `langchain-tests` excludes the headers `"authorization"`, `"x-api-key"`, and `"api-key"` from VCR cassettes. To pick up this configuration, you will need to add `conftest.py` as shown below. You can also exclude additional headers, override the default exclusions, or apply other customizations to the VCR configuration. See example below: >  > tests/conftest.py\# >           >          import pytest >          from langchain_tests.conftest import _base_vcr_config as _base_vcr_config >           >          _EXTRA_HEADERS = [ >              # Specify additional headers to redact >              ("user-agent", "PLACEHOLDER"), >          ] >           >           >          def remove_response_headers(response: dict) -> dict: >              # If desired, remove or modify headers in the response. >              response["headers"] = {} >              return response >           >           >          @pytest.fixture(scope="session") >          def vcr_config(_base_vcr_config: dict) -> dict:  # noqa: F811 >              """Extend the default configuration from langchain_tests.""" >              config = _base_vcr_config.copy() >              config.setdefault("filter_headers", []).extend(_EXTRA_HEADERS) >              config["before_record_response"] = remove_response_headers >           >              return config >           >  > Compressing cassettes >  > `langchain-tests` includes a custom VCR serializer that compresses cassettes using gzip. To use it, register the `"yaml.gz"` serializer to your VCR fixture and enable this serializer in the config. See example below: >  > tests/conftest.py\# >           >          import pytest >          from langchain_tests.conftest import CustomPersister, CustomSerializer >          from langchain_tests.conftest import _base_vcr_config as _base_vcr_config >          from vcr import VCR >           >          _EXTRA_HEADERS = [ >              # Specify additional headers to redact >              ("user-agent", "PLACEHOLDER"), >          ] >           >           >          def remove_response_headers(response: dict) -> dict: >              # If desired, remove or modify headers in the response. >              response["headers"] = {} >              return response >           >           >          @pytest.fixture(scope="session") >          def vcr_config(_base_vcr_config: dict) -> dict:  # noqa: F811 >              """Extend the default configuration from langchain_tests.""" >              config = _base_vcr_config.copy() >              config.setdefault("filter_headers", []).extend(_EXTRA_HEADERS) >              config["before_record_response"] = remove_response_headers >              # New: enable serializer and set file extension >              config["serializer"] = "yaml.gz" >              config["path_transformer"] = VCR.ensure_suffix(".yaml.gz") >           >              return config >           >           >          def pytest_recording_configure(config: dict, vcr: VCR) -> None: >              vcr.register_persister(CustomPersister()) >              vcr.register_serializer("yaml.gz", CustomSerializer()) >           >  > You can inspect the contents of the compressed cassettes \(e.g., to ensure no sensitive information is recorded\) using >           >          gunzip -k /path/to/tests/cassettes/TestClass_test.yaml.gz >           >  > or by using the serializer: >           >          from langchain_tests.conftest import CustomPersister, CustomSerializer >           >          cassette_path = "/path/to/tests/cassettes/TestClass_test.yaml.gz" >          requests, responses = CustomPersister().load_cassette(path, CustomSerializer()) >          

  3. Run tests to generate VCR cassettes.

> Example: >           >          uv run python -m pytest tests/integration_tests/test_chat_models.py::TestMyModel::test_stream_time >           >  > This will generate a VCR cassette for the test in `tests/integration_tests/cassettes/`. >  > Important >  > You should inspect the generated cassette to ensure that it does not contain sensitive information. If it does, you can modify the `vcr_config` fixture to exclude headers or modify the response before it is recorded. >  > You can then commit the cassette to your repository. Subsequent test runs will use the cassette instead of making HTTP calls.

Attributes

`chat_model_class` | The chat model class to test, e.g., `ChatParrotLink`.   ---|---   `chat_model_params` | Initialization parameters for the chat model.   `enable_vcr_tests` | \(bool\) whether to enable VCR tests for the chat model.   `has_structured_output` | \(bool\) whether the chat model supports structured output.   `has_tool_calling` | \(bool\) whether the model supports tool calling.   `has_tool_choice` | \(bool\) whether the model supports tool calling.   `returns_usage_metadata` | \(bool\) whether the chat model returns usage metadata on invoke and streaming responses.   `structured_output_kwargs` | If specified, additional kwargs for with\_structured\_output.   `supported_usage_metadata_details` | \(dict\) what usage metadata details are emitted in invoke and stream.   `supports_anthropic_inputs` | \(bool\) whether the chat model supports Anthropic-style inputs.   `supports_audio_inputs` | \(bool\) whether the chat model supports audio inputs, defaults to `False`.   `supports_image_inputs` | \(bool\) whether the chat model supports image inputs, defaults to `False`.   `supports_image_tool_message` | \(bool\) whether the chat model supports ToolMessages that include image content.   `supports_image_urls` | \(bool\) whether the chat model supports image inputs from URLs, defaults to `False`.   `supports_json_mode` | \(bool\) whether the chat model supports JSON mode.   `supports_pdf_inputs` | \(bool\) whether the chat model supports PDF inputs, defaults to `False`.   `supports_video_inputs` | \(bool\) whether the chat model supports video inputs, defaults to `False`.   `tool_choice_value` | \(None or str\) to use for tool choice when used in tests.      Methods

`test_abatch`\(model\) | Test to verify that await model.abatch\(\[messages\]\) works.   ---|---   `test_agent_loop`\(model\) | Test that the model supports a simple ReAct agent loop.   `test_ainvoke`\(model\) | Test to verify that await model.ainvoke\(simple\_message\) works.   `test_anthropic_inputs`\(model\) | Test that model can process Anthropic-style message histories.   `test_astream`\(model\) | Test to verify that await model.astream\(simple\_message\) works.   `test_audio_inputs`\(model\) | Test that the model can process audio inputs.   `test_batch`\(model\) | Test to verify that model.batch\(\[messages\]\) works.   `test_bind_runnables_as_tools`\(model\) | Test that the model generates tool calls for tools that are derived from LangChain runnables.   `test_conversation`\(model\) | Test to verify that the model can handle multi-turn conversations.   `test_double_messages_conversation`\(model\) | Test to verify that the model can handle double-message conversations.   `test_image_inputs`\(model\) | Test that the model can process image inputs.   `test_image_tool_message`\(model\) | Test that the model can process ToolMessages with image inputs.   `test_invoke`\(model\) | Test to verify that model.invoke\(simple\_message\) works.   `test_json_mode`\(model\) | Test structured output via \`JSON mode.   `test_message_with_name`\(model\) | Test that HumanMessage with values for the `name` field can be handled.   `test_pdf_inputs`\(model\) | Test that the model can process PDF inputs.   `test_stop_sequence`\(model\) | Test that model does not fail when invoked with the `stop` parameter, which is a standard parameter for stopping generation at a certain token.   `test_stream`\(model\) | Test to verify that model.stream\(simple\_message\) works.   `test_stream_time`\(model, benchmark, vcr\) | Test that streaming does not introduce undue overhead.   `test_structured_few_shot_examples`\(model, ...\) | Test that the model can process few-shot examples with tool calls.   `test_structured_output`\(model, schema\_type\) | Test to verify structured output is generated both on invoke and stream.   `test_structured_output_async`\(model, schema\_type\) | Test to verify structured output is generated both on invoke and stream.   `test_structured_output_optional_param`\(model\) | Test to verify we can generate structured output that includes optional parameters.   `test_structured_output_pydantic_2_v1`\(model\) | Test to verify we can generate structured output using pydantic.v1.BaseModel.   `test_tool_calling`\(model\) | Test that the model generates tool calls.   `test_tool_calling_async`\(model\) | Test that the model generates tool calls.   `test_tool_calling_with_no_arguments`\(model\) | Test that the model generates tool calls for tools with no arguments.   `test_tool_choice`\(model\) | Test that the model can force tool calling via the `tool_choice` parameter.   `test_tool_message_error_status`\(model, ...\) | Test that ToolMessage with `status="error"` can be handled.   `test_tool_message_histories_list_content`\(...\) | Test that message histories are compatible with list tool contents \(e.g. Anthropic format\).   `test_tool_message_histories_string_content`\(...\) | Test that message histories are compatible with string tool contents \(e.g. OpenAI format\).   `test_usage_metadata`\(model\) | Test to verify that the model returns correct usage metadata.   `test_usage_metadata_streaming`\(model\) | Test usage metadata in streaming mode.      _async _test\_abatch\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_abatch)\#     

Test to verify that await model.abatch\(\[messages\]\) works.

This should pass for all integrations. Tests the model’s ability to process multiple prompts in a single batch asynchronously.

Troubleshooting

First, debug `test_batch()` and `test_ainvoke()` because abatch has a default implementation that calls ainvoke for each message in the batch.

If those tests pass but not this one, you should make sure your abatch method does not raise any exceptions, and that it returns a list of valid `AIMessage` objects.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_agent\_loop\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_agent_loop)\#     

Test that the model supports a simple ReAct agent loop. This test is skipped if the `has_tool_calling` property on the test class is set to False.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that `bind_tools` is implemented to correctly translate LangChain tool objects into the appropriate schema for your chat model.

Check also that all required information \(e.g., tool calling identifiers\) from AIMessage objects is propagated correctly to model payloads.

This test may fail if the chat model does not consistently generate tool calls in response to an appropriate query. In these cases you can `xfail` the test:               @pytest.mark.xfail(reason=("Does not support tool_choice."))     def test_agent_loop(self, model: BaseChatModel) -> None:         super().test_agent_loop(model)     

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

_async _test\_ainvoke\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_ainvoke)\#     

Test to verify that await model.ainvoke\(simple\_message\) works.

This should pass for all integrations. Passing this test does not indicate a “natively async” implementation, but rather that the model can be used in an async context.

Troubleshooting

First, debug `test_invoke()`. because ainvoke has a default implementation that calls invoke in an async context.

If that test passes but not this one, you should make sure your \_agenerate method does not raise any exceptions, and that it returns a valid [`ChatResult`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_result.ChatResult.html#langchain_core.outputs.chat_result.ChatResult "langchain_core.outputs.chat_result.ChatResult") like so:               return ChatResult(         generations=[ChatGeneration(             message=AIMessage(content="Output text")         )]     )     

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_anthropic\_inputs\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_anthropic_inputs)\#     

Test that model can process Anthropic-style message histories.

These message histories will include `AIMessage` objects with `tool_use` content blocks, e.g.,               AIMessage(         [             {"type": "text", "text": "Hmm let me think about that"},             {                 "type": "tool_use",                 "input": {"fav_color": "green"},                 "id": "foo",                 "name": "color_picker",             },         ]     )     

as well as `HumanMessage` objects containing `tool_result` content blocks:               HumanMessage(         [             {                 "type": "tool_result",                 "tool_use_id": "foo",                 "content": [                     {                         "type": "text",                         "text": "green is a great pick! that's my sister's favorite color",  # noqa: E501                     }                 ],                 "is_error": False,             },             {"type": "text", "text": "what's my sister's favorite color"},         ]     )     

This test should be skipped if the model does not support messages of this form \(or doesn’t support tool calling generally\). See Configuration below.

Configuration

To disable this test, set `supports_anthropic_inputs` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def supports_anthropic_inputs(self) -> bool:             return False     

Troubleshooting

If this test fails, check that:

  1. The model can correctly handle message histories that include message objects with list content.

  2. The `tool_calls` attribute on AIMessage objects is correctly handled and passed to the model in an appropriate format.

  3. HumanMessages with “tool\_result” content blocks are correctly handled.

Otherwise, if Anthropic tool call and result formats are not supported, set the `supports_anthropic_inputs` property to False.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

_async _test\_astream\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_astream)\#     

Test to verify that await model.astream\(simple\_message\) works.

This should pass for all integrations. Passing this test does not indicate a “natively async” or “streaming” implementation, but rather that the model can be used in an async streaming context.

Troubleshooting

First, debug `test_stream()`. and `test_ainvoke()`. because astream has a default implementation that calls \_stream in an async context if it is implemented, or ainvoke and yields the result as a single chunk if not.

If those tests pass but not this one, you should make sure your \_astream method does not raise any exceptions, and that it yields valid [`ChatGenerationChunk`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") objects like so:               yield ChatGenerationChunk(         message=AIMessageChunk(content="chunk text")     )     

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_audio\_inputs\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_audio_inputs)\#     

Test that the model can process audio inputs.

This test should be skipped \(see Configuration below\) if the model does not support audio inputs. These will take the form:               {         "type": "audio",         "source_type": "base64",         "data": "<base64 audio data>",         "mime_type": "audio/wav",  # or appropriate mime-type     }     

See <https://python.langchain.com/docs/concepts/multimodality/>

Configuration

To disable this test, set `supports_audio_inputs` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):              @property         def supports_audio_inputs(self) -> bool:             return False     

Troubleshooting

If this test fails, check that the model can correctly handle messages with audio content blocks, specifically base64-encoded files. Otherwise, set the `supports_audio_inputs` property to False.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_batch\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_batch)\#     

Test to verify that model.batch\(\[messages\]\) works.

This should pass for all integrations. Tests the model’s ability to process multiple prompts in a single batch.

Troubleshooting

First, debug `test_invoke()` because batch has a default implementation that calls invoke for each message in the batch.

If that test passes but not this one, you should make sure your batch method does not raise any exceptions, and that it returns a list of valid `AIMessage` objects.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_bind\_runnables\_as\_tools\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_bind_runnables_as_tools)\#     

Test that the model generates tool calls for tools that are derived from LangChain runnables. This test is skipped if the `has_tool_calling` property on the test class is set to False.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that `bind_tools` is implemented to correctly translate LangChain tool objects into the appropriate schema for your chat model.

This test may fail if the chat model does not support a `tool_choice` parameter. This parameter can be used to force a tool call. If `tool_choice` is not supported and the model consistently fails this test, you can `xfail` the test:               @pytest.mark.xfail(reason=("Does not support tool_choice."))     def test_bind_runnables_as_tools(self, model: BaseChatModel) -> None:         super().test_bind_runnables_as_tools(model)     

Otherwise, ensure that the `tool_choice_value` property is correctly specified on the test class.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_conversation\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_conversation)\#     

Test to verify that the model can handle multi-turn conversations.

This should pass for all integrations. Tests the model’s ability to process a sequence of alternating human and AI messages as context for generating the next response.

Troubleshooting

First, debug `test_invoke()` because this test also uses model.invoke\(\).

If that test passes but not this one, you should verify that: 1\. Your model correctly processes the message history 2\. The model maintains appropriate context from previous messages 3\. The response is a valid `AIMessage`

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_double\_messages\_conversation\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_double_messages_conversation)\#     

Test to verify that the model can handle double-message conversations.

This should pass for all integrations. Tests the model’s ability to process a sequence of double-system, double-human, and double-ai messages as context for generating the next response.

Troubleshooting

First, debug `test_invoke()` because this test also uses model.invoke\(\).

Second, debug `test_conversation()` because this test is the “basic case” without double messages.

If that test passes those but not this one, you should verify that: 1\. Your model API can handle double messages, or the integration should

> merge messages before sending them to the API.

  2. The response is a valid `AIMessage`

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_image\_inputs\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_image_inputs)\#     

Test that the model can process image inputs.

This test should be skipped \(see Configuration below\) if the model does not support image inputs. These will take the form:               {         "type": "image",         "source_type": "base64",         "data": "<base64 image data>",         "mime_type": "image/jpeg",  # or appropriate mime-type     }     

For backward-compatibility, we must also support OpenAI-style image content blocks:               [         {"type": "text", "text": "describe the weather in this image"},         {             "type": "image_url",             "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},         },     ]     

See <https://python.langchain.com/docs/concepts/multimodality/>

If the property `supports_image_urls` is set to True, the test will also check that we can process content blocks of the form:               {         "type": "image",         "source_type": "url",         "url": "<url>",     }     

Configuration

To disable this test, set `supports_image_inputs` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def supports_image_inputs(self) -> bool:             return False              # Can also explicitly disable testing image URLs:         @property         def supports_image_urls(self) -> bool:             return False     

Troubleshooting

If this test fails, check that the model can correctly handle messages with image content blocks, including base64-encoded images. Otherwise, set the `supports_image_inputs` property to False.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_image\_tool\_message\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_image_tool_message)\#     

Test that the model can process ToolMessages with image inputs.

This test should be skipped if the model does not support messages of the form:               ToolMessage(         content=[             {                 "type": "image_url",                 "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},             },         ],         tool_call_id="1",         name="random_image",     )     

containing image content blocks in OpenAI Chat Completions format, in addition to messages of the form:               ToolMessage(         content=[             {                 "type": "image",                 "source_type": "base64",                 "data": image_data,                 "mime_type": "image/jpeg",             },         ],         tool_call_id="1",         name="random_image",     )     

containing image content blocks in standard format.

This test can be skipped by setting the `supports_image_tool_message` property to False \(see Configuration below\).

Configuration

To disable this test, set `supports_image_tool_message` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def supports_image_tool_message(self) -> bool:             return False     

Troubleshooting

If this test fails, check that the model can correctly handle messages with image content blocks in ToolMessages, including base64-encoded images. Otherwise, set the `supports_image_tool_message` property to False.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_invoke\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_invoke)\#     

Test to verify that model.invoke\(simple\_message\) works.

This should pass for all integrations.

Troubleshooting

If this test fails, you should make sure your \_generate method does not raise any exceptions, and that it returns a valid [`ChatResult`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_result.ChatResult.html#langchain_core.outputs.chat_result.ChatResult "langchain_core.outputs.chat_result.ChatResult") like so:               return ChatResult(         generations=[ChatGeneration(             message=AIMessage(content="Output text")         )]     )     

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_json\_mode\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_json_mode)\#     

Test structured output via [JSON mode.](https://python.langchain.com/docs/concepts/structured_outputs/#json-mode).

This test is optional and should be skipped if the model does not support the JSON mode feature \(see Configuration below\).

Configuration

To disable this test, set `supports_json_mode` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def supports_json_mode(self) -> bool:             return False     

Troubleshooting

See example implementation of `with_structured_output` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.with_structured_output>

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_message\_with\_name\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_message_with_name)\#     

Test that HumanMessage with values for the `name` field can be handled.

These messages may take the form:               HumanMessage("hello", name="example_user")     

If possible, the `name` field should be parsed and passed appropriately to the model. Otherwise, it should be ignored.

Troubleshooting

If this test fails, check that the `name` field on `HumanMessage` objects is either ignored or passed to the model appropriately.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_pdf\_inputs\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_pdf_inputs)\#     

Test that the model can process PDF inputs.

This test should be skipped \(see Configuration below\) if the model does not support PDF inputs. These will take the form:               {         "type": "image",         "source_type": "base64",         "data": "<base64 image data>",         "mime_type": "application/pdf",     }     

See <https://python.langchain.com/docs/concepts/multimodality/>

Configuration

To disable this test, set `supports_pdf_inputs` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):              @property         def supports_pdf_inputs(self) -> bool:             return False     

Troubleshooting

If this test fails, check that the model can correctly handle messages with pdf content blocks, including base64-encoded files. Otherwise, set the `supports_pdf_inputs` property to False.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_stop\_sequence\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_stop_sequence)\#     

Test that model does not fail when invoked with the `stop` parameter, which is a standard parameter for stopping generation at a certain token.

More on standard parameters here: <https://python.langchain.com/docs/concepts/chat_models/#standard-parameters>

This should pass for all integrations.

Troubleshooting

If this test fails, check that the function signature for `_generate` \(as well as `_stream` and async variants\) accepts the `stop` parameter:               def _generate(         self,         messages: List[BaseMessage],         stop: Optional[List[str]] = None,         run_manager: Optional[CallbackManagerForLLMRun] = None,         **kwargs: Any,     ) -> ChatResult:     

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_stream\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_stream)\#     

Test to verify that model.stream\(simple\_message\) works.

This should pass for all integrations. Passing this test does not indicate a “streaming” implementation, but rather that the model can be used in a streaming context.

Troubleshooting

First, debug `test_invoke()`. because stream has a default implementation that calls invoke and yields the result as a single chunk.

If that test passes but not this one, you should make sure your \_stream method does not raise any exceptions, and that it yields valid [`ChatGenerationChunk`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") objects like so:               yield ChatGenerationChunk(         message=AIMessageChunk(content="chunk text")     )     

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_stream\_time\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _benchmark : BenchmarkFixture_,     _vcr : Cassette_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_stream_time)\#     

Test that streaming does not introduce undue overhead.

See `enable_vcr_tests` dropdown `above` for more information.

Configuration

This test can be enabled or disabled using the `enable_vcr_tests` property. For example, to disable the test, set this property to `False`:               @property     def enable_vcr_tests(self) -> bool:         return False     

Important

VCR will by default record authentication headers and other sensitive information in cassettes. See `enable_vcr_tests` dropdown `above` for how to configure what information is recorded in cassettes.

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **benchmark** \(_BenchmarkFixture_\)

  * **vcr** \(_Cassette_\)

Return type:     

None

test\_structured\_few\_shot\_examples\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _my\_adder\_tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_structured_few_shot_examples)\#     

Test that the model can process few-shot examples with tool calls.

These are represented as a sequence of messages of the following form:

  * `HumanMessage` with string content;

  * `AIMessage` with the `tool_calls` attribute populated;

  * `ToolMessage` with string content;

  * `AIMessage` with string content \(an answer\);

  * `HumanMessage` with string content \(a follow-up question\).

This test should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

This test uses a utility function in `langchain_core` to generate a sequence of messages representing “few-shot” examples: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.tool_example_to_messages.html>

If this test fails, check that the model can correctly handle this sequence of messages.

You can `xfail` the test if tool calling is implemented but this format is not supported.               @pytest.mark.xfail(reason=("Not implemented."))     def test_structured_few_shot_examples(self, *args: Any) -> None:         super().test_structured_few_shot_examples(*args)     

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **my\_adder\_tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_structured\_output\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _schema\_type : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_structured_output)\#     

Test to verify structured output is generated both on invoke and stream.

This test is optional and should be skipped if the model does not support structured output \(see Configuration below\).

Configuration

To disable structured output tests, set `has_structured_output` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_structured_output(self) -> bool:             return False     

By default, `has_structured_output` is True if a model overrides the `with_structured_output` or `bind_tools` methods.

Troubleshooting

If this test fails, ensure that the model’s `bind_tools` method properly handles both JSON Schema and Pydantic V2 models. `langchain_core` implements a utility function that will accommodate most formats: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html>

See example implementation of `with_structured_output` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.with_structured_output>

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **schema\_type** \(_str_\)

Return type:     

None

_async _test\_structured\_output\_async\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _schema\_type : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_structured_output_async)\#     

Test to verify structured output is generated both on invoke and stream.

This test is optional and should be skipped if the model does not support structured output \(see Configuration below\).

Configuration

To disable structured output tests, set `has_structured_output` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_structured_output(self) -> bool:             return False     

By default, `has_structured_output` is True if a model overrides the `with_structured_output` or `bind_tools` methods.

Troubleshooting

If this test fails, ensure that the model’s `bind_tools` method properly handles both JSON Schema and Pydantic V2 models. `langchain_core` implements a utility function that will accommodate most formats: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html>

See example implementation of `with_structured_output` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.with_structured_output>

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **schema\_type** \(_str_\)

Return type:     

None

test\_structured\_output\_optional\_param\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_structured_output_optional_param)\#     

Test to verify we can generate structured output that includes optional parameters.

This test is optional and should be skipped if the model does not support structured output \(see Configuration below\).

Configuration

To disable structured output tests, set `has_structured_output` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_structured_output(self) -> bool:             return False     

By default, `has_structured_output` is True if a model overrides the `with_structured_output` or `bind_tools` methods.

Troubleshooting

If this test fails, ensure that the model’s `bind_tools` method properly handles Pydantic V2 models with optional parameters. `langchain_core` implements a utility function that will accommodate most formats: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html>

See example implementation of `with_structured_output` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.with_structured_output>

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_structured\_output\_pydantic\_2\_v1\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_structured_output_pydantic_2_v1)\#     

Test to verify we can generate structured output using pydantic.v1.BaseModel.

pydantic.v1.BaseModel is available in the pydantic 2 package.

This test is optional and should be skipped if the model does not support structured output \(see Configuration below\).

Configuration

To disable structured output tests, set `has_structured_output` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_structured_output(self) -> bool:             return False     

By default, `has_structured_output` is True if a model overrides the `with_structured_output` or `bind_tools` methods.

Troubleshooting

If this test fails, ensure that the model’s `bind_tools` method properly handles both JSON Schema and Pydantic V1 models. `langchain_core` implements a utility function that will accommodate most formats: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html>

See example implementation of `with_structured_output` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.with_structured_output>

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_tool\_calling\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_calling)\#     

Test that the model generates tool calls. This test is skipped if the `has_tool_calling` property on the test class is set to False.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that `bind_tools` is implemented to correctly translate LangChain tool objects into the appropriate schema for your chat model.

This test may fail if the chat model does not support a `tool_choice` parameter. This parameter can be used to force a tool call. If `tool_choice` is not supported and the model consistently fails this test, you can `xfail` the test:               @pytest.mark.xfail(reason=("Does not support tool_choice."))     def test_tool_calling(self, model: BaseChatModel) -> None:         super().test_tool_calling(model)     

Otherwise, in the case that only one tool is bound, ensure that `tool_choice` supports the string `"any"` to force calling that tool.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

_async _test\_tool\_calling\_async\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_calling_async)\#     

Test that the model generates tool calls. This test is skipped if the `has_tool_calling` property on the test class is set to False.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that `bind_tools` is implemented to correctly translate LangChain tool objects into the appropriate schema for your chat model.

This test may fail if the chat model does not support a `tool_choice` parameter. This parameter can be used to force a tool call. If `tool_choice` is not supported and the model consistently fails this test, you can `xfail` the test:               @pytest.mark.xfail(reason=("Does not support tool_choice."))     async def test_tool_calling_async(self, model: BaseChatModel) -> None:         await super().test_tool_calling_async(model)     

Otherwise, in the case that only one tool is bound, ensure that `tool_choice` supports the string `"any"` to force calling that tool.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_tool\_calling\_with\_no\_arguments\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_calling_with_no_arguments)\#     

Test that the model generates tool calls for tools with no arguments. This test is skipped if the `has_tool_calling` property on the test class is set to False.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that `bind_tools` is implemented to correctly translate LangChain tool objects into the appropriate schema for your chat model. It should correctly handle the case where a tool has no arguments.

This test may fail if the chat model does not support a `tool_choice` parameter. This parameter can be used to force a tool call. It may also fail if a provider does not support this form of tool. In these cases, you can `xfail` the test:               @pytest.mark.xfail(reason=("Does not support tool_choice."))     def test_tool_calling_with_no_arguments(self, model: BaseChatModel) -> None:         super().test_tool_calling_with_no_arguments(model)     

Otherwise, in the case that only one tool is bound, ensure that `tool_choice` supports the string `"any"` to force calling that tool.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_tool\_choice\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_choice)\#     

Test that the model can force tool calling via the `tool_choice` parameter. This test is skipped if the `has_tool_choice` property on the test class is set to False.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_choice` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_choice(self) -> bool:             return False     

Troubleshooting

If this test fails, check whether the `test_tool_calling` test is passing. If it is not, refer to the troubleshooting steps in that test first.

If `test_tool_calling` is passing, check that the underlying model supports forced tool calling. If it does, `bind_tools` should accept a `tool_choice` parameter that can be used to force a tool call.

It should accept \(1\) the string `"any"` to force calling the bound tool, and \(2\) the string name of the tool to force calling that tool.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_tool\_message\_error\_status\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _my\_adder\_tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_message_error_status)\#     

Test that ToolMessage with `status="error"` can be handled.

These messages may take the form:               ToolMessage(         "Error: Missing required argument 'b'.",         name="my_adder_tool",         tool_call_id="abc123",         status="error",     )     

If possible, the `status` field should be parsed and passed appropriately to the model.

This test is optional and should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that the `status` field on `ToolMessage` objects is either ignored or passed to the model appropriately.

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **my\_adder\_tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_tool\_message\_histories\_list\_content\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _my\_adder\_tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_message_histories_list_content)\#     

Test that message histories are compatible with list tool contents \(e.g. Anthropic format\).

These message histories will include AIMessage objects with “tool use” and content blocks, e.g.,               [         {"type": "text", "text": "Hmm let me think about that"},         {             "type": "tool_use",             "input": {"fav_color": "green"},             "id": "foo",             "name": "color_picker",         },     ]     

This test should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that:

  1. The model can correctly handle message histories that include AIMessage objects with list content.

  2. The `tool_calls` attribute on AIMessage objects is correctly handled and passed to the model in an appropriate format.

  3. The model can correctly handle ToolMessage objects with string content and arbitrary string values for `tool_call_id`.

You can `xfail` the test if tool calling is implemented but this format is not supported.               @pytest.mark.xfail(reason=("Not implemented."))     def test_tool_message_histories_list_content(self, *args: Any) -> None:         super().test_tool_message_histories_list_content(*args)     

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **my\_adder\_tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_tool\_message\_histories\_string\_content\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _my\_adder\_tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_tool_message_histories_string_content)\#     

Test that message histories are compatible with string tool contents \(e.g. OpenAI format\). If a model passes this test, it should be compatible with messages generated from providers following OpenAI format.

This test should be skipped if the model does not support tool calling \(see Configuration below\).

Configuration

To disable tool calling tests, set `has_tool_calling` to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def has_tool_calling(self) -> bool:             return False     

Troubleshooting

If this test fails, check that:

  1. The model can correctly handle message histories that include AIMessage objects with `""` content.

  2. The `tool_calls` attribute on AIMessage objects is correctly handled and passed to the model in an appropriate format.

  3. The model can correctly handle ToolMessage objects with string content and arbitrary string values for `tool_call_id`.

assert tool\_call.get\(“type”\) == “tool\_call”     

You can `xfail` the test if tool calling is implemented but this format is not supported.               @pytest.mark.xfail(reason=("Not implemented."))     def test_tool_message_histories_string_content(self, *args: Any) -> None:         super().test_tool_message_histories_string_content(*args)     

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **my\_adder\_tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_usage\_metadata\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_usage_metadata)\#     

Test to verify that the model returns correct usage metadata.

This test is optional and should be skipped if the model does not return usage metadata \(see Configuration below\).

Changed in version 0.3.17: Additionally check for the presence of model\_name in the response metadata, which is needed for usage tracking in callback handlers.

Configuration

By default, this test is run. To disable this feature, set returns\_usage\_metadata to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def returns_usage_metadata(self) -> bool:             return False     

This test can also check the format of specific kinds of usage metadata based on the supported\_usage\_metadata\_details property. This property should be configured as follows with the types of tokens that the model supports tracking:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def supported_usage_metadata_details(self) -> dict:             return {                 "invoke": [                     "audio_input",                     "audio_output",                     "reasoning_output",                     "cache_read_input",                     "cache_creation_input",                 ],                 "stream": [                     "audio_input",                     "audio_output",                     "reasoning_output",                     "cache_read_input",                     "cache_creation_input",                 ],             }     

Troubleshooting

If this test fails, first verify that your model returns [`UsageMetadata`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") dicts attached to the returned AIMessage object in \_generate:               return ChatResult(         generations=[ChatGeneration(             message=AIMessage(                 content="Output text",                 usage_metadata={                     "input_tokens": 350,                     "output_tokens": 240,                     "total_tokens": 590,                     "input_token_details": {                         "audio": 10,                         "cache_creation": 200,                         "cache_read": 100,                     },                     "output_token_details": {                         "audio": 10,                         "reasoning": 200,                     }                 }             )         )]     )     

Check also that the response includes a `"model_name"` key in its `usage_metadata`.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_usage\_metadata\_streaming\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/chat_models.html#ChatModelIntegrationTests.test_usage_metadata_streaming)\#     

Test usage metadata in streaming mode.

Test to verify that the model returns correct usage metadata in streaming mode.

Changed in version 0.3.17: Additionally check for the presence of model\_name in the response metadata, which is needed for usage tracking in callback handlers.

Configuration

By default, this test is run. To disable this feature, set returns\_usage\_metadata to False in your test class:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def returns_usage_metadata(self) -> bool:             return False     

This test can also check the format of specific kinds of usage metadata based on the supported\_usage\_metadata\_details property. This property should be configured as follows with the types of tokens that the model supports tracking:               class TestMyChatModelIntegration(ChatModelIntegrationTests):         @property         def supported_usage_metadata_details(self) -> dict:             return {                 "invoke": [                     "audio_input",                     "audio_output",                     "reasoning_output",                     "cache_read_input",                     "cache_creation_input",                 ],                 "stream": [                     "audio_input",                     "audio_output",                     "reasoning_output",                     "cache_read_input",                     "cache_creation_input",                 ],             }     

Troubleshooting

If this test fails, first verify that your model yields [`UsageMetadata`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") dicts attached to the returned AIMessage object in \_stream that sum up to the total usage metadata.

Note that input\_tokens should only be included on one of the chunks \(typically the first or the last chunk\), and the rest should have 0 or None to avoid counting input tokens multiple times.

output\_tokens typically count the number of tokens in each chunk, not the sum. This test will pass as long as the sum of output\_tokens across all chunks is not 0.               yield ChatResult(         generations=[ChatGeneration(             message=AIMessage(                 content="Output text",                 usage_metadata={                     "input_tokens": (                         num_input_tokens if is_first_chunk else 0                     ),                     "output_tokens": 11,                     "total_tokens": (                         11+num_input_tokens if is_first_chunk else 11                     ),                     "input_token_details": {                         "audio": 10,                         "cache_creation": 200,                         "cache_read": 100,                     },                     "output_token_details": {                         "audio": 10,                         "reasoning": 200,                     }                 }             )         )]     )     

Check also that the aggregated response includes a `"model_name"` key in its `usage_metadata`.

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

__On this page