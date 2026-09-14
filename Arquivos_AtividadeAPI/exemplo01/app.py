from flask import Flask, render_template, request

app = Flask(__name__)

itenschurrasco = []

@app.route("/", methods=["GET","POST"])
def principal():
    if request.method =="POST":
        if request.form.get("item"):
            itenschurrasco.append(request.form.get("item"))
    return render_template("index.html", itenschurrasco=itenschurrasco)

if __name__=="__main__":
    app.run(debug=True)