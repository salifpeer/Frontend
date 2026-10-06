import requests
import streamlit as st


API_URL = "https://backend-7-xlro.onrender.com"


def api_request(method, endpoint, **kwargs):

    token = st.session_state.get("token")

    headers = kwargs.pop("headers", {})

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.request(
        method,
        f"{API_URL}{endpoint}",
        headers=headers,
        **kwargs
    )

    return response