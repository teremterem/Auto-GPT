"""This module is responsible for sending requests to Swipy Platform."""
from typing import Any

import httpx

_client = httpx.Client()


def log_text_completion_request(
    caller_name: str, args: tuple[Any, ...], kwargs: dict[str, Any]
) -> None:
    """Log a text completion request to Swipy Platform."""
    payload = {
        "caller_name": caller_name,
        "args": args,
        "kwargs": kwargs,
    }
    _client.post(
        "http://localhost:8000/swipy_client_webhook/",
        json=payload,
    )
