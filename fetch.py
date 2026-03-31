"""
Este script tiene como funcion extraer los datos mas recientes del sitio de sicop
Vease utils.py para el valor de las constantes

https://github.com/ariasj07/sicop-tracker

"""

from utils import SICOP_WEB_URL, BIENES_XPATH, API_SICOP
import requests
from bs4 import BeautifulSoup

def get_bienes_licitaciones():
    res = requests.post(
        url=API_SICOP,
        json={
            "pageNumber": 0,
            "pageSize": 10,
            "tableSorter": {
                "sorter": "",
                "order": "desc"
            },
            "formFilters": [
                {
                    "field": "ppsType",
                    "value": 1
                }
            ]
        }
    )
    if res.status_code == 200:
        print("todo bien")
        print(res.json())
    else:
        print("codigo si la requests sale mal")
        print(res.text)

if __name__ == "__main__":
    get_bienes_licitaciones()