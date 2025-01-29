import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Access the variables
apikey = os.getenv("apikey")

genai.configure(api_key=apikey)
model=genai.GenerativeModel(model_name="gemini-1.5-flash")


def generate_content(prompt):
    return model.generate_content(prompt)

def translate_content(prompt, target_language):
    return model.generate_content(f'translate this text to the target language -  {target_language}: {prompt}')

# Just some text generation with a vague prompt - 
print(generate_content("Quick brown fox"))
# Get a summary - 
print(generate_content(f'Summarize this: A quick brown fox jumps over the lazy dog, and the dog feels slighted.'))
# translate the prompt to hindi- 
print(translate_content("Quick brown fox", "hindi"))