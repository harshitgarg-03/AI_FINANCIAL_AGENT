from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv();

groq_api = os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    max_completion_tokens=2000
)

# response=llm.invoke(
#     "hello"
# )
# 
# print(response.content)