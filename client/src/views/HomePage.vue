<script setup lang="ts">
import IngredientsTable, { type Ingredient } from '@/components/IngredientsTable.vue';
import { ref, type Ref } from 'vue';

type IngredientsTable = {
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
            document.getElementById(`error-${i}`)?.classList.remove('table__error--hidden')
            error = true
        }
        else{
            document.getElementById(`error-${i}`)?.classList.add('table__error--hidden')
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
        <main class="main">
            <IngredientsTable ref="ingredientsTable"/>
            <button @click="generateDishes">Generate Dishes</button>
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
.main{
   display: flex;
   flex-direction: column;
   align-items: center;
   gap: 4rem;
   max-width: 35rem;
   width: 100%;
}
</style>
