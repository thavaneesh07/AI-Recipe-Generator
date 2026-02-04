import subprocess

def generate_recipe_ai(ingredients: str, cuisine: str) -> str:
    prompt = f"""
You are a professional chef.

Create a detailed cooking recipe.

Ingredients:
{ingredients}

Cuisine preference: {cuisine}

Include:
- Recipe name
- Ingredients list
- Step-by-step instructions
- Cooking time
- Serving size
- Difficulty(easy,medium,hard)
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0 or not result.stdout.strip():
            return "⚠️ Failed to generate recipe."

        return result.stdout.strip()

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"
