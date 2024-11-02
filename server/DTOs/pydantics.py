from typing import List, Optional

from pydantic import BaseModel

class DtoIngredient(BaseModel):
    name: str
    quantity: Optional[str]

    def to_llm_input_format(self) -> str:
        resp=self.name
        if self.quantity:
            resp+=" "+self.quantity
        return resp


class OutputRecipe(BaseModel):
    name: str
    description: str
    image: str
    ingredients: List[DtoIngredient]
    instructions: List[str]

