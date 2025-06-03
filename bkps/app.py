#from speech_listener import listen_to_speech
#from chatgpt_client import get_chatgpt_response
#from config import MODE
#
#if MODE == "mobile":
#    from web_display import run_web_display
#    import requests
#    import threading
#    threading.Thread(target=run_web_display, daemon=True).start()
#
#from gui_display import show_popup
#
#def main_loop():
#    while True:
#        question = listen_to_speech()
#        print("Heard:", question)
#        answer = get_chatgpt_response(question)
#        print("Answer:", answer)
#
#        if MODE == "desktop":
#            show_popup(answer)
#        else:
#            requests.post("http://localhost:5000/update", data={"response": answer})
#
#if __name__ == "__main__":
#    main_loop()
    
from speech_listener import listen_to_speech
from chatgpt_client import correct_transcription, get_chatgpt_response
from config import MODE

if MODE == "mobile":
    from web_display import run_web_display
    import threading
    threading.Thread(target=run_web_display, daemon=True).start()

from gui_display import show_popup

def main_loop():
    while True:
        raw_q = listen_to_speech()
        if not raw_q:
            continue
        question = correct_transcription(raw_q)
        print(f"Corrected Question: {question}")
        answer = get_chatgpt_response(question)
        print(f"Answer: {answer}")
        if MODE == "desktop":
            show_popup(answer)
        else:
            import requests
            requests.post("http://localhost:5000/update", data={"response": answer})

if __name__ == "__main__":
    main_loop()
