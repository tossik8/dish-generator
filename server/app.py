from typing import List

import uvicorn

from server.DTOs import DtoIngredient, OutputRecipe
from fastapi import FastAPI, Request
from server.RecipeModel import generate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/gen_recipies")
async def gen_recipies(ingredients: List[DtoIngredient]) -> list[OutputRecipe]:
    ingredients:List[str] = [i.to_llm_input_format() for i in ingredients]
    return await generate(ingredients)
# call from root:
# !python3 -m server.app
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="localhost", port=8000, reload=True)