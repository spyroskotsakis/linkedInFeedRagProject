# EvaluatorType — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html
**Word Count:** 237
**Links Count:** 163
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# EvaluatorType\#

_class _langchain.evaluation.schema.EvaluatorType\(_value_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#EvaluatorType)\#     

The types of the evaluators.

QA _ = 'qa'_\#     

Question answering evaluator, which grades answers to questions directly using an LLM.

COT\_QA _ = 'cot\_qa'_\#     

Chain of thought question answering evaluator, which grades answers to questions using chain of thought ‘reasoning’.

CONTEXT\_QA _ = 'context\_qa'_\#     

Question answering evaluator that incorporates ‘context’ in the response.

PAIRWISE\_STRING _ = 'pairwise\_string'_\#     

The pairwise string evaluator, which predicts the preferred prediction from between two models.

SCORE\_STRING _ = 'score\_string'_\#     

The scored string evaluator, which gives a score between 1 and 10 to a prediction.

LABELED\_PAIRWISE\_STRING _ = 'labeled\_pairwise\_string'_\#     

The labeled pairwise string evaluator, which predicts the preferred prediction from between two models based on a ground truth reference label.

LABELED\_SCORE\_STRING _ = 'labeled\_score\_string'_\#     

The labeled scored string evaluator, which gives a score between 1 and 10 to a prediction based on a ground truth reference label.

AGENT\_TRAJECTORY _ = 'trajectory'_\#     

The agent trajectory evaluator, which grades the agent’s intermediate steps.

CRITERIA _ = 'criteria'_\#     

The criteria evaluator, which evaluates a model based on a custom set of criteria without any reference labels.

LABELED\_CRITERIA _ = 'labeled\_criteria'_\#     

The labeled criteria evaluator, which evaluates a model based on a custom set of criteria, with a reference label.

STRING\_DISTANCE _ = 'string\_distance'_\#     

Compare predictions to a reference answer using string edit distances.

EXACT\_MATCH _ = 'exact\_match'_\#     

Compare predictions to a reference answer using exact matching.

REGEX\_MATCH _ = 'regex\_match'_\#     

Compare predictions to a reference answer using regular expressions.

PAIRWISE\_STRING\_DISTANCE _ = 'pairwise\_string\_distance'_\#     

Compare predictions based on string edit distances.

EMBEDDING\_DISTANCE _ = 'embedding\_distance'_\#     

Compare a prediction to a reference label using embedding distance.

PAIRWISE\_EMBEDDING\_DISTANCE _ = 'pairwise\_embedding\_distance'_\#     

Compare two predictions using embedding distance.

JSON\_VALIDITY _ = 'json\_validity'_\#     

Check if a prediction is valid JSON.

JSON\_EQUALITY _ = 'json\_equality'_\#     

Check if a prediction is equal to a reference JSON.

JSON\_EDIT\_DISTANCE _ = 'json\_edit\_distance'_\#     

Compute the edit distance between two JSON strings after canonicalization.

JSON\_SCHEMA\_VALIDATION _ = 'json\_schema\_validation'_\#     

Check if a prediction is valid JSON according to a JSON schema.

__On this page