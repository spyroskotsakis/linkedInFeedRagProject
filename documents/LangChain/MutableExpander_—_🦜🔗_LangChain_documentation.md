# MutableExpander — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.mutable_expander.MutableExpander.html
**Word Count:** 216
**Links Count:** 207
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# MutableExpander\#

_class _langchain\_community.callbacks.streamlit.mutable\_expander.MutableExpander\(

    _parent\_container : DeltaGenerator_,     _label : str_,     _expanded : bool_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander)\#     

Streamlit expander that can be renamed and dynamically expanded/collapsed.

Create a new MutableExpander.

Parameters:     

  * **parent\_container** \(_DeltaGenerator_\) – 

The st.container that the expander will be created inside.

The expander transparently deletes and recreates its underlying st.expander instance when its label changes, and it uses parent\_container to ensure it recreates this underlying expander in the same location onscreen.

  * **label** \(_str_\) – The expander’s initial label.

  * **expanded** \(_bool_\) – The expander’s initial expanded value.

Attributes

`expanded` | True if the expander was created with expanded=True.   ---|---   `label` | Expander's label string.      Methods

`__init__`\(parent\_container, label, expanded\) | Create a new MutableExpander.   ---|---   `append_copy`\(other\) | Append a copy of another MutableExpander's children to this MutableExpander.   `clear`\(\) | Remove the container and its contents entirely.   `exception`\(exception, \*\[, index\]\) | Add an Exception element to the container and return its index.   `markdown`\(body\[, unsafe\_allow\_html, help, index\]\) | Add a Markdown element to the container and return its index.   `update`\(\*\[, new\_label, new\_expanded\]\) | Change the expander's label and expanded state      \_\_init\_\_\(

    _parent\_container : DeltaGenerator_,     _label : str_,     _expanded : bool_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander.__init__)\#     

Create a new MutableExpander.

Parameters:     

  * **parent\_container** \(_DeltaGenerator_\) – 

The st.container that the expander will be created inside.

The expander transparently deletes and recreates its underlying st.expander instance when its label changes, and it uses parent\_container to ensure it recreates this underlying expander in the same location onscreen.

  * **label** \(_str_\) – The expander’s initial label.

  * **expanded** \(_bool_\) – The expander’s initial expanded value.

append\_copy\(

    _other : MutableExpander_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander.append_copy)\#     

Append a copy of another MutableExpander’s children to this MutableExpander.

Parameters:     

**other** \(_MutableExpander_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander.clear)\#     

Remove the container and its contents entirely. A cleared container can’t be reused.

Return type:     

None

exception\(

    _exception : BaseException_,     _\*_ ,     _index : int | None = None_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander.exception)\#     

Add an Exception element to the container and return its index.

Parameters:     

  * **exception** \(_BaseException_\)

  * **index** \(_int_ _|__None_\)

Return type:     

int

markdown\(

    _body : SupportsStr_,     _unsafe\_allow\_html : bool = False_,     _\*_ ,     _help : str | None = None_,     _index : int | None = None_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander.markdown)\#     

Add a Markdown element to the container and return its index.

Parameters:     

  * **body** \(_SupportsStr_\)

  * **unsafe\_allow\_html** \(_bool_\)

  * **help** \(_Optional_ _\[__str_ _\]_\)

  * **index** \(_Optional_ _\[__int_ _\]_\)

Return type:     

int

update\(

    _\*_ ,     _new\_label : str | None = None_,     _new\_expanded : bool | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#MutableExpander.update)\#     

Change the expander’s label and expanded state

Parameters:     

  * **new\_label** \(_str_ _|__None_\)

  * **new\_expanded** \(_bool_ _|__None_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)