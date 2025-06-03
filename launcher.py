import tkinter as tk
import os
from dotenv import set_key, load_dotenv
import subprocess
import sys

# Load .env or create if missing
env_path = ".env"
if not os.path.exists(env_path):
    with open(env_path, "w") as f:
        f.write("MODE=desktop\n")
load_dotenv(env_path)

def save_mode_and_launch(mode):
    set_key(env_path, "MODE", mode)
    window.destroy()

    # Launch the main interview app after mode selection
    python_exe = os.path.join(os.getcwd(), "python-embed", "python.exe") if os.path.exists("python-embed") else sys.executable
    subprocess.run([python_exe, "app.py"])

# GUI launcher
window = tk.Tk()
window.title("Select Interview Mode")
window.geometry("300x150")

label = tk.Label(window, text="Choose your mode:")
label.pack(pady=10)

desktop_btn = tk.Button(window, text="Desktop Mode", width=20, command=lambda: save_mode_and_launch("desktop"))
desktop_btn.pack(pady=5)

mobile_btn = tk.Button(window, text="Mobile Mode", width=20, command=lambda: save_mode_and_launch("mobile"))
mobile_btn.pack(pady=5)

window.mainloop()





