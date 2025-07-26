# SteamWebAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.steam.SteamWebAPIWrapper.html
**Word Count:** 80
**Links Count:** 281
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# SteamWebAPIWrapper\#

_class _langchain\_community.utilities.steam.SteamWebAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Steam API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _operations _: List\[dict\]__ = \[\{'description': '\n This tool is a wrapper around python-steam-api\'s steam.apps.search\_games API and \n steam.apps.get\_app\_details API, useful when you need to search for a game.\n The input to this tool is a string specifying the name of the game you want to \n search for. For example, to search for a game called "Counter-Strike: Global \n Offensive", you would input "Counter-Strike: Global Offensive" as the game name.\n This input will be passed into steam.apps.search\_games to find the game id, link \n and price, and then the game id will be passed into steam.apps.get\_app\_details to \n get the detailed description and supported languages of the game. Finally the \n results are combined and returned as a string.\n', 'mode': 'get\_game\_details', 'name': 'Get Game Details'\}, \{'description': '\n This tool is a wrapper around python-steam-api\'s steam.users.get\_owned\_games API \n and steamspypi\'s steamspypi.download API, useful when you need to get a list of \n recommended games. The input to this tool is a string specifying the steam id of \n the user you want to get recommended games for. For example, to get recommended \n games for a user with steam id 76561197960435530, you would input \n "76561197960435530" as the steam id. This steamid is then utilized to form a \n data\_request sent to steamspypi\'s steamspypi.download to retrieve genres of user\'s \n owned games. Then, calculates the frequency of each genre, identifying the most \n popular one, and stored it in a dictionary. Subsequently, use steamspypi.download\n to returns all games in this genre and return 5 most-played games that is not owned\n by the user.\n\n', 'mode': 'get\_recommended\_games', 'name': 'Get Recommended Games'\}\]_\#     

_param _steam _: Any_ _ = None_\#     

details\_of\_games\(_name : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.details_of_games)\#     

Parameters:     

**name** \(_str_\)

Return type:     

str

get\_id\_link\_price\(_games : dict_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.get_id_link_price)\#     

The response may contain more than one game, so we need to choose the right one and return the id.

Parameters:     

**games** \(_dict_\)

Return type:     

dict

get\_operations\(\) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.get_operations)\#     

Return a list of operations.

Return type:     

_List_\[dict\]

get\_steam\_id\(_name : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.get_steam_id)\#     

Parameters:     

**name** \(_str_\)

Return type:     

str

get\_users\_games\(

    _steam\_id : str_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.get_users_games)\#     

Parameters:     

**steam\_id** \(_str_\)

Return type:     

_List_\[str\]

parse\_to\_str\(_details : dict_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.parse_to_str)\#     

Parse the details result.

Parameters:     

**details** \(_dict_\)

Return type:     

str

recommended\_games\(_steam\_id : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.recommended_games)\#     

Parameters:     

**steam\_id** \(_str_\)

Return type:     

str

remove\_html\_tags\(_html\_string : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.remove_html_tags)\#     

Parameters:     

**html\_string** \(_str_\)

Return type:     

str

run\(_mode : str_, _game : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/steam.html#SteamWebAPIWrapper.run)\#     

Parameters:     

  * **mode** \(_str_\)

  * **game** \(_str_\)

Return type:     

str

Examples using SteamWebAPIWrapper

  * [Steam Toolkit](https://python.langchain.com/docs/integrations/tools/steam/)

__On this page