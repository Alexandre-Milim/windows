import customtkinter as tk
from tkcalendar import Calendar
from Modulos import *
def registrar_pedido():
    TelaReserva.deiconify()
    Tela1.withdraw()
    Data = calendario.get_date()
    Horario = CaixaHora.get()
    Pessoas = CaixaReservarPessoas.get()
    Local = Combox3.get()
    Lb_Data2.configure(text=Data)
    Lb_Hora2.configure(text=Horario)
    Lb_Pessoas2.configure(text=Pessoas)
    Lb_Mesa2.configure(text=Local)


Tela1 = CriarJanela("revisão","300x500+650+150",1)


frame = CriarFrame(Tela1,2,6, 700,750)
frame.configure(fg_color="#171717")
Imagem = CriarImagem(frame,"img/unnamed.png",1,4,70,200)
calendario = Calendario(frame,2,4)
CaixaHora = CriarCaixaDeTexto(frame,200,35,4,4,"Hora Desejada")
CaixaHora.grid(sticky="S")
CaixaHora.configure(fg_color="#ffbc4f")
CaixaHora.configure(text_color="black")


CaixaReservarPessoas = CriarCaixaDeTexto(frame,200,35,6,4,"Quantidade de pessoas")
CaixaReservarPessoas.grid(sticky="S")
CaixaReservarPessoas.configure(fg_color="#ffbc4f")
CaixaReservarPessoas.configure(text_color="black")


Combox3 = CriarComboBox(frame, 200, 35,['Food Hall','Praça de Alimentação'], 8,4)
Combox3.configure(fg_color="#ffbc4f")
Combox3.configure(text_color="#000000")

btn_Reservar = CriarBotao(frame,"Reservar",registrar_pedido,10,4,5,35)
btn_Reservar.configure(fg_color="Orange")
btn_Reservar.configure(hover_color="#ff7b00")
btn_Reservar.configure(text_color="#000000")



CriarLabelDoCtt = CriarLabel(frame,"Cozinha moderna \n \n Telefone: (18) 92001-8334 \nSábado e Domingo: 12h00 - 23h00",9,4)
CriarLabelDoCtt.configure(font=("Helvetica",14))
CriarLabelDoCtt.configure(text_color="white")

def btnMudarTela():
    pass

Tela3 = CriarJanela("Reserva", "700x500+700+200", 2)
Tela3.withdraw()
Tela3.configure(fg_color="#171717")

imagemLogo = CriarImagem(Tela3, "img/caue.png", 1, 5, 100, 100)

Abas = CriarAbas(Tela3, 3, 3, 150, 150, "opção1","opção2")

Aba2 = CriarAbas(Tela3, 3, 5, 150, 150, "opção1","opção2")
Aba3 = CriarAbas(Tela3, 3, 7, 150, 150, "opção1","opção2")

imagemAba1 = CriarImagem(Abas.tab("opção1"), "img/sobe1.png", 0, 5, 100, 100)
ImagemAba1 = CriarImagem(Abas.tab("opção2"), "img/sobe2.png", 0, 5, 100, 100)

Lb_Desc_Bolo = CriarLabel(Abas.tab("opção1"), "img/Bolo", 2, 0)
Lb_Desc_Bolo.grid(sticky="S",columnspan=13)
Lb_Preco_Bolo = CriarLabel(Abas.tab("opção1"), "R$50,00", 3, 0)
Lb_Preco_Bolo.grid(sticky="S", columnspan=13)
Check_Bolo=CriarCheckBox(Abas.tab("opção1"),"Selecione", 5,0)
Check_Bolo.grid(columnspan=13)

Lb_Desc_Torta = CriarLabel(Abas.tab("opção2"), "Torta Holandesa ", 2, 5)
Lb_Desc_Torta.grid(sticky="S")
Lb_Preco_Torta = CriarLabel(Abas.tab("opção2"), "R$75,00", 3, 5)
Lb_Preco_Torta.grid(sticky="S")
Check_Torta=CriarCheckBox(Abas.tab("opção2"),"Selecione", 5,0)
Check_Torta.grid(columnspan=13)

imagemAba2 = CriarImagem(Aba2.tab("opção1"), "img/mafi2.png", 0, 5, 100, 100)
imagemAba2 = CriarImagem(Aba2.tab("opção2"), "img/mafi.png", 0, 5, 100, 100)

