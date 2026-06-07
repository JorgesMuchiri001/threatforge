from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.test_case import LLMTestCaseParams


def run_deepeval(architecture_description, final_report):

    test_case = LLMTestCase(
        input=architecture_description,
        actual_output=final_report,
    )

    metrics = [
        AnswerRelevancyMetric(threshold=0.7),

        GEval(
            name="Threat Model Completeness",
            criteria="""
            Determine whether the threat model identifies assets,
            trust boundaries, STRIDE threats, mitigations,
            and risk ratings.
            """,
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT
            ]
        )
    ]

    results = []

    for metric in metrics:

        metric_name = getattr(
            metric,
            "name",
            metric.__class__.__name__
        )

        try:
            metric.measure(test_case)

            results.append({
                "Metric": metric_name,
                "Score": metric.score,
                "Reason": getattr(
                    metric,
                    "reason",
                    "No reason provided"
                )
            })

        except Exception as e:

            results.append({
                "Metric": metric_name,
                "Score": 0,
                "Reason": str(e)
            })

    return results
