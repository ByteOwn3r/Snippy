import json, sys
import subprocess
import threading
import queue
import tkinter as tk
from typing import Any
from pynput import keyboard
from pynput.keyboard import Key, Controller
from datetime import datetime
import Variables
import gui

buffer = ""
kb = Controller()
key = Key
data: Any = {}
expanding = False
EMAILS = Variables.EMAILS
PATH = Variables.PATH

gui_queue = queue.Queue()


def reload():
    global data
    with open(PATH, mode="r", encoding="utf-8") as f:
        data = json.load(f)

def type_text(text):
    kb.type(text)
    kb.press(key.space)
    kb.release(key.space)

def remove_key(length: int):
    for _ in range(length):
        kb.press(Key.backspace)
        kb.release(Key.backspace)

def on_press(key_event):
    global buffer, expanding

    if expanding:
        return

    char = getattr(key_event, "char", None)

    if char is not None:
        buffer += char
        buffer = buffer[-30:]
        if char == ";":
            buffer = ";"
    else:
        if key_event == Key.space:
            check_word()
            buffer = ""
        elif key_event == Key.backspace:
            buffer = buffer[:-1]
        elif key_event == key.shift or key_event == key.shift_l or key_event == key.shift_r:
            pass
        else:
            buffer = ""

def expand_variables(text: str, key_word: str, arg: str = None):
    if "{date}" in text:
        text = text.replace("{date}", datetime.today().strftime("%d/%m/%Y"))
    if "{hour}" in text:
        text = text.replace("{hour}", datetime.today().strftime("%H:%M"))
    if arg is not None and "{arg}" in text and key_word == ";email":
        text = text.replace("{arg}", EMAILS.get(str(arg), ""))
    if arg is not None and "{arg}" in text:
        text = text.replace("{arg}", arg)

    return text

def check_exceptions(key_word, type_, arg=None):
    global expanding

    if key_word == ";exit":
        sys.exit(0)
    if arg:
        if type_ == "open":
            subprocess.run(["open", "-a", arg])
            expanding = False
            return True
    if type_ == "command":
        subprocess.run(data[key_word]["value"], shell=True)
        expanding = False
        return True
    if type_ == "help":
        gui_queue.put("show_help")
        expanding = False
        return True
    if type_ == "reload":
        reload()
        expanding = False
        return True

    return False

def check_word():
    global buffer, expanding
    if "," in buffer:
        key_word, arg = buffer.split(",", 1)
        key_word = key_word.lower()
    else:
        key_word = buffer.lower()
        arg = None
    if key_word in data:
        expanding = True
        remove_key(len(buffer) + 1)

        if check_exceptions(key_word, data[key_word]["type"], arg):
            return

        text = expand_variables(data[key_word]["value"], key_word, arg)
        type_text(text)
        expanding = False
        return

def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

def check_gui_queue(root):
    try:
        while True:
            gui_queue.get_nowait()
            gui.help()
    except queue.Empty:
        pass
    root.after(200, check_gui_queue, root)

if __name__ == "__main__":
    reload()
    listener_thread = threading.Thread(target=start_listener, daemon=True)
    listener_thread.start()

    root = tk.Tk()
    root.withdraw()  # ventana raiz oculta, solo sirve para mantener el mainloop vivo
    check_gui_queue(root)
    root.mainloop()