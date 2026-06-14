from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a brief summary on given poem \n {text}",
    input_variables=["text"]
)

loader = TextLoader('cricket.txt',encoding='utf-8')

doc = loader.load()

doc_text = doc[0]

chain = prompt1 | model | parser

result= chain.invoke({"text":doc_text})

print(result)