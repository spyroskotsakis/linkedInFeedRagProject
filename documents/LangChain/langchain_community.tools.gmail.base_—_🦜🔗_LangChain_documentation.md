# langchain_community.tools.gmail.base — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/gmail/base.html
**Word Count:** 45
**Links Count:** 14
**Scraped:** 2025-07-21 09:16:48
**Status:** completed

---

# Source code for langchain\_community.tools.gmail.base               """Base class for Gmail tools."""          from __future__ import annotations          from typing import TYPE_CHECKING          from langchain_core.tools import BaseTool     from pydantic import Field          from langchain_community.tools.gmail.utils import build_resource_service          if TYPE_CHECKING:         # This is for linting and IDE typehints         from googleapiclient.discovery import Resource     else:         try:             # We do this so pydantic can resolve the types when instantiating             from googleapiclient.discovery import Resource         except ImportError:             pass                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gmail.base.GmailBaseTool.html#langchain_community.tools.gmail.base.GmailBaseTool)     class GmailBaseTool(BaseTool):         """Base class for Gmail tools."""              api_resource: Resource = Field(default_factory=build_resource_service)                         [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gmail.base.GmailBaseTool.html#langchain_community.tools.gmail.base.GmailBaseTool.from_api_resource)         @classmethod         def from_api_resource(cls, api_resource: Resource) -> "GmailBaseTool":             """Create a tool from an api resource.                  Args:                 api_resource: The api resource to use.                  Returns:                 A tool.             """             return cls(service=api_resource)  # type: ignore[call-arg]