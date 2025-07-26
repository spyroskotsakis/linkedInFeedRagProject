# MetricsTrackerAverage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.metrics.MetricsTrackerAverage.html
**Word Count:** 12
**Links Count:** 140
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# MetricsTrackerAverage\#

_class _langchain\_experimental.rl\_chain.metrics.MetricsTrackerAverage\(_step : int_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerAverage)\#     

Metrics Tracker Average.

Attributes

`score` |    ---|---      Methods

`__init__`\(step\) |    ---|---   `on_decision`\(\) |    `on_feedback`\(score\) |    `to_pandas`\(\) |       Parameters:     

**step** \(_int_\)

\_\_init\_\_\(_step : int_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerAverage.__init__)\#     

Parameters:     

**step** \(_int_\)

on\_decision\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerAverage.on_decision)\#     

Return type:     

None

on\_feedback\(_score : float_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerAverage.on_feedback)\#     

Parameters:     

**score** \(_float_\)

Return type:     

None

to\_pandas\(\) → pd.DataFrame[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/metrics.html#MetricsTrackerAverage.to_pandas)\#     

Return type:     

pd.DataFrame

__On this page