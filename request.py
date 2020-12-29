import requests, json

# Bir kere tanımladık daha sonra bu istenilen ile dolacak şimdilik böyle planlandı.
data = {'ip': "100.0.0.1", 'sicaklik': 77}

while 1:
    url = 'http://25.110.252.134:5000/bildir'

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} # type olark böyle yazılması oldukça önem arz ediyor.
    x = requests.post(url, data=json.dumps(data), headers=headers)

    print(x.status_code)

    if x.ok:
        print(x.json())
        data1 = x.json()
        if data1['istenilen']:    # Sayfa refresh edileceği için null da gelebilir. So bu kontrol yapıldı.
            data['sicaklik'] = int(data1['istenilen'])
        print(data)
    else:
        print("there are problem")



