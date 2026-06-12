from langgraph.checkpoint.postgres import PostgresSaver
import os
from langgraph.graph import (
    StateGraph,
    END
)

from app.agent.langgraph_approach.state import (
    FinancialState
)

from app.agent.langgraph_approach.nodes import (
    fetch_data_node,
    analysis_node,
    recommendation_node,
    response_node
)

builder = StateGraph(
    FinancialState
)

builder.add_node(
    "fetch_data",
    fetch_data_node
)

builder.add_node(
    "analysis",
    analysis_node
)

builder.add_node(
    "recommendation",
    recommendation_node
)

builder.add_node(
    "response",
    response_node
)

builder.set_entry_point(
    "fetch_data"
)

builder.add_edge(
    "fetch_data",
    "analysis"
)

builder.add_edge(
    "analysis",
    "recommendation"
)

builder.add_edge(
    "recommendation",
    "response"
)

builder.add_edge(
    "response",
    END
)

# graph = builder.compile()

DATABASE_URL = os.getenv("DATABASE_URL")

with PostgresSaver.from_conn_string(
    DATABASE_URL
) as checkpointer:

    graph = builder.compile(
        checkpointer=checkpointer
    )



# input_state = {

#     "user_id":"K96x7m4yUck5Z0hDCLxdQ5oYjtpm2cez",
#     "question":
#     "How can I save more money?"
# }

# result = graph.invoke(
#     input_state
# )


# if __name__ == "__main__":

#     result = graph.invoke(
#         {
#             "user_id": "K96x7m4yUck5Z0hDCLxdQ5oYjtpm2cez",
#             "question": "How can I save more money?"
#         }
#     )

#     print(result)