Lb_Desc_Parmegiana = CriarLabel(Aba2.tab("opção1"), "Parmegiana", 2, 5)
Lb_Desc_Parmegiana.grid(sticky="S")
Lb_Preco_Parmegiana = CriarLabel(Aba2.tab("opção1"), "R$75,00", 3, 5)
Lb_Preco_Parmegiana.grid(sticky="S")
Check_Parmegiana=CriarCheckBox(Aba2.tab("opção1"),"Selecione", 5,0)
Check_Parmegiana.grid(columnspan=13)

Lb_Desc_Camarão = CriarLabel(Aba2.tab("opção2"), "Camarão", 2, 5)
Lb_Desc_Camarão.grid(sticky="S")
Lb_Preco_Camarão = CriarLabel(Aba2.tab("opção2"), "R$75,00", 3, 5)
Lb_Preco_Camarão.grid(sticky="S")
Check_Camarão=CriarCheckBox(Aba2.tab("opção2"),"Selecione", 5,5)
Check_Camarão.grid(columnspan=13)

imagemAba3 = CriarImagem(Aba3.tab("opção1"), "img/coca.png", 0, 5, 100, 100)
imagemAba3 = CriarImagem(Aba3.tab("opção2"), "img/suco2.png", 0, 5, 100, 100)

Lb_Desc_Coca = CriarLabel(Aba3.tab("opção1"), "Coca", 2, 0)
Lb_Desc_Coca.grid(sticky="S",columnspan=13)
Lb_Preco_Coca = CriarLabel(Aba3.tab("opção1"), "R$50,00", 3, 0)
Lb_Preco_Coca.grid(sticky="S",columnspan=13)
Check_Coca=CriarCheckBox(Aba3.tab("opção1"),"Selecione", 5,0)
Check_Coca.grid(columnspan=13)

Lb_Desc_Suco = CriarLabel(Aba3.tab("opção2"), "Suco", 2, 0)
Lb_Desc_Suco.grid(sticky="S",columnspan=13)
Lb_Preco_Suco = CriarLabel(Aba3.tab("opção2"), "R$30,00", 3, 0)
Lb_Preco_Suco.grid(sticky="S",columnspan=13)
Check_Suco=CriarCheckBox(Aba3.tab("opção2"),"Selecione", 5,0)
Check_Suco.grid(columnspan=13)

botaoPassarProduto = CriarBotao(Tela3, "Confirmar", btnMudarTela, 7, 5, 60, 30)

def btnMudarTela():

    opcoes_selecionadas = "Opções Selecionadas:\n"

    if Check_Bolo.get():
        opcoes_selecionadas += " - Bolo\n"

    if Check_Torta.get():
        opcoes_selecionadas += " - Torta Holandesa\n"

    if Check_Parmegiana.get():
        opcoes_selecionadas += " - Parmegiana\n"

    if Check_Camarão.get():
        opcoes_selecionadas += " - Camarão\n"

    if Check_Coca.get():
        opcoes_selecionadas += " - Coca\n"

    if Check_Suco.get():
        opcoes_selecionadas += " - Suco\n"

    print(opcoes_selecionadas)


botaoPassarProduto = CriarBotao(Tela3, "Confirmar", btnMudarTela, 7, 5, 60, 30)

def Contatos():
    print("Função Contatos chamada.")
tk.set_appearance_mode("Dark")
TelaReserva = CriarJanela("Reserva", "350x500+650+150", 2)
TelaReserva.configure(fg_color="#171717")
TelaReserva.withdraw()
Abas = CriarAbas(TelaReserva, 3, 6, 350, 450, "Reservas", "Contato")
Abas.configure(state="normal")
Abas.configure(fg_color="#171717")

def EnviarDados():
    Lb_EnviarContatos.configure(text="Dados enviados!")

def ConfirmarReserva():
    Lb_ConfirmarReserva.configure(text="     Reserva confirmada!")

def MudarpContato():
    TelaReserva.withdraw()
    Tela3.deiconify()

def VoltarpReservas():
    Abas.set("Reservas")

def Finalizar():
    pass

def VoltarpRevisar():
    Abas.set("MudarpContato")

imgHeader = CriarImagem(TelaReserva, "img/unnamed.png", 1, 6, 50, 230)

