import sys, os, json, openai

config = json.load(open('config.json', 'r'))
openai.api_key = open("OPENAI_KEY").read().strip()
input_files = os.listdir('input')

for file in input_files:
    print("Reading", file, "...")
    chapter_text = open('input/' + file, encoding='utf-8').read()

    print("Sending text to OpenAI ...")
    chat_completion = openai.ChatCompletion.create(
        model = config['model'],
        messages = [
            {
                "role": "system",
                "content": config['prompt']
            },
            {
                "role": "user",
                "content": chapter_text
            }
        ]
    )

    print(chat_completion)

    output_text = chat_completion.choices[0].message.content

    print("Writing", file, "output to file ...")
    open('output/' + file, 'w', encoding='utf-8').write(output_text)
    print("Output saved")

print("All files completed")

