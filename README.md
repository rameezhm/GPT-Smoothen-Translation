# GPT-Smoothen-Translation
Sometimes fan translations can have clunky grammar and syntax to English 
readers. This python program takes a text file input and processes it through
an OpenAI model to help improve the readability of the fan translation. 
# Usage
Insert text files into `input` directory and navigate to project folder and run
```bash
python main.py
```
Output text files will be saved with their original names to the `output` directory
# OpenAI Key
Put OpenAI API key into a file named `OPENAI_KEY` in the root of this folder.
# Config
Config stored in `config.json`
## Models 
Specify the OpenAI model you want to use

**gpt-3.5-turbo** for 4k context. Cheaper API cost for smaller chapters.

**gpt-3.5-turbo-16k** for 16k context. I recommend this generally. 
## Prompt
The system prompt given to the AI model. Modify if you want to change any of 
the AI behavior for a specific use case.
## Webpage Mode
Work In Progress

**webpage_mode**: enable or disable web scraper

**wp_element**: the html element type containing the chapter text

**wp_class**: the class of the html element containing the chapter text