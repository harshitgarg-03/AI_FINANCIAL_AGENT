from app.llm.model import llm
from app.tools.registry import TOOLS

from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver 
from langchain.agents.middleware.types import AgentMiddleware
from langchain_core.messages import ToolMessage

# from app.db.postgres import Checkpointer


class GroqMessageSanitizerMiddleware(AgentMiddleware):
    def wrap_model_call(self, request, handler):
        cleaned_messages = []
        for msg in request.messages:
            if isinstance(msg, ToolMessage):
                content = msg.content
                if content is None:
                    msg = msg.model_copy(update={"content": "Success"})
                elif isinstance(content, list) and not content:
                    msg = msg.model_copy(update={"content": "[]"})
                elif isinstance(content, str) and not content.strip():
                    msg = msg.model_copy(update={"content": "Success"})
            cleaned_messages.append(msg)
        return handler(request.override(messages=cleaned_messages))


class FinancialAgent:
    def __init__(self):

        DB_URI = "postgresql://neondb_owner:npg_Rv7mDBZd5jwV@ep-soft-base-apz06tg5.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require"

        self.checkpointer_cm = (
            PostgresSaver.from_conn_string(DB_URI)
        )

        self.checkpointer = (
            self.checkpointer_cm.__enter__()
        )

        self.checkpointer.setup()

        self.agent = create_agent(
            model=llm,
            tools=TOOLS,
            checkpointer=self.checkpointer,
            middleware=[GroqMessageSanitizerMiddleware()],
        )

    def chat(
        self,
        user_id: str,
        question: str,
        thread_id: str
    ):

        thread_config = {
            "configurable": {
                "thread_id": thread_id,
                "user_id": user_id
            }
        }
        system_prompt = f"""
You are an expert AI Financial Advisor.

Current user id: {user_id}

Rules:
- Use tools whenever financial data is required.
- Never invent financial information.
- Use transaction, budget, income and goal tools.
- Give concise actionable advice.
"""
        
        
        response = self.agent.invoke(
    {
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            },
        ]

    },
    config=thread_config
)

        return response["messages"][-1].content