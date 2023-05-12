import openai
from setting import setting

openai.api_key = setting.OPENAI_API_KEY

# with open("sample.wav", "rb") as audio_file:
#     transcript = openai.Audio.transcribe("whisper-1", audio_file, api_key=OPENAI_API_KEY)

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)