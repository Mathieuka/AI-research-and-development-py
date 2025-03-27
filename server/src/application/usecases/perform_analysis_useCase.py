from server.src.infrastructure.controllers.perform_analysis.perform_analysis_controller import Resume
from server.src.infrastructure.agent.client import Agent

class PerformAnalysisUseCase:
    async def perform_analysis(self, resume: Resume, agent: Agent) -> str:
        response = await agent.execute(resume.text)
        return response
