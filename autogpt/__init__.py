"""This file used to be empty and is now used to patch the openai library to log requests to Swipy Platform."""
from swipy_client import patch_openai

patch_openai()
