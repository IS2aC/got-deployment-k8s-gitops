from flask import Flask, render_template

app = Flask(__name__)

characters = [
    {
        "name": "Jon Snow",
        "house": "Stark / Targaryen",
        "actor": "Kit Harington",
        "title": "Roi du Nord",
        "status": "Vivant",
        "quote": "Je ne sais rien.",
        "color": "#1a3a5c",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/38/Jon_Snow-Kit_Harington.jpg"
    },
    {
        "name": "Daenerys Targaryen",
        "house": "Targaryen",
        "actor": "Emilia Clarke",
        "title": "Mère des Dragons",
        "status": "Décédée",
        "quote": "Dracarys.",
        "color": "#5c1a1a",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/Daenerys_Targaryen_S8.png/220px-Daenerys_Targaryen_S8.png"
    },
    {
        "name": "Tyrion Lannister",
        "house": "Lannister",
        "actor": "Peter Dinklage",
        "title": "Main du Roi",
        "status": "Vivant",
        "quote": "Je bois et je sais des choses.",
        "color": "#5c4a1a",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/50/Tyrion_Lannister-Peter_Dinklage.jpg"
    },
    {
        "name": "Cersei Lannister",
        "house": "Lannister",
        "actor": "Lena Headey",
        "title": "Reine des Sept Couronnes",
        "status": "Décédée",
        "quote": "Quand tu joues au jeu des trônes, tu gagnes ou tu meurs.",
        "color": "#3a1a5c",
        "image": "https://upload.wikimedia.org/wikipedia/en/2/20/Cersei_Lannister_S8.png"
    },
    {
        "name": "Arya Stark",
        "house": "Stark",
        "actor": "Maisie Williams",
        "title": "La Fille Sans Visage",
        "status": "Vivante",
        "quote": "Une fille n'a pas de nom.",
        "color": "#1a5c2a",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/32/Arya_Stark-Maisie_Williams.jpg"
    },
    {
        "name": "Ned Stark",
        "house": "Stark",
        "actor": "Sean Bean",
        "title": "Seigneur de Winterfell",
        "status": "Décédé",
        "quote": "L'hiver vient.",
        "color": "#2a2a4a",
        "image": "https://upload.wikimedia.org/wikipedia/en/2/24/Ned_Stark-Sean_Bean.jpg"
    },
]

@app.route("/")
def index():
    return render_template("index.html", characters=characters)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")