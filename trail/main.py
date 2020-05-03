from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=="GET":
        return render_template('index.html')
def hello():
    if request.method=='POST':
        return 'ok'


if __name__ == "__main__":
    app.run()