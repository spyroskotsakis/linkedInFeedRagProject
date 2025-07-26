# create_structured_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/chains/langchain_google_vertexai.chains.create_structured_runnable.html
**Word Count:** 143
**Links Count:** 88
**Scraped:** 2025-07-21 08:27:19
**Status:** completed

---

# create\_structured\_runnable\#

langchain\_google\_vertexai.chains.create\_structured\_runnable\(

    _function : Type\[BaseModel\] | Sequence\[Type\[BaseModel\]\]_,     _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _\*_ ,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _use\_extra\_step : bool = False_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/chains.html#create_structured_runnable)\#     

Create a runnable sequence that uses OpenAI functions.

Parameters:     

  * **function** \(_Type_ _\[__BaseModel_ _\]__|__Sequence_ _\[__Type_ _\[__BaseModel_ _\]__\]_\) – Either a single `pydantic.BaseModel` class or a sequence of `pydantic.BaseModels` classes. For best results, `pydantic.BaseModels` should have descriptions of the parameters.

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\) – Language model to use, assumed to support the Google Vertex function-calling API.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – `BasePromptTemplate` to pass to the model.

  * **use\_extra\_step** \(_bool_\) – whether to make an extra step to parse output into a function

Returns:     

A runnable sequence that will pass in the given functions to the model when run.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from typing import Optional          from langchain_google_vertexai import ChatVertexAI, create_structured_runnable     from langchain_core.prompts import ChatPromptTemplate     from pydantic import BaseModel, Field               class RecordPerson(BaseModel):         """Record some identifying information about a person."""              name: str = Field(..., description="The person's name")         age: int = Field(..., description="The person's age")         fav_food: Optional[str] = Field(None, description="The person's favorite food")               class RecordDog(BaseModel):         """Record some identifying information about a dog."""              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")               llm = ChatVertexAI(model_name="gemini-pro")     prompt = ChatPromptTemplate.from_template("""     You are a world class algorithm for recording entities.     Make calls to the relevant function to record the entities in the following input: {input}     Tip: Make sure to answer in the correct format"""                              )     chain = create_structured_runnable([RecordPerson, RecordDog], llm, prompt=prompt)     chain.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})     # -> RecordDog(name="Harry", color="brown", fav_food="chicken")     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)