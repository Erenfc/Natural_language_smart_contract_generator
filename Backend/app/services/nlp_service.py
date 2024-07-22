import openai
from .utils import validate_user_input

openai.api_key = 'your_openai_api_key'

def generate_contract_code(user_input):
    validate_user_input(user_input)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a smart contract code for the following requirement: {user_input}",
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    else:
        raise ValueError("No valid response from NLP model")
