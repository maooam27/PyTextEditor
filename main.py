from tkinter import *


# Main window

root = Tk()
root.title("Python Write")
root.geometry("900x700")
root.resizable(False, False)


# Text editor

text = Text(root, width=100, height=30)
text.pack(fill="both", expand=True)


# Menubar

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

if __name__ == "__main__":
    root.mainloop()
