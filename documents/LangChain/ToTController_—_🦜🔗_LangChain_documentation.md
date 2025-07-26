# ToTController — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.controller.ToTController.html
**Word Count:** 65
**Links Count:** 111
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# ToTController\#

_class _langchain\_experimental.tot.controller.ToTController\(_c : int = 3_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/controller.html#ToTController)\#     

Tree of Thought \(ToT\) controller.

This is a version of a ToT controller, dubbed in the paper as a “Simple Controller”.

It has one parameter c which is the number of children to explore for each thought.

Initialize the controller.

Parameters:     

**c** \(_int_\) – The number of children to explore at each node.

Methods

`__init__`\(\[c\]\) | Initialize the controller.   ---|---      \_\_init\_\_\(_c : int = 3_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/controller.html#ToTController.__init__)\#     

Initialize the controller.

Parameters:     

**c** \(_int_\) – The number of children to explore at each node.

__On this page