from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

load_dotenv()

loader = TextLoader('docs.txt', encoding='utf-8')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(
    docs,
    OpenAIEmbeddings()
)

retriever = vectorstore.as_retriever()

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type='map_reduce'
)

query = 'What is the key takeaway from the document?'

answer = qa_chain.invoke({"query": query})

print("Answer:\n")
print(answer["result"])