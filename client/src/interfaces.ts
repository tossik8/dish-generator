export interface Ingredient {
    name: string
    quanity?: string
}

export interface Dish {
    name: string
    description: string
    image: string
    ingredients: Ingredient[]
    instructions: string[]
}
