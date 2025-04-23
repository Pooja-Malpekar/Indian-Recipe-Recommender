from flask import Flask, render_template, request
from recommender import recommend_recipes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input from form
    ingredients = request.form.get('ingredients')
    cuisine = request.form.get('cuisine')
    max_time = request.form.get('max_time')

    # Handle empty or invalid inputs
    if not ingredients or not cuisine:
        return "Please enter ingredients and cuisine.", 400

    try:
        max_time = int(max_time) if max_time else None
    except ValueError:
        max_time = None

    # Get recommendations
    recommendations = recommend_recipes(ingredients, cuisine, max_time)

    # Pass results to template
    return render_template('results.html', recipes=recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

