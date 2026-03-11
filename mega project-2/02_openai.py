from openai import OpenAI
client = OpenAI(
    api_key = "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"
)
command =  '''
[5:34 pm, 04/01/2026] jigo 💻: Hi
[5:35 pm, 04/01/2026] Aryan Patel: bol
[5:35 pm, 04/01/2026] jigo 💻: Kya kar raha he  
[5:35 pm, 04/01/2026] Aryan Patel: kuch nahi    
[5:35 pm, 04/01/2026] jigo 💻: Baar aja
[5:35 pm, 04/01/2026] Aryan Patel: kyu
[5:35 pm, 04/01/2026] jigo 💻: Aese hi chai pite he
[5:35 pm, 04/01/2026] Aryan Patel: ohk kaha au  
[5:35 pm, 04/01/2026] jigo 💻: Patel aja        
[5:35 pm, 04/01/2026] Aryan Patel: ruk abhi aata hu
[5:35 pm, 04/01/2026] jigo 💻: Ohk

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a parson named aryan who speaks hindi as well as english . he is from india and is a coder. you analyze chat history and respond like aryan."},
        {"role": "user", "content": command}
    ]
)
print(completion.choices[0].message.content)

