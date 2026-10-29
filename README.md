# 📂 Organizador de Arquivos

Organize os arquivos soltos de uma pasta por categoria. Escolha a pasta em uma janela, confirme a operação e o programa distribui os arquivos em subpastas como **Fotos**, **Vídeos**, **PDF** e **Planilhas**.


## Como funciona

1. Abre uma janela para selecionar a **pasta**.
2. Solicita confirmação do caminho escolhido.
3. Identifica a categoria pela extensão de cada arquivo.
4. Cria uma pasta exclusiva para a execução dentro da pasta escolhida: `Organizador`.
5. Cria as subpastas de categorias dentro dessa pasta exclusiva.
6. Verifica se o nome do arquivo já existe no destino e, em caso de conflito, acrescenta um número.
7. Move os arquivos e mostra as operações no console.

**Somente arquivos diretamente dentro da pasta selecionada são processados.** Arquivos que já estão em subpastas e extensões não cadastradas permanecem onde estão!

## Exemplo

Antes:

```text
Downloads/
├── foto.jpg
├── curriculo.pdf
├── vendas.xlsx
├── arquivo.xyz
└── Fotos/
    └── foto.jpg
```

Depois:

```text
Downloads/
├── arquivo.xyz
├── Fotos/
│   └── foto.jpg
└── Organizador/
    ├── Fotos/
    │   └── foto.jpg
    ├── PDF/
    │   └── curriculo.pdf
    └── Planilhas/
        └── vendas.xlsx
```

A foto já existente é preservada. O arquivo recebido ganha o próximo nome disponível: `foto_1.jpg`, `foto_2.jpg` e assim por diante.

## Categorias disponíveis

| Pasta | Extensões |
|---|---|
| Fotos | `.jpg`, `.jpeg`, `.png`, `.jfif`, `.webp`, `.bmp`, `.tiff`, `.svg` |
| Vídeos | `.mp4`, `.mkv`, `.mov` |
| Música | `.mp3`, `.wav`, `.flac` |
| PDF | `.pdf` |
| Documentos | `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.rtf` |
| Arquivos compactados | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Fontes | `.ttf`, `.otf`, `.woff`, `.woff2` |
| Pacote Adobe | `.psd`, `.ai`, `.indd`, `.xd` |
| Planilhas | `.xls`, `.xlsx`, `.csv` |
| Arte digital | `.sai`, `.sai2`, `.kra`, `.ora`, `.clip` |
| Imagens de disco | `.iso`, `.img` |
| Torrents | `.torrent` |


As extensões são comparadas em minúsculas: `FOTO.JPG` também é reconhecido. A classificação considera a última extensão do nome, sem examinar o conteúdo do arquivo.


## 📥 Baixar e usar

1. Acesse a [página de versões](https://github.com/caadu999/OrganizadorDeArquivos/releases/tag/v1.0.0).
2. Na seção **Assets**, baixe `Organizador.exe`.
3. Abra o executável.
4. Selecione a pasta e confirme a organização.

O programa organiza apenas os arquivos soltos da pasta escolhida.

## Como usar o executável no Windows

1. Depois de Baixar o `Organizador.exe`.
2. Abra o arquivo com dois cliques.
3. Escolha a pasta que deseja organizar.
4. Confira o caminho e clique em **Sim** para continuar.

Ao cancelar a seleção ou responder **Não** à confirmação, nenhum arquivo é organizado. O executável empacotado inclui o Python necessário para sua execução; Lembrando: O usuário não precisa instalar Python separadamente!!


## Executar pelo código-fonte

É necessário Python 3 com suporte a Tkinter. O projeto usa apenas módulos da biblioteca padrão: não há pacotes externos para instalar para executar o script.

Salve o código como `organizador.py`, abra o terminal na pasta do arquivo e execute:

```powershell
python organizador.py
```

O script foi desenvolvido em um ambiente Windows com Python 3.14. A compatibilidade com outros sistemas não foi validada.

## Gerar o executável

No Windows, instale o PyInstaller no ambiente do projeto:

```powershell
python -m pip install -U pyinstaller
```

Na pasta que contém `organizador.py`, execute:

```powershell
python -m PyInstaller --onefile --name Organizador organizador.py
```

O resultado será criado em `dist/Organizador.exe`. O PyInstaller é necessário apenas para gerar o executável.

O comando mantém o console visível para as mensagens de processamento. Após alterar o código, gere o executável novamente e feche a cópia anterior antes de substituí-la.

## Personalizar as categorias

Edite o dicionário `categorias` na função `identificar_arquivos()`. Cada chave define o nome da pasta; o conjunto associado contém as extensões aceitas, incluindo o ponto.

Evite cadastrar a mesma extensão em categorias diferentes: a primeira correspondência encontrada será usada.

## Estrutura do código

| Função | Responsabilidade |
|---|---|
| `identificar_arquivos()` | Encontrar a categoria a partir da extensão |
| `gerar_nome_arquivo()` | Escolher um nome de destino disponível |
| `mover_arquivos()` | Mover o arquivo e informar o resultado |
| `main()` | Percorrer os arquivos e coordenar a organização |

## Cuidados

- **Os arquivos são movidos, não copiados.** Não há desfazer automático nem backup. Teste inicialmente em uma pasta com cópias.
- Finalize os downloads e feche arquivos que possam estar em uso antes de executar. O programa não detecta se um download terminou.
- A escolha de nomes trata conflitos encontrados durante a execução, mas não oferece garantia contra outro programa ocupar o mesmo nome entre a verificação e a movimentação. Evite executar duas instâncias sobre a mesma pasta.
- Evite organizar arquivos de projetos que dependam de outros arquivos próximos: mudar a localização pode quebrar referências.


## Tecnologias

- **Python:** lógica e fluxo de execução.
- **pathlib:** caminhos, extensões e criação de diretórios.
- **shutil:** movimentação de arquivos.
- **Tkinter:** seleção de pasta e confirmação.
- **PyInstaller:** empacotamento para distribuição.

