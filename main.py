import sys
import json
import openai

config = json.load(open('config.json', 'r'))

openai.api_key = open("OPENAI_KEY").read().strip()
print("OpenAI key loaded")

print("Reading chapter text ...")
chapter_text = open("chapter.txt", encoding='utf-8').read()
print("Chapter text loaded")

print("Sending chapter to OpenAI ...")
chat_completion = openai.ChatCompletion.create(
    model = config.model,
    messages = [
        {
            "role": "system",
            "content": config.prompt
        },
        {
            "role": "user",
            "content": chapter_text
        }
    ]
)
print("AI processing complete")

output_text = chat_completion.choices[0].message.content

print("Writing output to file ...")
open("chapter_out.txt", 'w', encoding='utf-8').write(output_text)
print("Output saved")

