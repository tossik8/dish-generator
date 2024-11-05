import json
from typing import List

import uvicorn

from server.DTOs import DtoIngredient, OutputRecipe
from fastapi import FastAPI, Request
from server.RecipeModel import generate
from fastapi.middleware.cors import CORSMiddleware

from server.RecipeModel.Gen import generate_dummy

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

@app.post("/gen_recipies_real")
async def gen_recipies_real(ingredients: List[DtoIngredient]) -> str:
    ingredients:List[str] = [i.to_llm_input_format() for i in ingredients]
    print(("=" * 80) + "|Generating Recipies|" + ("=" * 80))
    print("Input:")
    print(json.dumps(ingredients, indent=4))
    resp=await generate(ingredients)
    payload=""
    for i in resp:
        payload+=i.choices[0].delta.content or ""
    print("-" * 181)
    print("Output:")
    print(payload)
    print(("=" * 83) + "|Recipies Sent|" + ("=" * 83))
    return payload


@app.post("/gen_recipies")
async def gen_recipies(ingredients: List[DtoIngredient]) -> list[OutputRecipe]:
    ingredients:List[str] = [i.to_llm_input_format() for i in ingredients]
    return await generate_dummy(ingredients)
# call from root:
# !python3 -m server.app
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)