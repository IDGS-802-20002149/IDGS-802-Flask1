from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/Boletos",methods=["GET"])
def layout():
    return render_template("Cinepolis.html")

@app.route("/resultadoCinepolis",methods=["POST"])
def resultadoCinepolis():

    numBoletos = int(request.form.get("txtCantidadBoletos"))
    terjetaCineco = request.form.get("rgroupTarjeta")

    if terjetaCineco == "1":
        descCliente = 0.9
    else:
        descCliente = 1

    if (numBoletos<3):
        res = "$" + str(numBoletos*12*descCliente)
    elif numBoletos>=3 and numBoletos<=5:
        res = "$" + str((12*numBoletos)*0.9*descCliente)
    elif numBoletos>5 and numBoletos<=7:
        res = "$" + str((12*numBoletos)*0.85*descCliente)
    elif numBoletos > 7:
        res = "No puedes comprar mas de 7 boletos"
    
    return render_template("resultadoCinepolis.html", res=res)

if __name__ == "__main__":
    app.run(debug=True, port=3000)