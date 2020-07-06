from tkinter import * 
from tkinter import ttk
import random
import time as tm
GUI = Tk()
GUI.geometry('500x200')
GUI.title("movies random")
rand = StringVar()
a1 = ttk.Label(GUI, textvariable=rand).place(x=50, y=100)
r1 = ttk.Button(GUI, text="สุ่ม", command=random).place(x=200, y=100)
movies = {"Frozan 2":"https://www.newmovie-hd.org/doonung/frozen-ii-2019/",
        "Jumanji Next level 2019":"https://www.newmovie-hd.org/doonung/jumanji-the-next-level-2019/"}
movieslit = list(movies.keys())
def random():
    rand.set(movies)

GUI.mainloop()