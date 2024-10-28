from typing import List
from DTOs import DtoIngredient, OutputRecipe
from fastapi import FastAPI
from RecipeModel import generate

app = FastAPI()


@app.post("/gen_recipies/")
async def gen_recipies(ingredients: List[DtoIngredient]) -> list[OutputRecipe]:
    ingredients:List[str] = [i.to_llm_input_format() for i in ingredients]
    return await generate(ingredients)