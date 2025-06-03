import tkinter as tk
from chatgpt_client import get_chatgpt_response, reset_chat_history

def show_popup(initial_text):
    def regenerate():
        user_q = entry.get().strip()
        if user_q:
            response = get_chatgpt_response(user_q)
            text_box.config(state=tk.NORMAL)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, response)
            text_box.config(state=tk.DISABLED)
            root.update_idletasks()
            adjust_window_height(response)

    def adjust_window_height(text):
        # Estimate height based on content
        lines = text.count('\n') + text.count('.') // 2 + 3
        lines = max(10, min(30, lines))
        text_box.config(height=lines)

    def on_reset_chat():
        reset_chat_history()
        root.destroy()  # Close current window so it starts fresh next time

    root = tk.Tk()
    root.title("Mock Interview Assistant")

    # Position top center below webcam
    screen_width = root.winfo_screenwidth()
    x = int((screen_width / 2) - 300)
    y = 100
    root.geometry(f"+{x}+{y}")

    entry = tk.Entry(root, width=80)
    entry.pack(pady=(10, 5), padx=10)

    submit_btn = tk.Button(root, text="Regenerate Answer", command=regenerate)
    submit_btn.pack(pady=(0, 10))

    text_box = tk.Text(root, wrap=tk.WORD, width=80, height=10)
    text_box.insert(tk.END, initial_text)
    text_box.config(state=tk.DISABLED)
    text_box.pack(padx=10, pady=(0, 10))

    # Buttons for closing and resetting
    close_btn = tk.Button(root, text="Close", command=root.destroy)
    close_btn.pack(pady=(0, 5))

    reset_btn = tk.Button(root, text="Reset Chat", command=on_reset_chat)
    reset_btn.pack(pady=(0, 10))

    adjust_window_height(initial_text)
    root.mainloop()




