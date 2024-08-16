from bs4 import BeautifulSoup
import requests
import time


def send_telegram_notification(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    while True:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Notificação enviada com sucesso.")
            break
        elif response.status_code == 429:
            print("Erro 429: Too Many Requests. Aguardando 25 segundos...")
            time.sleep(25)
        else:
            print(f"Erro ao enviar notificação: {response.status_code} - {response.text}")
            break


def globo(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            headline_tags = soup.find_all('a', class_='feed-post-link')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                headlines.append({'texto':f'{tag.get_text(strip=True)}','fonte':f'{tag['href']}'})
            
    except Exception as e:
        print(f"Ocorreu um erro com {url}: {e}")

    return headlines


def sportBusiness(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('a', class_= 'sf-card__title-link')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                headlines.append({'texto':f'{tag.get_text(strip=True)}','fonte': tag['href']}) 

    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def the_guardian(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('a', class_= 'dcr-lv2v9o')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                headlines.append({'texto':f'{tag['aria-label']}','fonte':f'https://theguardian.com{tag['href']}'}) 

    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def cnn_brasil(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('li', class_= 'block__news__item has--thumb')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                link_tag = tag.find('a')
                if link_tag:
                    headlines.append({'texto':f'{tag.get_text(strip=True)}', 'fonte': link_tag['href']}) 
           
    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def ap_news(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('h3', class_= 'PagePromo-title')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                link_tag = tag.find('a')
                if link_tag:
                    headlines.append({'texto':f'{tag.get_text(strip=True)}', 'fonte': link_tag['href']}) 
           
    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def sportico(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('div', class_= 'lrv-a-grid lrv-a-cols3@tablet')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                a_tag = tag.find('a', class_='c-title__link lrv-a-unstyle-link u-color-brand-primary:hover')
                if a_tag:
                    headlines.append({'texto':f'{a_tag.get_text(strip=True)}', 'fonte': a_tag['href']})

    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def sports_business_journal(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('h2')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                a_tag = tag.find('a')
                if a_tag:
                    headlines.append({'texto':f'{a_tag.get_text(strip=True)}', 'fonte': a_tag['href']})

    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def mkt_esportivo(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('div', class_='post-blog')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                h3_tag = tag.find('h3')
                a_tag = tag.find('a')
                if a_tag:
                    headlines.append({'texto':f'{h3_tag.get_text(strip=True)}', 'fonte': a_tag['href']})


    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def bleacher_report(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('a', class_='atom articleTitle lowerMargin')
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                headlines.append({'texto':f'{tag.get_text(strip=True)}','fonte':f'{tag['href']}'}) 

    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def record_pt(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('div', class_='noticia_box')
            print(f"Encontradas {len(headline_tags)} manchetes.")
  
            for tag in headline_tags:
                h1_tag = tag.find('h1')
                h2_tag = tag.find('h2')

                if h1_tag:
                    a_tag = h1_tag.find('a')
                    if a_tag and 'href' in a_tag.attrs:    
                        headlines.append({'texto':f'{h1_tag.get_text(strip=True)}','fonte':f'https://www.record.pt{a_tag['href']}'})

                if h2_tag:
                    a_tag = h2_tag.find('a')
                    if a_tag and 'href' in a_tag.attrs:    
                        headlines.append({'texto':f'{h2_tag.get_text(strip=True)}','fonte':f'https://www.record.pt{a_tag['href']}'})
     
    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines


def lance(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('a', href=True)
            print(f"Encontradas {len(headline_tags)} manchetes.")

            for tag in headline_tags:
                href = tag['href']
                if 'olimpiadas/' in href.lower():
                    texto = tag.get_text(strip=True)
                    if texto and len(texto) > 5 and not any(char in texto for char in "�") and 'Ver mais' not in texto and 'Veja mais' not in texto:
                        if 'https://www.lance.com.br/olimpiadas' in href:
                            headlines.append({'texto': tag['data-ga4-param-title'], 'fonte': tag['href']})
                        else:
                            headlines.append({'texto': texto, 'fonte': f'https://www.lance.com.br{href}'})

    except Exception as e:
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines