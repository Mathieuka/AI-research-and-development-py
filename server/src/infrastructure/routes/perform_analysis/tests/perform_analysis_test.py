from fastapi.testclient import TestClient
from server.src.main import app
from server.src.infrastructure.routes.perform_analysis.dependencies import get_agent

class MockAgent:
    async def execute(self, text: str) -> str:
        return text

def test_analysis():
    app.dependency_overrides[get_agent] = lambda: MockAgent()
    client = TestClient(app)
    response = client.post("/perform-analysis", json={"text": "test"})
    assert response.text == '"test"'
    assert response.status_code == 200