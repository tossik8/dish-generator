<script setup lang="ts">
import IngredientsList from '@/components/IngredientsList.vue';
import type { Dish, Ingredient } from '@/interfaces';
import { ref, type Ref } from 'vue';

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
    const valid = validateIngredients()
    if (!valid) {
        return
    }
    let dishes: Dish[]
    try {
        dishes = await fetchDishes()
    }
    catch (error) {
        console.error(error)
        alert('Something went wrong. Try again.')
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
    const response = await fetch(
        "http://localhost:8000",
        {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(ingredientsList.value.ingredients)
        }
    )
    if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}. URL: ${response.url}`)
    }
    return await response.json()
}

/**
 * Checks that each ingredient has a name.
 *
 * @returns {boolean} `true` if all ingredients are valid.
 */
function validateIngredients(): boolean {
    let error = false
    let i = 0
    for (let ingredient of ingredientsList.value.ingredients) {
        ingredient.name = ingredient.name.trim()
        if (!ingredient.name) {
            document.getElementById(`error-${i}`)?.classList.remove('ingredients__error--hidden')
            error = true
        }
        else {
            document.getElementById(`error-${i}`)?.classList.add('ingredients__error--hidden')
        }
        ++i
    }
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
            <button class="main__button" @click="generateDishes">Generate Dishes</button>
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

.header{
    text-align: center;
}

.header__title{
    color: var(--md-sys-color-primary);
}

.header__slogan{
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

.main__button{
    background-color: var(--md-sys-color-primary);
    color: var(--md-sys-color-on-primary);
    cursor: pointer;
    border: none;
    padding: 1rem;
    border-radius: 2rem;
}
</style>
