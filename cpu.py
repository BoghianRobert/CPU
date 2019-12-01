from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title("Componente")
root.iconbitmap('cpu.ico')
root.geometry("500x300")

f1 = Frame(root, width=500, height=300, bg='grey')
f1.place(x=0 ,y=0)
f2 = Frame(root, width=500, height=300, bg='grey')
f2.place(x=0, y=0)



nume = Label(f1, text="Nume", fg='white', bg='grey')
parola = Label(f1, text="Parola", fg='white', bg='grey')
nume.place(x=180, y=108)
parola.place(x=180, y=134)


nume_entry = Entry(f1)
parola_entry = Entry(f1, show="*")
nume_entry.place(x=230, y=108)
parola_entry.place(x=230, y=134)


# buton verificare

def verificare():
    nume_introdus = nume_entry.get()
    if nume_introdus == "":
        tkinter.messagebox.showinfo("Mesaj", "Introduceti un nume de utilizator")
    else:
        parola_introdusa = parola_entry.get()
        if parola_introdusa == 'parola':
            nume_utilizator = nume_entry.get()
            name_tag = Label(f2, text=nume_utilizator, bg='grey')
            name_tag.place(x=10, y=10)
            raise_frame(f2)
            parola_entry.delete(0, "end")
        else:
            tkinter.messagebox.showinfo("Mesaj", "Parola este gresita")
            parola_entry.delete(0, "end")


parola_entry.bind('<Return>', lambda event: verificare())

verifica = Button(f1, text='verifica', fg='white', bg='grey', command=verificare)
verifica.place(x=250, y=165)

# f2



# centrul ferestrei
procesoare = [
    ['i3 8100', '3500 Mhz', '4 nuclee'],
    ['i5 7400', '3000 Mhz', '4 nuclee'],
    ['i7 3370', '3400 Mhz', '4 nuclee'],
    ['i7 9700k', '3600 Mhz', '8 nuclee'],
    ['i9 9900k', '3600 Mhz', '8 nuclee']
]


procesor1 = StringVar()
procesoare1 = ttk.Combobox(f2, textvariable=procesor1,
    values=[procesoare[0][0], procesoare[1][0], procesoare[2][0], procesoare[3][0], procesoare[4][0]])
procesoare1.place(x=115, y=70)


procesor2 = StringVar()
procesoare2 = ttk.Combobox(f2, textvariable=procesor2,
    values=[procesoare[0][0], procesoare[1][0], procesoare[2][0], procesoare[3][0], procesoare[4][0]])
procesoare2.place(x=255, y=70)


textfield1 = Text(f2, width=16, height=4)
textfield1.place(x=115, y=130)
textfield2 = Text(f2, width=16, height=4)
textfield2.place(x=255, y=130)


def comparatie():
    textfield1.delete('1.0', END)
    textfield2.delete('1.0', END)
    if procesor1.get() == '' and procesor2.get() == '':
        tkinter.messagebox.showinfo("Mesaj", "Selectati cel putin un procesor")
    for i in range(0, 5):
        if procesoare[i][0] == procesor1.get():
            textfield1.insert(END, procesoare[i][0]+'\n'+procesoare[i][1]+'\n'+procesoare[i][2])
        if procesoare[i][0] == procesor2.get():
            textfield2.insert(END, procesoare[i][0]+'\n'+procesoare[i][1]+'\n'+procesoare[i][2])




procesoare2.bind('<Return>', lambda event: comparatie())



compara = Button(f2, text="Compara", bg='grey', command=comparatie)
compara.place(x=220, y=100)





inapoi = Button(f2, text="Inapoi", bg='grey', command=lambda: raise_frame(f1))
inapoi.place(x=10, y=260)


def cul_negru():
    procesoare1.config(foreground='black')
    procesoare2.config(foreground='black')
    compara.config(fg='black')
    textfield1.config(fg='black')
    textfield2.config(fg='black')
    inapoi.config(fg='black')
    nume_utilizator = nume_entry.get()
    name_tag = Label(f2, text=nume_utilizator, fg='black', bg='grey')
    name_tag.place(x=10, y=10)


def cul_albastru():
    procesoare1.config(foreground='blue')
    procesoare2.config(foreground='blue')
    compara.config(fg='blue')
    textfield1.config(fg='blue')
    textfield2.config(fg='blue')
    inapoi.config(fg='blue')
    nume_utilizator = nume_entry.get()
    name_tag = Label(f2, text=nume_utilizator, fg='blue', bg='grey')
    name_tag.place(x=10, y=10)



def cul_verde():
    procesoare1.config(foreground='green')
    procesoare2.config(foreground='green')
    compara.config(fg='green')
    textfield1.config(fg='green')
    textfield2.config(fg='green')
    inapoi.config(fg='green')
    nume_utilizator = nume_entry.get()
    name_tag = Label(f2, text=nume_utilizator, fg='green', bg='grey')
    name_tag.place(x=10, y=10)


culoare = IntVar()
negru = Radiobutton(f2, text="negru", variable=culoare, value=1, bg='grey', command=cul_negru)
albastru = Radiobutton(f2, text="albastru", variable=culoare, value=2, bg='grey', command=cul_albastru)
verde = Radiobutton(f2, text="verde", variable=culoare, value=3, bg='grey', command=cul_verde)


negru.place(x=10, y=30)
albastru.place(x=10, y=50)
verde.place(x=10, y=70)

raise_frame(f1)
root.mainloop()
