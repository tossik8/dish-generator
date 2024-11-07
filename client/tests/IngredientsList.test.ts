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
        const addButton = wrapper.find(
            "button.ingredients__button--add"
        ) as DOMWrapper<HTMLButtonElement>
        const count = 10
        await clickButton(addButton, count)

        expect(ingredients.childElementCount).toBe(count + 1)
        expect(ingredients.scroll).toHaveBeenCalledTimes(count)
    })

    test("remove ingredients", async () => {
        const addButton = wrapper.find(
            "button.ingredients__button--add"
        ) as DOMWrapper<HTMLButtonElement>
        const addCount = 10
        await clickButton(addButton, addCount)

        const removeButton = wrapper.find(
            "button.ingredients__button--remove"
        ) as DOMWrapper<HTMLButtonElement>
        const removeCount = 3
        await clickButton(removeButton, removeCount)

        expect(ingredients.childElementCount).toBe(addCount - removeCount + 1)
    })

    test("enter the ingredient information", async () => {
        const addButton = wrapper.find(
            "button.ingredients__button--add"
        ) as DOMWrapper<HTMLButtonElement>
        await clickButton(addButton)

        // prettier-ignore
        const ingredientNameInput = wrapper.find(
            "input[name=ingredient-name]"
        )
        const ingredientQuantityInput = wrapper.find(
            "input[name=ingredient-quantity]"
        )

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

    /**
     * Triggers a specified button click a given number of times.
     *
     * @param {DOMWrapper<HTMLButtonElement>} button - The button DOM wrapper to be clicked.
     * @param {number} [count=1] - The number of times to click the button. Defaults to 1 if not specified.
     * @returns {Promise<void>} - A promise that resolves when all clicks are completed.
     */
    async function clickButton(
        button: DOMWrapper<HTMLButtonElement>,
        count: number = 1
    ): Promise<void> {
        for (let i = 0; i < count; ++i) {
            await button.trigger("click")
        }
    }
})
