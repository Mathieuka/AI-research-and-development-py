import asyncio


class AnalysisUseCase:
    async def perform_analysis(self, resume: str):
        resolve: asyncio.Future = asyncio.Future()
        resolve.set_result("Analysis performed successfully")
        return await resolve
