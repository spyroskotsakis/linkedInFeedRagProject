# tool_example_to_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.tool_example_to_messages.html
**Word Count:** 211
**Links Count:** 168
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# tool\_example\_to\_messages\#

langchain\_core.utils.function\_calling.tool\_example\_to\_messages\(

    _input : str_,     _tool\_calls : list\[BaseModel\]_,     _tool\_outputs : list\[str\] | None = None_,     _\*_ ,     _ai\_response : str | None = None_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/function_calling.html#tool_example_to_messages)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Convert an example into a list of messages that can be fed into an LLM.

This code is an adapter that converts a single example to a list of messages that can be fed into a chat model.

The list of messages per example by default corresponds to:

  1. HumanMessage: contains the content from which content should be extracted.

  2. AIMessage: contains the extracted information from the model

  3. ToolMessage: contains confirmation to the model that the model requested a tool correctly.

If ai\_response is specified, there will be a final AIMessage with that response.

The ToolMessage is required because some chat models are hyper-optimized for agents rather than for an extraction use case.

Parameters:     

  * **input** \(_str_\) – string, the user input

  * **tool\_calls** \(_list_ _\[__BaseModel_ _\]_\) – list\[BaseModel\], a list of tool calls represented as Pydantic BaseModels

  * **tool\_outputs** \(_list_ _\[__str_ _\]__|__None_\) – Optional\[list\[str\]\], a list of tool call outputs. Does not need to be provided. If not provided, a placeholder value will be inserted. Defaults to None.

  * **ai\_response** \(_str_ _|__None_\) – Optional\[str\], if provided, content for a final AIMessage.

Returns:     

A list of messages

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Examples               from typing import Optional     from pydantic import BaseModel, Field     from langchain_openai import ChatOpenAI          class Person(BaseModel):         '''Information about a person.'''         name: Optional[str] = Field(..., description="The name of the person")         hair_color: Optional[str] = Field(             ..., description="The color of the person's hair if known"         )         height_in_meters: Optional[str] = Field(             ..., description="Height in METERS"         )          examples = [         (             "The ocean is vast and blue. It's more than 20,000 feet deep.",             Person(name=None, height_in_meters=None, hair_color=None),         ),         (             "Fiona traveled far from France to Spain.",             Person(name="Fiona", height_in_meters=None, hair_color=None),         ),     ]               messages = []          for txt, tool_call in examples:         messages.extend(             tool_example_to_messages(txt, [tool_call])         )     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)