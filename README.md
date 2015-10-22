# Python Client for RajaOngkir.com

> RajaOngkir memiliki API yang dapat Anda manfaatkan untuk membuat aplikasi Android, iOS, Blackberry atau perhitungan ongkir otomatis di toko online Anda.

> Data ongkos kirim diambil langsung dari web masing-masing kurir untuk menjamin akurasi data. Anda juga bisa melaporkan kepada kami jika ada ongkir yang tidak akurat.

*cited from http://rajaongkir.com/*

## Instalation

`$ pip install git+git://github.com/kalarau/rajaongkir-python.git`

## Usage

```
#!/usr/bin/env python
from RajaOngkir import Client

KEY = 'YOUR-RAJAONGKIR-API-KEY'
ACCOUNT_TYPE = 'YOUR-RAJAONGKIR-ACCOUNT-TYPE'

#: build client
c = Client(KEY, ACCOUNT_TYPE)

#: get cost for starter / basic account
cost = c.cost(courier='jne', weight=1700, origin='501', destination='114')
print cost

#: or, more advanced query on pro account
pro_cost = c.cost(courier='jne', weight=2.3,
                    origin=501, destination=574,
                    originType='city', destinationType='subdistrict',
                    width=3, height=15)
print pro_cost
```

## Todo

- implement all available endpoint on rajaongkir.com
- create a better documentation

## License

see `LICENSE`
