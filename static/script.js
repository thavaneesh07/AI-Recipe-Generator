async function generateRecipe() {
  const ingredients = document.getElementById("ingredients").value.trim();
  const cuisine = document.getElementById("cuisine").value;
  const result = document.getElementById("result");

  if (!ingredients) {
    result.textContent = "Please enter ingredients.";
    return;
  }

  result.textContent = "Generating recipe...";

  const res = await fetch("/generate-recipe", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ingredients, cuisine })
  });

  const data = await res.json();
  result.textContent = data.recipe || "Error generating recipe.";

  loadHistory();
}

async function loadHistory() {
  const history = document.getElementById("history");
  history.innerHTML = "";

  const res = await fetch("/recipes/latest");
  const recipes = await res.json();

  if (recipes.length === 0) {
    history.innerHTML = "<p>No recipe history yet. Generate one!🍳</p>";
    return;
  }

  recipes.forEach(r => {
    history.innerHTML += `
      <div class="history-card">
        <img src="/static/images/food.jpg" class="history-img" alt="">

        <div class="history-meta">
          <span class="cuisine-label">${r.cuisine || "Any"} Cuisine</span>
        </div>

        <pre>${r.recipe}</pre>

        <div class="actions">
          <button onclick="toggleFavorite(${r.id})">
            ${r.is_favorite ? "⭐" : "☆"}
          </button>
          <button onclick="deleteRecipe(${r.id})">🗑️</button>
        </div>
      </div>
    `;
  });
}

async function toggleFavorite(id) {
  await fetch(`/recipes/${id}/favorite`, { method: "POST" });
  loadHistory();
}

async function deleteRecipe(id) {
  await fetch(`/recipes/${id}`, { method: "DELETE" });
  loadHistory();
}

loadHistory();
