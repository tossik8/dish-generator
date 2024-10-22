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
            <div>
                <IngredientsTable ref="ingredientsTable"/>
                <button id="add-ingredient" @click="ingredientsTable?.addIngredient()">+ Add Ingredient</button>
            </div>
            <button id="generate-dishes" @click="generateDishes">Generate Dishes</button>
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
main{
   display: flex;
   flex-direction: column;
   align-items: center;
   gap: 4rem;
   max-width: 35rem;
   width: 100%;
}
main > div{
    width: 100%;
}
#add-ingredient{
    width: 100%;
}
#generate-dishes{
    width: fit-content;
}
</style>
