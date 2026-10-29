import shutil
from pathlib import Path
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
        showerror(title="Erro", message=f"Erro ao mover o arquivo {arquivo.name}: {e}")
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


if __name__ == "__main__":
    pasta_computador = askdirectory(title="Selecione a pasta que deseja organizar")

    if pasta_computador:
        confirmacao = askyesno(
            title="Confirmar Organização",
            message=f"Você selecionou a pasta:\n{Path(pasta_computador).name}\n\nArquivos dentro de subpastas não serão alterados.\n\nDeseja continuar?",
        )
        if confirmacao:
            main(pasta_computador)
        else:
            showinfo(title="Cancelado", message="A organização da pasta foi cancelada.")
    else:
        showinfo(title="Cancelado", message="Nenhuma pasta foi selecionada.")
