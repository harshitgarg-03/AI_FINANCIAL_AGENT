from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from app.agent.financial_agent import FinancialAgent
from contextlib import asynccontextmanager


app = FastAPI(title="AI Financial Agent API")

# Add CORS middleware to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = FinancialAgent()

class ChatRequest(BaseModel):
    user_id: str
    question: str
    thread_id: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    global agent
    agent = FinancialAgent()
    yield
    agent.cleanup()  # Add a cleanup() method to FinancialAgent

app = FastAPI(title="AI Financial Agent API", lifespan=lifespan)


@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):

    # print("hello inm main .py ", request.user_id, request.question, request, request.thread_id)
    try:
        response = agent.chat(
            user_id=request.user_id,
            question=request.question,
            thread_id=request.thread_id
        )
        print("response is ::", response)
        return {"response":   response}
    except Exception as e:
        import traceback

        print("ERROR OCCURRED:")
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/")
def home():
    return {"status": "ok", "message": "AI Financial Agent is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)