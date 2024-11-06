import { DOMWrapper, mount, VueWrapper } from "@vue/test-utils"
import { beforeEach, describe, expect, test, vi } from "vitest"
import IngredientsList from "../src/App.vue"

describe("IngredientsList.vue", () => {
    let wrapper: VueWrapper
    let ingredients: HTMLUListElement

    beforeEach(() => {
        wrapper = mount(IngredientsList)
        ingredients = wrapper.find("ul.ingredients").element as HTMLUListElement
        ingredients.scroll = vi.fn()
    })

    test("add ingredients", async () => {
        const addButton = wrapper.find("button.ingredients__button--add")
        const count = 10
        await clickButton(addButton, count)

        expect(ingredients.childElementCount).toBe(count + 1)
        expect(ingredients.scroll).toHaveBeenCalledTimes(count)
    })

    test("remove ingredients", async () => {
        const addButton = wrapper.find("button.ingredients__button--add")
        const addCount = 10
        await clickButton(addButton, addCount)

        const removeButton = wrapper.find("button.ingredients__button--remove")
        const removeCount = 3
        await clickButton(removeButton, removeCount)

        expect(ingredients.childElementCount).toBe(addCount - removeCount + 1)
    })

    test("enter the ingredient information", async () => {
        const addButton = wrapper.find("button.ingredients__button--add")
        await clickButton(addButton, 1)

        const ingredientNameInput = wrapper.find("input[name=ingredient-name]")
        // prettier-ignore
        const ingredientQuantityInput = wrapper.find("input[name=ingredient-quantity]")

        // prettier-ignore
        expect((ingredientNameInput.element as HTMLInputElement).value).toBe("")
        // prettier-ignore
        expect((ingredientQuantityInput.element as HTMLInputElement).value).toBe("")

        const ingredientName = "Bread"
        await ingredientNameInput.setValue(ingredientName)
        const ingredientQuantity = "1 loaf"
        await ingredientQuantityInput.setValue(ingredientQuantity)

        // prettier-ignore
        expect((ingredientNameInput.element as HTMLInputElement).value).toBe(ingredientName)
        // prettier-ignore
        expect((ingredientQuantityInput.element as HTMLInputElement).value).toBe(ingredientQuantity)
    })

    async function clickButton(
        button: DOMWrapper<Element>,
        count: number
    ): Promise<void> {
        for (let i = 0; i < count; ++i) {
            await button.trigger("click")
        }
    }
})
