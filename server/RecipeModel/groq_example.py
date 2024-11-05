from groq import Groq

prompt='''I have following items: bread, pasta, tomato, onion, peanut butter
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
for i in completion:
    print(i.choices[0].delta.content or "", end="")
