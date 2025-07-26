# analyze_text — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.wandb_callback.analyze_text.html
**Word Count:** 60
**Links Count:** 181
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# analyze\_text\#

langchain\_community.callbacks.wandb\_callback.analyze\_text\(

    _text : str_,     _complexity\_metrics : bool = True_,     _visualize : bool = True_,     _nlp : Any = None_,     _output\_dir : str | Path | None = None_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/wandb_callback.html#analyze_text)\#     

Analyze text using textstat and spacy.

Parameters:     

  * **text** \(_str_\) – The text to analyze.

  * **complexity\_metrics** \(_bool_\) – Whether to compute complexity metrics.

  * **visualize** \(_bool_\) – Whether to visualize the text.

  * **nlp** \(_spacy.lang_\) – The spacy language model to use for visualization.

  * **output\_dir** \(_str_\) – The directory to save the visualization files to.

Returns:     

A dictionary containing the complexity metrics and visualization     

files serialized in a wandb.Html element.

Return type:     

\(dict\)

__On this page