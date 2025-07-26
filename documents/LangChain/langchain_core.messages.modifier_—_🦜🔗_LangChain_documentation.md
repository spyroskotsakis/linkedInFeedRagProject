# langchain_core.messages.modifier — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/messages/modifier.html
**Word Count:** 56
**Links Count:** 13
**Scraped:** 2025-07-21 08:57:35
**Status:** completed

---

# Source code for langchain\_core.messages.modifier               """Message responsible for deleting other messages."""          from typing import Any, Literal          from langchain_core.messages.base import BaseMessage                              [[docs]](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.modifier.RemoveMessage.html#langchain_core.messages.modifier.RemoveMessage)     class RemoveMessage(BaseMessage):         """Message responsible for deleting other messages."""              type: Literal["remove"] = "remove"         """The type of the message (used for serialization). Defaults to "remove"."""              def __init__(             self,             id: str,  # noqa: A002             **kwargs: Any,         ) -> None:             """Create a RemoveMessage.                  Args:                 id: The ID of the message to remove.                 kwargs: Additional fields to pass to the message.                  Raises:                 ValueError: If the 'content' field is passed in kwargs.             """             if kwargs.pop("content", None):                 msg = "RemoveMessage does not support 'content' field."                 raise ValueError(msg)                  super().__init__("", id=id, **kwargs)