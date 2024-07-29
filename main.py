from tkinter import *
from tkinter import filedialog


# Main window

root = Tk()
root.title("Python Write")
root.geometry("900x700")
root.resizable(False, False)


# Text editor

text = Text(root, width=100, height=30)
text.pack(fill="both", expand=True)


# Functions

def new_file():
    text.delete(1.0, END)


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt")
        ],
    )
    if file_path:
        with open(file_path, "wb") as file:
            text_content = text.get(1.0, END)
            file.write(text_content.encode("utf-8"))


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text files", "*.txt")
        ],
    )
    if file_path:
        with open(file_path, "rb") as file:
            text.delete(1.0, END)
            text.insert(1.0, file.read().decode("utf-8"))


# Menubar

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

root.bind_all("<Control-n>", lambda event: new_file())
root.bind_all("<Control-N>", lambda event: new_file())

root.bind_all("<Control-q>", lambda event: root.quit())
root.bind_all("<Control-Q>", lambda event: root.quit())

root.bind_all("<Control-s>", lambda event: save_file())
root.bind_all("<Control-S>", lambda event: save_file())

root.bind_all("<Control-o>", lambda event: open_file())
root.bind_all("<Control-O>", lambda event: open_file())


if __name__ == "__main__":
    root.mainloop()
