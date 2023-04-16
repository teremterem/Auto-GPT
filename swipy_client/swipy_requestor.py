"""This module is responsible for sending requests to Swipy Platform."""
import httpx

_client = httpx.Client()


def log_text_completion_request() -> None:
    """Log a text completion request to Swipy Platform."""
    _client.post(
        "http://localhost:8000/swipy_client_webhook/",
        json={"hello": "world"},
    )
