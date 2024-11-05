import asyncio
import json
from groq import Groq, Stream
from typing import List, Dict, Any

from pydantic_core._pydantic_core import ValidationError

from server import OutputRecipe

async def generate_dummy(ingredients: List[str]) -> list[OutputRecipe]:
    await asyncio.sleep(1)
    dummy_resp = [
        {
            "name": "Toast",
            "description": "Bread, Crunchy",
            "image": "https://www.fuller.edu/wp-content/uploads/2022/11/secondary-banner-placeholder.jpg",
            "ingredients": [
                {"name": "Sliced Bread", "quantity": "4 pieces"},
                {"name": "Butter", "quantity": "to taste"}
            ],
            "instructions": [
                "Put bread in toaster",
                "Wait until you smell something burning",
                "Pop out the half burnt toast",
                "Apply Butter"
            ]
        },
        {
            "name": "Anything",
            "description": "Absolutely Anything",
            "image": "https://www.fuller.edu/wp-content/uploads/2022/11/secondary-banner-placeholder.jpg",
            "ingredients": [
                {"name": "Phone", "quantity": "1"},
                {"name": "Internet", "quantity": "decent bandwidth"},
                {"name": "Credit Card", "quantity": "Just 1 but with enough limit"}
            ],
            "instructions": [
                "Install UberEats",
                "Order whatever you want",
                "Pay with credit card",
                "Wait for Delivery",
                "Enjoy"
            ]
        }
    ]
    print(("="*80)+"|Generating Recipies|"+("="*80))
    print("Input:")
    print(json.dumps(ingredients, indent=4))
    print("-"*181)
    try:
        resp=[OutputRecipe(**i) for i in dummy_resp]
    except ValidationError as e:
        print("Error: Incorrect format generated!")
        print(e.__traceback__)
        return []
    print("Output:")
    print(json.dumps(dummy_resp, indent=4))
    print(("=" * 83) + "|Recipies Sent|" + ("=" * 83))
    return(
        resp
    )

async def generate(ingredients: List[str]) -> Stream:

    print("-" * 181)
    ingredients = ", ".join(ingredients)
    prompt = '''I have following items: input_ingredients
        Give me dishes that can be made using them. I want to output in this json format,do not include any additional text:
        [
          {
            "name": "<dish name>",
            "description": "<description>",
             "ingredients": [
              {"name": "<ingredient 1 name>", "quantity": "<quantity>"},
              {"name": "<ingredient 2 name>"}
             ],
             "instructions":[
                "<step 1>",
                "<step 2>"
             ]
          }
        ]'''
    prompt=prompt.replace("input_ingredients",ingredients)
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    return completion