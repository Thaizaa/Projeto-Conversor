from os import readlink
from tkinter import *
from tkinter import ttk
from funcao import lista_moedas, converte, trata_valor

janela = Tk()
frm = ttk.Frame(janela, padding=5)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=janela.destroy).grid(column=1, row=0)
janela.title("Conversor de Moedas")
janela.configure(background="#990000")
janela.geometry("500x300")
# caixa  de texto do valor inicial
label = Label(janela, text="Valor Inicial")
label.grid(row=0, column=0)
valor_inicial = Entry(janela, bd=2, width=10)
valor_inicial.grid(row=0, column=1)

# Lista de moedas
primeira_moeda = ttk.Combobox(janela, width=10, state="readonly", values=lista_moedas())
primeira_moeda.grid(column=1, row=2)
primeira_moeda.current(18)
print(primeira_moeda.current(), primeira_moeda.get())

segunda_moeda = ttk.Combobox(janela, width=10, state="readonly", values=lista_moedas())
segunda_moeda.grid(column=2, row=2)
segunda_moeda.current(0)

# Botão
valor_moeda = valor_inicial.get()
valor_primeira_moeda = primeira_moeda.get()
valor_segunda_moeda = segunda_moeda.get()


def calcula_valores():
    valor_moeda = trata_valor(valor_inicial.get())
    valor_primeira_moeda = primeira_moeda.get()
    valor_segunda_moeda = segunda_moeda.get()
    print(converte(valor_moeda, valor_primeira_moeda, valor_segunda_moeda))


ttk.Button(janela, text="Converter", command=calcula_valores).grid(column=3, row=2)


visualizacao = Text(janela, height=5, width=52).grid(column=7, row=4)
visualizacao.pack()
visualizacao.insert(janela.END, "valor aqui")


janela.mainloop()
