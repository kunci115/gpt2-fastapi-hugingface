from fastapi import FastAPI
from pydantic import BaseModel
from runner import generate

app = FastAPI()

class GenerateRequest(BaseModel):
    prefix: str
    max_length: int = 800
    top_k: int = 5

@app.post("/generate")
async def generate_text(request: GenerateRequest):
    """
     Generate text based on the prefix asynchronously
    """
    generated_sentence = await generate(request.prefix, request.max_length, request.top_k)
    return {"generated_sentence": generated_sentence}
