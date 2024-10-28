import asyncio

from RecipeModel import generate

resp=asyncio.run(generate(["bread","onion","apples 2"]))

# [{"name":"bread","quantity":""},{"name":"onion","quantity":""},{"name":"apples","quantity":"2"}] -> (["bread","onion","apples 2"]