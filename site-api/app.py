from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pokemon")
def pagina_pokemon():
    return render_template("pokemon.html")


@app.route("/buscar_pokemon")
def buscar_pokemon():

    nome = request.args.get("nome")

    if not nome:
        return render_template(
            "erro.html",
            mensagem="Digite o nome de um Pokémon."
        )

    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"

    resposta = requests.get(url)

    if resposta.status_code != 200:
        return render_template(
            "erro.html",
            mensagem="Pokémon não encontrado."
        )

    dados = resposta.json()

    pokemon = {
        "nome": dados["name"].title(),
        "imagem": dados["sprites"]["front_default"],

        "tipos": [
            tipo["type"]["name"].title()
            for tipo in dados["types"]
        ],

        "altura": dados["height"] / 10,
        "peso": dados["weight"] / 10
    }
    return render_template(
        "resultado_pokemon.html",
        pokemon=pokemon
    )



@app.route("/paises")
def pagina_paises():
    return render_template("paises.html")



@app.route("/buscar_pais")
def buscar_pais():

    pais = request.args.get("pais")

    if not pais:
        return render_template(
            "erro.html",
            mensagem="Digite o nome de um país."
        )

    url = f"https://restcountries.com/v3.1/name/{pais}"

    resposta = requests.get(url)

    if resposta.status_code != 200:
        return render_template(
            "erro.html",
            mensagem="País não encontrado."
        )

    dados = resposta.json()

    pais_info = {
        "nome": dados[0]["name"]["common"],
        "capital": dados[0]["capital"][0],

        "populacao": f"{dados[0]['population']:,}".replace(",", "."),

        "bandeira": dados[0]["flags"]["png"],
        "continente": dados[0]["continents"][0]
    }

    return render_template(
        "resultado_pais.html",
        pais=pais_info
    )

if __name__ == "__main__":
    app.run(debug=True)