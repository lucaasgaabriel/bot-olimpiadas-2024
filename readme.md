# Bot Scrapper de notícias das olimpíadas 2024
Esse bot visa o scrapping de 11 jornais do mundo inteiro. Onde faz o scrapping, monta uma mensagem e encaminha pelo **Telegram** utilizando **Python**.

## Requisitos
Crie um ambiente virtual para a execução e instalação das bibliotecas do projeto:
```bash
python3 -m venv venv
```
Ative o virtual enviroment em sua máquina:
- Windows
```bash
venv/Scripts/Activate.ps1
```
- MacOS/Linux:
```bash
source venv/bin/activate
```
Instalação das bibliotecas requisito do projeto:
```bash
pip install -r requirements.txt
```
## Execução
Para a criação de um bot, busque por [Bot Father](https://t.me/BotFather) no **Telegram** e siga os passos para a criação do seu próprio bot.
Certifique-se de ter preenchido ```main.py``` com suas informações de bot e grupo/chat de envio.

Execução do projeto:
```bash
python main.py
```