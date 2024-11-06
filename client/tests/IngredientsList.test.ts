import { mount } from "@vue/test-utils"
import { describe, expect, test, vi } from "vitest"
import IngredientsList from "../src/App.vue"

describe("IngredientsList.vue", () => {
    test("add ingredient", async () => {
        const wrapper = mount(IngredientsList)
        const ingredients = wrapper.find("ul.ingredients").element
        ingredients.scroll = vi.fn()

        const button = wrapper.find("button.ingredients__button--add")
        const count = 10
        for (let i = 0; i < count; ++i) {
            await button.trigger("click")
        }

        expect(ingredients.childElementCount).toBe(count + 1)
        expect(ingredients.scroll).toHaveBeenCalledTimes(count)
    })

    test("remove ingredient", async () => {
        const wrapper = mount(IngredientsList)
        const ingredients = wrapper.find("ul.ingredients").element
        ingredients.scroll = vi.fn()

        const add_button = wrapper.find("button.ingredients__button--add")
        const add_count = 10
        for (let i = 0; i < add_count; ++i) {
            await add_button.trigger("click")
        }

        const remove_button = wrapper.find("button.ingredients__button--remove")
        const remove_count = 3
        for (let i = 0; i < remove_count; ++i) {
            await remove_button.trigger("click")
        }

        expect(ingredients.childElementCount).toBe(add_count - remove_count + 1)
    })
})
