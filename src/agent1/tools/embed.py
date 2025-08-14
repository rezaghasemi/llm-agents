import openai
from src.agent1.config import OPENAI_API_KEY, MODEL

_client = openai.OpenAI(
    api_key=OPENAI_API_KEY
)

def embed(text: str)-> str:
    response = _client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]