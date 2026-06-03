from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv();

groq_api = os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model="llama-3.3-70b-versatile"
)

response=llm.invoke(
    "hello"
)

print(response.content)