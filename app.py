from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_normalitas(berat, massa_molar, volume_ml, valensi):
    volume_liter = volume_ml / 1000
    mol = berat / massa_molar
    normalitas = (mol / volume_liter) * valensi
    return normalitas

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        try:
            berat = float(request.form['berat'])
            massa_molar = float(request.form['massa_molar'])
            volume_ml = float(request.form['volume_ml'])
            valensi = int(request.form['valensi'])

            hasil = hitung_normalitas(berat, massa_molar, volume_ml, valensi)
        except:
            hasil = "Input tidak valid!"
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
