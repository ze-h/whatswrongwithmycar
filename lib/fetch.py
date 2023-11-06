import json
import requests
#from vehicle import Vehicle

vpic = "https://vpic.nhtsa.dot.gov/api/"
wiki_key = open("./lib/keyring/wikipedia", 'r').read()

def get_car(v: str) -> str:
    res = requests.get(url=(vpic + "vehicles/decodevin/{}?format=json".format(v)))
    res = res.json()
    year = res.get('Results')[10].get('Value')
    make = res.get('Results')[7].get('Value')
    model = res.get('Results')[9].get('Value')
    return "{} {} {}".format(year, make, model)

def get_wiki_page(q: str) -> dict:
    language_code = 'en'
    number_of_results = 1
    headers = {
    'Authorization': wiki_key,
    'User-Agent': 'whatswrongwithmycar'
    }
    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': q, 'limit': number_of_results}
    return requests.get(url, headers=headers, params=parameters).json()

def get_thumb_url(res: dict) -> str:
    return "https:{}".format(res.get('pages')[0].get('thumbnail').get('url'))

def get_image_url(res: dict) -> str:
    url = "https:{}".format(res.get('pages')[0].get('thumbnail').get('url'))
    nurl = ""
    for i in range(0, len(url.split('/')) - 1):
        nurl += url.split('/')[i] + "/"
    return nurl[0:-1].replace("/thumb", "")

def download_file(url: str) -> str:
    headers = {
    'Authorization': wiki_key,
    'User-Agent': 'whatswrongwithmycar'
    }
    try:
        c = requests.get(url=url, headers=headers).content
    except(requests.exceptions.ConnectionError):
        return None
    fn = url.split('/')[-1].replace("%", "")
    with open(fn, mode="wb") as file:
        file.write(c)
    return fn