from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="qwen2.5:3b")

prompt = PromptTemplate.from_template(
   """
    Answer in maximum 30 words.

    Question: {question}
    """
)

chain = prompt | llm

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    response = chain.invoke({
        "question": chat_history
    })
    chat_history.append(AIMessage(content=response.content))
    print("Bot:", response.content)

print("Chat history:", chat_history)