"""Patch openai to log requests to Swipy Platform."""
from typing import Any

import openai

from swipy_client.swipy_requestor import log_text_completion_request


def patch_openai() -> None:
    """Patch openai to log requests to Swipy Platform."""
    chat_completion_create_original = openai.ChatCompletion.create

    def swipy_chat_completion_create(*args, **kwargs) -> dict[str, Any]:
        log_text_completion_request("openai.ChatCompletion.create", args, kwargs)
        return chat_completion_create_original(*args, **kwargs)

    openai.ChatCompletion.create = swipy_chat_completion_create
