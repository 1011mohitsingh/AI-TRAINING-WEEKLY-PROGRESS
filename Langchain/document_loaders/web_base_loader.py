from langchain_community.document_loaders import WebBaseLoader
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
    template="Answer the following question \n {question} from following text \n {text}",
    input_variables=["question","text"]
)

url="https://docs.langchain.com/oss/python/langchain/overview"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt1 | model | parser

result = chain.invoke({"question":"What is short term memory event","text":docs[0].page_content})

print(result)