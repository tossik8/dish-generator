<script setup lang="ts">
import type { Ingredient } from '@/interfaces';
import { nextTick, ref, type Ref } from 'vue';

const ingredients: Ref<Ingredient[]> = ref([])

/**
 * Handles the click event to add a new ingredient and scroll the list into view.
 *
 * @returns {void}
 */
function handleAddIngredientClick(): void {
    addIngredient()
    scrollListIntoView()
}

/**
 * Adds a new, empty ingredient to the list.
 *
 * @returns {void}
 */
function addIngredient(): void {
    const ingredient: Ingredient = {
        name: ""
    }
    ingredients.value.push(ingredient)
}

/**
 * Scrolls the ingredients list smoothly to the latest entry.
 *
 * @returns {void}
 */
function scrollListIntoView(): void {
    const ingredients = document.getElementsByClassName("ingredients")[0]
    nextTick(() => {
        ingredients.scroll({
            top: ingredients.scrollHeight,
            left: 0,
            behavior: 'smooth'
        })
    })
}

/**
 * Removes an ingredient from the list by index.
 *
 * @param {number} index - The position of the ingredient to remove.
 * @returns {void}
 */
function removeIngredient(index: number): void {
    ingredients.value.splice(index, 1)
}

defineExpose({
    ingredients
})
</script>

<template>
    <div class="ingredients-container">
        <ul class="ingredients">
            <li v-for="(ingredient, index) in ingredients" :key="index">
                <div class="ingredients__container">
                    <input
                        class="ingredients__input"
                        v-model="ingredient.name"
                        name="ingredient-name"
                        type="text"
                        placeholder="Ingredient name"
                    />
                    <input
                        class="ingredients__input ingredients__input--short"
                        v-model="ingredient.quanity"
                        type="text"
                        name="ingredient-quantity"
                        placeholder="Quantity"
                    />
                    <button
                        class="ingredients__button ingredients__button--remove"
                        @click="removeIngredient(index)">
                        <font-awesome-icon
                            :icon="['fas', 'trash']"
                            class="trash-icon"
                        />
                    </button>
                </div>
                <p
                    :id="`error-${index}`"
                    class="ingredients__error ingredients__error--hidden">
                    Ingredient name is required
                </p>
            </li>
            <li class="ingredients__item--add">
                <button
                    class="ingredients__button ingredients__button--add"
                    @click="handleAddIngredientClick()">
                    + Add Ingredient
                </button>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.ingredients-container {
    background-color: var(--md-sys-color-on-background);
    padding: 0.5rem;
    width: inherit;
}

.ingredients {
    max-height: 20rem;
    min-height: 20rem;
    overflow-y: auto;
    width: inherit;
    list-style-type: none;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    padding-inline-start: 0;
}

.ingredients__item--add {
    position: sticky;
    bottom: 0;
    flex: 100%;
}

.ingredients__container {
    display: flex;
    gap: 0.5rem;
    width: 100%;
}

.ingredients__input {
    width: 100%;
    padding: 1rem;
    caret-color: var(--md-sys-color-primary);
}

.ingredients__input--short {
    flex: 35%;
}

.ingredients__error {
    color: var(--md-sys-color-error);
    font-size: 0.8rem;
}

.ingredients__error--hidden {
    display: none;
}

.ingredients__button {
    cursor: pointer;
}

.ingredients__button--remove {
    padding: 0 0.5rem;
    background-color: var(--md-sys-color-error);
    border: none;
}

.ingredients__button--add {
    width: 100%;
    background-color: var(--md-sys-color-secondary);
    color: var(--md-sys-color-on-secondary);
    border: none;
    padding: 1rem;
}

.trash-icon{
    color: var(--md-sys-color-on-error);
}
</style>
