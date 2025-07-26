# QueryTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.QueryTransformer.html
**Word Count:** 45
**Links Count:** 253
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# QueryTransformer\#

_class _langchain.chains.query\_constructor.parser.QueryTransformer\(

    _\* args: Any_,     _allowed\_comparators : Sequence\[[Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\] | None = None_,     _allowed\_operators : Sequence\[[Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\] | None = None_,     _allowed\_attributes : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer)\#     

Transform a query string into an intermediate representation.

Methods

`__init__`\(\*args\[, allowed\_comparators, ...\]\) |    ---|---   `args`\(\*items\) |    `date`\(item\) |    `datetime`\(item\) |    `false`\(\) |    `float`\(item\) |    `func_call`\(func\_name, args\) |    `int`\(item\) |    `list`\(item\) |    `program`\(\*items\) |    `string`\(item\) |    `transform`\(tree\) | Transform the given tree, and return the final result   `true`\(\) |       Parameters:     

  * **args** \(_Any_\)

  * **allowed\_comparators** \(_Sequence_ _\[_[_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator") _\]__|__None_\)

  * **allowed\_operators** \(_Sequence_ _\[_[_Operator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator") _\]__|__None_\)

  * **allowed\_attributes** \(_Sequence_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _\* args: Any_,     _allowed\_comparators : Sequence\[[Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\] | None = None_,     _allowed\_operators : Sequence\[[Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\] | None = None_,     _allowed\_attributes : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.__init__)\#     

Parameters:     

  * **args** \(_Any_\)

  * **allowed\_comparators** \(_Sequence_ _\[_[_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator") _\]__|__None_\)

  * **allowed\_operators** \(_Sequence_ _\[_[_Operator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator") _\]__|__None_\)

  * **allowed\_attributes** \(_Sequence_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

args\(_\* items: Any_\) → tuple[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.args)\#     

Parameters:     

**items** \(_Any_\)

Return type:     

tuple

date\(

    _item : Any_, \) → [ISO8601Date](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601Date.html#langchain.chains.query_constructor.parser.ISO8601Date "langchain.chains.query_constructor.parser.ISO8601Date")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.date)\#     

Parameters:     

**item** \(_Any_\)

Return type:     

[_ISO8601Date_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601Date.html#langchain.chains.query_constructor.parser.ISO8601Date "langchain.chains.query_constructor.parser.ISO8601Date")

datetime\(

    _item : Any_, \) → [ISO8601DateTime](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601DateTime.html#langchain.chains.query_constructor.parser.ISO8601DateTime "langchain.chains.query_constructor.parser.ISO8601DateTime")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.datetime)\#     

Parameters:     

**item** \(_Any_\)

Return type:     

[_ISO8601DateTime_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601DateTime.html#langchain.chains.query_constructor.parser.ISO8601DateTime "langchain.chains.query_constructor.parser.ISO8601DateTime")

false\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.false)\#     

Return type:     

bool

float\(_item : Any_\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.float)\#     

Parameters:     

**item** \(_Any_\)

Return type:     

float

func\_call\(

    _func\_name : Any_,     _args : list_, \) → [FilterDirective](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.func_call)\#     

Parameters:     

  * **func\_name** \(_Any_\)

  * **args** \(_list_\)

Return type:     

[_FilterDirective_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective")

int\(_item : Any_\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.int)\#     

Parameters:     

**item** \(_Any_\)

Return type:     

int

list\(_item : Any_\) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.list)\#     

Parameters:     

**item** \(_Any_\)

Return type:     

list

program\(_\* items: Any_\) → tuple[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.program)\#     

Parameters:     

**items** \(_Any_\)

Return type:     

tuple

string\(_item : Any_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.string)\#     

Parameters:     

**item** \(_Any_\)

Return type:     

str

transform\(

    _tree : Tree\[\_Leaf\_T\]_, \) → \_Return\_T\#     

Transform the given tree, and return the final result

Parameters:     

**tree** \(_Tree_ _\[__\_Leaf\_T_ _\]_\)

Return type:     

_\_Return\_T_

true\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#QueryTransformer.true)\#     

Return type:     

bool

__On this page