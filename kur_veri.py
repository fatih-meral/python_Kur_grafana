import requests
import time
from influxdb import InfluxDBClient

# InfluxDB bağlantı bilgileri
host = '192.168.253.71'
port = 8086
user = 'root'
password = 'Deneme123!'
dbname = 'satisdb'

client = InfluxDBClient(host, port, user, password, dbname)
# InfluxDB bağlantı bilgileri



while True:
    
    try:
        response = requests.get("https://api.genelpara.com/embed/doviz.json")
        data = response.json()
        usd_data = data["USD"]["satis"]    
        dolar=float(usd_data)
        print(dolar)
        json_body = [
            {
                "measurement": "Kur",
                "tags": {
                    "kur": "USD"
                },
                "fields": {
                    "fiyat": dolar
                }
            }
        ]
        client.write_points(json_body)
       
        time.sleep(900)#15 dakika
    except Exception:
        print("siteye erişilemedi")
        time.sleep(15)