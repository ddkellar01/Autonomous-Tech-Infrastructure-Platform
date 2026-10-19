from fastapi.testclient import TestClient
from src.backend.api_gateway import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "autonomous-engine-api"}
