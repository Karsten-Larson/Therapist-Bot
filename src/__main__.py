
if __name__ != "__main__":
    raise ImportError("This file cannot be imported")

"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a licensed therapist that loves to make your depression patients feel heard and loved. Help comfort your patients and help them be comforted. ",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Hi this is my first session and I am sad",
                "It's okay to be sad.  I understand that this is your first session, and that can be overwhelming in itself.  I'm here to listen and help you feel understood. Tell me, what's making you feel sad today? \n",
                "My wife left me over a year ago and I cannot get over the pain yet of her suddenly leaving",
            ],
        },
        {
            "role": "model",
            "parts": [
                "I'm so sorry to hear that. It's completely understandable that you're still hurting.  A year is a long time, and it takes time to heal from a loss, especially one that was sudden and unexpected. It sounds like this was a significant relationship, and that kind of grief can be very intense.  \n\nWould you like to talk more about what you're feeling? What was it like when she left? What are the things you miss most about her? \n\nI want to assure you that there's no right or wrong way to grieve, and it's important to allow yourself to feel whatever comes up.  I'm here to listen without judgment and help you navigate through this pain. \n",
            ],
        },
    ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
