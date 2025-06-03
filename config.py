import os

# OpenRouter or OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
# Model selection
GPT_MODEL = "openai/gpt-3.5-turbo"

# Base URL for OpenRouter (skip if using official OpenAI)
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")
# Mode: "desktop" or "mobile"
MODE = os.getenv("MODE", "desktop")
AUDIO_INPUT = os.getenv("AUDIO_INPUT", "mic")