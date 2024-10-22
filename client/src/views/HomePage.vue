<script setup lang="ts">
import IngredientsTable, { type Ingredient } from '@/components/IngredientsTable.vue';
import { ref, type Ref } from 'vue';

type IngredientsTable = {
    addIngredient: () => void,
    ingredients: Ingredient[]
}
const ingredientsTable: Ref<IngredientsTable> = ref(null!)

function generateDishes(){
    console.log(ingredientsTable.value.ingredients)
}

</script>

<template>
    <div class="container">
        <header>
            <h1>Dish Generator</h1>
            <h2>List. Generate. Cook.</h2>
        </header>

        <main>
            <IngredientsTable ref="ingredientsTable"/>
            <button @click="ingredientsTable?.addIngredient()">+ Add Ingredient</button>
            <button @click="generateDishes">Generate</button>
        </main>
    </div>
</template>

<style scoped>
.container{
    display: flex;
    flex-direction: column;
    gap: 4rem;
    place-items: center;
    justify-content: center;
    min-height: inherit;
}
</style>
