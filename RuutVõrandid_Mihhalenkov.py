from math import *
from tkinter import *
k=0
#def klikker():
#    global k
#    k+=1
#    nupp.configure(text=k)
def reshit():
    print("")

def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

tekst="Aken"
aken=Tk()
aken.geometry("700x300")
aken.title(tekst)
aken.iconbitmap("image2.ico") #Для иконки

pealkiri=Label(aken, #Надпись сверху
               text="Решение квадратного уравнения  ",
               bg="Lightblue",
               fg="#24ab67",
               font="Times_New_Roman 20", #Algerian
               height=1,
               width=28)
tekst_kast=Entry(aken,
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)
pealkiri1=Label(aken, #Пишет x**2
               text="x**2+",
               fg="#24ab67",
               font="Times_New_Roman 20", #Algerian
               height=2,
               width=5)
tekst_kast1=Entry(aken,
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=2,
                 justify=LEFT)
pealkiri2=Label(aken, #Пишет x+
               text="x+",
               fg="#24ab67",
               font="Times_New_Roman 20", #Algerian
               height=2,
               width=2)
tekst_kast2=Entry(aken,
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)
pealkiri3=Label(aken, #Пишет x+
               text="=0",
               fg="#24ab67",
               font="Times_New_Roman 20", #Algerian
               height=2,
               width=2)
nupp=Button(aken, #Кнопка Решить
            text="Решить",
            bg="green",
            fg="black",
            font="Algerian 20",
            height=2,
            width=10,
            command=reshit)
nupp2=Button(aken,
            text="Решение",
            bg="yellow",
            fg="black",
            font="Algerian 20",
            height=2,
            width=20,
            command=reshit)

tekst_kast.bind("<Return>",text_to_lbl) #Enter







pealkiri.pack()
nupp2.pack(side=BOTTOM)
tekst_kast.pack(side=LEFT)#side-LEFT,RIGHT
pealkiri1.pack(side=LEFT)
tekst_kast1.pack(side=LEFT)
pealkiri2.pack(side=LEFT)
tekst_kast2.pack(side=LEFT)
pealkiri3.pack(side=LEFT)
nupp.pack(side=LEFT)
aken.mainloop()
