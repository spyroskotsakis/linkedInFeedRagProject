# MlflowLogger — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.mlflow_callback.MlflowLogger.html
**Word Count:** 223
**Links Count:** 225
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# MlflowLogger\#

_class _langchain\_community.callbacks.mlflow\_callback.MlflowLogger\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger)\#     

Callback Handler that logs metrics and artifacts to mlflow server.

Parameters:     

  * **name** \(_str_\) – Name of the run.

  * **experiment** \(_str_\) – Name of the experiment.

  * **tags** \(_dict_\) – Tags to be attached for the run.

  * **tracking\_uri** \(_str_\) – MLflow tracking server uri.

  * **kwargs** \(_Any_\)

This handler implements the helper functions to initialize, log metrics and artifacts to the mlflow server.

Methods

`__init__`\(\*\*kwargs\) |    ---|---   `artifact`\(path\) | To upload the file from given path as artifact.   `finish_run`\(\) | To finish the run.   `html`\(html, filename\) | To log the input html string as html file artifact.   `jsonf`\(data, filename\) | To log the input data as json file artifact.   `langchain_artifact`\(chain\) |    `metric`\(key, value\) | To log metric to mlflow server.   `metrics`\(data\[, step\]\) | To log all metrics in the input dict.   `start_run`\(name, tags\[, run\_id\]\) | If run\_id is provided, it will reuse the run with the given run\_id.   `table`\(name, dataframe\) | To log the input pandas dataframe as a html table   `text`\(text, filename\) | To log the input text as text file artifact.      \_\_init\_\_\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.__init__)\#     

Parameters:     

**kwargs** \(_Any_\)

artifact\(_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.artifact)\#     

To upload the file from given path as artifact.

Parameters:     

**path** \(_str_\)

Return type:     

None

finish\_run\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.finish_run)\#     

To finish the run.

Return type:     

None

html\(_html : str_, _filename : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.html)\#     

To log the input html string as html file artifact.

Parameters:     

  * **html** \(_str_\)

  * **filename** \(_str_\)

Return type:     

None

jsonf\(

    _data : Dict\[str, Any\]_,     _filename : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.jsonf)\#     

To log the input data as json file artifact.

Parameters:     

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **filename** \(_str_\)

Return type:     

None

langchain\_artifact\(_chain : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.langchain_artifact)\#     

Parameters:     

**chain** \(_Any_\)

Return type:     

None

metric\(_key : str_, _value : float_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.metric)\#     

To log metric to mlflow server.

Parameters:     

  * **key** \(_str_\)

  * **value** \(_float_\)

Return type:     

None

metrics\(

    _data : Dict\[str, float\] | Dict\[str, int\]_,     _step : int | None = 0_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.metrics)\#     

To log all metrics in the input dict.

Parameters:     

  * **data** \(_Dict_ _\[__str_ _,__float_ _\]__|__Dict_ _\[__str_ _,__int_ _\]_\)

  * **step** \(_int_ _|__None_\)

Return type:     

None

start\_run\(

    _name : str_,     _tags : Dict\[str, str\]_,     _run\_id : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.start_run)\#     

If run\_id is provided, it will reuse the run with the given run\_id. Otherwise, it starts a new run, auto generates the random suffix for name.

Parameters:     

  * **name** \(_str_\)

  * **tags** \(_Dict_ _\[__str_ _,__str_ _\]_\)

  * **run\_id** \(_str_ _|__None_\)

Return type:     

None

table\(

    _name : str_,     _dataframe : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.table)\#     

To log the input pandas dataframe as a html table

Parameters:     

  * **name** \(_str_\)

  * **dataframe** \(_Any_\)

Return type:     

None

text\(_text : str_, _filename : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/mlflow_callback.html#MlflowLogger.text)\#     

To log the input text as text file artifact.

Parameters:     

  * **text** \(_str_\)

  * **filename** \(_str_\)

Return type:     

None

__On this page