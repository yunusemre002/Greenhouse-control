import serial, math, requests, json

# Bir kere tanımladık daha sonra bu istenilen ile dolacak şimdilik böyle planlandı.
data = {'ip': "25.11.1.18", 'sicaklik': 0}
url = 'http://25.110.252.134:5000/bildir'
# url = 'http://127.0.0.1:5000/bildir'
headers = {'Content-type': 'application/json',
           'Accept': 'text/plain'}  # type olark böyle yazılması oldukça önem arz ediyor.

def serverCom(okunan):

    data['sicaklik'] = okunan
    x = requests.post(url, data=json.dumps(data), headers=headers)
    # print(x.status_code)

    if x.ok:
        # print(x.json())
        data1 = x.json()
        if data1['istenilen']:    # Sayfa refresh edileceği için null da gelebilir. So bu kontrol yapıldı.
            # data['sicaklik'] = int(data1['istenilen'])
            print("En son istenen sıcaklık : ", int(data1['istenilen']))
            return int(data1['istenilen'])
        else:
            return None
    else:
        print("there are problem")


while (1):
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM1'
    ser.open()                  # Üstte portu belirledik ve açtık

    s = ser.readline()                      # Portu okunur
    okunan = s.decode('utf-8')              # Seradan gelen değeri aldım okuyacağımız değere çevirdim ama str
    okunan = float(okunan.rstrip())         # Bu str' nin sonunda \n\r vardı onları kaldırıp floata çevirdim.
    #okunan = int(math.ceil(okunan))        # Üste yuvarlayıp inte çevirdim.


    print("Sera göstergesi", okunan)
    isThereRequest = serverCom(okunan)
    if(isThereRequest):
        ser.write(str(isThereRequest).encode('utf-8'))
    else:
        print("istenen değer yok!")

ser.close()
print(ser.is_open)


