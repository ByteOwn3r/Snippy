import json
import tkinter as tk
from tkinter import ttk
import Variables

PATH = Variables.PATH

def help():
    with open(PATH, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    data = [(k, v['type'], v.get('value', '')) for k, v in data.items()]

    window = tk.Toplevel()
    window.title("Snippy")
    window.geometry("900x700")

    columns = ("Key", "Type", "Value")
    tree = ttk.Treeview(window, columns=columns, show="headings")

    tree.column("Key", width=100)
    tree.column("Type", width=75)
    tree.column("Value", width=725)

    tree.heading("Key", text="Key")
    tree.heading("Type", text="Type")
    tree.heading("Value", text="Value")

    for d in data:
        tree.insert("", tk.END, values=d)

    tree.pack(expand=True, fill="both")