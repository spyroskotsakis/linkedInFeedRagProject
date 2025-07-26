# TracerSessionBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.schemas.TracerSessionBase.html
**Word Count:** 321
**Links Count:** 189
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# TracerSessionBase\#

_class _langchain\_core.tracers.schemas.TracerSessionBase\(

    _\*_ ,     _start\_time : datetime = None_,     _name : str | None = None_,     _extra : dict\[str, Any\] | None = None_,     _tenant\_id : UUID_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/schemas.html#TracerSessionBase)\#     

Deprecated since version 0.1.0: It will not be removed until langchain-core==1.0.

Base class for TracerSession.

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

Attributes

Methods

`__init__`\(\*\*data\) | Create a new model by parsing and validating input data from keyword arguments.   ---|---   `construct`\(\[\_fields\_set\]\) | Creates a new model setting \_\_dict\_\_ and \_\_fields\_set\_\_ from trusted or pre-validated data.   `copy`\(\*\[, include, exclude, update, deep\]\) | Duplicate a model, optionally choose which fields to include, exclude and change.   `dict`\(\*\[, include, exclude, by\_alias, ...\]\) | Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.   `from_orm`\(obj\) |    `json`\(\*\[, include, exclude, by\_alias, ...\]\) | Generate a JSON representation of the model, include and exclude arguments as per dict\(\).   `parse_file`\(path, \*\[, content\_type, ...\]\) |    `parse_obj`\(obj\) |    `parse_raw`\(b, \*\[, content\_type, encoding, ...\]\) |    `schema`\(\[by\_alias, ref\_template\]\) |    `schema_json`\(\*\[, by\_alias, ref\_template\]\) |    `update_forward_refs`\(\*\*localns\) | Try to update ForwardRefs on fields based on this Model, globalns and localns.   `validate`\(value\) |       Parameters:     

  * **start\_time** \(_datetime_\)

  * **name** \(_str_ _|__None_\)

  * **extra** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **tenant\_id** \(_UUID_\)

\_\_init\_\_\(_\*\* data: Any_\) → None\#     

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

Parameters:     

**data** \(_Any_\)

Return type:     

None

_classmethod _construct\(

    _\_fields\_set : SetStr | None = None_,     _\*\* values: Any_, \) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Creates a new model setting \_\_dict\_\_ and \_\_fields\_set\_\_ from trusted or pre-validated data. Default values are respected, but no other validation is performed. Behaves as if Config.extra = ‘allow’ was set since it adds all passed values

Parameters:     

  * **\_fields\_set** \(_SetStr_ _|__None_\)

  * **values** \(_Any_\)

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

copy\(

    _\*_ ,     _include : AbstractSetIntStr | MappingIntStrAny | None = None_,     _exclude : AbstractSetIntStr | MappingIntStrAny | None = None_,     _update : DictStrAny | None = None_,     _deep : bool = False_, \) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Duplicate a model, optionally choose which fields to include, exclude and change.

Parameters:     

  * **include** \(_AbstractSetIntStr_ _|__MappingIntStrAny_ _|__None_\) – fields to include in new model

  * **exclude** \(_AbstractSetIntStr_ _|__MappingIntStrAny_ _|__None_\) – fields to exclude from new model, as with values this takes precedence over include

  * **update** \(_DictStrAny_ _|__None_\) – values to change/add in the new model. Note: the data is not validated before creating the new model: you should trust this data

  * **deep** \(_bool_\) – set to True to make a deep copy of the model

  * **self** \([_Model_](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\)

Returns:     

new model instance

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

dict\(

    _\*_ ,     _include : AbstractSetIntStr | MappingIntStrAny | None = None_,     _exclude : AbstractSetIntStr | MappingIntStrAny | None = None_,     _by\_alias : bool = False_,     _skip\_defaults : bool | None = None_,     _exclude\_unset : bool = False_,     _exclude\_defaults : bool = False_,     _exclude\_none : bool = False_, \) → DictStrAny\#     

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:     

  * **include** \(_AbstractSetIntStr_ _|__MappingIntStrAny_ _|__None_\)

  * **exclude** \(_AbstractSetIntStr_ _|__MappingIntStrAny_ _|__None_\)

  * **by\_alias** \(_bool_\)

  * **skip\_defaults** \(_bool_ _|__None_\)

  * **exclude\_unset** \(_bool_\)

  * **exclude\_defaults** \(_bool_\)

  * **exclude\_none** \(_bool_\)

Return type:     

DictStrAny

_classmethod _from\_orm\(_obj : Any_\) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Parameters:     

**obj** \(_Any_\)

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

json\(

    _\*_ ,     _include : AbstractSetIntStr | MappingIntStrAny | None = None_,     _exclude : AbstractSetIntStr | MappingIntStrAny | None = None_,     _by\_alias : bool = False_,     _skip\_defaults : bool | None = None_,     _exclude\_unset : bool = False_,     _exclude\_defaults : bool = False_,     _exclude\_none : bool = False_,     _encoder : Callable\[\[Any\], Any\] | None = None_,     _models\_as\_dict : bool = True_,     _\*\* dumps\_kwargs: Any_, \) → str\#     

Generate a JSON representation of the model, include and exclude arguments as per dict\(\).

encoder is an optional function to supply as default to json.dumps\(\), other arguments as per json.dumps\(\).

Parameters:     

  * **include** \(_AbstractSetIntStr_ _|__MappingIntStrAny_ _|__None_\)

  * **exclude** \(_AbstractSetIntStr_ _|__MappingIntStrAny_ _|__None_\)

  * **by\_alias** \(_bool_\)

  * **skip\_defaults** \(_bool_ _|__None_\)

  * **exclude\_unset** \(_bool_\)

  * **exclude\_defaults** \(_bool_\)

  * **exclude\_none** \(_bool_\)

  * **encoder** \(_Callable_ _\[__\[__Any_ _\]__,__Any_ _\]__|__None_\)

  * **models\_as\_dict** \(_bool_\)

  * **dumps\_kwargs** \(_Any_\)

Return type:     

str

_classmethod _parse\_file\(

    _path : str | Path_,     _\*_ ,     _content\_type : str = None_,     _encoding : str = 'utf8'_,     _proto : Protocol = None_,     _allow\_pickle : bool = False_, \) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Parameters:     

  * **path** \(_str_ _|__Path_\)

  * **content\_type** \(_str_\)

  * **encoding** \(_str_\)

  * **proto** \(_Protocol_\)

  * **allow\_pickle** \(_bool_\)

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

_classmethod _parse\_obj\(_obj : Any_\) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Parameters:     

**obj** \(_Any_\)

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

_classmethod _parse\_raw\(

    _b : str | bytes_,     _\*_ ,     _content\_type : str = None_,     _encoding : str = 'utf8'_,     _proto : Protocol = None_,     _allow\_pickle : bool = False_, \) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Parameters:     

  * **b** \(_str_ _|__bytes_\)

  * **content\_type** \(_str_\)

  * **encoding** \(_str_\)

  * **proto** \(_Protocol_\)

  * **allow\_pickle** \(_bool_\)

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

_classmethod _schema\(

    _by\_alias : bool = True_,     _ref\_template : str = '\#/definitions/\{model\}'_, \) → DictStrAny\#     

Parameters:     

  * **by\_alias** \(_bool_\)

  * **ref\_template** \(_str_\)

Return type:     

DictStrAny

_classmethod _schema\_json\(

    _\*_ ,     _by\_alias : bool = True_,     _ref\_template : str = '\#/definitions/\{model\}'_,     _\*\* dumps\_kwargs: Any_, \) → str\#     

Parameters:     

  * **by\_alias** \(_bool_\)

  * **ref\_template** \(_str_\)

  * **dumps\_kwargs** \(_Any_\)

Return type:     

str

_classmethod _update\_forward\_refs\(

    _\*\* localns: Any_, \) → None\#     

Try to update ForwardRefs on fields based on this Model, globalns and localns.

Parameters:     

**localns** \(_Any_\)

Return type:     

None

_classmethod _validate\(_value : Any_\) → [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")\#     

Parameters:     

**value** \(_Any_\)

Return type:     

[Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)