import json
from flask import Flask, Response
app = Flask(__name__)

class empleados:
    sueldo = 0
    hdiurnas = 0
    hnocturnas = 0
    auxilio = 0
    totalDed = 0
    totalDev = 0
    total = 0
    diurnas = 0
    nocturnas = 0
    def __init__(self, sueldo, diurnas, nocturnas):
        self.sueldo = sueldo
        self.hdiurnas = diurnas
        self.hnocturnas = nocturnas

    def calculoDeduciones(self):
        self.totalDed = self.sueldo*0.08

    def calculoDevengado(self):
        hora = int((self.sueldo/30)/8)
        self.totalDev = int(((hora*self.hdiurnas)*0.125)+((hora*self.hnocturnas)*0.175))

    def totalF(self):
        self.total = (self.sueldo + self.totalDev) - self.totalDed

@app.route('/user/<int:sueldo>/<int:diurnas>/<int:nocturnas>', methods=['GET', 'POST'])
def proceso(sueldo,diurnas,nocturnas):
        emp1 = empleados(sueldo,diurnas,nocturnas)
        emp1.calculoDeduciones()
        emp1.calculoDevengado()
        emp1.totalF()
        lista = { "empleado":[{ "sueldo" : emp1.total, "devengadoAdicional" : emp1.totalDev, "deducido" : emp1.totalDed}]}
        return Response(json.dumps(lista),  mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')
    #app.run(debug=True)