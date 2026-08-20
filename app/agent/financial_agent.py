from app.llm.model import llm
from app.tools.registry import TOOLS
from psycopg_pool import ConnectionPool
from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver 
from langchain.agents.middleware.types import AgentMiddleware
from langchain_core.messages import ToolMessage
import os 
from dotenv import load_dotenv
load_dotenv();

from langchain.agents.middleware import SummarizationMiddleware

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

        self.pool = ConnectionPool(
            conninfo=os.getenv("DATABASE_URL"),
            max_size=10,
            kwargs={"autocommit": True}
        )

        with PostgresSaver.from_conn_string(os.getenv("DATABASE_URL")) as checkpointer:
            checkpointer.setup()

        self.agent = create_agent(
            model=llm,
            tools=TOOLS,
            checkpointer=PostgresSaver(self.pool),
            middleware=[GroqMessageSanitizerMiddleware(),
            SummarizationMiddleware(
                model=llm,
                trigger=("tokens", 3500),
                keep=("messages", 6),
                trim_tokens_to_summarize=1800,
            )]
        )
    
    def cleanup(self):
        if hasattr(self, 'pool'):
            self.pool.close()
        elif hasattr(self, 'checkpointer_cm'):
            self.checkpointer_cm.__exit__(None, None, None)

    def chat(self, user_id: str, question: str, thread_id: str):

        thread_config = {
            "configurable": {
                "thread_id": thread_id,
                "user_id": user_id
            }
        }
        system_prompt = f"""
            You are an AI Financial Advisor.

            User ID: {user_id}

            Rules:
            - Use tools only when needed.
            - Never make up financial data.
            - Give short, actionable answers.
            """
        with PostgresSaver.from_conn_string(os.getenv("DATABASE_URL")) as checkpointer:
            agent = create_agent(
            model=llm,
            tools=TOOLS,
            checkpointer=checkpointer,
            middleware=[
                GroqMessageSanitizerMiddleware(),
                SummarizationMiddleware(
                    model=llm,
                    trigger=("tokens", 3500),
                    keep=("messages", 6),
                    trim_tokens_to_summarize=1800,
                )
            ]
        )
            response = agent.invoke(
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