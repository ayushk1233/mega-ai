import json
import sseclient
import streamlit as st
import requests


st.set_page_config(
    page_title="Mega AI Platform",
    layout="wide"
)

st.title("🚀 Mega AI Platform")

st.caption(
    "Real-Time Multi-Agent AI Orchestration"
)

query = st.text_area(
    "Enter Query"
)

run_button = st.button(
    "Run Orchestration"
)


if run_button and query:

    status_container = st.container()

    synthesis_container = st.container()

    critique_container = st.container()

    provenance_container = st.expander(
        "Provenance"
    )

    telemetry_container = st.expander(
        "Telemetry"
    )

    stream_response = requests.get(
        f"http://127.0.0.1:8000/stream?query={query}",
        stream=True
    )

    response = sseclient.SSEClient(
        stream_response
    )

    for event in response.events():

        payload = json.loads(
            event.data
        )

        if payload["type"] == "status":

            status_container.info(
                payload["message"]
            )

        elif payload["type"] == "final":

            data = payload["data"]

            synthesis = data[
                "agent_outputs"
            ]["synthesis"]["output"]

            critique = data[
                "agent_outputs"
            ]["critique"]["output"]

            st.success(
                "Orchestration Completed"
            )

            synthesis_container.subheader(
                "Synthesis"
            )

            synthesis_container.write(
                synthesis
            )

            critique_container.subheader(
                "Critique"
            )

            critique_container.write(
                critique
            )

            provenance_container.json(
                data["provenance"]
            )

            telemetry = requests.get(
                "http://127.0.0.1:8000/metrics"
            ).json()

            telemetry_container.json(
                telemetry
            )