Lb_Data = CriarLabel(Abas.tab("Reservas"), "Data:", 1,2)
Lb_Data.grid(columnspan=6)
Lb_Data2 = CriarLabel(Abas.tab("Reservas"), "Data", 1, 6)
Lb_Data2.grid(columnspan=6)

Lb_Hora = CriarLabel(Abas.tab("Reservas"), "Hora:", 3, 2)
Lb_Hora.grid(columnspan=6)
Lb_Hora2 = CriarLabel(Abas.tab("Reservas"), "Hora", 3, 6)
Lb_Hora2.grid(columnspan=6)

Lb_Pessoas = CriarLabel(Abas.tab("Reservas"), "Número de pessoas:            ", 5, 2)
Lb_Pessoas.grid(columnspan=6)
Lb_Pessoas2 = CriarLabel(Abas.tab("Reservas"), "Pessoas", 5, 6)
Lb_Pessoas2.grid(columnspan=6)

Lb_Mesa = CriarLabel(Abas.tab("Reservas"), "Mesa reservada            :  ", 7, 2)
Lb_Mesa.grid(columnspan=6)
Lb_Mesa2 = CriarLabel(Abas.tab("Reservas"), "Mesa", 7, 6)
Lb_Mesa2.grid(columnspan=6)

Lb_polCancelamento = CriarLabel(Abas.tab("Reservas"), "POLÍTICAS DE CANCELAMENTO:", 9, 0)
Lb_polCancelamento.configure(text_color="Red")
Lb_polCancelamento.grid(columnspan=13)
Lb_polCancelamento2 = CriarLabel(Abas.tab("Reservas"), "Ao desmarcar de última hora, você prejudica"
                                                       "\n a chance de outras pessoas desfrutarem"
                                                       "\n da experiência.", 10, 0)
Lb_polCancelamento2.configure(text_color="#FFFF00")
Lb_polCancelamento2.grid(columnspan=13)


Lb_ConfirmarReserva = CriarLabel(Abas.tab("Reservas"), "", 11, 6)
btnConfirmarReserva = CriarBotao(Abas.tab("Reservas"), "Confirmar reserva!", ConfirmarReserva, 12, 3, 30, 30)
btnConfirmarReserva.configure(fg_color="#ffbc4f")

btnMudarpRevisar = CriarBotao(Abas.tab("Reservas"), "Avançar ->",MudarpContato, 12, 12, 30, 30)
btnMudarpRevisar.configure(fg_color="#ffbc4f")

Lb_Cad_Nome = CriarLabel(Abas.tab("Contato"), "Nome:", 1, 5)
Lb_Cad_Nome.grid(sticky="S")
Cx_Cad_Nome = CriarCaixaDeTexto(Abas.tab("Contato"), 150, 30, 1, 6, "Insira seu nome")
Cx_Cad_Nome.grid(sticky="S")
Cx_Cad_Nome.configure(fg_color="#ffbc4f")

Lb_Cad_Tel = CriarLabel(Abas.tab("Contato"), "Telefone:", 2, 5)
Lb_Cad_Tel.grid(sticky="S")
Cx_Cad_Tel = CriarCaixaDeTexto(Abas.tab("Contato"), 150, 30, 2, 6, "Insira seu telefone")
Cx_Cad_Tel.grid(sticky="S")
Cx_Cad_Tel.configure(fg_color="#ffbc4f")

Lb_Cad_Email = CriarLabel(Abas.tab("Contato"), "Email:", 3, 5)
Lb_Cad_Email.grid(sticky="S")
Cx_Cad_Email = CriarCaixaDeTexto(Abas.tab("Contato"), 150, 30, 3, 6, "Insira seu email")
Cx_Cad_Email.grid(sticky="S")
Cx_Cad_Email.configure(fg_color="#ffbc4f")

btnVoltarpRevisar = CriarBotao(Abas.tab("Contato"), "<- Voltar", VoltarpRevisar, 12, 2, 30, 30)
btnVoltarpRevisar.configure(fg_color="#ffbc4f")

Lb_EnviarContatos = CriarLabel(Abas.tab("Contato"), "", 11, 6)
btnEnviarContatos = CriarBotao(Abas.tab("Contato"), "Enviar", EnviarDados, 12, 10, 30, 30)
btnEnviarContatos.configure(fg_color="#ffbc4f")

Tela1.mainloop()
