import asyncio
import json
from typing import List, Dict, Any

from pydantic_core._pydantic_core import ValidationError

from server import OutputRecipe

async def generate(ingredients: List[str]) -> list[OutputRecipe]:
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
        return []
    print("Output:")
    print(json.dumps(dummy_resp, indent=4))
    print(("=" * 83) + "|Recipies Sent|" + ("=" * 83))
    return(
        resp
    )
