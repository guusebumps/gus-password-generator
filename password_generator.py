import random
from tkinter import *

def generate_password():

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '#@$%&*-=+/.'

    all = lower + upper + numbers + symbols
    length = 16

    password = "".join(random.sample(all, length))
    print(f'Your password: {password}')

    texto_resposta['text'] = f'''
    Password: {password}'''


window = Tk()
window.title("Password Generator")
texto = Label(window, text="Click to generate a strong password")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(window, text="Generate", command=generate_password)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(window, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()
