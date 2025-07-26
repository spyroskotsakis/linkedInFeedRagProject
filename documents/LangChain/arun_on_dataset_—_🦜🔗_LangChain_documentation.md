# arun_on_dataset — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.runner_utils.arun_on_dataset.html
**Word Count:** 244
**Links Count:** 114
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# arun\_on\_dataset\#

_async _langchain.smith.evaluation.runner\_utils.arun\_on\_dataset\(

    _client : Client | None_,     _dataset\_name : str_,     _llm\_or\_chain\_factory : Callable\[\[\], [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\] | [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | Callable\[\[dict\], Any\] | [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") | [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")_,     _\*_ ,     _evaluation : [RunEvalConfig](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.RunEvalConfig.html#langchain.smith.evaluation.config.RunEvalConfig "langchain.smith.evaluation.config.RunEvalConfig") | None = None_,     _dataset\_version : datetime | str | None = None_,     _concurrency\_level : int = 5_,     _project\_name : str | None = None_,     _project\_metadata : dict\[str, Any\] | None = None_,     _verbose : bool = False_,     _revision\_id : str | None = None_,     _\*\* kwargs: Any_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/runner_utils.html#arun_on_dataset)\#     

Run the Chain or language model on a dataset and store traces to the specified project name.

Parameters:     

  * **dataset\_name** \(_str_\) – Name of the dataset to run the chain on.

  * **llm\_or\_chain\_factory** \(_Callable_ _\[__\[__\]__,_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") _|_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\]__|_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__Callable_ _\[__\[__dict_ _\]__,__Any_ _\]__|_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _|_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")\) – Language model or Chain constructor to run over the dataset. The Chain constructor is used to permit independent calls on each example without carrying over state.

  * **evaluation** \([_RunEvalConfig_](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.RunEvalConfig.html#langchain.smith.evaluation.config.RunEvalConfig "langchain.smith.evaluation.config.RunEvalConfig") _|__None_\) – Configuration for evaluators to run on the results of the chain

  * **concurrency\_level** \(_int_\) – The number of async tasks to run concurrently.

  * **project\_name** \(_str_ _|__None_\) – Name of the project to store the traces in. Defaults to \{dataset\_name\}-\{chain class name\}-\{datetime\}.

  * **project\_metadata** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to add to the project. Useful for storing information the test variant. \(prompt version, model version, etc.\)

  * **client** \(_Client_ _|__None_\) – LangSmith client to use to access the dataset and to log feedback and run traces.

  * **verbose** \(_bool_\) – Whether to print progress.

  * **tags** – Tags to add to each run in the project.

  * **revision\_id** \(_str_ _|__None_\) – Optional revision identifier to assign this test run to track the performance of different versions of your system.

  * **dataset\_version** \(_datetime_ _|__str_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

A dictionary containing the run’s project name and the resulting model outputs.

Return type:     

dict\[str, _Any_\]

For the \(usually faster\) async version of this function, see `arun_on_dataset()`.

Examples               from langsmith import Client     from langchain_openai import ChatOpenAI     from langchain.chains import LLMChain     from langchain.smith import smith_eval.RunEvalConfig, run_on_dataset          # Chains may have memory. Passing in a constructor function lets the     # evaluation framework avoid cross-contamination between runs.     def construct_chain():         llm = ChatOpenAI(temperature=0)         chain = LLMChain.from_string(             llm,             "What's the answer to {your_input_key}"         )         return chain          # Load off-the-shelf evaluators via config or the EvaluatorType (string or enum)     evaluation_config = smith_eval.RunEvalConfig(         evaluators=[             "qa",  # "Correctness" against a reference answer             "embedding_distance",             smith_eval.RunEvalConfig.Criteria("helpfulness"),             smith_eval.RunEvalConfig.Criteria({                 "fifth-grader-score": "Do you have to be smarter than a fifth grader to answer this question?"             }),         ]     )          client = Client()     await arun_on_dataset(         client,         dataset_name="<my_dataset_name>",         llm_or_chain_factory=construct_chain,         evaluation=evaluation_config,     )     

You can also create custom evaluators by subclassing the [`StringEvaluator`](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html#langchain.evaluation.schema.StringEvaluator "langchain.evaluation.schema.StringEvaluator") or LangSmith’s RunEvaluator classes.               from typing import Optional     from langchain.evaluation import StringEvaluator          class MyStringEvaluator(StringEvaluator):              @property         def requires_input(self) -> bool:             return False              @property         def requires_reference(self) -> bool:             return True              @property         def evaluation_name(self) -> str:             return "exact_match"              def _evaluate_strings(self, prediction, reference=None, input=None, **kwargs) -> dict:             return {"score": prediction == reference}          evaluation_config = smith_eval.RunEvalConfig(         custom_evaluators = [MyStringEvaluator()],     )          await arun_on_dataset(         client,         dataset_name="<my_dataset_name>",         llm_or_chain_factory=construct_chain,         evaluation=evaluation_config,     )     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)