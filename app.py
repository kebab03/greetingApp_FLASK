from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="GET":
        return render_template("index@34.html")
    if request.method=="POST":
        return render_template("greet.html",name = request.form.get("name","world"))

#        "TODO"
if __name__ == '__main__':
    app.run()
