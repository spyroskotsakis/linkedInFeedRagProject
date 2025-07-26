# TwilioAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.twilio.TwilioAPIWrapper.html
**Word Count:** 173
**Links Count:** 265
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# TwilioAPIWrapper\#

_class _langchain\_community.utilities.twilio.TwilioAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/twilio.html#TwilioAPIWrapper)\#     

Bases: `BaseModel`

Messaging Client using Twilio.

To use, you should have the `twilio` python package installed, and the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_FROM_NUMBER`, or pass account\_sid, auth\_token, and from\_number as named parameters to the constructor.

Example               from langchain_community.utilities.twilio import TwilioAPIWrapper     twilio = TwilioAPIWrapper(         account_sid="ACxxx",         auth_token="xxx",         from_number="+10123456789"     )     twilio.run('test', '+12484345508')     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _account\_sid _: str | None_ _ = None_\#     

Twilio account string identifier.

_param _auth\_token _: str | None_ _ = None_\#     

Twilio auth token.

_param _from\_number _: str | None_ _ = None_\#     

A Twilio phone number in \[E.164\]\(<https://www.twilio.com/docs/glossary/what-e164>\) format, an \[alphanumeric sender ID\]\(<https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id>\), or a \[Channel Endpoint address\]\(<https://www.twilio.com/docs/sms/channels#channel-addresses>\) that is enabled for the type of message you want to send. Phone numbers or \[short codes\]\(<https://www.twilio.com/docs/sms/api/short-code>\) purchased from Twilio also work here. You cannot, for example, spoof messages from a private cell phone number. If you are using messaging\_service\_sid, this parameter must be empty.

run\(_body : str_, _to : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/twilio.html#TwilioAPIWrapper.run)\#     

Run body through Twilio and respond with message sid.

Parameters:     

  * **body** \(_str_\) – The text of the message you want to send. Can be up to 1,600 characters in length.

  * **to** \(_str_\) – The destination phone number in \[E.164\]\(<https://www.twilio.com/docs/glossary/what-e164>\) format for SMS/MMS or \[Channel user address\]\(<https://www.twilio.com/docs/sms/channels#channel-addresses>\) for other 3rd-party channels.

Return type:     

str

Examples using TwilioAPIWrapper

  * [Twilio](https://python.langchain.com/docs/integrations/tools/twilio/)

__On this page