import autogen
from config.settings import llm_config


def create_architecture_agent():
    return autogen.AssistantAgent(
        name="ArchitectureAnalyst",
        system_message="""
        You are a banking security architect.
        Analyze the architecture and identify:
        1. Assets
        2. Data Flows
        3. Trust Boundaries
        4. Entry Points
        5. Critical Systems

        Return findings in markdown.
        """,
        llm_config=llm_config
    )


def create_threat_agent():
    return autogen.AssistantAgent(
        name="ThreatModeler",
        system_message="""
        You are a STRIDE threat modeling expert.

        For every asset identify:
        S - Spoofing
        T - Tampering
        R - Repudiation
        I - Information Disclosure
        D - Denial of Service
        E - Elevation of Privilege

        Return a structured threat table.
        """,
        llm_config=llm_config
    )


def create_risk_agent():
    return autogen.AssistantAgent(
        name="RiskAssessor",
        system_message="""
        You are a banking cyber risk expert.

        For every threat:
        - Estimate Likelihood
        - Estimate Impact
        - Assign Risk Level

        Use: Low, Medium, High, Critical.

        Produce a risk register.
        """,
        llm_config=llm_config
    )


def create_compliance_agent():
    return autogen.AssistantAgent(
        name="ComplianceAgent",
        system_message="""
        You are a banking compliance expert.

        Map threats and risks to:
        - PCI DSS
        - ISO 27001
        - NIST CSF
        - SWIFT CSP
        - CBK Cybersecurity Guidelines

        Produce compliance mapping.
        """,
        llm_config=llm_config
    )


def create_mitigation_agent():
    return autogen.AssistantAgent(
        name="MitigationAgent",
        system_message="""
        Recommend controls for each risk.

        Examples:
        MFA, WAF, SIEM, Encryption, Network Segmentation, Zero Trust.

        Return prioritized recommendations.
        """,
        llm_config=llm_config
    )


def create_writer_agent():
    return autogen.AssistantAgent(
        name="ReportWriter",
        system_message="""
        Produce a professional banking threat model report.

        Sections:
        1. Executive Summary
        2. Architecture Analysis
        3. STRIDE Findings
        4. Risk Register
        5. Compliance Mapping
        6. Mitigation Recommendations

        Use markdown.
        """,
        llm_config=llm_config
    )


def create_reviewer_agent():
    return autogen.AssistantAgent(
        name="SecurityReviewer",
        system_message="""
        Review the report.

        Validate:
        - Completeness
        - STRIDE coverage
        - Risk accuracy
        - Compliance coverage

        Reply APPROVED if acceptable.
        """,
        llm_config=llm_config
    )