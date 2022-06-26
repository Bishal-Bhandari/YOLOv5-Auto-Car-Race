import os
from tkinter import messagebox


def askMe():
    res = messagebox.askquestion('askquestion', 'Do you want to try again?')
    if res == 'yes':
        os.system('python "D:\Project\YOLOgame\main.py"')
    elif res == 'no':
        quit()
    else:
        messagebox.showwarning('error', 'Something went wrong!')
        quit()
    return res
