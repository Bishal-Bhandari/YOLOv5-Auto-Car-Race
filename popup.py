import os
import sys
from tkinter import messagebox


def askMe():
    res = messagebox.askquestion('askquestion', 'Do you want to try again?')
    if res == 'yes':
        os.startfile(sys.argv[0])
        sys.exit()
    elif res == 'no':
        quit()
    else:
        messagebox.showwarning('error', 'Something went wrong!')
        quit()
