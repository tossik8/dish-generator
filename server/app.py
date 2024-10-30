from typing import List

import uvicorn

from DTOs import DtoIngredient, OutputRecipe
from fastapi import FastAPI
from RecipeModel import generate

app = FastAPI()


@app.post("/gen_recipies/")
async def gen_recipies(ingredients: List[DtoIngredient]) -> list[OutputRecipe]:
    ingredients:List[str] = [i.to_llm_input_format() for i in ingredients]
    return await generate(ingredients)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)