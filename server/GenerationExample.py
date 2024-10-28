import asyncio

from server.RecipeModel import generate

print(asyncio.run(generate(["bread","onion","apples 2"])))

# TODO: Switch format
# # [{"name":"bread","quantity":""},{"name":"onion","quantity":""},{"name":"apples","quantity":"2"}] -> (["bread","onion","apples 2"]