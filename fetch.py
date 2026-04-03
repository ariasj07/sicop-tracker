"""
Este script tiene como funcion extraer los datos mas recientes del sitio de sicop
Vease utils.py para el valor de las constantes

https://github.com/ariasj07/sicop-tracker

"""


from utils import SICOP_WEB_URL, BIENES_XPATH, API_SICOP, API_LICIATION
import json
import requests
from bs4 import BeautifulSoup
from start_db import INSERTAR_ENTIDAD, INSERTAR_LICITACIONES

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
        data = res.json()
        if data["content"]:
            for _ in data["content"]:
                licitacion_id: int = _["cartelNo"]
                print(licitacion_id)
                res = requests.post(
                    url=API_LICIATION,
                    json={
                        "cartelNo": f"{licitacion_id}",
                        "cartelSeq": "00"
                    }
                )
                if res.status_code == 200:
                    data = res.json()
                    institucion = data["cartelInstNm"]
                    # Inserto la institución
                    id_nuevo = INSERTAR_ENTIDAD(
                        Nombre=institucion
                    )
                    monto = data["cartelBudget"]
                    descripcion = data["cartelNm"]
                    maximo_de_ofertantes = data["biddocMaxCnt"]
                    fecha_apertura = data["regDt"]
                    vencimiento = data["biddocValDur"]
                    INSERTAR_LICITACIONES(
                        ID_Entidad=id_nuevo,
                        Descripcion=descripcion,
                        Monto_crc=float(monto),
                        N_Ofertas=int(maximo_de_ofertantes),
                        Fecha_Cierre=vencimiento,
                        Fecha_Apertura=fecha_apertura
                    )

                    print(f"CRC: {data["cartelBudget"]}")
                else:
                    print(res.text)
                    print("busq licitacion")
    else:
        print("codigo si la requests sale mal")
        print(res.text)

if __name__ == "__main__":
    get_bienes_licitaciones()