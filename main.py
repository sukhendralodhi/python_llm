from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

app = FastAPI()

llm = ChatOllama(model="qwen2.5:3b")

prompt = PromptTemplate.from_template(
    """
    Answer in maximum 10 words.

    Question: {question}
    """
)
chain = prompt | llm

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = chain.invoke({
        "question": req.message
    })

    return {
        "response": response.content
    }