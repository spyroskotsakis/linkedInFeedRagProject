# VectorType — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.VectorType.html
**Word Count:** 1161
**Links Count:** 132
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# VectorType\#

_class _langchain\_sqlserver.vectorstores.VectorType\(_length : int_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#VectorType)\#     

VectorType - A custom type definition.

\_\_init\_\_ for VectorType class.

Attributes

`cache_ok` | Indicate if statements using this `ExternalType` are "safe to cache".   ---|---   `ensure_kwarg` | a regular expression that indicates method names for which the method should accept `**kw` arguments.   `hashable` | Flag, if False, means values from this type aren't hashable.   `python_type` | Return the Python type object expected to be returned by instances of this type, if known.   `render_bind_cast` | Render bind casts for `BindTyping.RENDER_CASTS` mode.   `render_literal_cast` | render casts when rendering a value as an inline literal, e.g. with `TypeEngine.literal_processor()`.   `should_evaluate_none` | If True, the Python constant `None` is considered to be handled explicitly by this type.   `sort_key_function` | A sorting function that can be passed as the key to sorted.      Methods

`__init__`\(length\) | \_\_init\_\_ for VectorType class.   ---|---   `adapt`\(cls, \*\*kw\) | Produce an "adapted" form of this type, given an "impl" class to work with.   `as_generic`\(\[allow\_nulltype\]\) | Return an instance of the generic type corresponding to this type using heuristic rule.   `bind_expression`\(bindvalue\) | Given a bind value \(i.e. a `BindParameter` instance\), return a SQL expression in its place.   `bind_processor`\(dialect\) | bind\_processor function for VectorType class.   `coerce_compared_value`\(op, value\) | Suggest a type for a 'coerced' Python value in an expression.   `column_expression`\(colexpr\) | Given a SELECT column expression, return a wrapping SQL expression.   `compare_values`\(x, y\) | Compare two values for equality.   `compile`\(\[dialect\]\) | Produce a string-compiled form of this `TypeEngine`.   `copy`\(\*\*kw\) |    `copy_value`\(value\) |    `dialect_impl`\(dialect\) | Return a dialect-specific implementation for this `TypeEngine`.   `evaluates_none`\(\) | Return a copy of this type which has the `should_evaluate_none` flag set to True.   `get_col_spec`\(\*\*kw\) | get\_col\_spec function for VectorType class.   `get_dbapi_type`\(dbapi\) | Return the corresponding type object from the underlying DB-API, if any.   `literal_processor`\(dialect\) | Return a conversion function for processing literal values that are to be rendered directly without using binds.   `result_processor`\(dialect, coltype\) | result\_processor function for VectorType class.   `with_variant`\(type\_, \*dialect\_names\) | Produce a copy of this type object that will utilize the given type when applied to the dialect of the given name.      Parameters:     

**length** \(_int_\)

\_\_init\_\_\(_length : int_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#VectorType.__init__)\#     

\_\_init\_\_ for VectorType class.

Parameters:     

**length** \(_int_\)

Return type:     

None

adapt\(

    _cls : Type\[TypeEngine | TypeEngineMixin\]_,     _\*\* kw: Any_, \) → TypeEngine\#     

Produce an “adapted” form of this type, given an “impl” class to work with.

This method is used internally to associate generic types with “implementation” types that are specific to a particular dialect.

Parameters:     

  * **cls** \(_Type_ _\[__TypeEngine_ _|__TypeEngineMixin_ _\]_\)

  * **kw** \(_Any_\)

Return type:     

_TypeEngine_

as\_generic\(

    _allow\_nulltype : bool = False_, \) → TypeEngine\#     

Return an instance of the generic type corresponding to this type using heuristic rule. The method may be overridden if this heuristic rule is not sufficient.               >>> from sqlalchemy.dialects.mysql import INTEGER     >>> INTEGER(display_width=4).as_generic()     Integer()                    >>> from sqlalchemy.dialects.mysql import NVARCHAR     >>> NVARCHAR(length=100).as_generic()     Unicode(length=100)     

Added in version 1.4.0b2.

See also

metadata\_reflection\_dbagnostic\_types \- describes the use of `_types.TypeEngine.as_generic()` in conjunction with the `_sql.DDLEvents.column_reflect()` event, which is its intended use.

Parameters:     

**allow\_nulltype** \(_bool_\)

Return type:     

_TypeEngine_

bind\_expression\(

    _bindvalue : BindParameter\[\_T\]_, \) → ColumnElement\[\_T\] | None\#     

Given a bind value \(i.e. a `BindParameter` instance\), return a SQL expression in its place.

This is typically a SQL function that wraps the existing bound parameter within the statement. It is used for special data types that require literals being wrapped in some special database function in order to coerce an application-level value into a database-specific format. It is the SQL analogue of the `TypeEngine.bind_processor()` method.

This method is called during the **SQL compilation** phase of a statement, when rendering a SQL string. It is **not** called against specific values.

Note that this method, when implemented, should always return the exact same structure, without any conditional logic, as it may be used in an executemany\(\) call against an arbitrary number of bound parameter sets.

Note

This method is only called relative to a **dialect specific type object** , which is often **private to a dialect in use** and is not the same type object as the public facing one, which means it’s not feasible to subclass a `types.TypeEngine` class in order to provide an alternate `_types.TypeEngine.bind_expression()` method, unless subclassing the `_types.UserDefinedType` class explicitly.

To provide alternate behavior for `_types.TypeEngine.bind_expression()`, implement a `_types.TypeDecorator` class and provide an implementation of `_types.TypeDecorator.bind_expression()`.

See also

types\_typedecorator

See also

types\_sql\_value\_processing

Parameters:     

**bindvalue** \(_BindParameter_ _\[__\_T_ _\]_\)

Return type:     

Optional\[ColumnElement\[\_T\]\]

bind\_processor\(

    _dialect : Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#VectorType.bind_processor)\#     

bind\_processor function for VectorType class.

Parameters:     

**dialect** \(_Any_\)

Return type:     

_Any_

coerce\_compared\_value\(

    _op : OperatorType | None_,     _value : Any_, \) → TypeEngine\[Any\]\#     

Suggest a type for a ‘coerced’ Python value in an expression.

Default behavior for `UserDefinedType` is the same as that of `TypeDecorator`; by default it returns `self`, assuming the compared value should be coerced into the same type as this one. See `TypeDecorator.coerce_compared_value()` for more detail.

Parameters:     

  * **op** \(_Optional_ _\[__OperatorType_ _\]_\)

  * **value** \(_Any_\)

Return type:     

TypeEngine\[Any\]

column\_expression\(

    _colexpr : ColumnElement\[\_T\]_, \) → ColumnElement\[\_T\] | None\#     

Given a SELECT column expression, return a wrapping SQL expression.

This is typically a SQL function that wraps a column expression as rendered in the columns clause of a SELECT statement. It is used for special data types that require columns to be wrapped in some special database function in order to coerce the value before being sent back to the application. It is the SQL analogue of the `TypeEngine.result_processor()` method.

This method is called during the **SQL compilation** phase of a statement, when rendering a SQL string. It is **not** called against specific values.

Note

This method is only called relative to a **dialect specific type object** , which is often **private to a dialect in use** and is not the same type object as the public facing one, which means it’s not feasible to subclass a `types.TypeEngine` class in order to provide an alternate `_types.TypeEngine.column_expression()` method, unless subclassing the `_types.UserDefinedType` class explicitly.

To provide alternate behavior for `_types.TypeEngine.column_expression()`, implement a `_types.TypeDecorator` class and provide an implementation of `_types.TypeDecorator.column_expression()`.

See also

types\_typedecorator

See also

types\_sql\_value\_processing

Parameters:     

**colexpr** \(_ColumnElement_ _\[__\_T_ _\]_\)

Return type:     

Optional\[ColumnElement\[\_T\]\]

compare\_values\(

    _x : Any_,     _y : Any_, \) → bool\#     

Compare two values for equality.

Parameters:     

  * **x** \(_Any_\)

  * **y** \(_Any_\)

Return type:     

bool

compile\(_dialect : Dialect | None = None_\) → str\#     

Produce a string-compiled form of this `TypeEngine`.

When called with no arguments, uses a “default” dialect to produce a string result.

Parameters:     

**dialect** \(_Optional_ _\[__Dialect_ _\]_\) – a `Dialect` instance.

Return type:     

str

copy\(_\*\* kw: Any_\) → Self\#     

Parameters:     

**kw** \(_Any_\)

Return type:     

_Self_

copy\_value\(_value : Any_\) → Any\#     

Parameters:     

**value** \(_Any_\)

Return type:     

_Any_

dialect\_impl\(_dialect : Dialect_\) → TypeEngine\[\_T\]\#     

Return a dialect-specific implementation for this `TypeEngine`.

Parameters:     

**dialect** \(_Dialect_\)

Return type:     

TypeEngine\[\_T\]

evaluates\_none\(\) → Self\#     

Return a copy of this type which has the `should_evaluate_none` flag set to True.

E.g.:               Table(         "some_table",         metadata,         Column(             String(50).evaluates_none(),             nullable=True,             server_default="no value",         ),     )     

The ORM uses this flag to indicate that a positive value of `None` is passed to the column in an INSERT statement, rather than omitting the column from the INSERT statement which has the effect of firing off column-level defaults. It also allows for types which have special behavior associated with the Python None value to indicate that the value doesn’t necessarily translate into SQL NULL; a prime example of this is a JSON type which may wish to persist the JSON value `'null'`.

In all cases, the actual NULL SQL value can be always be persisted in any column by using the `_expression.null` SQL construct in an INSERT statement or associated with an ORM-mapped attribute.

Note

The “evaluates none” flag does **not** apply to a value of `None` passed to :paramref:\`\_schema.Column.default\` or :paramref:\`\_schema.Column.server\_default\`; in these cases, `None` still means “no default”.

See also

session\_forcing\_null \- in the ORM documentation

:paramref:\`.postgresql.JSON.none\_as\_null\` \- PostgreSQL JSON interaction with this flag.

`TypeEngine.should_evaluate_none` \- class-level flag

Return type:     

_Self_

get\_col\_spec\(_\*\* kw: Any_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#VectorType.get_col_spec)\#     

get\_col\_spec function for VectorType class.

Parameters:     

**kw** \(_Any_\)

Return type:     

str

get\_dbapi\_type\(

    _dbapi : ModuleType_, \) → Any | None\#     

Return the corresponding type object from the underlying DB-API, if any.

This can be useful for calling `setinputsizes()`, for example.

Parameters:     

**dbapi** \(_ModuleType_\)

Return type:     

_Any_ | None

literal\_processor\(

    _dialect : Dialect_, \) → \_LiteralProcessorType\[\_T\] | None\#     

Return a conversion function for processing literal values that are to be rendered directly without using binds.

This function is used when the compiler makes use of the “literal\_binds” flag, typically used in DDL generation as well as in certain scenarios where backends don’t accept bound parameters.

Returns a callable which will receive a literal Python value as the sole positional argument and will return a string representation to be rendered in a SQL statement.

Note

This method is only called relative to a **dialect specific type object** , which is often **private to a dialect in use** and is not the same type object as the public facing one, which means it’s not feasible to subclass a `types.TypeEngine` class in order to provide an alternate `_types.TypeEngine.literal_processor()` method, unless subclassing the `_types.UserDefinedType` class explicitly.

To provide alternate behavior for `_types.TypeEngine.literal_processor()`, implement a `_types.TypeDecorator` class and provide an implementation of `_types.TypeDecorator.process_literal_param()`.

See also

types\_typedecorator

Parameters:     

**dialect** \(_Dialect_\)

Return type:     

Optional\[\_LiteralProcessorType\[\_T\]\]

result\_processor\(

    _dialect : Any_,     _coltype : Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#VectorType.result_processor)\#     

result\_processor function for VectorType class.

Parameters:     

  * **dialect** \(_Any_\)

  * **coltype** \(_Any_\)

Return type:     

_Any_

with\_variant\(

    _type\_ : \_TypeEngineArgument\[Any\]_,     _\* dialect\_names: str_, \) → Self\#     

Produce a copy of this type object that will utilize the given type when applied to the dialect of the given name.

e.g.:               from sqlalchemy.types import String     from sqlalchemy.dialects import mysql          string_type = String()          string_type = string_type.with_variant(         mysql.VARCHAR(collation="foo"), "mysql", "mariadb"     )     

The variant mapping indicates that when this type is interpreted by a specific dialect, it will instead be transmuted into the given type, rather than using the primary type.

Changed in version 2.0: the `_types.TypeEngine.with_variant()` method now works with a `_types.TypeEngine` object “in place”, returning a copy of the original type rather than returning a wrapping object; the `Variant` class is no longer used.

Parameters:     

  * **type\_** \(_\_TypeEngineArgument_ _\[__Any_ _\]_\) – a `TypeEngine` that will be selected as a variant from the originating type, when a dialect of the given name is in use.

  * **\*dialect\_names** \(_str_\) – 

one or more base names of the dialect which uses this type. \(i.e. `'postgresql'`, `'mysql'`, etc.\)

Changed in version 2.0: multiple dialect names can be specified for one variant.

Return type:     

Self

See also

types\_with\_variant \- illustrates the use of `_types.TypeEngine.with_variant()`.

__On this page