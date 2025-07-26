# langchain_community.tools.slack.base — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/slack/base.html
**Word Count:** 33
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:23
**Status:** completed

---

# Source code for langchain\_community.tools.slack.base               """Base class for Slack tools."""          from __future__ import annotations          from typing import TYPE_CHECKING          from langchain_core.tools import BaseTool     from pydantic import Field          from langchain_community.tools.slack.utils import login          if TYPE_CHECKING:         # This is for linting and IDE typehints         from slack_sdk import WebClient     else:         try:             # We do this so pydantic can resolve the types when instantiating             from slack_sdk import WebClient         except ImportError:             pass                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.slack.base.SlackBaseTool.html#langchain_community.tools.slack.base.SlackBaseTool)     class SlackBaseTool(BaseTool):         """Base class for Slack tools."""              client: WebClient = Field(default_factory=login)         """The WebClient object."""