from typing import Annotated
from fastapi import Depends
from server.src.infrastructure.agent.client import Agent
from server.src.application.usecases import PerformAnalysisUseCase

def get_agent() -> Agent:
    return Agent()

def get_analysis_use_case(agent: Annotated[Agent, Depends(get_agent)] ):
    return PerformAnalysisUseCase(agent)