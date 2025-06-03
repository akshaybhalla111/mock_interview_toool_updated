#import tkinter as tk
#
#def show_popup(text):  # manual close
#    root = tk.Tk()
#    root.title("Mock Interview Assistant")
#    label = tk.Label(root, text=text, padx=20, pady=20, wraplength=400)
#    label.pack(padx=10, pady=10)
#    close_btn = tk.Button(root, text="Close", command=root.destroy, padx=10, pady=5)
#    close_btn.pack(pady=(0, 10))
#    root.mainloop()
    
    
    
#import tkinter as tk
#
#def show_popup(text):  # manual close
#    root = tk.Tk()
#    root.title("Mock Interview Assistant")
#
#    # Set window size and position at top center
#    window_width = 450
#    window_height = 200
#    screen_width = root.winfo_screenwidth()
#    x = int((screen_width / 2) - (window_width / 2))
#    y = 100  # Top center, adjust if needed
#    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
#
#    label = tk.Label(root, text=text, padx=20, pady=20, wraplength=400)
#    label.pack(padx=10, pady=10)
#    close_btn = tk.Button(root, text="Close", command=root.destroy, padx=10, pady=5)
#    close_btn.pack(pady=(0, 10))
#    root.mainloop()
    
# import tkinter as tk

# def show_popup(text):  # manual close
    # root = tk.Tk()
    # root.title("Mock Interview Assistant")

    # # Dynamically size the window to fit content
    # label = tk.Label(root, text=text, padx=20, pady=20, wraplength=600, justify='left')
    # label.pack(padx=10, pady=10)

    # close_btn = tk.Button(root, text="Close", command=root.destroy, padx=10, pady=5)
    # close_btn.pack(pady=(0, 10))

    # root.update_idletasks()

    # # Center it at the top of screen below webcam
    # window_width = root.winfo_reqwidth()
    # window_height = root.winfo_reqheight()
    # screen_width = root.winfo_screenwidth()
    # x = int((screen_width / 2) - (window_width / 2))
    # y = 100
    # root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # root.mainloop()



import tkinter as tk
from tkinter import scrolledtext
from chatgpt_client import reset_chat_history

def show_popup(message):
    window = tk.Tk()
    window.title("Interview Assistant")
    window.attributes('-topmost', True)
    window.configure(bg="#f5f5f5")

    width = 500
    screen_width = window.winfo_screenwidth()
    x = int((screen_width - width) / 2)
    y = 50
    window.geometry(f"{width}x300+{x}+{y}")  # Initial height

    text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Helvetica", 11), bg="white", fg="black")
    text_box.insert(tk.END, message)
    text_box.configure(state="disabled")
    text_box.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    # Dynamically resize height
    def adjust_window_height(text):
        num_lines = text.count('\n') + len(text) // 80
        height = min(max(10, num_lines), 30)
        text_box.config(height=height)

    adjust_window_height(message)

    def on_reset():
        reset_chat_history()
        window.destroy()

    reset_btn = tk.Button(window, text="Reset Chat", command=on_reset, bg="#ffcccc", font=("Helvetica", 10, "bold"))
    reset_btn.pack(pady=(0, 10))

    window.mainloop()




