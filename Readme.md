# AI Recipe Generator 🍳

A full-stack web application that generates cooking recipes based on user-provided ingredients and cuisine preferences.  
Built with Flask, SQLite, and a clean dark-themed frontend.

---

## Features

- Generate recipes from custom ingredients
- Cuisine selection (Indian, Italian, Chinese, etc.)
- Stores recent recipes using SQLite
- View the last 10 generated recipes
- Mark recipes as favorites
- Delete unwanted recipes
- Clean dark-themed UI
- Responsive and minimal design

---

## Tech Stack

**Backend**
- Python
- Flask
- Flask-SQLAlchemy
- SQLite

**Frontend**
- HTML
- CSS (Dark Theme)
- Vanilla JavaScript (Fetch API)

---

## Project Structure

ai_recipe_generator/
│
├── backend/
│ ├── app.py # Flask application & API routes
│
├── static/
│ ├── style.css # Dark theme styles
│ ├── script.js # Frontend logic
│ └── images/
│ └── food.jpg # Static food image
│
├── templates/
│ └── index.html # Main UI template
│
├── recipes.db # SQLite database (auto-created)
└── README.md



---

## How It Works

1. User enters ingredients and selects a cuisine.
2. The backend generates a recipe (currently placeholder / local AI-ready).
3. The recipe is saved to a SQLite database.
4. Recent recipes are displayed with options to favorite or delete.
5. A static food image is used for consistent visuals.

---

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-recipe-generator.git

cd ai-recipe-generator


2. Create a virtual environment

python -m venv venv


3. Activate the virtual environment
a.Windows (PowerShell / CMD)
venv\Scripts\activate

b.macOS / Linux 
source venv/bin/activate
Once activated, you should see (venv) in your terminal.

4. Install dependencies

pip install flask flask-sqlalchemy


5. Run the application
python -m backend.app


Open your browser and go to:

http://127.0.0.1:5000