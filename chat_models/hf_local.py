from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs={"max_length": 2048, "temperature": 0.7},
)

model = ChatHuggingFace(llm=llm)

result = model.invoke([HumanMessage(content="What is the reactjs code to create a button?")])
print(result.content)