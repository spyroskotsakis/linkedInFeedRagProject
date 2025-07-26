# ContentHandlerAmazonAPIGateway — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.amazon_api_gateway.ContentHandlerAmazonAPIGateway.html
**Word Count:** 36
**Links Count:** 290
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# ContentHandlerAmazonAPIGateway\#

_class _langchain\_community.llms.amazon\_api\_gateway.ContentHandlerAmazonAPIGateway[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/amazon_api_gateway.html#ContentHandlerAmazonAPIGateway)\#     

Adapter to prepare the inputs from Langchain to a format that LLM model expects.

It also provides helper function to extract the generated text from the model response.

Methods

`transform_input`\(prompt, model\_kwargs\) |    ---|---   `transform_output`\(response\) |       _classmethod _transform\_input\(

    _prompt : str_,     _model\_kwargs : Dict\[str, Any\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/amazon_api_gateway.html#ContentHandlerAmazonAPIGateway.transform_input)\#     

Parameters:     

  * **prompt** \(_str_\)

  * **model\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

_Dict_\[str, _Any_\]

_classmethod _transform\_output\(

    _response : Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/amazon_api_gateway.html#ContentHandlerAmazonAPIGateway.transform_output)\#     

Parameters:     

**response** \(_Any_\)

Return type:     

str

__On this page