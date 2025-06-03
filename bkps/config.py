# config.py

#import os
#
## Load environment variables (optional if you want to use a .env file)
## from dotenv import load_dotenv
## load_dotenv()
#
## Use your OpenRouter API key here
#OPENAI_API_KEY = "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"
#
## Set this to the model you want to use via OpenRouter
## Some options: "openai/gpt-3.5-turbo", "mistralai/mixtral-8x7b", etc.
#GPT_MODEL = "openai/gpt-3.5-turbo"
#
## API Base URL for OpenRouter
#OPENAI_API_BASE = "https://openrouter.ai/api/v1"
#
## Mode selector
#MODE = "desktop"  # or "mobile"





import os

# OpenRouter or OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
# Model selection
GPT_MODEL = "openai/gpt-3.5-turbo"

# Base URL for OpenRouter (skip if using official OpenAI)
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")
# Mode: "desktop" or "mobile"
MODE = os.getenv("MODE", "desktop")
