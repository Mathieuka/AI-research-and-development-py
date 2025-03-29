from typing import Annotated
from fastapi import Depends
from server.src.infrastructure.agent.client import Agent
from server.src.application.usecases import PerformAnalysisUseCase
from server.src.core.domain.repositories.document import DocumentRepository
from sqlmodel import Session


def get_agent() -> Agent:
    return Agent()


def get_document_repository() -> DocumentRepository:
    class PGDocumentRepository:
        def add(self, document: str, session: Session) -> None: ...

    return PGDocumentRepository()


def get_analysis_use_case(
    agent: Annotated[Agent, Depends(get_agent)],
    document_repository: Annotated[
        DocumentRepository, Depends(get_document_repository)
    ],
):
    return PerformAnalysisUseCase(agent, document_repository)
