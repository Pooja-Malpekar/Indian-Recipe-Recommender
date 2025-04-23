# Indian Recipe Recommender System (IRS) 🍲

A content-based recipe recommendation system built using Flask, Pandas, and Scikit-Learn. Users can input ingredients, cuisine type, and max cooking time to receive the top similar Indian recipes.

## 🔍 Features
- Ingredient-based recipe recommendation
- Filter by cuisine (South Indian, Punjabi, etc.)
- Filter by total cooking time
- Clean, simple Flask UI
- Dockerized and ready to deploy on Render

## 🚀 How It Works
1. Recipes are vectorized using TF-IDF from their ingredients + cuisine.
2. Cosine similarity is used to find the closest matches.
3. The top N results are returned with full instructions and timing.

## 📦 Tech Stack
- Python 3.11
- Flask
- Pandas
- Scikit-learn (TF-IDF + cosine similarity)
- Docker
- HTML (Jinja templates)

## 🚀 Demo

👉 Live URL: _[coming soon after Render deployment]_


## ▶️ Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/irs-flask.git
cd irs-flask

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
