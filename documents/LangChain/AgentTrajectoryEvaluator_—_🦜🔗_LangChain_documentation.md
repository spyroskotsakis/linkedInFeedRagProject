# AgentTrajectoryEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.AgentTrajectoryEvaluator.html
**Word Count:** 89
**Links Count:** 135
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# AgentTrajectoryEvaluator\#

_class _langchain.evaluation.schema.AgentTrajectoryEvaluator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#AgentTrajectoryEvaluator)\#     

Interface for evaluating agent trajectories.

Attributes

`requires_input` | Whether this evaluator requires an input string.   ---|---   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`aevaluate_agent_trajectory`\(\*, prediction, ...\) | Asynchronously evaluate a trajectory.   ---|---   `evaluate_agent_trajectory`\(\*, prediction, ...\) | Evaluate a trajectory.      _async _aevaluate\_agent\_trajectory\(

    _\*_ ,     _prediction : str_,     _agent\_trajectory : Sequence\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _input : str_,     _reference : str | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#AgentTrajectoryEvaluator.aevaluate_agent_trajectory)\#     

Asynchronously evaluate a trajectory.

Parameters:     

  * **prediction** \(_str_\) – The final predicted response.

  * **agent\_trajectory** \(_List_ _\[__Tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – The intermediate steps forming the agent trajectory.

  * **input** \(_str_\) – The input to the agent.

  * **reference** \(_Optional_ _\[__str_ _\]_\) – The reference answer.

  * **kwargs** \(_Any_\)

Returns:     

The evaluation result.

Return type:     

dict

evaluate\_agent\_trajectory\(

    _\*_ ,     _prediction : str_,     _agent\_trajectory : Sequence\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _input : str_,     _reference : str | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#AgentTrajectoryEvaluator.evaluate_agent_trajectory)\#     

Evaluate a trajectory.

Parameters:     

  * **prediction** \(_str_\) – The final predicted response.

  * **agent\_trajectory** \(_List_ _\[__Tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – The intermediate steps forming the agent trajectory.

  * **input** \(_str_\) – The input to the agent.

  * **reference** \(_Optional_ _\[__str_ _\]_\) – The reference answer.

  * **kwargs** \(_Any_\)

Returns:     

The evaluation result.

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)