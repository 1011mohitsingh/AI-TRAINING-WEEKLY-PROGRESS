from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# does not work well with scanned (written) text and complex layouts

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

doc_text = docs[0]

print(len(docs))

