# main.py
import os
from dotenv import load_dotenv
from config import MODE
from chatgpt_client import get_chatgpt_response, correct_transcription
from speech_listener import listen_to_speech

# Load .env file
load_dotenv()

# Choose display method based on MODE
if MODE == "desktop":
    from gui_display import show_popup
elif MODE == "mobile":
    from web_display import run_web_display
    import threading
else:
    raise ValueError("MODE must be 'desktop' or 'mobile'")

def main_loop():
    while True:
        spoken_question = listen_to_speech()
        corrected_question = correct_transcription(spoken_question)
        print(f"Corrected: {corrected_question}")
        response = get_chatgpt_response(corrected_question)

        if MODE == "desktop":
            show_popup(response)
        elif MODE == "mobile":
            import requests
            try:
                requests.post("http://127.0.0.1:5000/update", data={"response": response})
            except Exception as e:
                print("❌ Failed to send update to mobile web display:", e)

if __name__ == "__main__":
    if MODE == "mobile":
        threading.Thread(target=run_web_display, daemon=True).start()

    print(f"🔁 Running in {MODE.upper()} mode...")
    main_loop()
