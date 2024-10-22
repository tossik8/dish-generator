<script setup lang="ts">
import IngredientsTable, { type Ingredient } from '@/components/IngredientsTable.vue';
import { ref, type Ref } from 'vue';

type IngredientsTable = {
    addIngredient: () => void,
    ingredients: Ingredient[]
}
const ingredientsTable: Ref<IngredientsTable> = ref(null!)

function generateDishes(): void{
    const valid = validateIngredients()
    if(!valid){
        console.log('Invalid')
        return
    }
    console.log('Valid')
}

function validateIngredients(): boolean{
    let error = false
    let i = 0
    for(let ingredient of ingredientsTable.value.ingredients){
        ingredient.name = ingredient.name.trim()
        if(!ingredient.name){
            document.getElementById(`error-${i}`)?.classList.remove('hidden')
            error = true
        }
        else{
            document.getElementById(`error-${i}`)?.classList.add('hidden')
        }
        ++i
    }
    return !error
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
    justify-content: center;
    align-items: center;
    min-height: inherit;
}
</style>
