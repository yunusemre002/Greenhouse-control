from flask import Flask, render_template, request, redirect, url_for, jsonify
import sys

app = Flask(__name__)

# gelen   = { "sera1": [ip, sicaklik], "sera2": [ip, sicaklik], "sera3": [ip, sicaklik]}
gelen     = { "sera1": ["127.0.0.1", 0], "sera2": ["100.0.0.1", 0], "sera3": ["0.0.0.0", 0]}
istenilen = { "sera1": ["0.0.0.0", 1], "sera2": ["0.0.0.0", 1], "sera3": ["0.0.0.0", 1]}


# Clientler ile konuşuyor.
#  !!! Bunu yaptıktan sonra refresh etmem gerekir. Elle
# Requesti jsona dönüştürmek -- Dönüşen requestten ip adresi && sıcaklık  alma -- Bunları gelen dict'e yerleştirme.
# Return dictionary istenilen sıcaklık değerini  ilgili talebi yapan kişiye geri gönderiyor. json karşı taraf null mı diye kontrol edecek
@app.route('/bildir', methods=['POST'])
def bildir():
    req_data = request.get_json()
    print(req_data['sicaklik'])

    if req_data['ip'] == gelen['sera1'][0]:
        gelen['sera1'][1]=req_data['sicaklik']
        data = {'istenilen': istenilen['sera1'][1]}
        return jsonify(data)

    elif req_data['ip'] == gelen['sera2'][0]:
        gelen['sera2'][1]=req_data['sicaklik']
        data = {'istenilen': istenilen['sera2'][1]}
        return jsonify(data)

    elif req_data['ip'] == gelen['sera3'][0]:
        gelen['sera3'][1]=req_data['sicaklik']
        data = {'istenilen': istenilen['sera3'][1]}
        return jsonify(data)
    
    
# Ön tarafla(js) konuşuyor elleme :) 
# 1.Request jsona dönecek -- 2.Ip adresi && sıcaklık jsondan alınacak -- 3.Dict'e  2. dict (istenilen sıcaklıklar dict'i) yazılacak
@app.route('/iste', methods=['POST'])
def iste():
    req_data = request.form
    print(req_data)
    sera = req_data["sera"]
    value = req_data["value"]
    istenilen[sera][1] = value
    return redirect(url_for('index'))


@app.route('/',  methods=['POST', 'GET'])
def index():
    dizi = [gelen["sera1"][1], gelen["sera2"][1], gelen["sera3"][1]]
    return render_template('home.html', dizi = dizi)


if __name__ == '__main__':
    app.run(debug =True, host = '0.0.0.0')





# 1. fonksiyon sera bilgilerini dönecek - monitörde o bilgiler görüntülenecek.
# 2. fonksiyon seralar bize anlık sıcaklık değeri döndürecek. İlgili seraların değerleri ekranda gösterilecek. ({ip addresi : sıcaklık } map yap )
# 3. Monitörden sıcaklık değeri gönderilecek ilgili seralara (yani {sera bilgisi : sıcaklık değeri})
#  endpoint biçimleri 3 tane

# @app.route('/other/<string:id>')
# def other(id):
#     return render_template('other.html', id=id)