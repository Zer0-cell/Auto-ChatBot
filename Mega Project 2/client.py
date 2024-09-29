from openai import OpenAI
client = OpenAI(
    openai = "<Enter your openai api>"
)

command = '''

'''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Samir who speaks Bangla as well as English. He is a student from Bangladesh. You analyze chat history and respond like Sammir."},
        {
            "role": "user",
            "content": command
        }
    ]
)

response = completion.choices[0].message

