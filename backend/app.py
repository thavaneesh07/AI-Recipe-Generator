import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from backend.ai_engine import generate_recipe_ai


# Absolute path to project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates"),
)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "recipes.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -------------------- Database Model --------------------
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String, nullable=False)
    recipe = db.Column(db.Text, nullable=False)
    cuisine = db.Column(db.String)
    is_favorite = db.Column(db.Boolean, default=False)

# Create DB
with app.app_context():
    db.create_all()

# -------------------- Routes --------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    data = request.json
    ingredients = data.get("ingredients", "").strip()
    cuisine = data.get("cuisine", "Any")

    if not ingredients:
        return jsonify({"error": "Ingredients are required"}), 400

    # TEMPORARY placeholder (AI comes next)
    recipe_text = generate_recipe_ai(ingredients, cuisine)


    new_recipe = Recipe(
        ingredients=ingredients,
        recipe=recipe_text,
        cuisine=cuisine
    )

    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({"recipe": recipe_text})

@app.route("/recipes/latest")
def latest_recipes():
    recipes = Recipe.query.order_by(Recipe.id.desc()).limit(10).all()

    return jsonify([
        {
            "id": r.id,
            "recipe": r.recipe,
            "cuisine": r.cuisine,
            "is_favorite": r.is_favorite
        }
        for r in recipes
    ])

@app.route("/recipes/<int:rid>/favorite", methods=["POST"])
def toggle_favorite(rid):
    r = Recipe.query.get_or_404(rid)
    r.is_favorite = not r.is_favorite
    db.session.commit()
    return jsonify({"ok": True})

@app.route("/recipes/<int:rid>", methods=["DELETE"])
def delete_recipe(rid):
    r = Recipe.query.get_or_404(rid)
    db.session.delete(r)
    db.session.commit()
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
