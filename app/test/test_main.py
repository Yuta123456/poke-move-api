from fastapi.testclient import TestClient
import sys
import os


sys.path.append("./")
sys.path.append("../")
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_get_user():
    response = client.get("/user")
    print("response: ", response)
    assert response.status_code == 200


def test_get_challenge():
    user = client.get("/user").json()
    print(user)
    access_token = user["api_token"]
    challenge = client.get(
        "/challenge", headers={"Authorization": "Bearer " + access_token}
    )
    print(challenge)
    assert challenge.status_code == 404
