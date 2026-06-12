from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv();

groq_api = os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model="qwen/qwen3-32b"
)

# response=llm.invoke(
#     "hello"
# )
# 
# print(response.content)