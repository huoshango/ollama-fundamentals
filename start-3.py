import ollama

response = ollama.list()



res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "why is the sky blue?"},
    ],
    stream=True,
)

print(res["message"]["content"])

