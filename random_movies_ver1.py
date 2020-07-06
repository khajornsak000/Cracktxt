from tkinter import * 
from tkinter import ttk
import random 
import time as tm
GUI = Tk()
ttk.Frame(height=200, width=500).pack()
GUI.title("วันนี้ดูหนังไรดี")
inp = StringVar()
strvalue = StringVar()
wait = StringVar()
gou = ttk.Radiobutton(GUI, text="หนังผี", value="goust", variable=strvalue).place(x= 400,y=30)
ani = ttk.Radiobutton(GUI, text="อนิเมชั่น", value="animation", variable=strvalue).place(x= 400,y=60)
act = ttk.Radiobutton(GUI, text="แอคชั่น บ้าระห่ำ", value="action", variable=strvalue).place(x= 400,y=90)
com = ttk.Radiobutton(GUI, text="ตลกคอมเมดี้", value="commady", variable=strvalue).place(x= 400,y=120)

value = strvalue.get()
movies ={"Frozen 2":"https://www.newmovie-hd.org/doonung/frozen-ii-2019/",
         "Jumanji Next level 2019":"https://www.newmovie-hd.org/doonung/jumanji-the-next-level-2019/",
         "Star war the rise of skywalker":"https://www.newmovie-hd.org/doonung/star-wars-the-rise-of-skywalker-2019/",
         "Maleficent":"https://www.newmovie-hd.org/doonung/maleficent-mistress-of-evil-2019/",
         "Next Gen":"https://www.newmovie-hd.org/doonung/next-gen-2018/",
         "จ้างผีมาเลี้ยงเด็ก":"https://www.doomovie-hd.com/?r=movie_view&id=21163",
         "Terminator 6 the Fate": "https://www.newmovie-hd.org/doonung/terminator-dark-fate-2019/",
         }
movieslist = list(movies.keys())
def random():
    import random
    inp.set(random.choice(movieslist))
    b1 = ttk.Button(GUI, text="ลิ้งดูหนัง", command=link).place(x=150, y=80)
    wait.set("")
def link(): 
    
    import webbrowser
    webbrowser.open(movies[inp.get()],new=2)
    wait.set("รอสักครู่...")
    """
    inp1.set(movies[inp.get()])
    """   
def help():
    import tkinter as tk
    mainfrm = tk.Tk()
    txt = tk.Text(mainfrm,font=("Angsana New", 14),  height=10, width=30, padx=5, pady=5)
    txt.pack(padx=5, pady=5)
    mainfrm.mainloop()

out1 = ttk.Label(GUI, textvariable=inp, font=('Angsana New', 20))
out1.place(x=80, y=30)
wai = ttk.Label(GUI, textvariable=wait, font=('Angsana New', 12))
wai.place(x=120, y=120)
"""
out2 = ttk.Label(GUI, textvariable=inp1)
out2.place(x=60, y=50)
"""
bt1 = ttk.Button(GUI, text="สุ่ม", command=random)
bt1.place(x=50, y=80)
hel = ttk.Button(GUI, text="ต้องการความช่วยเหลือ", command=help).place(x=380, y=170)
GUI.mainloop()


