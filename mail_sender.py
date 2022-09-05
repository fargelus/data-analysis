import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Select files for zip')

        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side='top')

        ttk.Button(
            self.top_frame,
            text='Select files',
            command=self.select_files
        ).pack(side='left', expand=True, padx=5)

        ttk.Button(
            self.top_frame,
            text='Zip files',
            state=tk.DISABLED
        ).pack(side='left', expand=True, padx=5)

    def select_files(self):
        filenames = fd.askopenfilenames(
            title='Open a file',
            initialdir='.'
        )
        print(filenames)

    def draw(self):
        self.root.mainloop()

MainWindow().draw()
