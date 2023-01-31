from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/operasbas",methods=["GET"])
def operasbas():
    return render_template("operasbas.html")

@app.route("/resultado",methods=["POST"])
def resultado():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    contador = 0
    cadena = " "
    res = 0
    
    while contador < int(n2):
        res += int(n1)
        if contador == 0:
            cadena += n1
        elif contador != int(n2):
            cadena += "+" + n1
        contador += 1

    return render_template("resultado.html",res=res, cadena=cadena)

if __name__ == "__main__":
    app.run(debug=True, port=3000)