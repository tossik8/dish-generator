<script setup lang="ts">
import { nextTick, ref, type Ref } from 'vue';

export type Ingredient = {
    name: string,
    quanity?: string
}
const ingredients: Ref<Ingredient[]> = ref([])

function addIngredient(): void{
    const ingredient: Ingredient = {
        name: ""
    }
    ingredients.value.push(ingredient)
    scrollTableIntoView()
}

function scrollTableIntoView(){
    const ingredientsTable = document.getElementById('ingredients-table')!
    nextTick(() => {
        ingredientsTable.scrollIntoView({block: 'end'})
    })
}

function removeIngredient(index: number): void{
    ingredients.value.splice(index, 1)
}

defineExpose({
    addIngredient,
    ingredients
})

</script>

<template>
    <div class="table-wrapper">
        <table id="ingredients-table">
            <tbody>
                <tr v-for="(ingredient, index) in ingredients" :key="index">
                    <td>
                        <input v-model="ingredient.name" name="ingredient-name" type="text" placeholder="Ingredient name">
                        <p :id="`error-${index}`" class="hidden error">Ingredient name is required</p>
                    </td>
                    <td>
                        <input v-model="ingredient.quanity" type="text" name="ingredient-quantity" placeholder="Quantity">
                    </td>
                    <td>
                        <button @click="removeIngredient(index)">X</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.table-wrapper{
    min-height: 15rem;
    max-height: 15rem;
    overflow-y: auto;
    width: 100%;
}

table{
    background-color: black;
    border-spacing: 0.5rem;
}

tr{
    vertical-align: baseline;
}

td:nth-of-type(1){
    width: 70%;
}

td input{
    width: 100%;
    padding: 1rem;
}

.error{
    color: red;
    font-size: 0.8rem;
}
.hidden{
    display: none;
}
</style>
