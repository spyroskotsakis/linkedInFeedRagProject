# MetricsTrackerRollingWindow — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.metrics.MetricsTrackerRollingWindow.html
**Word Count:** 14
**Links Count:** 140
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# MetricsTrackerRollingWindow\#

_class _langchain\_experimental.rl\_chain.metrics.MetricsTrackerRollingWindow\(_window\_size : int_, _step : int_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerRollingWindow)\#     

Metrics Tracker Rolling Window.

Attributes

`score` |    ---|---      Methods

`__init__`\(window\_size, step\) |    ---|---   `on_decision`\(\) |    `on_feedback`\(value\) |    `to_pandas`\(\) |       Parameters:     

  * **window\_size** \(_int_\)

  * **step** \(_int_\)

\_\_init\_\_\(

    _window\_size : int_,     _step : int_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerRollingWindow.__init__)\#     

Parameters:     

  * **window\_size** \(_int_\)

  * **step** \(_int_\)

on\_decision\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerRollingWindow.on_decision)\#     

Return type:     

None

on\_feedback\(

    _value : float_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerRollingWindow.on_feedback)\#     

Parameters:     

**value** \(_float_\)

Return type:     

None

to\_pandas\(\) → pd.DataFrame[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerRollingWindow.to_pandas)\#     

Return type:     

pd.DataFrame

__On this page