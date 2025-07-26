# AsciiCanvas — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_ascii.AsciiCanvas.html
**Word Count:** 254
**Links Count:** 214
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# AsciiCanvas\#

_class _langchain\_core.runnables.graph\_ascii.AsciiCanvas\(_cols : int_, _lines : int_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas)\#     

Class for drawing in ASCII.

Create an ASCII canvas.

Parameters:     

  * **cols** \(_int_\) – number of columns in the canvas. Should be > 1.

  * **lines** \(_int_\) – number of lines in the canvas. Should be > 1.

Attributes

`TIMEOUT` |    ---|---      Methods

`__init__`\(cols, lines\) | Create an ASCII canvas.   ---|---   `box`\(x0, y0, width, height\) | Create a box on ASCII canvas.   `draw`\(\) | Draws ASCII canvas on the screen.   `line`\(x0, y0, x1, y1, char\) | Create a line on ASCII canvas.   `point`\(x, y, char\) | Create a point on ASCII canvas.   `text`\(x, y, text\) | Print a text on ASCII canvas.      \_\_init\_\_\(_cols : int_, _lines : int_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas.__init__)\#     

Create an ASCII canvas.

Parameters:     

  * **cols** \(_int_\) – number of columns in the canvas. Should be > 1.

  * **lines** \(_int_\) – number of lines in the canvas. Should be > 1.

Return type:     

None

box\(

    _x0 : int_,     _y0 : int_,     _width : int_,     _height : int_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas.box)\#     

Create a box on ASCII canvas.

Parameters:     

  * **x0** \(_int_\) – x coordinate of the box corner.

  * **y0** \(_int_\) – y coordinate of the box corner.

  * **width** \(_int_\) – box width.

  * **height** \(_int_\) – box height.

Return type:     

None

draw\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas.draw)\#     

Draws ASCII canvas on the screen.

Return type:     

str

line\(

    _x0 : int_,     _y0 : int_,     _x1 : int_,     _y1 : int_,     _char : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas.line)\#     

Create a line on ASCII canvas.

Parameters:     

  * **x0** \(_int_\) – x coordinate where the line should start.

  * **y0** \(_int_\) – y coordinate where the line should start.

  * **x1** \(_int_\) – x coordinate where the line should end.

  * **y1** \(_int_\) – y coordinate where the line should end.

  * **char** \(_str_\) – character to draw the line with.

Return type:     

None

point\(_x : int_, _y : int_, _char : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas.point)\#     

Create a point on ASCII canvas.

Parameters:     

  * **x** \(_int_\) – x coordinate. Should be >= 0 and < number of columns in the canvas.

  * **y** \(_int_\) – y coordinate. Should be >= 0 an < number of lines in the canvas.

  * **char** \(_str_\) – character to place in the specified point on the canvas.

Return type:     

None

text\(_x : int_, _y : int_, _text : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#AsciiCanvas.text)\#     

Print a text on ASCII canvas.

Parameters:     

  * **x** \(_int_\) – x coordinate where the text should start.

  * **y** \(_int_\) – y coordinate where the text should start.

  * **text** \(_str_\) – string that should be printed.

Return type:     

None

__On this page