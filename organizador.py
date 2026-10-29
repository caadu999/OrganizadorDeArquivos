import shutil
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showerror, showinfo


def identificar_arquivos(arquivo):

    categorias = {
        "Fotos": {".jpg", ".jpeg", ".png", ".jfif", ".webp", ".bmp", ".tiff", ".svg"},
        "Vídeos": {".mp4", ".mkv", ".mov", ".avi", ".webm", ".wmv", ".m4v"},
        "Música": {".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"},
        "PDF": {".pdf"},
        "Documentos": {".doc", ".docx", ".txt", ".ppt", ".pptx", ".rtf"},
        "Arquivos compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
        "Fontes": {".ttf", ".otf", ".woff", ".woff2"},
        "Pacote Adobe": {".psd", ".ai", ".indd", ".xd"},
        "Planilhas": {".xls", ".xlsx", ".csv"},
        "Torrents": {".torrent"},
        "Arte digital": {".sai", ".sai2", ".kra", ".ora", ".clip"},
        "Imagens de disco": {".iso", ".img"},
    }

    for categoria, extensoes in categorias.items():
        if arquivo.suffix.lower() in extensoes:
            return categoria


def gerar_nome_arquivo(arquivo, destino):
    nome = f"{arquivo.stem}{arquivo.suffix}"
    destinoA = destino / nome
    contador = 1

    while destinoA.exists():
        nome = f"{arquivo.stem}_{contador}{arquivo.suffix}"
        destinoA = destino / nome
        contador += 1
    return destinoA


def mover_arquivos(arquivo, destino):
    try:
        shutil.move(arquivo, destino)
    except (OSError, shutil.Error) as e:
        showerror(
            parent=janela,
            title="Erro",
            message=f"Erro ao mover o arquivo {arquivo.name}: {e}",
        )
        return False
    else:
        return True


def main(caminho: str):
    base = Path(caminho)
    pasta_organizada = base / "Organizador"
    movidos = 0

    for arquivo in base.iterdir():
        if not arquivo.is_file():
            continue

        pasta_nome = identificar_arquivos(arquivo)

        if pasta_nome is None:
            continue

        pasta = pasta_organizada / pasta_nome

        if not pasta.exists():
            pasta.mkdir(parents=True, exist_ok=True)

        destino = gerar_nome_arquivo(arquivo, pasta)

        if mover_arquivos(arquivo, destino):
            movidos += 1

    showinfo(
        title="Resultado",
        message=f"{movidos} arquivo(s) movido(s) com sucesso para {pasta_organizada}",
    )


def selecionar_e_organizar():
    pasta_computador = askdirectory(
        parent=janela,
        title="Selecione a pasta que deseja organizar",
    )

    if not pasta_computador:
        return

    confirmacao = askyesno(
        parent=janela,
        title="Confirmar organização",
        message=(
            f"Pasta selecionada:\n{Path(pasta_computador).name}\n\n"
            "Os arquivos soltos reconhecidos serão movidos "
            "para a pasta Organizador.\n\n"
            "Arquivos dentro de subpastas não serão alterados.\n\n"
            "Deseja continuar?"
        ),
    )

    if not confirmacao:
        return

    try:
        main(pasta_computador)
    except OSError as erro:
        showerror(
            parent=janela,
            title="Organização interrompida",
            message=(
                f"Não foi possível concluir:\n{erro}\n\n"
                "Os arquivos já movidos permanecem no destino."
            ),
        )


if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Organizador de Arquivos")
    janela.geometry("440x240")
    janela.resizable(False, False)

    ttk.Label(
        janela,
        text="Organizador de Arquivos",
        font=("Segoe UI", 17, "bold"),
    ).pack(pady=(25, 12))

    ttk.Label(
        janela,
        text=(
            "Escolha uma pasta para separar os arquivos por categoria.\n"
            "Os arquivos dentro das subpastas serão preservados."
        ),
        justify="center",
    ).pack(pady=(0, 20))

    ttk.Button(
        janela,
        text="Selecionar pasta e organizar",
        command=selecionar_e_organizar,
    ).pack(pady=5)

    ttk.Button(
        janela,
        text="Sair",
        command=janela.destroy,
    ).pack(pady=5)

    janela.mainloop()
