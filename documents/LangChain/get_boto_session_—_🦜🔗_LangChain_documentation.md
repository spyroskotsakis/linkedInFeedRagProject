# get_boto_session — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.utils.get_boto_session.html
**Word Count:** 35
**Links Count:** 89
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# get\_boto\_session\#

langchain\_aws.agents.utils.get\_boto\_session\(

    _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _endpoint\_url : str | None = None_,     _config : Config | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/agents/utils.html#get_boto_session)\#     

Construct the boto3 session

Parameters:     

  * **credentials\_profile\_name** \(_str_ _|__None_\) – AWS profile name to use for credentials

  * **region\_name** \(_str_ _|__None_\) – AWS region to use

  * **endpoint\_url** \(_str_ _|__None_\) – Custom endpoint URL to use

  * **config** \(_Config_ _|__None_\) – Optional boto3 Config object

Return type:     

_Any_

__On this page