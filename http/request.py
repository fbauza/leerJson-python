import requests
from requests.exceptions import HTTPError
import pprint
import json
import sys

urlBaseLocal = 'http://localhost:3300/vehicles/plate'
urlBaseDev = 'https://aavaliar-api.development.karvi.com.ar/vehicles/plate'


def queryParam(placa):
    if ambiente == 'local':
        url = urlBaseLocal
    else:
        url = urlBaseDev

    try:
        response = requests.get(url,
        params={'plate':placa})

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

    Respuesta = response.json()
    data = Respuesta['data']
    #pprint.pprint( data['payload']['plate'])

    if not data['messages']:
        pprint.pprint(data['payload'])
    else:
        pprint.pprint(data['messages'])

def fetchAA(placa):
    print(placa)
    try:    
        url = 'http://localhost:3300/vehicles/plate?plate=' + placa
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

    Respuesta = response.json()
    data = Respuesta['data']
    pprint.pprint( data['payload']['plate'])


'''
resp = requests.get('http://localhost:3300/health')

print(resp.encoding)
print(resp.status_code)

resp = requests.get('http://localhost:3300/vehicles/plate?plate=FEU0807')

if resp.status_code == 200:
    print(resp.status_code)
    Respuesta = resp.json()
    print(Respuesta.success)
'''
'''
session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}
url = 'http://localhost:3300/vehicles/plate?plate=FEU0807'
req = session.get(url, headers=headers)

Respuesta = req.json()

print(Respuesta)
'''
'''
try:
    response = requests.get('http://localhost:3300/vehicles/plate?plate=FEU0807')

    response.raise_for_status()
except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
else:
        print('Success!')

Respuesta = response.json()
pprint.pprint(Respuesta)
'''

print(len(sys.argv))
if len(sys.argv) < 1:
    ambiente = 'local'
else:
    ambiente = sys.argv[1]

print('Ambiente: ', ambiente)

patentes = []
with open('plates.json') as file:
    data = json.load(file)

    for plate in data['payload']:
        placa = plate['plate']
        if placa:
            patentes.append(placa)

indice = 0
while indice < len(patentes):
    #print(patentes[indice])
    indice += 1

print(indice)

indice = 0
while indice < 10:
    queryParam(patentes[indice])
    indice += 1


