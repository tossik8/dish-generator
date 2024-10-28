import asyncio
from typing import List, Dict, Any


async def generate(ingredients: List[str]) -> list[dict[str, list[str] | str | list[dict[str, str] | dict[str, str]]]]:
    await asyncio.sleep(1)
    return(
        [
            {
                "name": "Toast",
                "description": "Bread, Crunchy",
                "image": "https://www.fuller.edu/wp-content/uploads/2022/11/secondary-banner-placeholder.jpg",
                "ingredients": [
                    {"name": "Sliced Bread", "quantity": "4 pieces"},
                    {"name": "Butter", "quantity": "to taste"}
                ],
                "instructions":[
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
    )
