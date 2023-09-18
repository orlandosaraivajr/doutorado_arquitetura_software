#!/usr/bin/env python
import requests

URL = 'http://masterdev.ddns.net:8081/acesso/ABC7D13'


def main():
    # r = requests.get(URL, auth=('user', 'pass'))
    r = requests.get(URL)
    dados = r.json()
    print(dados[0])
    print(dados[0].get('data'))
    print(dados[0].get('hora'))

main()