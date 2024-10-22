<script setup lang="ts">
import { nextTick, ref, type Ref } from 'vue';

export type Ingredient = {
    name: string,
    quanity: string
}
const ingredients: Ref<Ingredient[]> = ref([])

function addIngredient(): void{
    const ingredient: Ingredient = {
        name: "",
        quanity: ""
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
                    <td><input v-model="ingredient.name" type="text" placeholder="Ingredient name"></td>
                    <td><input v-model="ingredient.quanity"type="text" placeholder="Quantity"></td>
                    <td><button @click="removeIngredient(index)">X</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.table-wrapper{
    min-height: 10rem;
    max-height: 10rem;
    overflow-y: auto;
}
</style>
