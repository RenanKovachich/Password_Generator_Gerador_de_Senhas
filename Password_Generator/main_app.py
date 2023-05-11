# https://www.usandopy.com/pt/artigo/como-gerar-senhas-aleatorias-em-python-usando-o-modulo-random/
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import random
import string

# Cores ---------------

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#f05a43"  # vermelha

fundo_dark = "#484f60"
fundo_claro = "#fff"

fundo = co1

# Janela ---------------

root = Tk()
root.title("Password Generator")
root.geometry('300x360')
root.configure(bg=fundo)
root.resizable(width=FALSE, height=FALSE)

# Frames ---------------

frameMain = Frame(root, width=300, height=110, bg=fundo, padx=0, pady=0, relief='flat')
frameMain.grid(row=0, column=0)

frameBox = Frame(root, width=300, height=220, bg=fundo, pady=0, padx=0, relief='flat')
frameBox.grid(row=1, column=0)

style = ttk.Style(root)
style.theme_use('clam')

img_0 = Image.open('logo.png')
img_0 = img_0.resize((30, 30), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

app_imagem = Label(frameMain, height=60, image=img_0, compound=LEFT, padx=10, relief='flat', anchor=NW,
                   font='Ivy 16 bold', bg=co1, fg=co3)
app_imagem.place(x=2, y=0)

app_name = Label(frameMain, text='Gerador de Senhas', width=20, height=1, padx=0, relief='flat', anchor=NW,
                 font='Ivy 16 bold', bg=co1, fg=co0)
app_name.place(x=35, y=2)

app_linha = Label(frameMain, text='', width=400, height=1, padx=0, relief='flat', anchor=NW, font="Arial 1", bg=co3,
                  fg=co1)
app_linha.place(x=0, y=35)




def criar_senha():
    alfabeto_menos = string.ascii_lowercase
    alfabeto_mais = string.ascii_uppercase
    numeros = '0123456789'
    simbolos = "#![]{}()*;/,_-"

    global combinar

    # --- condicao para maiusculas
    if estado_1.get() == alfabeto_mais:
        combinar = combinar - alfabeto_mais
    else:
        pass

    # --- condicao para minuscula
    if estado_2.get() == alfabeto_menos:
        combinar = combinar - alfabeto_menos
    else:
        pass

    # --- condicao para numeros
    if estado_3.get() == numeros:
        combinar = combinar - numeros
    else:
        pass

    # --- condicao para simbolos
    if estado_4.get() == simbolos:
        combinar = combinar - simbolos
    else:
        pass

    # --- Comprimento da senha

    comprimento = int(spin.get())

    # --- Senha

    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    # funcao para cpiar a senha

    def copiar_senha():
        info = senha
        frameBox.clipboard_clear()
        frameBox.clipboard_append(info)
        messagebox.showinfo("Sucesso", "A senha foi copiada com sucesso")

    b_copiar = Button(frameBox, command=copiar_senha, text="Copiar", width=7, height=1, overrelief=SOLID, bg=co1,
                      fg=co0, font='Ivy 10 bold', anchor="center", relief=RAISED)
    b_copiar.grid(row=0, column=2, columnspan=2, sticky=NSEW, pady=10, padx=1)


alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = '0123456789'
simbolos = "#![]{}()*;/,_-"
combinar = alfabeto_mais + alfabeto_menos + numeros + simbolos

var = IntVar()
var.set(8)
app_info = Label(frameMain, text="Número total de caracteres na senha", height=1, padx=0, relief='flat', anchor=NW,
                 font='Ivy 10 bold', bg=fundo, fg=co0)
app_info.place(x=15, y=60)

spin = Spinbox(frameMain, from_=0, to=20, width=5, textvariable=var)
spin.place(x=20, y=90)

app_senha = Label(frameBox, text='- - -', width=20, height=2, padx=0, relief='solid', anchor=CENTER, font='Ivy 10 bold',
                  bg=fundo, fg=co0)
app_senha.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=10, padx=2)

# Letras Maiúsculas ---------------

app_info = Label(frameBox, text="ABC Letras maiúsculas", height=1, padx=0, relief='flat', anchor=NW, justify='center',
                 font='Ivy 10 bold', bg=co1, fg=co0)
app_info.grid(row=1, column=1, sticky=NSEW, pady=5, padx=2)

estado_1 = BooleanVar()
estado_1.set(False)
check_1 = Checkbutton(frameBox, width=1, onvalue=alfabeto_mais, offvalue='off', bg=fundo)
check_1.grid(row=1, column=0, sticky=NSEW, pady=5, padx=2)

# ------------ Letras minúsculas ------------------

app_info = Label(frameBox, text="abc Letras minúsculas", height=1, padx=0, relief="flat", anchor="nw", justify='center',
                 font='Ivy 10 bold', bg=co1, fg=co0)
app_info.grid(row=2, column=1, sticky=NSEW, pady=5, padx=2)

estado_2 = BooleanVar()
estado_2.set(False)  # set check state
chek_2 = Checkbutton(frameBox, width=1, onvalue=alfabeto_menos, offvalue='off', bg=fundo)
chek_2.grid(row=2, column=0, sticky=NSEW, pady=5, padx=2)

# ------------ Números ------------------

app_info = Label(frameBox, text="123 Números", height=1, padx=0, relief="flat", anchor="nw", justify='center',
                 font='Ivy 10 bold', bg=co1, fg=co0)
app_info.grid(row=3, column=1, sticky=NSEW, pady=5, padx=2)

estado_3 = BooleanVar()
estado_3.set(False)  # set check state
chek_3 = Checkbutton(frameBox, width=1, onvalue=numeros, offvalue='off', bg=fundo)
chek_3.grid(row=3, column=0, sticky=NSEW, pady=5, padx=2)

# ------------ Símbolos ------------------

app_info = Label(frameBox, text="!@# Símbolos", height=1, padx=0, relief="flat", anchor="nw", justify='center',
                 font='Ivy 10 bold', bg=co1, fg=co0)
app_info.grid(row=4, column=1, sticky=NSEW, pady=1, padx=2)

estado_4 = BooleanVar()
estado_4.set(False)  # set check state
chek_4 = Checkbutton(frameBox, width=1, onvalue=simbolos, offvalue='off', bg=fundo)
chek_4.grid(row=4, column=0, sticky=NSEW, pady=1, padx=2)

# ------------ Botao gerar senha ------------------

b_gerar_senha = Button(frameBox, command=criar_senha, text="Gerar senha", width=32, height=1, overrelief=SOLID, bg=co3,
                       fg="white", font='Ivy 10 bold', anchor="center", relief=FLAT)
b_gerar_senha.grid(row=5, column=0, sticky=NSEW, pady=20, padx=0, columnspan=5)

root.mainloop()
