# chatgpt_client.py
#import openai
#from config import OPENAI_API_KEY, GPT_MODEL, OPENAI_API_BASE
#
## Configure OpenRouter endpoint using OpenAI v0.28 SDK
#openai.api_key = OPENAI_API_KEY
## Direct base URL to OpenRouter
#openai.api_base = OPENAI_API_BASE
## Use default API type for OpenAI-compatible services
#openai.api_type = "open_ai"
#
## chat completion using old API style
#
#def get_chatgpt_response(prompt):
#    try:
#        response = openai.ChatCompletion.create(
#            model=GPT_MODEL,
#            messages=[
#                {"role": "system", "content": "You are a helpful assistant for mock interviews."},
#                {"role": "user", "content": prompt},
#            ]
#        )
#        return response.choices[0].message["content"].strip()
#    except Exception as e:
#        return f"Error: {str(e)}"
        
        
import openai
from config import OPENAI_API_KEY, GPT_MODEL, OPENAI_API_BASE

openai.api_key = OPENAI_API_KEY
if OPENAI_API_BASE:
    openai.api_base = OPENAI_API_BASE
    openai.api_type = "open_ai"

SYSTEM_PROMPT = (
    "Act as an interviewee in a technical interview. "
    "Be concise when possible, but if the question asks for lists or deep explanations, give complete and helpful answers, even if long."
)

CORRECT_PROMPT = "You are a transcription assistant. Correct the following spoken interview question for clarity."

chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def get_chatgpt_response(prompt):
    chat_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=chat_history

    )
    reply = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": reply})
    return reply

def correct_transcription(text):
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": CORRECT_PROMPT},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def reset_chat_history():
    global chat_history
    chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]
