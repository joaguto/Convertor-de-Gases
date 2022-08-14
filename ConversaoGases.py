# Importando pacote necessario
from tkinter import *
from IPython.display import Image
import os

# Criando a interface gráfica
class Application:
    def __init__(self, master=None):
        # Criando o espaço do titulo
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        # Criando o espaço do Valor do gás
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        # Criando o espaço do Valor da temperatura
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        #Criando o espaço do Valor da pressao
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        # Criando o espaço do Valor da massa molecular
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        #Criando o espaço da Resposta final
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        # Opção de escolha de qual transformação
        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack()

        # Definindo o titulo
        self.titulo = Label(self.primeiroContainer, text="Calculadora de Conversão de gases")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Valor do gás
        self.gasLabel = Label(self.segundoContainer, text="Valor do Gás", font=self.fontePadrao)
        self.gasLabel.pack(side=LEFT)

        self.gas = Entry(self.segundoContainer)
        self.gas["width"] = 30
        self.gas["font"] = self.fontePadrao
        self.gas.pack(side=LEFT)

        # Valor da temperatura
        self.tempLabel = Label(self.terceiroContainer, text="Temperatura (C°)", font=self.fontePadrao)
        self.tempLabel.pack(side=LEFT)

        self.temp = Entry(self.terceiroContainer)
        self.temp["width"] = 30
        self.temp["font"] = self.fontePadrao
        self.temp.pack(side=LEFT)

        # Valor da pressão
        self.pressaoLabel = Label(self.quartoContainer, text="Pressão (atm)", font=self.fontePadrao)
        self.pressaoLabel.pack(side=LEFT)

        self.pressao = Entry(self.quartoContainer)
        self.pressao["width"] = 30
        self.pressao["font"] = self.fontePadrao
        self.pressao.pack(side=LEFT)

        # Valor da massa molecular
        self.MMLabel = Label(self.quintoContainer, text="Massa Molecular", font=self.fontePadrao)
        self.MMLabel.pack(side=LEFT)

        self.MM = Entry(self.quintoContainer)
        self.MM["width"] = 30
        self.MM["font"] = self.fontePadrao
        self.MM.pack(side=LEFT)

        # Opção numero 1
        self.autenticar = Button(self.setimoContainer)
        self.autenticar["text"] = "Transformar PPM para mg/m^3"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 30
        self.autenticar["command"] = self.ppm_to_mg
        self.autenticar.pack(side=LEFT)

        # Opção numero 2
        self.autenticar = Button(self.setimoContainer)
        self.autenticar["text"] = "Transformar mg/m^3 para PPM"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 30
        self.autenticar["command"] = self.mg_to_ppm
        self.autenticar.pack(side=RIGHT)

        # Resultado final
        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Transformar ppm para mg
    def ppm_to_mg(self):
        # Inputs
        temp = float(self.temp.get())
        pressao = float(self.pressao.get())
        MM = float(self.MM.get())
        valor = float(self.gas.get())

        # Formula de conversão
        resultado = round((valor * (1 / (6.02 * 10 ** 23))) / ((1.66 * 10 ** (-18) * (0.082) * (273 + (temp)) /
                                                                (pressao))) * ((MM) * 1000 * 1000), 2)
        self.mensagem["text"] = resultado, 'mg/m^3'

    def mg_to_ppm(self):
        # Inputs
        temp = float(self.temp.get())
        pressao = float(self.pressao.get())
        MM = float(self.MM.get())
        valor = float(self.gas.get())

        # Formula de conversão
        resultado2 = round((valor) * (1.66 * 10 ** (-18)) * (0.082) * (273 + (temp)) / (
                (pressao) * (MM) * (1000) * (1000) * (1 / (6.02 * 10 ** (23)))), 2)

        self.mensagem["text"] = resultado2, 'ppm'


root = Tk()
Application(root)
root.mainloop()