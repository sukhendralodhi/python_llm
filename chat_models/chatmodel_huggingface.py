from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
import os

# Get API token - either from env var or prompt user
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN environment variable is not set. "
                     "Please set it with your HuggingFace API token.")

# Create the underlying LLM
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    huggingfacehub_api_token=api_token,
)

# Wrap it with ChatHuggingFace
chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke([HumanMessage(content="What is the reactjs code to create a button?")])
print(result.content)