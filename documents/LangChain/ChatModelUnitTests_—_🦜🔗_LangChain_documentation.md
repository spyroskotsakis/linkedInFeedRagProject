# ChatModelUnitTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/unit_tests/langchain_tests.unit_tests.chat_models.ChatModelUnitTests.html
**Word Count:** 1393
**Links Count:** 132
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# ChatModelUnitTests\#

_class _langchain\_tests.unit\_tests.chat\_models.ChatModelUnitTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests)\#     

Base class for chat model unit tests.

Test subclasses must implement the `chat_model_class` and `chat_model_params` properties to specify what model to test and its initialization parameters.

Example:               from typing import Type          from langchain_tests.unit_tests import ChatModelUnitTests     from my_package.chat_models import MyChatModel               class TestMyChatModelUnit(ChatModelUnitTests):         @property         def chat_model_class(self) -> Type[MyChatModel]:             # Return the chat model class to test here             return MyChatModel              @property         def chat_model_params(self) -> dict:             # Return initialization parameters for the model.             return {"model": "model-001", "temperature": 0}     

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

Deprecated since version 0.3.15: This property will be removed in version 0.3.20. If a model does not support forcing tool calling, override the `has_tool_choice` property to return `False`. Otherwise, models should accept values of `"any"` or the name of a tool in `tool_choice`.

Example:               @property     def tool_choice_value(self) -> Optional[str]:         return "any"     

has\_tool\_choice

Boolean property indicating whether the chat model supports forcing tool calling via a `tool_choice` parameter.

By default, this is determined by whether the parameter is included in the signature for the corresponding `bind_tools` method.

If `True`, the minimum requirement for this feature is that `tool_choice="any"` will force a tool call, and `tool_choice=<tool name>` will force a call to a specific tool.

Example override:               @property     def has_tool_choice(self) -> bool:         return False     

has\_structured\_output

Boolean property indicating whether the chat model supports structured output.

By default, this is determined by whether the chat model overrides the `with_structured_output` or `bind_tools` methods. If the base implementations are intended to be used, this method should be overridden.

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

Testing initialization from environment variables     

Some unit tests may require testing initialization from environment variables. These tests can be enabled by overriding the `init_from_env_params` property \(see below\):

init\_from\_env\_params

This property is used in unit tests to test initialization from environment variables. It should return a tuple of three dictionaries that specify the environment variables, additional initialization args, and expected instance attributes to check.

Defaults to empty dicts. If not overridden, the test is skipped.

Example:               @property     def init_from_env_params(self) -> Tuple[dict, dict, dict]:         return (             {                 "MY_API_KEY": "api_key",             },             {                 "model": "bird-brain-001",             },             {                 "my_api_key": "api_key",             },         )     

Attributes

`chat_model_class` | The chat model class to test, e.g., `ChatParrotLink`.   ---|---   `chat_model_params` | Initialization parameters for the chat model.   `enable_vcr_tests` | \(bool\) whether to enable VCR tests for the chat model.   `has_structured_output` | \(bool\) whether the chat model supports structured output.   `has_tool_calling` | \(bool\) whether the model supports tool calling.   `has_tool_choice` | \(bool\) whether the model supports tool calling.   `init_from_env_params` | \(tuple\) environment variables, additional initialization args, and expected instance attributes for testing initialization from environment variables.   `returns_usage_metadata` | \(bool\) whether the chat model returns usage metadata on invoke and streaming responses.   `structured_output_kwargs` | If specified, additional kwargs for with\_structured\_output.   `supported_usage_metadata_details` | \(dict\) what usage metadata details are emitted in invoke and stream.   `supports_anthropic_inputs` | \(bool\) whether the chat model supports Anthropic-style inputs.   `supports_audio_inputs` | \(bool\) whether the chat model supports audio inputs, defaults to `False`.   `supports_image_inputs` | \(bool\) whether the chat model supports image inputs, defaults to `False`.   `supports_image_tool_message` | \(bool\) whether the chat model supports ToolMessages that include image content.   `supports_image_urls` | \(bool\) whether the chat model supports image inputs from URLs, defaults to `False`.   `supports_json_mode` | \(bool\) whether the chat model supports JSON mode.   `supports_pdf_inputs` | \(bool\) whether the chat model supports PDF inputs, defaults to `False`.   `supports_video_inputs` | \(bool\) whether the chat model supports video inputs, defaults to `False`.   `tool_choice_value` | \(None or str\) to use for tool choice when used in tests.      Methods

