from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'martina'


@app.route('/')         
def index():
    return render_template("index.html")


@app.route('/process_money', methods=['POST'])         
def process_money():
    print(request.form)
    
    if request.form['building'] == 'farm':
        numero_random = random.randint(10,20)
        operacion = random.choice(['suma', 'resta'])
        if operacion == 'suma':
            session["mioro"]+= numero_random
        else:
            session["mioro"]-= numero_random
            if session["mioro"] < 0:
                session["mioro"] = 0
        
    elif request.form['building'] == 'cave':
        numero_random = random.randint(5,10)
        operacion = random.choice(['suma', 'resta'])
        if operacion == 'suma':
            session["mioro"]+= numero_random
        else:
            session["mioro"]-= numero_random
            if session["mioro"] < 0:
                session["mioro"] = 0

    elif request.form['building'] == 'house':
        numero_random = random.randint(2,20)
        operacion = random.choice(['suma', 'resta'])
        if operacion == 'suma':
            session["mioro"]+= numero_random
        else:
            session["mioro"]-= numero_random
            if session["mioro"] < 0:
                session["mioro"] = 0

    elif request.form['building'] == 'casino':
        numero_random = random.randint(0,50)
        operacion = random.choice(['suma', 'resta'])
        if operacion == 'suma':
            session["mioro"]+= numero_random
        else:
            session["mioro"]-= numero_random
            if session["mioro"] < 0:
                session["mioro"] = 0
    
    elif request.form["building"] == "pop":
        session["mioro"] = 0
    
    
    return redirect("/")





if __name__=="__main__":   
    app.run(debug=True)