from sqlalchemy import create_engine
from dotenv import load_dotenv
# from langgraph.checkpoint.postgres import PostgresSaver

import os;

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL");

engine = create_engine(DATABASE_URL);

from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.fetchone())


# def Checkpointer() :
#     with PostgresSaver.from_conn_string(DATABASE_URL) as checkpointer:
#         checkpointer.__exit__(None, None, None)
#         checkpointer.setup()
#         return checkpointer  
