from flask import Flask, render_template, request, redirect
from fuzzy_spk import hitung_fuzzy

app = Flask(__name__)


@app.route('/')
def kriteria():
    return render_template("kriteria.html")

@app.route('/process', methods=['POST'])
def process():
    harga = int(request.form['harga'])
    jarak = int(request.form['jarak'])
    fasilitas = int(request.form['fasilitas'])

    hasil = hitung_fuzzy(harga, jarak, fasilitas)  

    if hasil == "santai":
        return redirect('/hasil_santai')
    elif hasil == "mato":
        return redirect('/hasil_mato')
    elif hasil == "bento":
        return redirect('/hasil_bento')
    elif hasil == "senja":
        return redirect('/hasil_senja')
    else:
        return redirect('/hasil_mato') 

@app.route('/hasil_santai')
def hasil_santai():
    return render_template("hasilSantai.html")

@app.route('/hasil_mato')
def hasil_mato():
    return render_template("hasilMato.html")

@app.route('/hasil_bento')
def hasil_bento():
    return render_template("hasilBento.html")

@app.route('/hasil_senja')
def hasil_senja():
    return render_template("hasilSenja.html")

if __name__ == "__main__":
    app.run(debug=True)
