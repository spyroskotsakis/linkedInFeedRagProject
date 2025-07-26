# TavilySearchInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/tavily/tavily_search/langchain_tavily.tavily_search.TavilySearchInput.html
**Word Count:** 679
**Links Count:** 93
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# TavilySearchInput\#

_class _langchain\_tavily.tavily\_search.TavilySearchInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tavily/tavily_search.html#TavilySearchInput)\#     

Bases: `BaseModel`

Input for \[TavilySearch\]

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _end\_date _: str | None_ _ = None_\#     

Filters search results to include only content published on or before this date.

Use this parameter when you need to: \- Exclude content published after a certain date \- Study historical information or past events \- Research how topics were covered during specific time periods \- Combine with start\_date to create a custom date range

Format must be YYYY-MM-DD \(e.g., “2024-03-31” for March 31, 2024\).

Examples: \- “2024-03-31” - Results up to and including March 31, 2024 \- “2023-12-31” - Results up to and including December 31, 2023

When combined with start\_date, creates a precise date range filter. For example: start\_date=”2024-01-01”, end\_date=”2024-03-31” returns results from Q1 2024 only.

Default is None \(no end date restriction\).

_param _exclude\_domains _: List\[str\] | None_ _ = \[\]_\#     

A list of domains to exclude from search results.

Use this parameter when: 1\. The user explicitly requests to avoid certain websites \(e.g., “Find information about climate change but not from twitter.com”\) 2\. The user mentions not wanting results from specific organizations without naming the domain \(e.g., “Find phone reviews but nothing from Apple”\)

In both cases, you should determine the appropriate domains to exclude \(e.g., \[“twitter.com”\] or \[“apple.com”\]\) and set this parameter.

Results will filter out all content from the specified domains. Default is None \(no domain exclusion\).

_param _include\_domains _: List\[str\] | None_ _ = \[\]_\#     

A list of domains to restrict search results to.

Use this parameter when: 1\. The user explicitly requests information from specific websites \(e.g., “Find climate data from nasa.gov”\) 2\. The user mentions an organization or company without specifying the domain \(e.g., “Find information about iPhones from Apple”\)

In both cases, you should determine the appropriate domains \(e.g., \[“nasa.gov”\] or \[“apple.com”\]\) and set this parameter.

Results will ONLY come from the specified domains - no other sources will be included. Default is None \(no domain restriction\).

_param _include\_favicon _: bool | None_ _ = False_\#     

Determines whether to include favicon URLs for each search result.

When enabled, each search result will include the website’s favicon URL, which can be useful for: \- Building rich UI interfaces with visual website indicators \- Providing visual cues about the source’s credibility or brand \- Creating bookmark-like displays with recognizable site icons

Set to True when creating user interfaces that benefit from visual branding or when favicon information enhances the user experience.

Default is False to minimize response size and API usage.

_param _include\_images _: bool | None_ _ = False_\#     

Determines if the search returns relevant images along with text results.

Set to True when the user explicitly requests visuals or when images would significantly enhance understanding \(e.g., “Show me what black holes look like,” “Find pictures of Renaissance art”\).

Leave as False \(default\) for most informational queries where text is sufficient.

_param _query _: str_ _\[Required\]_\#     

Search query to look up

_param _search\_depth _: Literal\['basic', 'advanced'\] | None_ _ = 'basic'_\#     

Controls search thoroughness and result comprehensiveness.

Use “basic” for simple queries requiring quick, straightforward answers.

Use “advanced” \(default\) for complex queries, specialized topics, rare information, or when in-depth analysis is needed.

_param _start\_date _: str | None_ _ = None_\#     

Filters search results to include only content published on or after this date.

Use this parameter when you need to: \- Find recent developments or updates on a topic \- Exclude outdated information from search results \- Focus on content within a specific timeframe \- Combine with end\_date to create a custom date range

Format must be YYYY-MM-DD \(e.g., “2024-01-15” for January 15, 2024\).

Examples: \- “2024-01-01” - Results from January 1, 2024 onwards \- “2023-12-25” - Results from December 25, 2023 onwards

When combined with end\_date, creates a precise date range filter.

Default is None \(no start date restriction\).

_param _time\_range _: Literal\['day', 'week', 'month', 'year'\] | None_ _ = None_\#     

Limits results to content published within a specific timeframe.

ONLY set this when the user explicitly mentions a time period \(e.g., “latest AI news,” “articles from last week”\).

For less popular or niche topics, use broader time ranges \(“month” or “year”\) to ensure sufficient relevant results.

Options: “day” \(24h\), “week” \(7d\), “month” \(30d\), “year” \(365d\).

Default is None.

_param _topic _: Literal\['general', 'news', 'finance'\] | None_ _ = 'general'_\#     

Specifies search category for optimized results.

Use “general” \(default\) for most queries, INCLUDING those with terms like “latest,” “newest,” or “recent” when referring to general information.

Use “finance” for markets, investments, economic data, or financial news.

Use “news” ONLY for politics, sports, or major current events covered by mainstream media - NOT simply because a query asks for “new” information.

__On this page