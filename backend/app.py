from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from backend.calculation import calculate_total
from backend.gpt_suggestions import get_suggestions

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    travel = float(request.form['travel'])
    transport = request.form['transport']
    diet = request.form['diet']
    electricity = float(request.form['electricity'])

    total, travel_kg, food_kg, electricity_kg = calculate_total(travel, transport, diet, electricity)
    suggestions = get_suggestions(travel, transport, diet, electricity, total)

    return render_template('index.html',
        result=total,
        travel=travel_kg,
        food=food_kg,
        electricity=electricity_kg,
        suggestion=suggestions
    )

if __name__ == '__main__':
    app.run(debug=True)
