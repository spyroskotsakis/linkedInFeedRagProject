# create_aws_client — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.create_aws_client.html
**Word Count:** 87
**Links Count:** 87
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# create\_aws\_client\#

langchain\_aws.utils.create\_aws\_client\(

    _service\_name : str_,     _region\_name : str | None = None_,     _credentials\_profile\_name : str | None = None_,     _aws\_access\_key\_id : SecretStr | None = None_,     _aws\_secret\_access\_key : SecretStr | None = None_,     _aws\_session\_token : SecretStr | None = None_,     _endpoint\_url : str | None = None_,     _config : Any = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utils.html#create_aws_client)\#     

Helper function to validate AWS credentials and create an AWS client.

Parameters:     

  * **service\_name** \(_str_\) – The name of the AWS service to create a client for.

  * **region\_name** \(_str_ _|__None_\) – AWS region name. If not provided, will try to get from environment variables.

  * **credentials\_profile\_name** \(_str_ _|__None_\) – The name of the AWS credentials profile to use.

  * **aws\_access\_key\_id** \(_SecretStr_ _|__None_\) – AWS access key ID.

  * **aws\_secret\_access\_key** \(_SecretStr_ _|__None_\) – AWS secret access key.

  * **aws\_session\_token** \(_SecretStr_ _|__None_\) – AWS session token.

  * **endpoint\_url** \(_str_ _|__None_\) – The complete URL to use for the constructed client.

  * **config** \(_Any_\) – Advanced client configuration options.

Returns:     

An AWS service client instance.

Return type:     

boto3.client

__On this page