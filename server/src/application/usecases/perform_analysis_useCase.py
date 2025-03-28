from server.src.infrastructure.agent.client import Agent
from pydantic import BaseModel

class Resume(BaseModel):
    text: str

class PerformAnalysisUseCase:
    def __init__(self, agent: Agent):
        self.agent = agent

    async def perform_analysis(self, resume: Resume) -> str:
        return await self.agent.execute(resume.text)
