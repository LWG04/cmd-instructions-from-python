import os
import tkinter as tk

def closepyw():
    os.system("TASKKILL /IM pythonw.exe /F")
    os.system("TASKKILL /IM python.exe /F")

def notepad():
    os.system("start notepad")

def install():
    toinstall = entry.get()
    entry.delete(0, tk.END)
    os.system("pip install --upgrade pip")
    os.system(f"pip install {toinstall}")

window = tk.Tk()

text = tk.Label(text="Execute the following commands in the cmd")
text.pack()

button1 = tk.Button(text="Close all python files", command = closepyw)
button1.pack()

button2 = tk.Button(text="Open notepad", command = notepad)
button2.pack()

entry = tk.Entry()
entry.pack()

button3 = tk.Button(text="Install python module", command = install)
button3.pack()

window.mainloop()
