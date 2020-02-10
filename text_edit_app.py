from tkinter import filedialog
from tkinter import *
import ntpath

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("GUI")
        
        self.pack()
        self.init_menu()
        
        # Sidebar
        self.sidebar = Frame(master, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

        # Mainarea
        self.mainarea = Frame(master, bg='#CCC', width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')

        # Scrollbar
        self.scrollbar = Scrollbar(self.mainarea)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Create text area
        self.text_area = Text(self.mainarea, highlightthickness=0, wrap=WORD, yscrollcommand=self.scrollbar.set)
        self.text_area.pack(expand=True, fill=BOTH)

        # Configure scrollbar to text area
        self.scrollbar.config(command=self.text_area.yview)

        self.filename = None

    def init_menu(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file = Menu(menubar)
        file.add_command(label='New', command=self.my_command)
        file.add_command(label='Open', command=self.open_file)
        file.add_command(label='Save', command=self.save_file)
        menubar.add_cascade(label='File', menu=file)

        edit = Menu(menubar)
        edit.add_command(label='Undo', command=self.my_command)
        edit.add_command(label='Redo', command=self.my_command)
        edit.add_command(label='Cut', command=self.my_command)
        edit.add_command(label='Copy', command=self.my_command)
        edit.add_command(label='Paste', command=self.my_command)
        menubar.add_cascade(label='Edit', menu=edit)

    def my_command(self):
        print('hello world')

    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("py files","*.py"), ("txt files", "*.txt"), ("all files","*.*")))
        if not self.filename: return

        try:
            text1 = open(self.filename).read()
            self.text_area.insert(END, text1)

            # Add filename to sidebar
            fname = pretty_filename(self.filename)
            self.add_file_to_sidebar(fname)

        except Exception:
            print('Error')

    def save_file(self):
        if self.filename == None:

            # If no filename in state, which means new file.
            f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:
                return
            text2save = str(self.text_area.get(1.0, END))
            f.write(text2save)
            f.close()
        else:
            # If filename in state, which means opened file
            f = open(self.filename, "r+")
            my_txt = str(self.text_area.get(1.0, END))
            f.writelines(my_txt)
            f.close()

    def add_file_to_sidebar(self, name):
        label = Label(self.sidebar, text=name, width=15, height=1, anchor=NW, justify=LEFT)
        label.pack(fill=X)

def pretty_filename(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

root = Tk()

app = Window(root)
root.mainloop()