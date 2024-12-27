import os
import getpass
import streamlit as st
from dotenv import load_dotenv




#define your environment variables 
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

#specify the model that you want to use
model = ChatOpenAI(model="gpt-4o-mini")

system_template = "Translate the following text from English to French"
prompt_template = ChatPromptTemplate.from_messages([("system",system_template),("user","{text}")])

# Prompt the user for input
text_to_translate = st.chat_input("Enter the English text you want to translate: ")

prompt = prompt_template.invoke({"language":"English","text":text_to_translate})
if text_to_translate:
  with st.spinner("Thinking... 🧠"):
    response = model.invoke(prompt)

    translated_text = response.content

    st.write(translated_text)

#for hebrew and arabic
# if language in ("Hebrew", "Arabic"):
#  reversed_text = translated_text[::-1]
#  print(reversed_text)
# else:
#  print(translated_text)
  




