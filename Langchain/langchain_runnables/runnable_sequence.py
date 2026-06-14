from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Prompt 1
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Output Parser
parser = StrOutputParser()

# Prompt 2
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# Chain
chain = (
    prompt1
    | model
    | parser
    | prompt2
    | model
    | parser
)

# Invoke
result = chain.invoke({'topic': 'AI'})

print(result)