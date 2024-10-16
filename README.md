# Sistema de Reconhecimento de Voz para Transcrição Automática

Este projeto é um sistema de reconhecimento de voz que permite a transcrição automática de arquivos de áudio. O sistema possui funcionalidades como upload de arquivos de áudio, transcrição automática e exportação para formatos como PDF ou DOCX.

## Funcionalidades

- **Upload de Arquivos de Áudio**: Permite o upload de arquivos de áudio para transcrição.
- **Transcrição Automática**: Realiza a transcrição do áudio enviado.
- **Exportação**: As transcrições podem ser exportadas para formatos PDF ou DOCX.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/): Micro framework para Python utilizado para criar a aplicação web.
- [Pydub](https://pydub.com/): Biblioteca para manipulação de áudio.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Biblioteca para reconhecimento de fala.
- [python-docx](https://python-docx.readthedocs.io/en/latest/): Biblioteca para criar e modificar arquivos DOCX.
- [fpdf](http://www.fpdf.org/): Biblioteca para criar documentos PDF.

## Pré-requisitos

- Python 3.6 ou superior
- Instalação do FFmpeg para manipulação de arquivos de áudio.

### Instalação do FFmpeg

Para instalar o FFmpeg, siga as instruções de instalação para seu sistema operacional:

- **Windows**: [Instruções de instalação do FFmpeg para Windows](https://ffmpeg.org/download.html#build-windows).
- **Mac**: Instale usando Homebrew:
  ```bash
  brew install ffmpeg

- **Linux**: Utilize o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu:
  ```bash
  sudo apt update
  sudo apt install ffmpeg

Instalação do Projeto

  Clone o repositório:
  
    git clone https://github.com/Clouddios/reconhecimento_de_fala.git
    cd reconhecimento_de_fala

Crie um ambiente virtual (opcional, mas recomendado):

  No Windows:

    python -m venv venv
    venv\Scripts\activate

  No Linux/Mac:

    python -m venv venv
    source venv/bin/activate

  Instale as dependências:

    pip install -r requirements.txt

Configuração do Ambiente

  Verifique a instalação do FFmpeg: Após instalar o FFmpeg, execute o seguinte comando no terminal para verificar a instalação:

    ffmpeg -version

  Crie o arquivo .env (se necessário): Se o projeto usa variáveis de ambiente, crie um arquivo .env na raiz do projeto e adicione suas variáveis.

Execução do Projeto

  Inicie o servidor Flask:

    flask run

Acesse a aplicação no seu navegador:
    Abra o navegador e vá para: http://127.0.0.1:5000

  Utilize a aplicação:
        Faça o upload do seu arquivo de áudio e aguarde a transcrição.

Testes

Para garantir que a aplicação esteja funcionando corretamente, você pode executar testes unitários, se disponíveis. Execute:

    pytest

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.
Licença

Este projeto está licenciado sob a MIT License.
