from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI()

st.header("Chat with OpenAI's Chat Model")

user_input = st.text_input("Enter your message:")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)