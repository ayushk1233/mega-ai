import json
import time
import requests
import sseclient
import streamlit as st


st.set_page_config(
    page_title="Mega AI Platform",
    layout="wide"
)

st.title("🪂 Mega AI Platform")

st.caption(
    "Multi-Agent AI Orchestration System"
)

left_col, right_col = st.columns(
    [2, 1]
)

with left_col:

    query = st.text_area(
        "Enter Query"
    )

    run_button = st.button(
        "Run Orchestration"
    )


if run_button and query:

    with left_col:

        timeline_placeholder = st.empty()

        status_placeholder = st.empty()

        synthesis_placeholder = st.empty()

        critique_placeholder = st.empty()

    with right_col:

        telemetry_placeholder = st.empty()

        provenance_placeholder = st.empty()

    stream_response = requests.get(
        f"http://127.0.0.1:8000/stream?query={query}",
        stream=True
    )

    response = sseclient.SSEClient(
        stream_response
    )

    timeline_entries = []

    for event in response.events():

        payload = json.loads(
            event.data
        )

        if payload["type"] == "status":

            timeline_entries.append(
                payload["message"]
            )

            timeline_md = "### ⚡ Orchestration Timeline\n\n"
            for entry in timeline_entries:
                timeline_md += f"- {entry}\n"

            timeline_placeholder.markdown(
                timeline_md
            )

        elif payload["type"] == "final":

            data = payload["data"]

            status_placeholder.success(
                "✅ Orchestration Completed"
            )

            synthesis_data = data[
                "agent_outputs"
            ]["synthesis"]["output"]

            critique_data = data[
                "agent_outputs"
            ]["critique"]["output"]

            synthesis_placeholder.subheader(
                "✨ Final Answer"
            )

            if isinstance(
                synthesis_data,
                dict
            ):

                final_answer = synthesis_data.get(
                    "final_answer",
                    ""
                )

                streamed_text = ""

                for word in final_answer.split():

                    streamed_text += (
                        word + " "
                    )

                    synthesis_placeholder.markdown(
                        streamed_text
                    )

                    time.sleep(0.03)

                insights = synthesis_data.get(
                    "key_insights",
                    []
                )

                if insights:

                    with left_col:

                        st.markdown(
                            "### Key Insights"
                        )

                        for item in insights:

                            st.markdown(
                                f"- {item}"
                            )

            else:

                synthesis_placeholder.write(
                    synthesis_data
                )

            critique_placeholder.subheader(
                "🛡 Critique"
            )

            if isinstance(
                critique_data,
                dict
            ):

                with left_col:

                    st.markdown(
                        f"**Grounding Assessment:** {critique_data.get('grounding_assessment', '')}"
                    )

                    st.markdown(
                        f"**Hallucination Risks:** {critique_data.get('hallucination_risks', '')}"
                    )

                    st.markdown(
                        f"**Confidence Analysis:** {critique_data.get('confidence_analysis', '')}"
                    )

            else:

                critique_placeholder.write(
                    critique_data
                )

            # Provenance as readable evidence cards
            with right_col:

                st.subheader("📚 Provenance")

                for item in data["provenance"]:

                    st.markdown(
                        f"""### Evidence Chunk
**Source Agent:** {item['source_agent']}

**Evidence:**
{item['evidence']}
"""
                    )

            # Telemetry
            metrics = requests.get(
                f"http://127.0.0.1:8000/metrics?job_id={data['job_id']}"
            ).json()

            telemetry_placeholder.subheader(
                "📊 Telemetry"
            )

            telemetry_placeholder.dataframe(
                metrics
            )