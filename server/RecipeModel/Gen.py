from typing import List, Dict, Any


def generate(ingredients: List[str]) -> list[dict[str, list[str] | str | list[dict[str, str] | dict[str, str]]]]:
    return(
        [
            {
                "Name": "Toast",
                "Description": "Bread, Crunchy",
                "Image": "https://www.fuller.edu/wp-content/uploads/2022/11/secondary-banner-placeholder.jpg",
                "Ingredients": [
                    {"Name": "Sliced Bread", "Quantity": "4 pieces"},
                    {"Name": "Butter", "Quantity": "to taste"}
                ],
                "Instructions":[
                    "Put bread in toaster",
                    "Wait until you smell something burning",
                    "Pop out the half burnt toast",
                    "Apply Butter"
                ]
            }
        ]
    )
