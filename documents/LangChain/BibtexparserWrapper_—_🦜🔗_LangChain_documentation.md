# BibtexparserWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bibtex.BibtexparserWrapper.html
**Word Count:** 83
**Links Count:** 256
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# BibtexparserWrapper\#

_class _langchain\_community.utilities.bibtex.BibtexparserWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/bibtex.html#BibtexparserWrapper)\#     

Bases: `BaseModel`

Wrapper around bibtexparser.

To use, you should have the `bibtexparser` python package installed. <https://bibtexparser.readthedocs.io/en/master/>

This wrapper will use bibtexparser to load a collection of references from a bibtex file and fetch document summaries.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

get\_metadata\(

    _entry : Mapping\[str, Any\]_,     _load\_extra : bool = False_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/bibtex.html#BibtexparserWrapper.get_metadata)\#     

Get metadata for the given entry.

Parameters:     

  * **entry** \(_Mapping_ _\[__str_ _,__Any_ _\]_\)

  * **load\_extra** \(_bool_\)

Return type:     

_Dict_\[str, _Any_\]

load\_bibtex\_entries\(

    _path : str_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/bibtex.html#BibtexparserWrapper.load_bibtex_entries)\#     

Load bibtex entries from the bibtex file at the given path.

Parameters:     

**path** \(_str_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

__On this page