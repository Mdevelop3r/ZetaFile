from tkinter import *
import subprocess
import os

file = r"C:\Users\lenovo\Downloads\ZetaFile\git.текстовый редактор.py"
file2 = r"C:\Users\lenovo\Downloads\ZetaFile\git.читатель.py"


window = Tk()
window.title("меню")
window.geometry("450x500")
window.resizable(width=False, height=False)


def click11():
    # Запускаем cmd, переходим в папку с файлом и запускаем редактор.
    # subprocess сам экранирует путь — кавычки расставлять вручную не нужно.
    subprocess.Popen(
        ['cmd', '/k', 'python', file],
        cwd=os.path.dirname(file)
    )
def click22():
    # Запускаем cmd, переходим в папку с файлом и запускаем редактор.
    # subprocess сам экранирует путь — кавычки расставлять вручную не нужно.
    subprocess.Popen(
        ['cmd', '/k', 'python', file2],
        cwd=os.path.dirname(file2)
    )

button1 = Button(text='текстовый редактор', font=(14), command=click11)
button1.place(x=150, y=100, width=150)

button2 = Button(text='читатель', font=("Arial", 14), command=click22)
button2.place(x=150, y=200, width=150)

window.mainloop()
