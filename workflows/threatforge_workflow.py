import autogen

from config.settings import llm_config
from agents.threatforge_agents import (
    create_architecture_agent,
    create_threat_agent,
    create_risk_agent,
    create_compliance_agent,
    create_mitigation_agent,
    create_writer_agent,
    create_reviewer_agent
)


def run_threatforge(architecture_description: str):
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=20,
        code_execution_config=False,
        is_termination_msg=lambda msg: "APPROVED" in msg.get("content", "")
    )

    groupchat = autogen.GroupChat(
        agents=[
            user_proxy,
            create_architecture_agent(),
            create_threat_agent(),
            create_risk_agent(),
            create_compliance_agent(),
            create_mitigation_agent(),
            create_writer_agent(),
            create_reviewer_agent()
        ],
        messages=[],
        max_round=30
    )

    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config
    )

    user_proxy.initiate_chat(
        manager,
        message=f"""
        Perform a complete STRIDE threat model
        for the following banking architecture:

        {architecture_description}

        Produce:
        1. Architecture Analysis
        2. Threat Model
        3. Risk Register
        4. Compliance Mapping
        5. Security Recommendations
        6. Executive Summary
        """
    )

    final_report = None

    for message in reversed(groupchat.messages):
        if message.get("name") == "ReportWriter":
            final_report = message.get("content")
            break

    return final_report, groupchat.messages