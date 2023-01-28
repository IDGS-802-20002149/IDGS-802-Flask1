from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas", methods=["GET","POST"])
def operasBas():
    if request.method=="POST":
        num1= request.form.get("N1")
        num2= request.form.get("N2")
        opc = request.form.get("operasbasicas")
        if opc == "1":
            return "<h2>La suma es: {}".format(str(int(num1)+int(num2)))
        elif opc == "2":
            return "<h2>La resta es: {}".format(str(int(num1)-int(num2)))
        elif opc == "3":
            return "<h2>La multiplicacion es: {}".format(str(int(num1)*int(num2)))
        elif opc == "4":
            return "<h2>La division es: {}".format(str(float(num1)/float(num2)))
    else:
        return '''
        <form action="/operasBas" method="POST">
            <label>N1: </label>
            <input type:"text" name="N1"/><br><br>
            <label>N2: </label>
            <input type:"text" name="N2"/><br><br>
                <input type="radio" name="operasbasicas" value="1"/>Suma
                <input type="radio" name="operasbasicas" value="2"/>Resta
                <input type="radio" name="operasbasicas" value="3"/>Multiplicacion
                <input type="submit" value="calcular"/>
                <br><br>
            <input type="radio" name="operasbasicas" value="4"/>Division
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True, port=3000)