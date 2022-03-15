import requests
from bs4 import BeautifulSoup

url = 'https://prawo.amu.edu.pl/pracownicy-badawczo-dydaktyczni/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

for info in soup.find_all('a', href=True):
    if 'tytul/' in info['href']:
        print(info['href'])
        with open('emails.txt', 'a') as file:
            file.write(info['href'] + '\n')
