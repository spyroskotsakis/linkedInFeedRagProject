# PALValidation — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/pal_chain/langchain_experimental.pal_chain.base.PALValidation.html
**Word Count:** 117
**Links Count:** 100
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# PALValidation\#

_class _langchain\_experimental.pal\_chain.base.PALValidation\(

    _solution\_expression\_name : str | None = None_,     _solution\_expression\_type : type | None = None_,     _allow\_imports : bool = False_,     _allow\_command\_exec : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/pal_chain/base.html#PALValidation)\#     

Validation for PAL generated code.

Initialize a PALValidation instance.

Parameters:     

  * **solution\_expression\_name** \(_str_\) – Name of the expected solution expression. If passed, solution\_expression\_type must be passed as well.

  * **solution\_expression\_type** \(_str_\) – AST type of the expected solution expression. If passed, solution\_expression\_name must be passed as well. Must be one of PALValidation.SOLUTION\_EXPRESSION\_TYPE\_FUNCTION, PALValidation.SOLUTION\_EXPRESSION\_TYPE\_VARIABLE.

  * **allow\_imports** \(_bool_\) – Allow import statements.

  * **allow\_command\_exec** \(_bool_\) – Allow using known command execution functions.

Methods

`__init__`\(\[solution\_expression\_name, ...\]\) | Initialize a PALValidation instance.   ---|---      \_\_init\_\_\(

    _solution\_expression\_name : str | None = None_,     _solution\_expression\_type : type | None = None_,     _allow\_imports : bool = False_,     _allow\_command\_exec : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/pal_chain/base.html#PALValidation.__init__)\#     

Initialize a PALValidation instance.

Parameters:     

  * **solution\_expression\_name** \(_str_\) – Name of the expected solution expression. If passed, solution\_expression\_type must be passed as well.

  * **solution\_expression\_type** \(_str_\) – AST type of the expected solution expression. If passed, solution\_expression\_name must be passed as well. Must be one of PALValidation.SOLUTION\_EXPRESSION\_TYPE\_FUNCTION, PALValidation.SOLUTION\_EXPRESSION\_TYPE\_VARIABLE.

  * **allow\_imports** \(_bool_\) – Allow import statements.

  * **allow\_command\_exec** \(_bool_\) – Allow using known command execution functions.

__On this page