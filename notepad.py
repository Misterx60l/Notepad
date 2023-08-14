from tkinter import *
from tkinter import filedialog, messagebox, font


def newFile():
    TextArea.delete(1.0, END)
    root.title("Untitled - Notepad")


def openFile():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())


def saveFile():
    global file
    if file is None:
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
                root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))


def saveAsFile():
    global file
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")


def quitApp():
    result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if result:
        root.destroy()


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def change_font_size():
    font_size = font_size_var.get()
    current_font = font.Font(font=TextArea["font"])
    new_font = (current_font.cget("family"), font_size)
    TextArea.configure(font=new_font)


def change_font_style():
    font_style = font_style_var.get()
    current_font = font.Font(font=TextArea["font"])
    new_font = (font_style, current_font.cget("size"))
    TextArea.configure(font=new_font)


def help():
    messagebox.showinfo("About", "This Notepad is developed by Anjaan Insaan")


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("800x500")

    # designing writable area here
    TextArea = Text(root, font="lucida 6")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # construct Menubar here
    MenuBar = Menu(root)
    root.config(menu=MenuBar)

    # File menu
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_command(label="Save As", command=saveAsFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Quit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # Edit menu
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Format menu
    FormatMenu = Menu(MenuBar, tearoff=0)

    font_size_var = IntVar()
    font_size_var.set(10)  # Default font size
    font_size_menu = Menu(FormatMenu, tearoff=0)
    for i in range(6, 31):
        font_size_menu.add_radiobutton(label=str(i), variable=font_size_var, command=change_font_size)
    FormatMenu.add_cascade(label="Font Size", menu=font_size_menu)

    font_style_var = StringVar()
    font_style_var.set("lucida")  # Default font style
    font_style_menu = Menu(FormatMenu, tearoff=0)
    font_style_menu.add_radiobutton(label="lucida", variable=font_style_var, command=change_font_style)
    font_style_menu.add_radiobutton(label="Arial", variable=font_style_var, command=change_font_style)
    font_style_menu.add_radiobutton(label="Times New Roman", variable=font_style_var, command=change_font_style)
    # Add more font styles as needed
    FormatMenu.add_cascade(label="Font Style", menu=font_style_menu)

    MenuBar.add_cascade(label="Format", menu=FormatMenu)

    # Help menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="Help", command=help)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
