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
        "image": "https://thronesapi.com/assets/images/jon-snow.jpg"
    },
    {
        "name": "Daenerys Targaryen",
        "house": "Targaryen",
        "actor": "Emilia Clarke",
        "title": "Mère des Dragons",
        "status": "Décédée",
        "quote": "Dracarys.",
        "color": "#5c1a1a",
        "image": "https://thronesapi.com/assets/images/daenerys.jpg"
    },
    {
        "name": "Cersei Lannister",
        "house": "Lannister",
        "actor": "Lena Headey",
        "title": "Reine des Sept Couronnes",
        "status": "Décédée",
        "quote": "Quand tu joues au jeu des trônes, tu gagnes ou tu meurs.",
        "color": "#3a1a5c",
        "image": "https://thronesapi.com/assets/images/cersei.jpg"
    }
]

@app.route("/")
def index():
    return render_template("index.html", characters=characters)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")