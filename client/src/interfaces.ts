export interface Ingredient {
    name: string
    quantity?: string
}

export interface Dish {
    name: string
    description: string
    image: string
    ingredients: Ingredient[]
    instructions: string[]
}
