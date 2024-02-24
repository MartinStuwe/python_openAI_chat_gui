from openai import OpenAI
import os, sys
from playsound import playsound
from pathlib import Path

client = OpenAI(api_key="")


def ask_gpt(question):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': question + ' Your response should be less than or equal to 25 words.'}
        ]
    )
    talk_gpt(completion.choices[0].message.content)
    return(completion.choices[0].message.content)

def talk_gpt(text):

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    response.stream_to_file(speech_file_path)
    playsound(speech_file_path)

    
    
    
    
