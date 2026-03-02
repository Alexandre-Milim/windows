import customtkinter as tk
from PIL import Image
from tkcalendar import *
primeiro = True

def CriarJanela(Titulo,Tamanho,Tipo,Cor=0,Redimensionar=False):
    if Tipo == 1:
        Janela = tk.CTk()
    elif Tipo==2:
        Janela = tk.CTkToplevel()
    elif Tipo == 3:
        Janela = tk.CTkInputDialog()
    Janela.title(Titulo)
    if Cor !=0:
     Janela.configure(fg_color=Cor)
    if Redimensionar==True:
     Janela.resizable(width=True, height=True)
    else:
     Janela.resizable(width=False, height=False)
    Colunas = list(range(13))
    Linhas = list(range(13))
    Janela.grid_columnconfigure(Colunas, weight=1)
    Janela.grid_rowconfigure(Linhas, weight=1)
    Janela.geometry(Tamanho)
    return Janela

def CriarBotao(Local,Texto,Comando,Linha,Coluna,Largura,Altura,Cor=0,CorHover=0,CorBackground=0,Imagem="Nada"):
    if Imagem!="Nada":
        imagem_pillow = Image.open(Imagem)
        imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
        botao = tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura, image=imageTk)
        botao.grid(row=Linha, column=Coluna)
    else:
        botao = tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura)
        botao.grid(row=Linha, column=Coluna)
    if Cor != 0:
            botao.configure(fg_color=Cor)
    if CorHover != 0:
            botao.configure(hover_color=CorHover)
    return botao

def CriarCaixaDeTexto(Local: object, Largura: object, Altura: object, Linha: object, Coluna: object, Texto: object = 0, Modo: object = "Padrão") -> object:
    Caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    Caixa.grid(row=Linha,column=Coluna)
    if Texto!=0:
     Caixa.configure(placeholder_text=Texto)
    if Modo == "Senha":
        Caixa.configure(show="*")
        def SenhaMostra():
            global primeiro
            if primeiro:
                imagem_pillow = Image.open("Imagens/eye.ico")
                imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                Caixa.configure(show="")
                primeiro = False
            else:
                imagem_pillow = Image.open("Imagens/eye2.ico")
                imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                Caixa.configure(show="*")
                primeiro = True
        MostraSenha = CriarBotao(Caixa, "", SenhaMostra, 0, 0, 10, 10, Imagem="Imagens/eye2.ico")
        MostraSenha.grid(sticky="e", padx=2)
        MostraSenha.configure(fg_color=Caixa.cget("fg_color"), hover_color=Caixa.cget("fg_color"), corner_radius=0)
    elif Modo == "Moeda":
        def format_moeda(event=None):
            text = Caixa.get().replace("R$", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "R$" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_moeda)
    elif Modo == "CPF":
        def format_cpf(event=None):
            text = Caixa.get().replace(".", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):

                if not text[index] in "0123456789": continue
                if index in [2, 5]:
                    new_text += text[index] + "."
                elif index == 8:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_cpf)
    elif Modo == "CNPJ":
        def format_CNPJ(event=None):
            text = Caixa.get().replace(".", "").replace("/", "").replace("-", "")[:14]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 7:
                    new_text += text[index] + "/"
                elif index == 11:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_CNPJ)
    elif Modo == "Telefone":
        def format_tel(event=None):
            text = Caixa.get().replace("(", "").replace(")", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 1:
                    new_text += text[index] + ")"
                elif index == 5:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_tel)
    elif Modo == "Data":
        def format_data(event=None):
            text = Caixa.get().replace("/", "")[:8]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue
                if index in [1, 3]:
                    new_text += text[index] + "/"
                elif index == 9:
                    new_text += text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_data)
    elif Modo == "CEP":
        def format_cep(event=None):
            text = Caixa.get().replace("-", "")[:8]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue
                if index == 5:
                    new_text += "-" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_cep)

    return Caixa

def CriarLabel(Local,Texto,Linha,Coluna,Cor="black"):
    Label = tk.CTkLabel(Local,text=Texto)
    Label.grid(row=Linha,column=Coluna)
    if Cor!="black":
        Label.configure(text_color=Cor)
    return Label

def CriarCheckBox(Local,Texto,Linha,Coluna,Comando=0):
    check = tk.CTkCheckBox(Local,text=Texto)
    check.grid(row=Linha,column=Coluna)
    if Comando!=0:
        check.configure(command=Comando)
    return check

def CriarCheckBox2(Local,Texto,Linha,Coluna,Comando=0):
    check = tk.CTkCheckBox(Local,text=Texto)
    check.grid(row=Linha, column = Coluna)
    if Comando!=0:
        check.configure(command=Comando)
    return check

def CriarComboBox(Local, Largura, Altura, Valores, Linha, Coluna, Comando=0, CorBackground=None):
    combo = tk.CTkComboBox(Local, width=Largura, height=Altura, values=Valores, state="readonly")
    combo.grid(row=Linha, column=Coluna)
    combo.set("Selecione")
    if Comando != 0:
        combo.configure(command=Comando)
    if CorBackground:
        combo.configure(bg_color=CorBackground)
    return combo

def CriarProgressBar(Local,Largura,Altura,Linha,Coluna):
    progress = tk.CTkProgressBar(Local,width=Largura,height=Altura)
    progress.grid(row=Linha,column=Coluna)
    progress.set(0)
    return progress

def CriarSwitch(Local,Texto,Linha,Coluna,Comando=0):
    switch = tk.CTkSwitch(Local,text=Texto)
    switch.grid(row=Linha,column=Coluna)
    if Comando!=0:
     switch.configure(command=Comando)
    return switch

def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider = tk.CTkSlider(Local,width=Largura,height=Altura)
    slider.grid(row=Linha,column=Coluna)
    slider.set(0)
    return slider

def CriarTexto(Local,Linha,Coluna,Texto,Largura=0,Altura=0):
    caixatxt= tk.CTkTextbox(Local,wrap="word")
    caixatxt.grid(row=Linha,column=Coluna,sticky="nsew")
    caixatxt.insert("0.0",Texto,)
    if Largura!=0:
        caixatxt.configure(width=Largura)
    if Altura!=0:
        caixatxt.configure(height=Altura)

    return caixatxt

def CriarImagem(Local,Caminho,Linha, Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.grid(row=Linha, column =Coluna)
    return imagem

def CriarData(Local,Linha,Coluna):
    pass

def CriarAbas(Local,Linha,Coluna,Largura,Altura,*Abas):
    aba = tk.CTkTabview(Local,width=Largura, height=Altura)
    for C in Abas:
        aba.add(C)
        Tamanho = list(range(13))
        aba.tab(C).grid_rowconfigure(Tamanho,weight=1)
        aba.tab(C).grid_columnconfigure(Tamanho, weight=1)
    aba.grid(row=Linha, column=Coluna)
    return aba

def CriarFrame(Local,Linha,Coluna,Largura,Altura):
    frame = tk.CTkFrame(Local,width=Largura,height=Altura)
    frame.grid(row=Linha, column=Coluna)
    Tamanho = list(range(13))
    frame.grid_propagate(False)
    frame.grid_rowconfigure(Tamanho, weight=1)
    frame.grid_columnconfigure(Tamanho, weight=1)
    return frame

def CriarFundo(Local,Largura,Altura,Caminho):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.place(x=0,y=0)
    return imagem

def Calendario(local, Linha, Coluna):
    cal = Calendar(local, selectmode='day',
                   year=2007, month=5, day=15,
                   font="Arial 14", locale='en_US')
    cal.grid(row=Linha, column=Coluna, padx=50, pady=10)

    return cal

