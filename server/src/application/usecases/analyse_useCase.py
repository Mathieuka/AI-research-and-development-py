# import asyncio
from server.src.agent.client import agent_execute


class AnalysisUseCase:
    async def perform_analysis(self, resume: str):
        # resolve: asyncio.Future = asyncio.Future()
        # resolve.set_result("Analysis performed successfully")
        response = await agent_execute()
        return response
