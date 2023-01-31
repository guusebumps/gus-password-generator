import random
from tkinter import *

def gerar_senhas():

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '#@$%&*-=+/.'

    all = lower + upper + numbers + symbols
    length = 16

    senha = "".join(random.sample(all, length))

    texto_resposta['text'] = f'''
    Senha: {senha}'''

janela = Tk()
janela.title("Gerador de Senhas")
texto = Label(janela, text="Clique no botão gerar uma senha")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Gerar senha", command=gerar_senhas)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
