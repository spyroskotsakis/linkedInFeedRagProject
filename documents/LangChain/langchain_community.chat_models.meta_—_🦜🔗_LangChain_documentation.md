# langchain_community.chat_models.meta — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/meta.html
**Word Count:** 16
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:00
**Status:** completed

---

# Source code for langchain\_community.chat\_models.meta               from typing import List          from langchain_core.messages import (         AIMessage,         BaseMessage,         ChatMessage,         HumanMessage,         SystemMessage,     )               def _convert_one_message_to_text_llama(message: BaseMessage) -> str:         if isinstance(message, ChatMessage):             message_text = f"\n\n{message.role.capitalize()}: {message.content}"         elif isinstance(message, HumanMessage):             message_text = f"[INST] {message.content} [/INST]"         elif isinstance(message, AIMessage):             message_text = f"{message.content}"         elif isinstance(message, SystemMessage):             message_text = f"<<SYS>> {message.content} <</SYS>>"         else:             raise ValueError(f"Got unknown type {message}")         return message_text                              [[docs]](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.meta.convert_messages_to_prompt_llama.html#langchain_community.chat_models.meta.convert_messages_to_prompt_llama)     def convert_messages_to_prompt_llama(messages: List[BaseMessage]) -> str:         """Convert a list of messages to a prompt for llama."""              return "\n".join(             [_convert_one_message_to_text_llama(message) for message in messages]         )