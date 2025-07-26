# langchain_community.utils.user_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/utils/user_agent.html
**Word Count:** 21
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:23
**Status:** completed

---

# Source code for langchain\_community.utils.user\_agent               import logging     import os          log = logging.getLogger(__name__)                              [[docs]](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.user_agent.get_user_agent.html#langchain_community.utils.user_agent.get_user_agent)     def get_user_agent() -> str:         """Get user agent from environment variable."""         env_user_agent = os.environ.get("USER_AGENT")         if not env_user_agent:             log.warning(                 "USER_AGENT environment variable not set, "                 "consider setting it to identify your requests."             )             return "DefaultLangchainUserAgent"         return env_user_agent