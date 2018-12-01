"""
Docstring:
Desktop app that runs search on main acadmeic search engines
"""

import tkinter as tk
from tkinter import ttk
import webbrowser

class Acad_engine:
    def __init__(self, window,title):
        self.window = window
        self.window.title(title)
        self.label = ttk.Label(self.window, text = "Query")
        self.label.grid(row = 0, column = 0)
        self.entry1 = ttk.Entry(self.window, width = 50)
        self.entry1.grid(row = 0, column = 1)
        self.string = tk.StringVar()


        self.btn1 = ttk.Button(self.window, text='Search', width=10, command=self.callback)
        self.btn1.grid(row=0, column=2)

        self.entry1.bind('<Return>', self.get)

        self.btn2 = ttk.Radiobutton(self.window, text='Semantic Scholar', value='Semantic Scholar', variable=self.string)
        self.btn2.grid(row=1, column=1, sticky='W')

        self.btn3 = ttk.Radiobutton(self.window, text='Nature', value='Nature', variable=self.string)
        self.btn3.grid(row=1, column=1, sticky='E')

        self.btn4 = ttk.Radiobutton(self.window, text='NCBI', value='NCBI', variable=self.string)
        self.btn4.grid(row=1, column=1, sticky='N')

        self.btn5 = ttk.Radiobutton(self.window, text='All', value='All', variable=self.string)
        self.btn5.grid(row=1, column=2, sticky='S')

        self.entry1.focus()

        self.window.wm_attributes('-topmost', 1)

        self.window.mainloop()



    def callback(self):
        """Uses the webbrowser to open an url"""
        if self.string.get() == 'Semantic Scholar':
            webbrowser.open('https://www.semanticscholar.org/search?q= ' + self.entry1.get())

        elif self.string.get() == 'Nature':
            webbrowser.open('https://www.nature.com/search?q='+self.entry1.get())

        elif self.string.get() == "NCBI":
            webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + self.entry1.get())

        elif self.string.get() == "All":
            webbrowser.open('https://www.semanticscholar.org/search?q= '+ self.entry1.get())
            webbrowser.open('https://www.nature.com/search?q='+self.entry1.get())
            webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + self.entry1.get())

    def get(self,event):
        """The same as the callback function but here we press enter key"""

        if self.string.get() == 'Semantic Scholar':
            webbrowser.open('https://www.semanticscholar.org/search?q= '+ self.entry1.get())

        elif self.string.get() == 'Nature':
            webbrowser.open('https://www.nature.com/search?q='+self.entry1.get())

        elif self.string.get() == "NCBI":
            webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + self.entry1.get())

        elif self.string.get() == "All":
            webbrowser.open('https://www.semanticscholar.org/search?q= '+ self.entry1.get())
            webbrowser.open('https://www.nature.com/search?q='+self.entry1.get())
            webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + self.entry1.get())

if __name__ == "__main__":
    Acad_engine(tk.Tk(), "Academic Seach Engine")
