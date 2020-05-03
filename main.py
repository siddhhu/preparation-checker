from flask import Flask,render_template,request
import pickle
with open("jee.pkl","rb") as file:
    logistic=pickle.load(file)
app = Flask(__name__)
@app.route("/demo")
def demo():
    return render_template('demo.html')
@app.route("/next")
def lamo():
    return render_template('next.html')
@app.route("/hello",methods=["GET","POST"])
def Back():
    if request.method=="POST":
        mydict=request.form
        user1=int(mydict['user1'])
        user2=int(mydict['user2'])
        user3=int(mydict['user3'])
        user4=int(mydict['user4'])
        user5=int(mydict['user5'])
        myvar=[user4,user5,user2,user3,user1]
        print([myvar])
        prob=logistic.predict_proba([myvar])[0][1]
        prob=prob*100
    else:
        return render_template('hello.html')
    return render_template('next.html',inf=round(prob,2))
  

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        mydict=request.form
        user1=int(mydict['user1'])
        user2=int(mydict['user2'])
        user3=int(mydict['user3'])
        user4=int(mydict['user4'])
        user5=int(mydict['user5'])
        myvar=[user4,user5,user2,user3,user1]
        print([myvar])
        prob=logistic.predict_proba([myvar])[0][1]
        prob=prob*100
    else:
        return render_template('hello.html')
    return render_template('next.html',inf=round(prob,2))
   
if __name__ == "__main__":

    app.run(debug=True)