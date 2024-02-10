from openai import OpenAI
import os, sys

def ask_gpt(question):

    client = OpenAI(api_key="<api key>")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': question + ' Your response should be less than or equal to 50 words.'}
        ]
    )
    return(completion.choices[0].message.content)

   