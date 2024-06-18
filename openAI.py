from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os 
#from dotenv import load_dotenva
from dotenv import main
import os

main.load_dotenv()
#load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Langsmith  tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"You are a helpful assistant. Answer all questions to the best of your ability."),
        ('user','question {question}')
    ]
)

# streamlit framework
st.title('Langchain demo with qwen2')
input_text = st.text_input(" Searech Here ")


# openAI 
llms = Ollama(model="openai")
output_paser = StrOutputParser()
chain = prompt|llms|output_paser

if input_text:
    st.write(chain.invoke({'question':input_text}))