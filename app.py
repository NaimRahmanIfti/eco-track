from flask import Flask, render_template, request, redirect
from ai.carbon_analyzer import analyze_carbon
from quantum.quantum_ecoluck import generate_ecoluck
from db.models import db, Log
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "transport": request.form.get("transport"),
        "energy": request.form.get("energy"),
        "diet": request.form.get("diet")
    }
    score, tip = analyze_carbon(data)
    ecoluck = generate_ecoluck()

    log = Log(
        date=datetime.now(),
        transport=data["transport"],
        energy=data["energy"],
        diet=data["diet"],
        score=score,
        tip=tip,
        ecoluck=ecoluck
    )
    db.session.add(log)
    db.session.commit()

    return render_template("dashboard.html", score=score, tip=tip, ecoluck=ecoluck)

if __name__ == "__main__":
    app.run(debug=True)
