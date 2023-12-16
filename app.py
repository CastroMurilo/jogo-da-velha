import tkinter as tk
import random

# Função para verificar se alguém ganhou o jogo
def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[i][coluna] == jogador for i in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if "-" in linha:
            return False
    return True

# Função para o movimento da IA
def fazer_movimento_ia(tabuleiro):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == "-":
            return linha, coluna

# Função para processar o movimento do jogador
def processar_movimento(linha, coluna):
    if tabuleiro[linha][coluna] == "-" and vez_do_jogador:
        tabuleiro[linha][coluna] = "X"
        botoes[linha][coluna].config(text="X", state=tk.DISABLED)
        if verificar_vitoria(tabuleiro, "X"):
            resultado_label.config(text="Você ganhou!")
        elif verificar_empate(tabuleiro):
            resultado_label.config(text="Empate!")
        else:
            linha_ia, coluna_ia = fazer_movimento_ia(tabuleiro)
            tabuleiro[linha_ia][coluna_ia] = "O"
            botoes[linha_ia][coluna_ia].config(text="O", state=tk.DISABLED)
            if verificar_vitoria(tabuleiro, "O"):
                resultado_label.config(text="IA ganhou!")
            elif verificar_empate(tabuleiro):
                resultado_label.config(text="Empate!")
    else:
        # Adicione uma lógica para lidar com a seleção de uma célula já preenchida
        print("Célula já preenchida. Escolha outra.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogo da Velha")

# Variáveis globais
tabuleiro = [["-" for _ in range(3)] for _ in range(3)]
vez_do_jogador = True

# Criação dos botões
botoes = []
for linha in range(3):
    linha_botoes = []
    for coluna in range(3):
        botao = tk.Button(janela, text="-", width=10, height=2, command=lambda l=linha, c=coluna: clicar_botao(l, c))
        botao.grid(row=linha, column=coluna)
        linha_botoes.append(botao)
    botoes.append(linha_botoes)

# Rótulo para exibir o resultado do jogo
resultado_label = tk.Label(janela, text="", font=("Helvetica", 16))
resultado_label.grid(row=3, column=0, columnspan=3)

# Função chamada quando um botão é clicado
def clicar_botao(linha, coluna):
    processar_movimento(linha, coluna)

# Iniciar a janela
janela.mainloop()
