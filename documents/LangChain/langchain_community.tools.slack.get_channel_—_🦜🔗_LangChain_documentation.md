# langchain_community.tools.slack.get_channel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/slack/get_channel.html
**Word Count:** 25
**Links Count:** 13
**Scraped:** 2025-07-21 09:13:23
**Status:** completed

---

# Source code for langchain\_community.tools.slack.get\_channel               import json     import logging     from typing import Any, Optional          from langchain_core.callbacks import CallbackManagerForToolRun          from langchain_community.tools.slack.base import SlackBaseTool                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.slack.get_channel.SlackGetChannel.html#langchain_community.tools.slack.get_channel.SlackGetChannel)     class SlackGetChannel(SlackBaseTool):         """Tool that gets Slack channel information."""              name: str = "get_channelid_name_dict"         description: str = (             "Use this tool to get channelid-name dict. There is no input to this tool"         )              def _run(             self, *args: Any, run_manager: Optional[CallbackManagerForToolRun] = None         ) -> str:             try:                 logging.getLogger(__name__)                      result = self.client.conversations_list()                 channels = result["channels"]                 filtered_result = [                     {key: channel[key] for key in ("id", "name", "created", "num_members")}                     for channel in channels                     if "id" in channel                     and "name" in channel                     and "created" in channel                     and "num_members" in channel                 ]                 return json.dumps(filtered_result, ensure_ascii=False)                  except Exception as e:                 return "Error creating conversation: {}".format(e)