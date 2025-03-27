from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")


model = ChatOpenAI(model="gpt-4o")

server_params = StdioServerParameters(
    command="python",
    args=["langchain-mcp-adapter-with-rag/math_server.py"],
)

rag_server_params = StdioServerParameters(
    command="python",
    args=["langchain-mcp-adapter-with-rag/doc_rag.py"],
)

class Agent:
    async def execute(self, resume) -> str:
        print("Resume " + resume)
        async with (
            stdio_client(server_params) as (math_read, math_write),
            stdio_client(rag_server_params) as (rag_read, rag_write),
        ):
            async with (
                ClientSession(math_read, math_write) as math_session,
                ClientSession(rag_read, rag_write) as rag_session,
            ):
                # Initialize the connection
                await math_session.initialize()
                await rag_session.initialize()

                # Get tools
                math_tools = await load_mcp_tools(math_session)
                rag_tools = await load_mcp_tools(rag_session)

                all_tools = [*math_tools, *rag_tools]

                short_system_prompt = """You are an assistant with access to two types of specialized tools:

                1. CV Search Tool:
                   - Use 'search_cv' to find relevant information in the CV
                   - Always search the CV first when asked about experience, skills, or career history
                   - Returns most relevant sections from the CV based on your query

                2. Mathematical Tools:
                   - 'add': Combines two numbers (a + b)
                   - 'multiply': Multiplies two numbers (a * b)
                   - Use these for any numerical calculations, especially with time periods and experience durations

                Follow these guidelines:
                - Always search the CV first before making calculations about experience
                - Extract numerical values from CV content before using math tools
                - Show your reasoning process step by step
                - Verify calculations by explaining the numbers you're using
                - When dealing with experience calculations, ensure to use appropriate math operations:
                  * Use 'add' for combining different periods
                  * Use 'multiply' for scaling experience (e.g., parallel projects)

                Explain your tool selection and reasoning at each step.
                """

                # Create and run the agent
                agent = create_react_agent(model, all_tools, prompt=short_system_prompt)

                test_question = """
                Based on my CV:
                1. Find all periods where I worked with JavaScript
                2. Calculate the total JavaScript experience by adding these periods
                3. Then, if I were to work on 2 JavaScript projects simultaneously, 
                   calculate how many equivalent years of experience I would have accumulated
                Please explain your reasoning step by step.
                """

                agent_response = await agent.ainvoke({"messages": test_question})
                print("RESULT " + agent_response["messages"][-1].content)
                result: str = agent_response["messages"][-1].content
                return result
