import requests
from bs4 import BeautifulSoup

url = 'https://kontan.co.id'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! response = {response.status_code}')
        # print(f'content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil Pemanggilan {url}')
        print(f'Tittle: {soup.title.string}')
    else:
        print(f'whoops, ada kesalahan requests {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')