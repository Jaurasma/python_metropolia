# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:numero>', methods=['GET'])
def tarkista_alkuluku(numero):
    on_alkuluku = is_prime(numero)
    return jsonify({
        "Number": numero,
        "isPrime": on_alkuluku
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)