from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import sys

def main():
    URL = sys.argv[-1]

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'html.parser')
    divs = soup.find_all('div', {'class': 'info-table__row'})

    with open('template.html', 'r') as f:
        html = f.read()
        with open('index.html', 'w') as f:
            f.write(html)

    for div in divs:
        try:
            key = div.find('dt', {'class': 'info-table__title'}).text
            value = div.find('dd', {'class': 'info-table__value'}).text

            match key:
                case 'Sijainti':
                    replace_text('[SIJAINTI]', value)
                    replace_text('[SIJAINTI_URL]', URL)
                case 'Kaupunginosa':
                    replace_text('[KAUPUNGINOSA]', value)
                case 'Asumiskulut':
                    replace_text('[ASUMISKULUT]', value)
                case 'Velaton hinta':
                    replace_text('[VELATON_HINTA]', value)
                case 'Hoitovastike':
                    replace_text('[HOITOVASTIKE]', value)
                case 'Vesimaksu':
                    replace_text('[VESIMAKSU]', value)
                case 'Sauna':
                    replace_text('[SAUNA]', value)
                case 'Saunan tyyppi':
                    replace_text('[SAUNAN_TYYPPI]', value)
                case 'Parveke':
                    replace_text('[PARVEKE]', value)
                case 'Koko':
                    replace_text('[KOKO]', value)
                case 'Kerros':
                    replace_text('[KERROS]', value)
        except AttributeError:
            continue

    time = dt.today().strftime("%d-%m-%Y %H:%M:%S")
    replace_text('[GENEROITU]', time)
    replace_text('[TITLE]', time)

def replace_text(key, value):
    with open('index.html', 'r') as f:
        html = f.read()
        html = html.replace(key, value)
        with open('index.html', 'w') as f:
            f.write(html)

if __name__ == '__main__':
    main()