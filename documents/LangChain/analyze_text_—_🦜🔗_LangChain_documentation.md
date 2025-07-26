# analyze_text — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.flyte_callback.analyze_text.html
**Word Count:** 38
**Links Count:** 181
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# analyze\_text\#

langchain\_community.callbacks.flyte\_callback.analyze\_text\(

    _text : str_,     _nlp : Any = None_,     _textstat : Any = None_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/flyte_callback.html#analyze_text)\#     

Analyze text using textstat and spacy.

Parameters:     

  * **text** \(_str_\) – The text to analyze.

  * **nlp** \(_spacy.lang_\) – The spacy language model to use for visualization.

  * **textstat** \(_Any_\)

Returns:     

A dictionary containing the complexity metrics and visualization     

files serialized to HTML string.

Return type:     

\(dict\)

__On this page