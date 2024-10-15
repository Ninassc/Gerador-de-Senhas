import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import random

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

class window(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.firstConfigs()
        self.frame()
        self.tema()
        self.corpo()

    
    def firstConfigs(self):
        self.geometry('400x500')
        self.title('Gerador de Senhas')
        self.resizable(False, False)

    
    def mudarTema(self, novoTema):
        ctk.set_appearance_mode(novoTema)


    def tema(self):
        labelTema = ctk.CTkLabel(self, text='Tema', font=('Arial bold',14), text_color=['#000', '#fff'])
        labelTema.place(x=10, y=435)

        escolherTema = ctk.CTkComboBox(self, values=['System', 'Dark'], border_color='#739c72', text_color=['#000', '#fff'], command=self.mudarTema)
        escolherTema.place(x=10, y=465)
        

    def frame(self):
        Frame = ctk.CTkFrame(self, width=400, height=100, fg_color='#739c72')
        Frame.place(x=0, y=0)

        titulo = ctk.CTkLabel(self, text='Gerador de Senhas', font=('Arial bold', 25), bg_color='#739c72', text_color='#fff')
        titulo.pack(pady=35)


    def corpo(self):
        labelQuantidade = ctk.CTkLabel(self, text='Número de caracteres: ', font=('Arial bold',16), text_color=['#000', '#fff'])
        labelQuantidade.pack(pady=15)

        entryQuantidade = ctk.CTkEntry(self, placeholder_text='Ex: 10', font=('Arial bold',14), text_color=['#000', '#fff'], border_color='#739c72')
        entryQuantidade.pack()


        def gerar():
            obterValor = entryQuantidade.get()
            print(obterValor)
            quantidadeCaracteres = int(obterValor)

            if quantidadeCaracteres <= 0:
                messagebox.showwarning('Nina System', 'Digite uma quantidade válida!')

            else:
                todos_caracteres = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@&')
                random.shuffle(todos_caracteres)
                senha = ''.join(todos_caracteres[:quantidadeCaracteres])
                print(senha)

                resultado.configure(text=senha)

        frameResultado = ctk.CTkFrame(self, width=300, height=50, fg_color='#739c72')
        frameResultado.pack(pady=30)

        resultado = ctk.CTkLabel(self, text=' ', font=('Arial bold',20), text_color='#fff', bg_color='#739c72')
        resultado.place(x=150, y=225)


        btnGerar = ctk.CTkButton(self, text='Gerar', font=('Arial bold',16), fg_color='#739c72', command=gerar)
        btnGerar.pack(pady=25)




janela = window()
janela.mainloop()
