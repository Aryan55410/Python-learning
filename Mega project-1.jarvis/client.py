from openai import OpenAI
client = OpenAI(
    api_key = "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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello world"}
    ]
)
print(completion.choices[0].message.content)

