# WikidataAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wikidata.WikidataAPIWrapper.html
**Word Count:** 106
**Links Count:** 271
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# WikidataAPIWrapper\#

_class _langchain\_community.utilities.wikidata.WikidataAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikidata.html#WikidataAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around the Wikidata API.

To use, you should have the `wikibase-rest-api-client` and \`\`mediawikiapi \`\` python packages installed. This wrapper will use the Wikibase APIs to conduct searches and fetch item content. By default, it will return the item content of the top-k results. It limits the Document content by doc\_content\_chars\_max.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _doc\_content\_chars\_max _: int_ _ = 4000_\#     

_param _lang _: str_ _ = 'en'_\#     

_param _load\_all\_available\_meta _: bool_ _ = False_\#     

_param _top\_k\_results _: int_ _ = 2_\#     

_param _wikidata\_props _: List\[str\]__ = \['P31', 'P279', 'P27', 'P361', 'P527', 'P495', 'P17', 'P585', 'P131', 'P106', 'P21', 'P569', 'P570', 'P577', 'P50', 'P571', 'P641', 'P625', 'P19', 'P69', 'P108', 'P136', 'P39', 'P161', 'P20', 'P101', 'P179', 'P175', 'P7937', 'P57', 'P607', 'P509', 'P800', 'P449', 'P580', 'P582', 'P276', 'P69', 'P112', 'P740', 'P159', 'P452', 'P102', 'P1142', 'P1387', 'P1576', 'P140', 'P178', 'P287', 'P25', 'P22', 'P40', 'P185', 'P802', 'P1416'\]_\#     

_param _wikidata\_rest _: Any_ _\[Required\]_\#     

load\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikidata.html#WikidataAPIWrapper.load)\#     

Run Wikidata search and get the item documents plus the meta information.

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikidata.html#WikidataAPIWrapper.run)\#     

Run Wikidata search and get item summaries.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using WikidataAPIWrapper

  * [Wikidata](https://python.langchain.com/docs/integrations/tools/wikidata/)

__On this page