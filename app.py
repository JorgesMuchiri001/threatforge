import streamlit as st
import pandas as pd
import plotly.express as px

from workflows.threatforge_workflow import run_threatforge
from evaluation.deepeval_runner import run_deepeval


st.set_page_config(
    page_title="ThreatForge",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ ThreatForge")
st.subheader("AI-Driven STRIDE Threat Modeling Platform for Financial Institutions")

default_architecture = """
Bank Architecture

Customers
    |
Mobile Banking App
    |
API Gateway
    |
Core Banking System
    |
Payment Switch
    |
SWIFT Gateway

External Systems:
- Credit Bureau
- M-Pesa Integration
- Card Processor

Security Controls:
- MFA
- WAF
- SIEM

Sensitive Data:
- Customer PII
- Account Data
- Card Data
"""

architecture_description = st.text_area(
    "Enter banking architecture description",
    value=default_architecture,
    height=300
)

if st.button("Generate Threat Model"):
    with st.spinner("Running ThreatForge multi-agent workflow..."):
        final_report, messages = run_threatforge(architecture_description)

    st.success("Threat model generated successfully.")

    tab1, tab2, tab3 = st.tabs([
        "Threat Model Report",
        "Agent Trace",
        "DeepEval Dashboard"
    ])

    with tab1:
        st.markdown(final_report)

    with tab2:
        for message in messages:
            st.markdown(f"### {message.get('name')}")
            st.write(message.get("content"))

    with tab3:
        with st.spinner("Running DeepEval assessment..."):
            eval_results = run_deepeval(
                architecture_description,
                final_report
            )

        df = pd.DataFrame(eval_results)

        st.dataframe(df, use_container_width=True)

        fig = px.bar(
            df,
            x="Metric",
            y="Score",
            title="DeepEval Scores"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Evaluation Reasons")
        for row in eval_results:
            st.markdown(f"**{row['Metric']}**")
            st.write(row["Reason"])