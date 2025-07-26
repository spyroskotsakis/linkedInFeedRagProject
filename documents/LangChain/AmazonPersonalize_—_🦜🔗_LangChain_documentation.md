# AmazonPersonalize — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/recommenders/langchain_experimental.recommenders.amazon_personalize.AmazonPersonalize.html
**Word Count:** 289
**Links Count:** 111
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# AmazonPersonalize\#

_class _langchain\_experimental.recommenders.amazon\_personalize.AmazonPersonalize\(

    _campaign\_arn : str | None = None_,     _recommender\_arn : str | None = None_,     _client : Any | None = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/recommenders/amazon_personalize.html#AmazonPersonalize)\#     

Amazon Personalize Runtime wrapper for executing real-time operations.

See \[this link for more details\]\(<https://docs.aws.amazon.com/personalize/latest/dg/API_Operations_Amazon_Personalize_Runtime.html>\).

Parameters:     

  * **campaign\_arn** \(_str_ _|__None_\) – str, Optional: The Amazon Resource Name \(ARN\) of the campaign to use for getting recommendations.

  * **recommender\_arn** \(_str_ _|__None_\) – str, Optional: The Amazon Resource Name \(ARN\) of the recommender to use to get recommendations

  * **client** \(_Any_ _|__None_\) – Optional: boto3 client

  * **credentials\_profile\_name** \(_str_ _|__None_\) – str, Optional :AWS profile name

  * **region\_name** \(_str_ _|__None_\) – str, Optional: AWS region, e.g., us-west-2

Example               

personalize\_client = AmazonPersonalize \(     

campaignArn=’<my-campaign-arn>’ \)

Methods

`__init__`\(\[campaign\_arn, recommender\_arn, ...\]\) |    ---|---   `get_personalized_ranking`\(user\_id, input\_list\) | Re-ranks a list of recommended items for the given user.   `get_recommendations`\(\[user\_id, item\_id, ...\]\) | Get recommendations from Amazon Personalize service.      \_\_init\_\_\(

    _campaign\_arn : str | None = None_,     _recommender\_arn : str | None = None_,     _client : Any | None = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/recommenders/amazon_personalize.html#AmazonPersonalize.__init__)\#     

Parameters:     

  * **campaign\_arn** \(_str_ _|__None_\)

  * **recommender\_arn** \(_str_ _|__None_\)

  * **client** \(_Any_ _|__None_\)

  * **credentials\_profile\_name** \(_str_ _|__None_\)

  * **region\_name** \(_str_ _|__None_\)

get\_personalized\_ranking\(

    _user\_id : str_,     _input\_list : List\[str\]_,     _filter\_arn : str | None = None_,     _filter\_values : Mapping\[str, str\] | None = None_,     _context : Mapping\[str, str\] | None = None_,     _metadata\_columns : Mapping\[str, Sequence\[str\]\] | None = None_,     _\*\* kwargs: Any_, \) → Mapping\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/recommenders/amazon_personalize.html#AmazonPersonalize.get_personalized_ranking)\#     

Re-ranks a list of recommended items for the given user.

<https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetPersonalizedRanking.html>

Parameters:     

  * **user\_id** \(_str_\) – str, Required: The user identifier for which to retrieve recommendations

  * **input\_list** \(_List_ _\[__str_ _\]_\) – List\[str\], Required: A list of items \(by itemId\) to rank

  * **filter\_arn** \(_str_ _|__None_\) – str, Optional: The ARN of the filter to apply

  * **filter\_values** \(_Mapping_ _\[__str_ _,__str_ _\]__|__None_\) – Mapping, Optional: The values to use when filtering recommendations.

  * **context** \(_Mapping_ _\[__str_ _,__str_ _\]__|__None_\) – Mapping, Optional: The contextual metadata to use when getting recommendations

  * **metadata\_columns** \(_Mapping_ _\[__str_ _,__Sequence_ _\[__str_ _\]__\]__|__None_\) – Mapping, Optional: The metadata Columns to be returned as part of the response.

  * **kwargs** \(_Any_\)

Returns:     

Mapping\[str, Any\]: Returns personalizedRanking     

and recommendationId.

Return type:     

response

Example               

personalize\_client = AmazonPersonalize\(campaignArn=’<my-campaign-arn>’ \)

response = personalize\_client.get\_personalized\_ranking\(user\_id=”1”,     

input\_list=\[“123,”256”\]\)

get\_recommendations\(

    _user\_id : str | None = None_,     _item\_id : str | None = None_,     _filter\_arn : str | None = None_,     _filter\_values : Mapping\[str, str\] | None = None_,     _num\_results : int | None = 10_,     _context : Mapping\[str, str\] | None = None_,     _promotions : Sequence\[Mapping\[str, Any\]\] | None = None_,     _metadata\_columns : Mapping\[str, Sequence\[str\]\] | None = None_,     _\*\* kwargs: Any_, \) → Mapping\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/recommenders/amazon_personalize.html#AmazonPersonalize.get_recommendations)\#     

Get recommendations from Amazon Personalize service.

See more details at: <https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html>

Parameters:     

  * **user\_id** \(_str_ _|__None_\) – str, Optional: The user identifier for which to retrieve recommendations

  * **item\_id** \(_str_ _|__None_\) – str, Optional: The item identifier for which to retrieve recommendations

  * **filter\_arn** \(_str_ _|__None_\) – str, Optional: The ARN of the filter to apply to the returned recommendations

  * **filter\_values** \(_Mapping_ _\[__str_ _,__str_ _\]__|__None_\) – Mapping, Optional: The values to use when filtering recommendations.

  * **num\_results** \(_int_ _|__None_\) – int, Optional: Default=10: The number of results to return

  * **context** \(_Mapping_ _\[__str_ _,__str_ _\]__|__None_\) – Mapping, Optional: The contextual metadata to use when getting recommendations

  * **promotions** \(_Sequence_ _\[__Mapping_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Sequence, Optional: The promotions to apply to the recommendation request.

  * **metadata\_columns** \(_Mapping_ _\[__str_ _,__Sequence_ _\[__str_ _\]__\]__|__None_\) – Mapping, Optional: The metadata Columns to be returned as part of the response.

  * **kwargs** \(_Any_\)

Returns:     

Mapping\[str, Any\]: Returns an itemList and recommendationId.

Return type:     

response

Example               

personalize\_client = AmazonPersonalize\(campaignArn=’<my-campaign-arn>’ \)

response = personalize\_client.get\_recommendations\(user\_id=”1”\)

__On this page