import tkinter as tk
from tkinter import messagebox

def on_button_click():
    userName=entry.get()
    if userName.strip()=="":
        messagebox.showwarning("Imput Error", "Please enter your name!")
    else:
        messagebox.showinfo("Greeting", f"Hello, {userName}! Welcome to Tkinter.")

root=tk.Tk()
root.title("Messagebox & Eent Handling Demo")
root.geometry("100x200")

label=tk.Label(root, text="enter your name:")
label.pack(pady=10)

entry=tk.Entry(root)
entry.pack(pady=5)

btn=tk.Button(root, text="submit", command=on_button_click)
btn.pack(pady=20)

root.bind("<Return>", lambda event: on_button_click())

root.mainloop()


