from tkinter import *
import subprocess
import os

# папка загрузок текущего пользователя — работает у всех
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
folder = os.path.join(downloads, "ZetaFile")


# у тебя:    C:\Users\lenovo\Downloads\ZetaFile
# у Ивана:   C:\Users\Ivan\Downloads\ZetaFile
# у Марии:   C:\Users\Мария\Downloads\ZetaFile


file = r"C:\Users\<name_name>\Downloads\ZetaFile\git.текстовый редактор.py"
file2 = r"C:\Users\lenovo\Downloads\ZetaFile\git.читатель.py"
file3 = r"C:\Users\lenovo\Downloads\ZetaFile\git.измена имени.py"
r = 0
window = Tk()
window.title("меню")
window.geometry("450x450")
window.resizable(width=False, height=False)


def click11():
    subprocess.Popen(
        ['cmd', '/k', 'python', file],
        cwd=os.path.dirname(file)
    )
def click22():
    subprocess.Popen(
        ['cmd', '/k', 'python', file2],
        cwd=os.path.dirname(file2)
    )

def click33():
    subprocess.Popen(
        ['cmd', '/k', 'python', file3],
        cwd=os.path.dirname(file3)
    )

button1 = Button(text='текстовый редактор', font=(20), command=click11)
button1.place(x=150, y=135, width=150)

button2 = Button(text='читатель', font=(20), command=click22)
button2.place(x=150, y=235, width=150)

button3 = Button(text='изменить имя', font=(20), command=click33)
button3.place(x=150, y=45, width=150)





window.mainloop()










