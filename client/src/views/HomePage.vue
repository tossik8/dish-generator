<script setup lang="ts">
import IngredientsList from "@/components/IngredientsList.vue"
import type { Dish, Ingredient } from "@/interfaces"
import { ref, type Ref } from "vue"

type IngredientsList = {
    ingredients: Ingredient[]
}
const ingredientsList: Ref<IngredientsList> = ref(null!)

/**
 * Validates ingredients and, if valid, fetches dishes from the server.
 * Shows an error message if fetching fails.
 *
 * @returns {Promise<void>}
 */
async function generateDishes(): Promise<void> {
    if (!validateIngredients()) {
        return
    }
    let dishes: Dish[]
    try {
        dishes = await fetchDishes()
        console.log(dishes)
    } catch (error) {
        alert("Something went wrong. Try again.")
        return
    }
}

/**
 * Fetches dishes based on ingredients from the server.
 *
 * @returns {Promise<Dish[]>} Resolves with a list of `Dish` objects.
 * @throws {Error} if the response is not successful.
 */
async function fetchDishes(): Promise<Dish[]> {
    const response = await fetch("http://localhost:8000/gen_recipies", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(ingredientsList.value.ingredients)
    })
    if (!response.ok) {
        throw new Error(
            `${response.status} - ${response.statusText}. URL: ${response.url}`
        )
    }
    return await response.json()
}

/**
 * Validates a list of ingredients.
 *
 * Iterates over each ingredient, trims whitespace, and checks if the name is empty.
 * Updates error message visibility accordingly.
 *
 * @returns {boolean} `true` if all ingredients are valid.
 */
function validateIngredients(): boolean {
    if (ingredientsList.value.ingredients.length === 0) {
        return false
    }
    let error = false
    ingredientsList.value.ingredients.forEach((ingredient, index) => {
        ingredient.name = ingredient.name.trim()
        const hasName = Boolean(ingredient.name)
        if (!hasName) {
            error = true
        }
        document
            .getElementById(`error-${index}`)
            ?.classList.toggle("ingredients__error--hidden", hasName)
    })
    return !error
}
</script>

<template>
    <div class="container">
        <header class="header">
            <h1 class="header__title">Dish Generator</h1>
            <h2 class="header__slogan">List. Generate. Cook.</h2>
        </header>
        <main class="main">
            <IngredientsList ref="ingredientsList" />
            <button class="main__button" @click="generateDishes">
                Generate Dishes
            </button>
        </main>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    gap: 4rem;
    justify-content: center;
    align-items: center;
    min-height: inherit;
    padding: 0 0.5rem;
}

.header {
    text-align: center;
}

.header__title {
    color: var(--md-sys-color-primary);
}

.header__slogan {
    color: var(--md-sys-color-secondary);
}

.main {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4rem;
    max-width: 35rem;
    width: 100%;
}

.main__button {
    background-color: var(--md-sys-color-primary);
    color: var(--md-sys-color-on-primary);
    cursor: pointer;
    border: none;
    padding: 1rem;
    border-radius: 2rem;
}
</style>
