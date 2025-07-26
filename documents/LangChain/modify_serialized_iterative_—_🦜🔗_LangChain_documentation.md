# modify_serialized_iterative — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.tracers.wandb.modify_serialized_iterative.html
**Word Count:** 108
**Links Count:** 181
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# modify\_serialized\_iterative\#

langchain\_community.callbacks.tracers.wandb.modify\_serialized\_iterative\(

    _runs : List\[Dict\[str, Any\]\]_,     _exact\_keys : Tuple\[str, ...\] = \(\)_,     _partial\_keys : Tuple\[str, ...\] = \(\)_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/tracers/wandb.html#modify_serialized_iterative)\#     

Utility to modify the serialized field of a list of runs dictionaries. removes any keys that match the exact\_keys and any keys that contain any of the partial\_keys. recursively moves the dictionaries under the kwargs key to the top level. changes the “id” field to a string “\_kind” field that tells WBTraceTree how to visualize the run. promotes the “serialized” field to the top level. :param runs: The list of runs to modify. :param exact\_keys: A tuple of keys to remove from the serialized field. :param partial\_keys: A tuple of partial keys to remove from the serialized

> field.

Returns:     

The modified list of runs.

Parameters:     

  * **runs** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **exact\_keys** \(_Tuple_ _\[__str_ _,__...__\]_\)

  * **partial\_keys** \(_Tuple_ _\[__str_ _,__...__\]_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

__On this page