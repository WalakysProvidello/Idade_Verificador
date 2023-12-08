import tkinter as tk
from tkinter import messagebox

def verificar_acesso():
    nome = entry_nome.get()
    idade_str = entry_idade.get()

    # Verificar se o nome é válido (não está vazio)
    if not nome:
        messagebox.showerror("Erro", "Por favor, digite um nome válido.")
        return

    # Verificar se a idade é um número inteiro
    try:
        idade = int(idade_str)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite uma idade válida.")
        return

    # Verificar se a idade é maior que 18
    if idade > 18:
        mensagem = f"{nome}, Acesso permitido"
    else:
        mensagem = f"{nome}, Acesso não permitido"

    messagebox.showinfo("Verificação de Acesso", mensagem)

def criar_frame_borda():
    frame_borda = tk.Frame(janela, borderwidth=5, relief=tk.SOLID)
    frame_borda.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    return frame_borda

def criar_widgets(frame):
    global entry_nome, entry_idade, botao_cinza

    label_nome = tk.Label(frame, text="Nome:")
    label_nome.pack(padx=5, pady=5)

    entry_nome = tk.Entry(frame)
    entry_nome.pack(padx=5, pady=5)

    label_idade = tk.Label(frame, text="Idade:")
    label_idade.pack(padx=5, pady=5)

    entry_idade = tk.Entry(frame)
    entry_idade.pack(padx=5, pady=5)

    botao_cinza = tk.Button(frame, text="Verificar Acesso", command=verificar_acesso, bg="gray", fg="white")
    botao_cinza.pack(padx=5, pady=5)

def criar_janela():
    global janela

    janela = tk.Tk()
    janela.title("Janela Azul com Botão Cinza")
    janela.geometry("600x600") # Definir o tamanho da janela
    janela.configure(bg="blue") # Configurar a cor de fundo azul
    janela.resizable(False, False) # Impede o redimensionamento da janela

def main():
    criar_janela()

    frame_borda = criar_frame_borda()
    criar_widgets(frame_borda)

    janela.mainloop()

if __name__ == "__main__":
    main()