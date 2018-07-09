"""
Docstring:
Desktop app that runs search on main acadmeic search engines
"""

import tkinter as tk
from tkinter import ttk
import webbrowser


ROOT = tk.Tk()
ROOT.title('Academic Search Engine')

LABELL = ttk.Label(ROOT, text='Query')
LABELL.grid(row=0, column=0)
ENTRY1 = ttk.Entry(ROOT, width=50)
ENTRY1.grid(row=0, column=1)

Btn2 = tk.StringVar()

def callback():
    """Uses the webbrowser to open an url"""
    if Btn2.get() == 'Semantic Scholar':
        webbrowser.open('https://www.semanticscholar.org/search?q= ' + ENTRY1.get())

    elif Btn2.get() == 'Nature':
        webbrowser.open('https://www.nature.com/search?q='+ENTRY1.get())

    elif Btn2.get() == "NCBI":
        webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + ENTRY1.get())

    elif Btn2.get() == "Todos":
        webbrowser.open('https://www.semanticscholar.org/search?q= '+ ENTRY1.get())
        webbrowser.open('https://www.nature.com/search?q='+ENTRY1.get())
        webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + ENTRY1.get())



def get(event):
    """The same as the callback function but here we press enter key"""

    if Btn2.get() == 'Semantic Scholar':
        webbrowser.open('https://www.semanticscholar.org/search?q= '+ ENTRY1.get())

    elif Btn2.get() == 'Nature':
        webbrowser.open('https://www.nature.com/search?q='+ENTRY1.get())

    elif Btn2.get() == "NCBI":
        webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + ENTRY1.get())

    elif Btn2.get() == "Todos":
        webbrowser.open('https://www.semanticscholar.org/search?q= '+ ENTRY1.get())
        webbrowser.open('https://www.nature.com/search?q='+ENTRY1.get())
        webbrowser.open("https://www.ncbi.nlm.nih.gov/search/?term=" + ENTRY1.get())


BUTTON_1 = ttk.Button(ROOT, text='Search', width=10, command=callback)
BUTTON_1.grid(row=0, column=2)

ENTRY1.bind('<Return>', get)

BUTTON_2 = ttk.Radiobutton(ROOT, text='Semantic Scholar', value='Semantic Scholar', variable=Btn2)
BUTTON_2.grid(row=1, column=1, sticky='W')

BUTTON_3 = ttk.Radiobutton(ROOT, text='Nature', value='Nature', variable=Btn2)
BUTTON_3.grid(row=1, column=1, sticky='E')

BUTTON_4 = ttk.Radiobutton(ROOT, text='NCBI', value='NCBI', variable=Btn2)
BUTTON_4.grid(row=1, column=1, sticky='N')

BUTTON_5 = ttk.Radiobutton(ROOT, text='Todos', value='Todos', variable=Btn2)
BUTTON_5.grid(row=1, column=2, sticky='S')




ENTRY1.focus()

ROOT.wm_attributes('-topmost', 1)

ROOT.mainloop()
