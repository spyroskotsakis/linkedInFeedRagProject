# TavilyCrawlInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/tavily/tavily_crawl/langchain_tavily.tavily_crawl.TavilyCrawlInput.html
**Word Count:** 592
**Links Count:** 101
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# TavilyCrawlInput\#

_class _langchain\_tavily.tavily\_crawl.TavilyCrawlInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tavily/tavily_crawl.html#TavilyCrawlInput)\#     

Bases: `BaseModel`

Input for \[TavilyCrawl\]

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allow\_external _: bool | None_ _ = False_\#     

Allow the crawler to follow external links.

Use when the user explicitly asks to allow or deny external links.

_param _categories _: List\[Literal\['Careers', 'Blogs', 'Documentation', 'About', 'Pricing', 'Community', 'Developers', 'Contact', 'Media'\]\] | None_ _ = None_\#     

Direct the crawler to crawl specific categories of a website.

Set this field to the category that best matches the user’s request. Use the following guide to choose the appropriate category:

> Careers: Crawl pages related to job listings, open positions, and company career information. Blogs: Crawl blog posts, news articles, and editorial content. Documentation: Crawl technical documentation, user guides, API references, and manuals. About: Crawl ‘About Us’ pages, company background, mission statements, and team information. Pricing: Crawl pages that detail product or service pricing, plans, and cost comparisons. Community: Crawl forums, discussion boards, user groups, and community-driven content. Developers: Crawl developer portals, SDKs, API documentation, and resources for software developers. Contact: Crawl contact information pages, support forms, and customer service details. Media: Crawl press releases, media kits, newsrooms, and multimedia content.

ex. “Crawl apple.com for career opportunities” —> categories=”Careers” ex. “Crawl tavily.com for API documentation” —> categories=”Documentation”

_param _exclude\_domains _: List\[str\] | None_ _ = None_\#     

Regex patterns to exclude URLs from specific domains or subdomains.

Use when the user explicitly asks to exclude a specific domain or subdomain from a website.

ex. “Crawl tavily.com but exclude the docs.tavily.com subdomain from the crawl” —> \[“^docs.tavily.com$”\]

_param _exclude\_paths _: List\[str\] | None_ _ = None_\#     

Regex patterns to exclude URLs from the crawl with specific path patterns.

Use when the user explicitly asks to exclude a specific path from a website.

ex. “Crawl example.com but exclude the /api/v1 path form the crawl” —> \[“/api/v1.\*”\] ex. “Crawl example.com but exclude the /documentation path from the crawl” —> \[“/documentation/.\*”\]

_param _extract\_depth _: Literal\['basic', 'advanced'\] | None_ _ = 'basic'_\#     

Advanced extraction retrieves more data, including tables and embedded content with higher success but may increase latency.

_param _include\_favicon _: bool | None_ _ = False_\#     

Whether to include the favicon URL for each result.

_param _include\_images _: bool | None_ _ = False_\#     

Whether to include images in the crawl results.

_param _instructions _: str | None_ _ = None_\#     

Natural language instructions for the crawler.

The instructions parameter allows the crawler to intelligently navigate through a website using natural language. Take the users request to set the instructions parameter to guide the crawler in the direction of the users request.

ex. “I want to find all the Javascript SDK documentation from Tavily” —> instructions = “Javascript SDK documentation”

_param _limit _: int | None_ _ = 50_\#     

Total number of links the crawler will process before stopping.

limit must be greater than 0

_param _max\_breadth _: int | None_ _ = 20_\#     

Max number of links to follow per level of the tree \(i.e., per page\).

tavily-crawl uses a BFS Depth: referring to the number of link hops from the root URL. A page directly linked from the root is at BFS depth 1, regardless of its URL structure.

Increase this parameter when: 1\. You want many links from each page to be crawled.

max\_breadth must be greater than 0

_param _max\_depth _: int | None_ _ = 1_\#     

Max depth of the crawl. Defines how far from the base URL the crawler can explore.

Increase this parameter when: 1\. To crawl large websites and get a comprehensive overview of its structure. 2\. To crawl a website that has a lot of links to other pages.

Set this parameter to 1 when: 1\. To stay local to the base\_url 2\. To crawl a single page

max\_depth must be greater than 0

_param _select\_domains _: List\[str\] | None_ _ = None_\#     

Regex patterns to select only URLs from specific domains or subdomains.

Use when the user explicitly asks for a specific domain or subdomain from a website.

ex. “Crawl only the docs.tavily.com subdomain” —> \[“^docs.tavily.com$”\]

_param _select\_paths _: List\[str\] | None_ _ = None_\#     

Regex patterns to select only URLs with specific path patterns.

Use when the user explicitly asks for a specific path from a website.

ex. “Only crawl the /api/v1 path” —> \[“/api/v1.\*”\] ex. “Only crawl the /documentation path” —> \[“/documentation/.\*”\]

_param _url _: str_ _\[Required\]_\#     

The root URL to begin the crawl.

__On this page