# tee_peer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.iter.tee_peer.html
**Word Count:** 78
**Links Count:** 166
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# tee\_peer\#

langchain\_core.utils.iter.tee\_peer\(

    _iterator : Iterator\[T\]_,     _buffer : deque\[T\]_,     _peers : list\[deque\[T\]\]_,     _lock : AbstractContextManager\[Any\]_, \) → Generator\[T, None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/iter.html#tee_peer)\#     

An individual iterator of a `tee()`.

This function is a generator that yields items from the shared iterator `iterator`. It buffers items until the least advanced iterator has yielded them as well. The buffer is shared with all other peers.

Parameters:     

  * **iterator** \(_Iterator_ _\[__T_ _\]_\) – The shared iterator.

  * **buffer** \(_deque_ _\[__T_ _\]_\) – The buffer for this peer.

  * **peers** \(_list_ _\[__deque_ _\[__T_ _\]__\]_\) – The buffers of all peers.

  * **lock** \(_AbstractContextManager_ _\[__Any_ _\]_\) – The lock to synchronise access to the shared buffers.

Yields:     

The next item from the shared iterator.

Return type:     

_Generator_\[_T_ , None, None\]

__On this page