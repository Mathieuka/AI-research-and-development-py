from server.src.infrastructure.controllers.perform_analysis.perform_analysis_controller import Resume

class PerformAnalysisUseCase:

    async def perform_analysis(self, resume: Resume, agent) -> str:
        response = await agent.execute(resume.text)
        return response
