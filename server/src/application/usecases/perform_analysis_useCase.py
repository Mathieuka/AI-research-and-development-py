from server.src.infrastructure.agent.client import Agent
from pydantic import BaseModel
from server.src.core.domain.repositories.document import DocumentRepository


class Resume(BaseModel):
    text: str


class PerformAnalysisUseCase:
    def __init__(self, agent: Agent, document_repository: DocumentRepository):
        self.agent = agent
        self.document_repository = document_repository

    async def perform_analysis(self, resume: Resume) -> str:
        print("document reposiroty : ", self.document_repository)
        return await self.agent.execute(resume.text)
