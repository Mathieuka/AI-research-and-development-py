from typing import Protocol
from sqlmodel import Session


class DocumentRepository(Protocol):
    def add(self, document: str, session: Session) -> None: ...
