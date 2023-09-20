import random
import string
import tkinter as tk
from tkinter import messagebox

# Lista de palavras e dicas
palavras_e_dicas = {
    "python": "Uma linguagem de programação",
    "computador": "Uma máquina que processa informações",
    "internet": "Rede global de computadores",
    # ... Adicione mais palavras e dicas aqui ...
}

# Função para escolher uma palavra e dica aleatória
def escolher_palavra_e_dica():
    palavra, dica = random.choice(list(palavras_e_dicas.items()))
    return palavra, dica

# Função para exibir a forca atual
def exibir_forca(erros):
    forca = [
        "  +---+",
        "  |   |",
        "  " + ('O' if erros > 0 else ' ') + "   |",
        " " + ('/|\\' if erros > 2 else '   '),
        " " + ('/ \\' if erros > 4 else '   '),
        "========="
    ]
    return "\n".join(forca[:erros])

# Função para validar se a entrada é uma letra ou palavra válida
def valida_letra_ou_palavra(letra_ou_palavra):
    return all(char in string.ascii_letters for char in letra_ou_palavra)

# Função para processar a tentativa do jogador
def tentativa():
    letra_ou_palavra = entrada.get().lower()

    if letra_ou_palavra in letras_usadas:
        messagebox.showinfo("Forca", "Você já tentou esta letra ou palavra.")
        return

    letras_usadas.append(letra_ou_palavra)

    if len(letra_ou_palavra) == 1 and letra_ou_palavra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra_ou_palavra:
                palavra_oculta[i] = letra_ou_palavra
    elif letra_ou_palavra == palavra:
        messagebox.showinfo("Forca", "Parabéns! Você acertou a palavra: " + palavra)
        root.quit()
    else:
        if valida_letra_ou_palavra(letra_ou_palavra):
            erros[0] += 1
            atualizar_boneco(erros[0])  # Atualizar o boneco enforcado
            if erros[0] == 6:
                messagebox.showinfo("Forca", "Fim de jogo! Você perdeu. A palavra era: " + palavra)
                root.quit()
        else:
            messagebox.showinfo("Forca", "Por favor, digite apenas letras ou a palavra inteira.")

    resultado.set(" ".join(palavra_oculta))
    entrada.delete(0, tk.END)

# Função para atualizar o boneco enforcado na interface
def atualizar_boneco(erros):
    forca_text.set(exibir_forca(erros))

# Função principal do jogo
def jogo_da_forca():
    global root, palavra, dica, palavra_oculta, letras_usadas, erros, resultado, entrada, forca_text

    root = tk.Tk()
    root.title("Jogo da Forca")

    palavra, dica = escolher_palavra_e_dica()
    palavra = palavra.lower()
    palavra_oculta = ["_" if letra.isalpha() else letra for letra in palavra]
    letras_usadas = []
    erros = [0]

    canvas = tk.Canvas(root, width=200, height=250)
    canvas.pack()

    forca_text = tk.StringVar()
    forca_text.set(exibir_forca(erros[0]))

    tk.Label(root, textvariable=forca_text).pack()
    tk.Label(root, text="Dica: " + dica).pack()

    resultado = tk.StringVar()
    resultado.set(" ".join(palavra_oculta))
    tk.Label(root, textvariable=resultado).pack()

    entrada = tk.Entry(root)
    entrada.pack()

    tentar_botao = tk.Button(root, text="Tentar", command=tentativa)
    tentar_botao.pack()

    root.mainloop()

# Iniciar o jogo
if __name__ == "__main__":
    jogo_da_forca()