`test_bind_tool_pydantic`\(model, my\_adder\_tool\) | Test that chat model correctly handles Pydantic models that are passed into `bind_tools`.   ---|---   `test_init`\(\) | Test model initialization.   `test_init_from_env`\(\) | Test initialization from environment variables.   `test_init_streaming`\(\) | Test that model can be initialized with `streaming=True`.   `test_init_time`\(benchmark\) | Test initialization time of the chat model.   `test_serdes`\(model, snapshot\) | Test serialization and deserialization of the model.   `test_standard_params`\(model\) | Test that model properly generates standard parameters.   `test_with_structured_output`\(model, schema\) | Test `with_structured_output` method.      test\_bind\_tool\_pydantic\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _my\_adder\_tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_bind_tool_pydantic)\#     

Test that chat model correctly handles Pydantic models that are passed into `bind_tools`. Test is skipped if the `has_tool_calling` property on the test class is False.

Troubleshooting

If this test fails, ensure that the model’s `bind_tools` method properly handles Pydantic V2 models. `langchain_core` implements a utility function that will accommodate most formats: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html>

See example implementation of `bind_tools` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.bind_tools>

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **my\_adder\_tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_init\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_init)\#     

Test model initialization. This should pass for all integrations.

Troubleshooting

If this test fails, ensure that:

  1. `chat_model_params` is specified and the model can be initialized from those params;

  2. The model accommodates standard parameters: <https://python.langchain.com/docs/concepts/chat_models/#standard-parameters>

Return type:     

None

test\_init\_from\_env\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_init_from_env)\#     

Test initialization from environment variables. Relies on the `init_from_env_params` property. Test is skipped if that property is not set.

Troubleshooting

If this test fails, ensure that `init_from_env_params` is specified correctly and that model parameters are properly set from environment variables during initialization.

Return type:     

None

test\_init\_streaming\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_init_streaming)\#     

Test that model can be initialized with `streaming=True`. This is for backward-compatibility purposes.

Troubleshooting

If this test fails, ensure that the model can be initialized with a boolean `streaming` parameter.

Return type:     

None

test\_init\_time\(

    _benchmark : BenchmarkFixture_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_init_time)\#     

Test initialization time of the chat model. If this test fails, check that we are not introducing undue overhead in the model’s initialization.

Parameters:     

**benchmark** \(_BenchmarkFixture_\)

Return type:     

None

test\_serdes\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _snapshot : SnapshotAssertion_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_serdes)\#     

Test serialization and deserialization of the model. Test is skipped if the `is_lc_serializable` property on the chat model class is not overwritten to return `True`.

Troubleshooting

If this test fails, check that the `init_from_env_params` property is correctly set on the test class.

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **snapshot** \(_SnapshotAssertion_\)

Return type:     

None

test\_standard\_params\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_standard_params)\#     

Test that model properly generates standard parameters. These are used for tracing purposes.

Troubleshooting

If this test fails, check that the model accommodates standard parameters: <https://python.langchain.com/docs/concepts/chat_models/#standard-parameters>

Check also that the model class is named according to convention \(e.g., `ChatProviderName`\).

Parameters:     

**model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

Return type:     

None

test\_with\_structured\_output\(

    _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _schema : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/chat_models.html#ChatModelUnitTests.test_with_structured_output)\#     

Test `with_structured_output` method. Test is skipped if the `has_structured_output` property on the test class is False.

Troubleshooting

If this test fails, ensure that the model’s `bind_tools` method properly handles Pydantic V2 models. `langchain_core` implements a utility function that will accommodate most formats: <https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html>

See example implementation of `with_structured_output` here: <https://python.langchain.com/api_reference/_modules/langchain_openai/chat_models/base.html#BaseChatOpenAI.with_structured_output>

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **schema** \(_Any_\)

Return type:     

None

__On this page