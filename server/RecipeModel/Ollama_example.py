import ollama
# TODO: Add img field before returning
response = ollama.chat(model='llama3.2', stream=True, messages=[
  {
    'role': 'user',
    'content':
    '''I have following items: bread, pasta, tomato, onion, peanut butter
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
    ]''',
  },
])
for i in response:
  print(i["message"]["content"],end="")

# Output:
'''
[
  {
    "name": "Peanut Butter Sandwich",
    "description": "A simple sandwich made with bread and peanut butter.",
    "ingredients": [
      {"name": "bread", "quantity": 2},
      {"name": "peanut butter", "quantity": 1}
    ],
    "instructions": [
      "Spread the peanut butter on one slice of bread.",
      "Place the second slice of bread on top to make a sandwich."
    ]
  },
  {
    "name": "Pasta with Tomato Sauce",
    "description": "A basic pasta dish made with tomato and onion.",
    "ingredients": [
      {"name": "pasta", "quantity": 1},
      {"name": "tomato", "quantity": 2},
      {"name": "onion", "quantity": 1}
    ],
    "instructions": [
      "Chop the onion and tomato into small pieces.",
      "Boil the pasta according to the package instructions, then mix with the chopped tomato and onion."
    ]
  }
]
'''