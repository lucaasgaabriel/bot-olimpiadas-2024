from datetime import datetime, timedelta, timezone
from functions import *

urls = {
    "https://ge.globo.com/olimpiadas/": 'Globo Esporte',
    "https://www.sportbusiness.com/event/2024-olympic-games/": 'Sport Business',
    "https://bleacherreport.com/olympics": 'Bleacher Report',
    "https://www.record.pt/modalidades/jogos-olimpicos/paris2024?ref=Masterpage_MenuDestaque": 'Record PT',
    "https://www.theguardian.com/sport/olympic-games-2024": 'The Guardian',
    "https://www.cnnbrasil.com.br/esportes/olimpiadas/": 'CNN Brasil',
    "https://apnews.com/hub/2024-paris-olympic-games": 'AP News',
    "https://www.sportico.com/c/leagues/olympics/": 'Sportico',
    "https://www.sportsbusinessjournal.com/Archive/Sections/Olympics.aspx": 'Sports Business Journal',
    "https://insidersport.com/": 'Insider Sports',
    "https://www.lance.com.br/olimpiadas": 'Lance',
    "https://www.mktesportivo.com/categoria/jogos-olimpicos-paris-2024/": 'Mkt Esportivo',
}

functions = {
    "https://ge.globo.com/olimpiadas/": globo,
    "https://www.sportbusiness.com/event/2024-olympic-games/": sportBusiness,
    "https://bleacherreport.com/olympics": bleacher_report,
    "https://www.record.pt/modalidades/jogos-olimpicos/paris2024?ref=Masterpage_MenuDestaque": record_pt,
    "https://www.theguardian.com/sport/olympic-games-2024": the_guardian,
    "https://www.cnnbrasil.com.br/esportes/olimpiadas/": cnn_brasil,
    "https://apnews.com/hub/2024-paris-olympic-games": ap_news,
    "https://www.sportico.com/c/leagues/olympics/": sportico,
    "https://www.sportsbusinessjournal.com/Archive/Sections/Olympics.aspx": sports_business_journal,
    "https://www.lance.com.br/olimpiadas": lance,
    "https://www.mktesportivo.com/categoria/jogos-olimpicos-paris-2024/": mkt_esportivo,
}

def main():
    # Configurações do Telegram
    telegram_token = ''
    # ID do grupo Telegram
    telegram_chat_id = ''

    for url, func in functions.items():
        try:
            headlines = func(url)
            batch_size = 10

            for i in range(0, len(headlines), batch_size):
                batch_headlines = headlines[i:i + batch_size]
                localtime = timezone(timedelta(hours=-3))
                now = datetime.now(localtime)
                date_time = now.strftime("%d/%m às %H:%M:%S")

                message_lines = [f'''🏅 {headline['texto']}\nFonte: {headline['fonte']}\n\n''' for headline in batch_headlines]
                message = f'''🏆📢 Últimas notícias do Poder Olímpico Bot!\nAqui estão as manchetes mais recentes de {urls[url]}\nData de extração: {date_time}\n\n''' + "\n".join(message_lines)

                send_telegram_notification(telegram_token, telegram_chat_id, message)

        except Exception as e:
            print(f"Erro ao extrair manchetes de {url}: {e}")

    return "Notificações enviadas com sucesso."

if __name__ == "__main__":
    main()
