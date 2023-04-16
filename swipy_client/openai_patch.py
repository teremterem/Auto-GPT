"""Patch openai to log requests to Swipy Platform."""


def patch_openai() -> None:
    """Patch openai to log requests to Swipy Platform."""
    import openai

    chat_completion_create_original = openai.ChatCompletion.create

    def swipy_chat_completion_create(*args, **kwargs) -> dict:
        print("swipy_chat_completion_create")
        return chat_completion_create_original(*args, **kwargs)

    openai.ChatCompletion.create = swipy_chat_completion_create
