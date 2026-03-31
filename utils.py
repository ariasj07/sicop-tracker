SICOP_WEB_URL="https://www.sicop.go.cr/app/module/bid/public/tenders"
API_SICOP="https://prod-api.sicop.go.cr/bid/api/v1/public/epCartel/searchEpCartelsByPpsType"

"""
# Headers enviados:

{
"pageNumber":0,
"pageSize":10,
"tableSorter":{"sorter":"","order":"desc"},
"tableFilters":[],
"formFilters":[{"field":"ppsType","value":"1"}]
}

---

`pageNumber` -> no reconocido aun
`pageSize` -> parace ser el numero de licitaciones que carga por requests, sin descubrir limite, no lleva cursor
`tableSorter` -> parecer que hay un sorter, no descubierto, y order que se aprecia desc, probablemente descendente
`probablemente` existe asce o asc
`tableFilters` -> filtros, sin descubrir
`formFilters` -> en el sitio vienen opciones, al tocar la primera, la de bienes, manda el value 1, parece
que se basa en filtros por enteros, 1 parece corresponder a las licitaciones de bienes

# Respuesta recibida:

content	(10)[ {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…} ]

> `content`: son las licitaciones, se desglosan así:
{ 
instCartelNo: "2026LE-000005-0001102207",
cartelNo: "20260302638",
cartelNm: "Tóxicos en Orina",
regDt	"2026-03-30T15:45:56"
cartelSeq	"00"
biddocStartDt	null
biddocEndDt	null
openbidDt	"2026-04-22T10:00:00"
cartelInstCd	"4000042147"
releaseYn	"Y"
cartelInstNm	"CAJA COSTARRICENSE DE SEGURO SOCIAL"
proceType	"LE"
cartelClsYn	""
biddocType	"XM"
proceTypeDetail	""
executorNm	"HAZEL YULIET ULATE FONSECA"
cartelStat	null
executorId	"L4000042147397"
cartelSecretYn	""
contReqYn	"Y"
reqPriceAmtYn	null
cartelStatStr	"Publicado"
}


pageable	{ pageNumber: 0, pageSize: 10, offset: 0, … }
totalPages	12637
totalElements	126370
last	false
numberOfElements	10
size	10
number	0
sort	{ unsorted: false, sorted: true, empty: false }
first	true
empty	false

""" 



# Este el XPATH al boton que lanza el sitio web con las ofertas
# relacionadas a bienes, es sensible a cualquier cambio en el layout
# Mantener actualizado, y si falla revisar que el sitio del SICOP aun maneje este XPATH

BIENES_XPATH="/html/body/app-root/div/app-private-layout/div/div/div/app-tenders/div/div[1]/div[3]/div/div[1]/div/p-card/div/div/div/div/div[2]/a"
