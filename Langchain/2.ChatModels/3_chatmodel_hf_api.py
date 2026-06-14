# this is the code which we are using when we are accessing the model of hugging face through api
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task = "task-generation"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of India")
print(result.content)
