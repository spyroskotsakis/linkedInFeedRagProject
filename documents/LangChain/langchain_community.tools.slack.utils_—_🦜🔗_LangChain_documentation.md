# langchain_community.tools.slack.utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/slack/utils.html
**Word Count:** 37
**Links Count:** 13
**Scraped:** 2025-07-21 09:16:02
**Status:** completed

---

# Source code for langchain\_community.tools.slack.utils               """Slack tool utils."""          from __future__ import annotations          import logging     import os     from typing import TYPE_CHECKING          if TYPE_CHECKING:         from slack_sdk import WebClient          logger = logging.getLogger(__name__)                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.slack.utils.login.html#langchain_community.tools.slack.utils.login)     def login() -> WebClient:         """Authenticate using the Slack API."""         try:             from slack_sdk import WebClient         except ImportError as e:             raise ImportError(                 "Cannot import slack_sdk. Please install the package with \                 `pip install slack_sdk`."             ) from e              if "SLACK_BOT_TOKEN" in os.environ:             token = os.environ["SLACK_BOT_TOKEN"]             client = WebClient(token=token)             logger.info("slack login success")             return client         elif "SLACK_USER_TOKEN" in os.environ:             token = os.environ["SLACK_USER_TOKEN"]             client = WebClient(token=token)             logger.info("slack login success")             return client         else:             logger.error(                 "Error: The SLACK_BOT_TOKEN or SLACK_USER_TOKEN \                 environment variable have not been set."             )                              UTC_FORMAT = "%Y-%m-%dT%H:%M:%S%z"     """UTC format for datetime objects."""