import openai
from config import OPENAI_API_KEY, GPT_MODEL, OPENAI_API_BASE

# Configure client for OpenRouter or OpenAI
openai.api_key = OPENAI_API_KEY
if OPENAI_API_BASE:
    openai.api_base = OPENAI_API_BASE
    openai.api_type = "open_ai"

# System prompts
SYSTEM_PROMPT = (
    "Act as an interviewee in a technical interview. "
    "Be concise when possible, but if the question asks for lists or deep explanations, give complete and helpful answers, even if long."
)
CORRECT_PROMPT = (
    "You are a transcription assistant. Correct the following spoken interview question for clarity, fixing any mistakes, "
    "and output only the corrected question."
)

# Maintain chat history for contextual Q&A
chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def get_chatgpt_response(prompt):
    chat_history.append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=chat_history
        )
        reply = response.choices[0].message.content.strip()
        chat_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print(f"❌ Error during ChatGPT response: {e}")
        return "⚠️ Sorry, I couldn’t process that question. Please try again."

def correct_transcription(text):
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": CORRECT_PROMPT},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error during transcription correction: {e}")
        return text  # Fallback to raw text if correction fails

def reset_chat_history():
    global chat_history
    chat_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
