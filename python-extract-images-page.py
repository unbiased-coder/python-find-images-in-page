from telnetlib import TUID
import requests

from bs4 import BeautifulSoup

page = 'https://unbiased-coder.com'


def download_image(url):
    if ',' in url:
        return
    if 'http' != url[:4]:
        turl = page + url
    else:
        turl = url

    print(f'Downloading file: {turl}')
    res = requests.get(turl)
    save_location = turl.split('/')[-1]
    print (f'Saving file to: {save_location}')
    with open(save_location, 'wb') as fd:
        fd.write(res.content)
    print (f'Successfully saved file')

print (f'Downloading page: {page}')
res = requests.get(page)

print (f'Got back response: {res.status_code}')
print (f'Page length: {len(res.text)}')

html = res.text
bs = BeautifulSoup(html, features='html.parser')

for url in bs.find_all('img'):
    download_image(url.get('src'))