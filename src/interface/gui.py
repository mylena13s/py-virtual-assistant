from tkinter import *

def setup_gui(callback):
    root = Tk()
    root.title("Virtual Assistant Wikipedia Voice Search")
    root.geometry("820x600")
    root.config(bg="#000045")

    response_label = Label(root, text="", wraplength=500, justify=LEFT, anchor="w", bg="#CCCCCC", fg="#FFFFFF", font=("Arial", 12))


    response_text = Text(root, height=30, width=100)
    response_text.pack(expand=True)

    listen_button = Button(root, text="Listen", command=lambda: callback(response_text), height=2, width=14, font=("Arial", 16))  # Ajuste de altura e largura do botão
    listen_button.pack(pady=13)  # Ajuste de margem para o botão

    return root, response_text


