# Sistema de Reconhecimento de Voz para Transcrição Automática

Este projeto é um sistema de reconhecimento de voz que permite a transcrição automática de arquivos de áudio. O sistema possui funcionalidades como upload de arquivos de áudio, transcrição automática e exportação para formatos como PDF ou DOCX.

## Funcionalidades

- **Upload de Arquivos de Áudio**: O usuário pode fazer o upload de arquivos de áudio para transcrição.
- **Transcrição Automática**: O sistema realiza a transcrição do áudio enviado.
- **Exportação**: As transcrições podem ser exportadas para formatos PDF ou DOCX.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Um micro framework para Python utilizado para criar a aplicação web.
- [Pydub](https://pydub.com/) - Biblioteca para manipulação de áudio.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Biblioteca para reconhecimento de fala.
- [python-docx](https://python-docx.readthedocs.io/en/latest/) - Biblioteca para criar e modificar arquivos DOCX.
- [fpdf](http://www.fpdf.org/) - Biblioteca para criar documentos PDF.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos:

- Python 3.6 ou superior
- Instalação do FFmpeg para manipulação de arquivos de áudio.

### Instalação do FFmpeg

Para instalar o FFmpeg, siga as instruções de instalação para seu sistema operacional:

- **Windows**: [Instruções de instalação do FFmpeg para Windows](https://ffmpeg.org/download.html#build-windows).
- **Mac**: Instale usando Homebrew:
  ```bash
  brew install ffmpeg
