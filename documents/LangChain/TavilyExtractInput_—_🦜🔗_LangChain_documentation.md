# TavilyExtractInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/tavily/tavily_extract/langchain_tavily.tavily_extract.TavilyExtractInput.html
**Word Count:** 137
**Links Count:** 81
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# TavilyExtractInput\#

_class _langchain\_tavily.tavily\_extract.TavilyExtractInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tavily/tavily_extract.html#TavilyExtractInput)\#     

Bases: `BaseModel`

Input for \[TavilyExtract\] Extract web page content from one or more specified URLs using Tavily Extract.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _extract\_depth _: Literal\['basic', 'advanced'\] | None_ _ = 'basic'_\#     

Controls the thoroughness of web content extraction.

Use “basic” for faster extraction of main text content.

Use “advanced” \(default\) to retrieve comprehensive content including tables and embedded elements. Always use “advanced” for LinkedIn and YouTube URLs for optimal results.

Better for complex websites but may increase response time.

_param _include\_favicon _: bool | None_ _ = False_\#     

Whether to include the favicon URL for each result.

_param _include\_images _: bool | None_ _ = False_\#     

Determines whether to extract and include images from the source URLs.

Set to True when visualizations are needed for better context or understanding.

Default is False \(extracts text content only\).

_param _urls _: List\[str\]__\[Required\]_\#     

list of urls to extract

__On this page