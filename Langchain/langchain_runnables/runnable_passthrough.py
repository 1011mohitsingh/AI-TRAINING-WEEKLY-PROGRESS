from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
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

# Parser
parser = StrOutputParser()

# Prompt 2
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# Joke Generation Chain
joke_gen_chain = prompt1 | model | parser

# Parallel Chain
parallel_chain = RunnableParallel(
    joke=RunnablePassthrough(),
    explanation=prompt2 | model | parser
)

# Final Chain
final_chain = joke_gen_chain | parallel_chain

# Invoke
result = final_chain.invoke({'topic': 'cricket'})

print("Joke:\n")
print(result['joke'])

print("\nExplanation:\n")
print(result['explanation'])