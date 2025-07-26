# BaseStepContainer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.BaseStepContainer.html
**Word Count:** 57
**Links Count:** 118
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# BaseStepContainer\#

_class _langchain\_experimental.plan\_and\_execute.schema.BaseStepContainer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/schema.html#BaseStepContainer)\#     

Bases: `BaseModel`

Base step container.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod _add\_step\(

    _step : [Step](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Step.html#langchain_experimental.plan_and_execute.schema.Step "langchain_experimental.plan_and_execute.schema.Step")_,     _step\_response : [StepResponse](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/schema.html#BaseStepContainer.add_step)\#     

Add step and step response to the container.

Parameters:     

  * **step** \([_Step_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Step.html#langchain_experimental.plan_and_execute.schema.Step "langchain_experimental.plan_and_execute.schema.Step")\)

  * **step\_response** \([_StepResponse_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")\)

Return type:     

None

_abstractmethod _get\_final\_response\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/schema.html#BaseStepContainer.get_final_response)\#     

Return the final response based on steps taken.

Return type:     

str

__On this page