from langchain.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

search = DuckDuckGoSearchRun()

template = """turn the following user input into a search query for a search engine:

{input}"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

chain = prompt | model | StrOutputParser() | search

chain.invoke({"input": "I'd like to figure out what games are tonight"})

