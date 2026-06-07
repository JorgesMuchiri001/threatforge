from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.test_case import LLMTestCaseParams


def run_deepeval(architecture_description, final_report):
    expected_output = """
    Spoofing
    Tampering
    Repudiation
    Information Disclosure
    Denial of Service
    Elevation of Privilege
    Risk Register
    Compliance Mapping
    Mitigations
    """

    test_case = LLMTestCase(
        input=architecture_description,
        actual_output=final_report,
        expected_output=expected_output
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
        ),

        GEval(
            name="Risk Assessment Quality",
            criteria="""
            Evaluate whether risk ratings are reasonable,
            likelihood and impact are justified,
            and critical banking assets receive higher risk scores.
            """,
            evaluation_params=[
                LLMTestCaseParams.ACTUAL_OUTPUT
            ]
        ),

        GEval(
            name="STRIDE Coverage",
            criteria="""
            Check whether the report covers Spoofing, Tampering,
            Repudiation, Information Disclosure, Denial of Service,
            and Elevation of Privilege.
            """,
            evaluation_params=[
                LLMTestCaseParams.ACTUAL_OUTPUT
            ]
        ),

        GEval(
            name="Compliance Mapping Quality",
            criteria="""
            Check whether threats are mapped to PCI DSS,
            ISO 27001, NIST CSF, SWIFT CSP,
            and CBK Cybersecurity Guidelines.
            """,
            evaluation_params=[
                LLMTestCaseParams.ACTUAL_OUTPUT
            ]
        )
    ]

    results = []

for metric in metrics:
    metric_name = getattr(metric, "name", metric.__class__.__name__)
    threshold = getattr(metric, "threshold", 0.7)

    try:
        metric.measure(test_case)

        score = metric.score if metric.score is not None else 0

        results.append({
            "Metric": metric_name,
            "Score": score,
            "Threshold": threshold,
            "Status": "PASS" if score >= threshold else "FAIL",
            "Reason": getattr(metric, "reason", "No reason provided")
        })

    except Exception as e:
        results.append({
            "Metric": metric_name,
            "Score": 0,
            "Threshold": threshold,
            "Status": "ERROR",
            "Reason": str(e)
        })

    return results
