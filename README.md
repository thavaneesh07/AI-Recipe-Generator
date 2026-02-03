# AI Recipe Generator

A web application that generates cooking recipes based on user-provided ingredients and optional cuisine preferences.  
The application uses a locally running language model for recipe generation, with a Flask backend, SQLite database, and a clean dark-themed frontend.

---

## Overview

The AI Recipe Generator allows users to:
- Enter a list of ingredients they have available
- Select a preferred cuisine (optional)
- Generate a structured recipe based on the input
- View, favorite, and manage previously generated recipes

All recipes are generated locally without relying on external APIs.

---

## Features

- **Recipe Generation**
  - Generates step-by-step cooking recipes from a list of ingredients
  - Adapts recipe style based on selected cuisine

- **Cuisine Selection**
  - Supports multiple cuisines such as Indian, Italian, Chinese, Mexican, and more
  - Cuisine preference is stored alongside the recipe

- **Recipe History**
  - Stores generated recipes in a SQLite database
  - Displays the most recent recipes
  - Includes a clear empty-state message when no recipes exist

- **Favorites & Deletion**
  - Mark recipes as favorites
  - Delete recipes from history

- **User Interface**
  - Dark-themed, card-based layout
  - Consistent and stable recipe imagery
  - Responsive design for different screen sizes

---

## Tech Stack

**Frontend**
- HTML
- CSS (Dark theme)
- JavaScript (Vanilla)

**Backend**
- Python
- Flask
- Flask-SQLAlchemy

**Database**
- SQLite

**Recipe Generation**
- Ollama (local language model runtime)

---

## Project Structure

_recipe_generator/
│
├── backend/
│ ├── app.py # Flask application and routes
│ └── ai_engine.py # Local AI integration
│
├── templates/
│ └── index.html # Main HTML template
│
├── static/
│ ├── style.css # Dark theme styling
│ ├── script.js # Frontend logic
│ └── images/
│ └── food.jpg # Static recipe image
│
├── recipes.db # SQLite database (auto-generated)
└── README.md




---

## Setup Instructions

### Prerequisites
- Python 3.10 or newer
- Ollama installed locally
- An Ollama-supported model (e.g. `llama3`)

Verify Ollama is running:
```bash
ollama run llama3


## Clone the repository: 

git clone https://github.com/your-username/ai-recipe-generator.git
cd ai-recipe-generator


## Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows


## Install dependencies:

pip install flask flask-sqlalchemy


## Run the application:

python -m backend.app


## Open in browser:

http://127.0.0.1:5000












