from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle


app = Flask(__name__)


with open("MLR_Model.pkl", "rb") as file:
    reg = pickle.load(file)


city_map = {
    'Shoreline': 0,
    'Seattle': 1,
    'Kent': 2,
    'Bellevue': 3,
    'Redmond': 4,
    'Maple Valley': 5,
    'North Bend': 6,
    'Lake Forest Park': 7,
    'Sammamish': 8,
    'Auburn': 9,
    'Des Moines': 10,
    'Bothell': 11,
    'Federal Way': 12,
    'Kirkland': 13,
    'Issaquah': 14,
    'Woodinville': 15,
    'Normandy Park': 16,
    'Fall City': 17,
    'Renton': 18,
    'Carnation': 19,
    'Snoqualmie': 20,
    'Duvall': 21,
    'Burien': 22,
    'Covington': 23,
    'Inglewood-Finn Hill': 24,
    'Kenmore': 25,
    'Newcastle': 26,
    'Mercer Island': 27,
    'Black Diamond': 28,
    'Ravensdale': 29,
    'Clyde Hill': 30,
    'Algona': 31,
    'Skykomish': 32,
    'Tukwila': 33,
    'Vashon': 34,
    'Yarrow Point': 35,
    'SeaTac': 36,
    'Medina': 37,
    'Enumclaw': 38,
    'Snoqualmie Pass': 39,
    'Pacific': 40,
    'Beaux Arts Village': 41,
    'Preston': 42,
    'Milton': 43
}


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqft_living = float(request.form['sqft_living'])
    sqft_lot = float(request.form['sqft_lot'])
    floors = float(request.form['floors'])
    waterfront = float(request.form['waterfront'])
    view = float(request.form['view'])
    condition = float(request.form['condition'])
    sqft_above = float(request.form['sqft_above'])
    sqft_basement = float(request.form['sqft_basement'])
    yr_built = float(request.form['yr_built'])
    yr_renovated = float(request.form['yr_renovated'])

    city = request.form['city']

    city_value = city_map[city]

    date = pd.to_datetime(request.form['date'])

    year = date.year
    month = date.month
    day = date.day

    country = 0

    input_data = np.array([[
        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        city_value,
        country,
        year,
        month,
        day
    ]])

    prediction = reg.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction_text=f"Predicted House Price: ${prediction:,.2f}"
    )


if __name__ == '__main__':
    app.run(debug=True)