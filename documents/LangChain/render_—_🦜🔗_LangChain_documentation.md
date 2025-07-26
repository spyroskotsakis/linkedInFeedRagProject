# render — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.mustache.render.html
**Word Count:** 188
**Links Count:** 166
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# render\#

langchain\_core.utils.mustache.render\(

    _template : str | list\[tuple\[str, str\]\] = ''_,     _data : Mapping\[str, Any\] = mappingproxy\(\{\}\)_,     _partials\_dict : Mapping\[str, str\] = mappingproxy\(\{\}\)_,     _padding : str = ''_,     _def\_ldel : str = '\{\{'_,     _def\_rdel : str = '\}\}'_,     _scopes : list\[Literal\[False, 0\] | Mapping\[str, Any\]\] | None = None_,     _warn : bool = False_,     _keep : bool = False_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/mustache.html#render)\#     

Render a mustache template.

Renders a mustache template with a data scope and inline partial capability.

Parameters:     

  * **template** \(_str_ _|__list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – A file-like object or a string containing the template.

  * **data** \(_Mapping_ _\[__str_ _,__Any_ _\]_\) – A python dictionary with your data scope.

  * **partials\_path** – The path to where your partials are stored. If set to None, then partials won’t be loaded from the file system \(defaults to ‘.’\).

  * **partials\_ext** – The extension that you want the parser to look for \(defaults to ‘mustache’\).

  * **partials\_dict** \(_Mapping_ _\[__str_ _,__str_ _\]_\) – A python dictionary which will be search for partials before the filesystem is. \{‘include’: ‘foo’\} is the same as a file called include.mustache \(defaults to \{\}\).

  * **padding** \(_str_\) – This is for padding partials, and shouldn’t be used \(but can be if you really want to\).

  * **def\_ldel** \(_str_\) – The default left delimiter \(“\{\{” by default, as in spec compliant mustache\).

  * **def\_rdel** \(_str_\) – The default right delimiter \(“\}\}” by default, as in spec compliant mustache\).

  * **scopes** \(_list_ _\[__Literal_ _\[__False_ _,__0_ _\]__|__~collections.abc.Mapping_ _\[__str_ _,__~typing.Any_ _\]__\]__|__None_\) – The list of scopes that get\_key will look through.

  * **warn** \(_bool_\) – Log a warning when a template substitution isn’t found in the data

  * **keep** \(_bool_\) – Keep unreplaced tags when a substitution isn’t found in the data.

Returns:     

A string containing the rendered template.

Return type:     

str

__On this page