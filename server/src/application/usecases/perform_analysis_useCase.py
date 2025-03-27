from server.src.infrastructure.controllers.perform_analysis.perform_analysis_controller import Resume

class PerformAnalysisUseCase:

    async def perform_analysis(self, resume: Resume, agent) -> str:
        print("resume " + resume.resume)
        response = await agent.execute(resume.resume)
        return response
