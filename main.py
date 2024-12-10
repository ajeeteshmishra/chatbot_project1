## define an LLM model

import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY']="AIzaSyB3tX8JcZUkinJzY_EVQEMli24_qKoFOm4"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config
)


## FastAPI deployment

from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse

# Declaring our FastAPI instance
app = FastAPI(title='Chatbot App')

# Defining path operation for root endpoint
@app.get('/',include_in_schema=False)
async def index_page():
  return RedirectResponse('/docs')

@app.post('/chatbot')
async def generate_response(query:dict):
  prompt = [
      {
          "role": "model",
          "parts": "You are a helpful and informative chatbot designed to assist the users according to their queries. You should be polite, respectful, and informative. Always provide clear and concise answers."
      },
      {
          "role":"user",
          "parts": ""
      }]

  prompt[1]['parts'] += (f"{query}")
  response = model.generate_content(prompt).text
  
  return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)