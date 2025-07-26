# ToTDFSMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.memory.ToTDFSMemory.html
**Word Count:** 130
**Links Count:** 145
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# ToTDFSMemory\#

_class _langchain\_experimental.tot.memory.ToTDFSMemory\(

    _stack : List\[[Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory)\#     

Memory for the Tree of Thought \(ToT\) chain.

It is implemented as a stack of thoughts. This allows for a depth first search \(DFS\) of the ToT.

Attributes

`level` | Return the current level of the stack.   ---|---      Methods

`__init__`\(\[stack\]\) |    ---|---   `current_path`\(\) | Return the thoughts path.   `pop`\(\[n\]\) | Pop the top n elements of the stack and return the last one.   `store`\(node\) | Add a node on the top of the stack.   `top`\(\) | Get the top of the stack without popping it.   `top_parent`\(\) | Get the parent of the top of the stack without popping it.      Parameters:     

**stack** \(_Optional_ _\[__List_ _\[_[_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") _\]__\]_\)

\_\_init\_\_\(

    _stack : List\[[Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory.__init__)\#     

Parameters:     

**stack** \(_List_ _\[_[_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") _\]__|__None_\)

current\_path\(\) → List\[[Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory.current_path)\#     

Return the thoughts path.

Return type:     

_List_\[[_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought")\]

pop\(

    _n : int = 1_, \) → [Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory.pop)\#     

Pop the top n elements of the stack and return the last one.

Parameters:     

**n** \(_int_\)

Return type:     

[_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") | None

store\(

    _node : [Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory.store)\#     

Add a node on the top of the stack.

Parameters:     

**node** \([_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought")\)

Return type:     

None

top\(\) → [Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory.top)\#     

Get the top of the stack without popping it.

Return type:     

[_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") | None

top\_parent\(\) → [Thought](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/memory.html#ToTDFSMemory.top_parent)\#     

Get the parent of the top of the stack without popping it.

Return type:     

[_Thought_](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought "langchain_experimental.tot.thought.Thought") | None

__On this page