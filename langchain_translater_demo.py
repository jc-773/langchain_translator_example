import os
import getpass

#define your environment variables 
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

#specify the model that you want to use
model = ChatOpenAI(model="gpt-4o-mini")

# Prompt the user for input
text_to_translate = input("Enter the English text you want to translate: ")
language = input("Enter what language you want this translated to: ")

is_hebrew = False



system_template = "Translate the following text from English to {language}"

prompt_template = ChatPromptTemplate.from_messages([("system",system_template),("user","{text}")])

prompt = prompt_template.invoke({"language":language,"text":text_to_translate})

response = model.invoke(prompt)

translated_text = response.content

#for hebrew and arabic
if language in ("Hebrew", "Arabic"):
 reversed_text = translated_text[::-1]
 print(reversed_text)
else:
 print(translated_text)
  




