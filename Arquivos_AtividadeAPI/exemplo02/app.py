from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/filmes/<propriedade>")
def filmes(propriedade):
    if propriedade == "Populares":
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key="
    elif propriedade == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key="
    elif propriedade == "drama":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key="
    else:
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key="
    
    key = "5f05a73c076265750b722093fd2077e1"
    resposta = urllib.request.urlopen(url+key)
    dados = resposta.read()
    jsondata = json.loads(dados)
    
    return render_template("filmes.html", filmes = jsondata['results'])

if __name__=="__main__":
    app.run(debug=True)