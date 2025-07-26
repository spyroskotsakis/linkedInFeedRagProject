# langchain_community.tools.gitlab.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/gitlab/tool.html
**Word Count:** 45
**Links Count:** 13
**Scraped:** 2025-07-21 09:19:06
**Status:** completed

---

# Source code for langchain\_community.tools.gitlab.tool               """     This tool allows agents to interact with the python-gitlab library     and operate on a GitLab repository.          To use this tool, you must first set as environment variables:         GITLAB_PRIVATE_ACCESS_TOKEN         GITLAB_REPOSITORY -> format: {owner}/{repo}          """          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool     from pydantic import Field          from langchain_community.utilities.gitlab import GitLabAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gitlab.tool.GitLabAction.html#langchain_community.tools.gitlab.tool.GitLabAction)     class GitLabAction(BaseTool):         """Tool for interacting with the GitLab API."""              api_wrapper: GitLabAPIWrapper = Field(default_factory=GitLabAPIWrapper)         mode: str         name: str = ""         description: str = ""              def _run(             self,             instructions: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the GitLab API to run an operation."""             return self.api_wrapper.run(self.mode, instructions)