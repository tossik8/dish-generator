<script setup lang="ts">
import { nextTick, ref, type Ref } from 'vue';

export type Ingredient = {
    name: string,
    quanity?: string
}
const ingredients: Ref<Ingredient[]> = ref([])

function addIngredient(): void {
    const ingredient: Ingredient = {
        name: ""
    }
    ingredients.value.push(ingredient)
    scrollTableIntoView()
}

function scrollTableIntoView() {
    const tbody = document.getElementsByTagName("tbody")[0]
    nextTick(() => {
        tbody.scroll({
            top: tbody.scrollHeight,
            left: 0,
            behavior: 'smooth'
        })
    })
}

function removeIngredient(index: number): void {
    ingredients.value.splice(index, 1)
}

defineExpose({
    ingredients
})
</script>

<template>
    <table id="ingredients-table" class="table">
        <tbody class="table__body">
            <tr class="table__row" v-for="(ingredient, index) in ingredients" :key="index">
                <td class="table__cell table__cell--wider">
                    <input class="table__input" v-model="ingredient.name" name="ingredient-name" type="text"
                        placeholder="Ingredient name">
                    <p :id="`error-${index}`" class="table__error table__error--hidden">Ingredient name is required</p>
                </td>
                <td class="table__cell">
                    <input class="table__input" v-model="ingredient.quanity" type="text" name="ingredient-quantity"
                        placeholder="Quantity">
                </td>
                <td class="table__cell">
                    <button @click="removeIngredient(index)">X</button>
                </td>
            </tr>
            <tr class="table__row table__row--add">
                <td class="table__cell table__cell--add" colspan="3">
                    <button class="table__button--add" @click="addIngredient()">+ Add Ingredient</button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<style scoped>
.table {
    width: 100%;
    border-spacing: 0;
}

.table__body {
    background-color: black;
    display: block;
    max-height: 20rem;
    min-height: 20rem;
    overflow-y: auto;
    border-spacing: 0.5rem;
}

.table__row {
    vertical-align: baseline;
}

.table__row--add {
    position: sticky;
    bottom: 0;
}

.table__cell {
    padding: 0;
}

.table__cell--wider {
    width: 70%;
}

.table__cell--add {
    width: 100em;
}

.table__input {
    width: 100%;
    padding: 1rem;
}

.table__error {
    color: red;
    font-size: 0.8rem;
}

.table__error--hidden {
    display: none;
}

.table__button--add {
    width: 100%;
}
</style>
