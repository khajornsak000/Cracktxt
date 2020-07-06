from tkinter import *
from tkinter import ttk
import random
GUI = Tk()
GUI.geometry('500x300')
GUI.title('ลงทะเบียนเยียวยาช่วงโควิด')
result = StringVar()
result2 = StringVar()
L1 = ttk.Label(GUI, textvariable=result,font=("Angsana New", 16))
L1.place(x=220, y=150)
L2 = ttk.Label(GUI, textvariable=result2,font=("Angsana New", 16))
L2.place(x= 210, y= 150) 
C1 = ttk.Label(GUI, text='คุณต้องการดำเนินต่อหรือไม่', font=("Angsana New", 20)).place(x=150, y=50)
vocab = {"success":"ลงทะเบียนสำเร็จ"}
vocabeng = list(vocab.keys())
def success():
    result.set("complete")
    result2.set("")
def close():
    result2.set("close")
    result.set("")
B2 = ttk.Button(GUI,text='ยกเลิก',command=close)
B1 = ttk.Button(GUI,text='ยืนยัน', command=success)
B1.grid(column=0, row=0, pady = 20, padx=20)
B2.grid(column=1, row=0)

GUI.mainloop()